#!/usr/bin/env python3
"""BFYP Vault V2 — local fallback voice-over (Kokoro, "BFYP-K1" blend) + objective QC.

Fallback only: ElevenLabs "Adam" remains the preferred voice. Never clones any voice:
BFYP-K1 is a weighted blend of stock Kokoro voices (am_michael 0.60 + am_onyx 0.25 + am_puck 0.15).

usage: vo.py <reel_name> <bpm> "line 1" "line 2" ...   -> reels/<reel_name>.vo.json + vo wav
"""
import hashlib
import json
import math
import os
import re
import sys

import numpy as np
import soundfile as sf
from scipy import signal

TTS_DIR = "/opt/bfyp/tts"
OUT_DIR = "/opt/bfyp/vo"
SR_OUT = 48000
BLEND = {"am_michael": 0.60, "am_onyx": 0.25, "am_puck": 0.15}
SPEED = 0.92
PRON = [  # applied to synthesis text only (script text unchanged)
    (r"\bVOO\b", "V.O.O."), (r"\bSPY\b", "S P Y"), (r"\bQQQ\b", "Q.Q.Q."), (r"\bBFYP\b", "B.F.Y.P."),
    (r"\bETFs\b", "E.T.F.s"), (r"\bETF\b", "E.T.F."), (r"\bSEC\b", "S.E.C."), (r"\bAI\b", "A.I."),
    (r"\b13F\b", "thirteen F"), (r"\bBetterForYourPocket\.com\b", "Better For Your Pocket dot com"), (r"\bBetterForYourPocket\b", "Better For Your Pocket"),
    (r"\bNVIDIA\b", "en-VID-ee-uh"), (r"\bForm 144\b", "Form one forty-four"), (r"\b144s\b", "one forty-fours"),
    (r"\bForm 4\b", "Form four"), (r"\bUSDC\b", "U.S.D.C."), (r"\bROI\b", "R.O.I."), (r"\bN-PORT\b", "N-port"),
    (r"\$1\.67 trillion", "one point six seven trillion dollars"), (r"\b24h\b", "twenty-four hours"),
    (r"\b30D\b", "thirty days"), (r"\bUTC\b", "U.T.C."), (r"\b31/100\b", "thirty-one out of a hundred"),
]


def pron(text):
    out = text
    for pat, rep in PRON:
        out = re.sub(pat, rep, out)
    return out


def load_voice(k):
    st = None
    for name, w in BLEND.items():
        v = k.get_voice_style(name) * w
        st = v if st is None else st + v
    return st.astype(np.float32)


def trim_silence(x, sr, thr_db=-40.0, pad=0.02):
    env = np.abs(x)
    win = max(1, int(0.01 * sr))
    env = np.convolve(env, np.ones(win) / win, mode="same")
    thr = 10 ** (thr_db / 20.0) * max(1e-9, np.max(env))
    idx = np.where(env > thr)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(pad * sr))
    b = min(len(x), idx[-1] + int(pad * sr))
    return x[a:b]


def synth(lines):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(TTS_DIR, "voices-v1.0.bin"))
    voice = load_voice(k)
    outs = []
    for ln in lines:
        audio, sr = k.create(pron(ln), voice=voice, speed=SPEED, lang="en-us", trim=True)
        audio = trim_silence(np.asarray(audio, dtype=np.float64), sr)
        audio = signal.resample_poly(audio, SR_OUT, sr)
        outs.append(audio)
    return outs


# ------------------------------------------------------------------ QC
def asr(wav48):
    import sherpa_onnx
    d = os.path.join(TTS_DIR, "sherpa-onnx-whisper-small.en")
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=os.path.join(d, "small.en-encoder.int8.onnx"),
                                                     decoder=os.path.join(d, "small.en-decoder.int8.onnx"),
                                                     tokens=os.path.join(d, "small.en-tokens.txt"), num_threads=2)
    x16 = signal.resample_poly(wav48, 1, 3).astype(np.float32)
    s = rec.create_stream()
    s.accept_waveform(16000, x16)
    rec.decode_stream(s)
    return s.result.text.strip()


ALIAS = {"nvidea": "nvidia", "bfyp": "b f y p", "fyp": "f y p", "voo": "v o o", "spy": "s p y", "sec": "s e c", "etf": "e t f", "etfs": "e t f s",
         "timeframe": "time frame", "betterforyourpocket": "better for your pocket", "com": "dot com", "ai": "a i", "usdc": "u s d c",
         "gov": "dot gov", "percent": "%"}
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def num_words(n):
    n = int(n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num_words(n % 100))
    if n < 1000000:
        return num_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + num_words(n % 1000))
    return str(n)


def norm_words(t):
    t = t.lower().replace("’", "'").replace("—", " ").replace("–", " ").replace("-", " ").replace("/", " ")
    t = re.sub(r"\.(com|gov)\b", r" \1", t)
    t = re.sub(r"\$([0-9]+(?:\.[0-9]+)?)\s*(trillion|billion|million)", r"\1 \2 dollars", t)
    t = re.sub(r"\$([0-9]+(?:\.[0-9]+)?)", r"\1 dollars", t)
    t = re.sub(r"([0-9]+)\.([0-9]+)", lambda m: m.group(1) + " point " + " ".join(m.group(2)), t)
    t = re.sub(r"[0-9]+", lambda m: " " + num_words(m.group(0)) + " ", t)
    t = re.sub(r"[^a-z%' ]", " ", t)
    ws = [w.strip("'") for w in t.split() if w.strip("'")]
    out = []
    for w in ws:
        out.extend(ALIAS.get(w, w).split())
    return [w for w in out if w not in ("the",)] if False else out


def word_match(ref, hyp):
    """Share of reference words recovered in order (LCS / len(ref))."""
    a, b = norm_words(ref), norm_words(hyp)
    if not a:
        return 1.0
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)] / len(a)


def f0_stats(x, sr=SR_OUT):
    import librosa
    y = signal.resample_poly(x, 1, 3)  # 16 kHz
    f0, vflag, vprob = librosa.pyin(y, fmin=60, fmax=300, sr=16000, frame_length=1024)
    f = f0[~np.isnan(f0)]
    if len(f) < 10:
        return None, None
    med = float(np.median(f))
    p10, p90 = np.percentile(f, [10, 90])
    spread = 12 * math.log2(p90 / p10)
    return med, spread


def build(name, bpm, lines, lead=0.15, min_gap=0.5, tail=0.45, starts=None):
    os.makedirs(OUT_DIR, exist_ok=True)
    clips = synth(lines)
    beat = 60.0 / bpm
    half = beat / 2
    t = lead
    placed = []
    for i, c in enumerate(clips):
        d = len(c) / SR_OUT
        if starts and i < len(starts) and starts[i] is not None:
            t = max(t, starts[i])
        placed.append({"i": i, "t0": round(t, 4), "t1": round(t + d, 4), "dur": round(d, 4), "text": lines[i]})
        nxt = t + d + min_gap
        t = math.ceil(nxt / half - 1e-6) * half  # next half-beat on the music grid
    total = placed[-1]["t1"] + tail
    vo = np.zeros(int(math.ceil(total * SR_OUT)) + 1)
    for p, c in zip(placed, clips):
        i0 = int(round(p["t0"] * SR_OUT))
        vo[i0:i0 + len(c)] += c
    peak = np.max(np.abs(vo))
    vo = vo / max(peak, 1e-9) * 0.89
    wav = os.path.join(OUT_DIR, f"{name}.vo.wav")
    sf.write(wav, vo, SR_OUT, subtype="PCM_16")
    # ---- QC
    words = sum(len(norm_words(pron(l))) for l in lines)  # pace measured on spoken words
    speech = sum(p["dur"] for p in placed)
    hyp = asr(vo)
    wm = word_match(" ".join(lines), hyp)
    wm_spoken = word_match(pron(" ".join(lines)), hyp)
    med, spread = f0_stats(vo)
    gaps = [placed[i + 1]["t0"] - placed[i]["t1"] for i in range(len(placed) - 1)]
    clip = bool(np.max(np.abs(vo)) >= 0.999)
    qc = {
        "asr_text": hyp,
        "word_match": round(max(wm, wm_spoken), 3), "word_match_script": round(wm, 3), "word_match_spoken": round(wm_spoken, 3), "words_per_s": round(words / speech, 2),
        "f0_median_hz": round(med, 1) if med else None, "f0_spread_st": round(spread, 2) if spread else None,
        "min_gap_s": round(min(gaps), 2) if gaps else None, "clipping": clip,
    }
    gates = {
        "word_match>=0.97": qc["word_match"] >= 0.97,
        "2.30<=wps<=3.30": 2.30 <= qc["words_per_s"] <= 3.30,
        "85<=F0<=120": bool(med and 85 <= med <= 120),
        "F0 spread>=6.4st": bool(spread and spread >= 6.4),
        "pause at sentence ends": (min(gaps) >= 0.3) if gaps else True,
        "no clipping": not clip,
    }
    qc["gates"] = gates
    qc["pass"] = all(gates.values())
    sha = hashlib.sha256(open(wav, "rb").read()).hexdigest()
    meta = {"name": name, "bpm": bpm, "lines": placed, "dur": round(total, 3), "wav": wav, "sha256": sha,
            "provenance": {"provider": "Kokoro-82M v1.0 (local, kokoro-onnx, Apache-2.0)", "voice": "BFYP-K1 blend " + json.dumps(BLEND),
                           "speed": SPEED, "lang": "en-us", "status": "fallback — replace with ElevenLabs Adam when available",
                           "model_sha256": "7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5",
                           "voices_sha256": "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d"},
            "qc": qc}
    with open(os.path.join("/opt/bfyp/reels", f"{name}.vo.json"), "w") as f:
        json.dump(meta, f, indent=1)
    return meta


if __name__ == "__main__":
    name, bpm = sys.argv[1], float(sys.argv[2])
    m = build(name, bpm, sys.argv[3:])
    print(json.dumps({k: m[k] for k in ("dur", "sha256")}, indent=1))
    print(json.dumps(m["qc"], indent=1))
    for p in m["lines"]:
        print(f'{p["t0"]:6.2f}-{p["t1"]:6.2f}  {p["text"]}')
