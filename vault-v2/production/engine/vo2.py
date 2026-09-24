#!/usr/bin/env python3
"""BFYP Vault V2 — directed voice-over "BFYP-K2": one voice direction per reel, fitted to the frozen edit.

Local and free only: Kokoro-82M v1.0 (kokoro-onnx, Apache-2.0), stock native-English voices or blends
of stock voices. No cloning, no paid service.

  vo2.py build <reel>            -> vo2/out/<reel>/<reel>.vo2.wav + <reel>.vo2.json   (spec: vo2/specs/<reel>.py)
  vo2.py mix <reel> <out.mp4>    -> copy of the validated reel with the audio rebuilt: same music and SFX,
                                    this VO, dynamic ducking. Video stream copied bit for bit.

A spec file defines SPEC = {"reel", "voice": {...}, "direction": {...}, "lines": [...]}.
Each line: {"at": start s, "until": latest end s, "text": script, "say": synthesis text (optional),
            "speed": 1.0, "gain_db": 0.0, "sp": sentence pause, "cp": clause pause}
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np
import soundfile as sf
from scipy import signal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vo as V  # noqa: E402  (pronunciation map, ASR, word match, F0)
from dsp import SR, butter, filt, band, compress, lufs, stereo, db  # noqa: E402

ROOT = "/opt/bfyp/vo2"
SPECS = os.path.join(ROOT, "specs")
OUT = os.path.join(ROOT, "out")
FINAL = "/opt/bfyp/out/final"
MODEL_SHA = "7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5"
VOICES_SHA = "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d"
MAX_FIT = 1.10  # a line may be sped up by at most 10 % to fit its window
_K = None
_UT = None


# BFYP-K2 palette: six recurring voices (3 F, 3 M), all stock Kokoro voices or a blend of stock voices
PALETTE = {
    "K2-F1": {"id": "K2-F1 · Analyst", "gender": "F", "kokoro": "af_heart", "lang": "en-us"},
    "K2-F2": {"id": "K2-F2 · Correspondent", "gender": "F", "kokoro": "bf_emma", "lang": "en-gb"},
    "K2-F3": {"id": "K2-F3 · Host", "gender": "F", "kokoro": "af_sarah", "lang": "en-us"},
    "K2-M1": {"id": "K2-M1 · Peer", "gender": "M", "kokoro": "am_puck", "lang": "en-us"},
    "K2-M2": {"id": "K2-M2 · Signal", "gender": "M", "kokoro": "am_fenrir", "lang": "en-us"},
    "K2-M3": {"id": "K2-M3 · Brit", "gender": "M", "kokoro": {"bm_george": 0.6, "bm_fable": 0.4}, "lang": "en-gb"},
}


def load_spec(reel):
    p = os.path.join(SPECS, reel + ".py")
    spec = importlib.util.spec_from_file_location("vo2spec_" + reel, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    S = m.SPEC
    v = S["voice"]
    if "use" in v:  # {"use": "K2-M3", "speed": 0.97} -> palette voice + per-reel speed
        S["voice"] = dict(PALETTE[v["use"]], **{k: x for k, x in v.items() if k != "use"})
    return S


def kokoro():
    global _K
    if _K is None:
        from kokoro_onnx import Kokoro
        _K = Kokoro(os.path.join(V.TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(V.TTS_DIR, "voices-v1.0.bin"))
    return _K


def style_of(voice):
    k = kokoro()
    kv = voice["kokoro"]
    if isinstance(kv, str):
        return k.get_voice_style(kv)
    st = None
    for n, w in kv.items():
        v = k.get_voice_style(n) * w
        st = v if st is None else st + v
    return st.astype(np.float32)


def utmos(x48):
    """Naturalness MOS (UTMOS22 strong, MIT) on a 48 kHz mono clip."""
    global _UT
    import torch
    if _UT is None:
        sys.path.insert(0, os.path.join(ROOT, "SpeechMOS"))
        from speechmos_utmos import load_utmos
        torch.set_num_threads(2)
        _UT = load_utmos()
    x16 = signal.resample_poly(x48, 1, 3).astype(np.float32)
    with torch.no_grad():
        return float(_UT(torch.from_numpy(x16).unsqueeze(0), 16000).item())


# The tokenizer already says SEC, FTC, AI and ETF(s) as fluent letter names; dotting them (the K1 map) adds stops.
RAW_OK = (r"\bSEC\b", r"\bETFs\b", r"\bETF\b", r"\bAI\b", r"\bBFYP\b", r"\bNVIDIA\b")  # K1's "en-VID-ee-uh" gets spelled V-I-D
# Raw "BFYP" comes out of the tokenizer as "bee-fip"; say it as one quick acronym instead of four stopped letters.
FAST_PH = {"bˈiːfˈɪp": "bˌiːˌɛfwˌaɪpˈiː"}


def pron2(text, legacy=False):
    """Synthesis text. legacy=True reproduces the validated prototypes' path exactly (K1 map, dotted acronyms)."""
    if legacy:
        return V.pron(text)
    out = text
    for pat, rep in V.PRON:
        if pat not in RAW_OK:
            out = re.sub(pat, rep, out)
    return out


def synth(text, voice, speed, sp=0.28, cp=0.12, legacy=False):
    k = kokoro()
    ph = k.tokenizer.phonemize(text, voice.get("lang", "en-us"))
    if not legacy:
        for a, b in FAST_PH.items():
            ph = ph.replace(a, b)
    a, sr = k.create(ph, voice=style_of(voice), speed=float(speed), lang=voice.get("lang", "en-us"), is_phonemes=True,
                     sentence_pause=sp, clause_pause=cp)
    a = V.trim_silence(np.asarray(a, dtype=np.float64), sr, thr_db=-46.0, pad=0.012)
    x = signal.resample_poly(a, SR, sr)
    n = min(len(x), int(0.006 * SR))
    x[:n] *= np.linspace(0, 1, n)
    x[-n:] *= np.linspace(1, 0, n)
    return x


def speech_rms(x):
    fr = int(0.02 * SR)
    m = len(x) // fr
    if m == 0:
        return float(np.sqrt(np.mean(x ** 2)) + 1e-9)
    r = np.sqrt(np.mean(x[: m * fr].reshape(m, fr) ** 2, axis=1))
    act = r[r > r.max() * 10 ** (-30 / 20)]
    return float(np.sqrt(np.mean(act ** 2)) + 1e-9)


def voice_chain(x, gender):
    """Broadcast-style voice processing: clean low end, presence, controlled sibilance, gentle compression."""
    x = butter(x, "hp", 85.0 if gender == "M" else 110.0, 2)
    x = filt(x, "peak", 300.0 if gender == "M" else 360.0, 1.0, -2.0)   # de-box
    x = filt(x, "peak", 3300.0, 0.8, 2.0)                                # presence
    x = filt(x, "highshelf", 9500.0, 0.7, 1.5)                           # air
    # de-esser: attenuate 5.5-10 kHz only when it spikes above the voice's own average
    s = band(x, 5500.0, 10000.0, 2)
    env = np.abs(signal.hilbert(s)) if len(s) < 4_000_000 else np.abs(s)
    k = np.exp(-1.0 / (0.004 * SR))
    env = signal.lfilter([1 - k], [1, -k], env)
    ref = np.percentile(env[env > 1e-6], 75) if np.any(env > 1e-6) else 1.0
    g = np.clip(ref * 1.8 / np.maximum(env, 1e-9), 10 ** (-6 / 20), 1.0)
    x = x - s + s * g
    x = compress(stereo(x), thresh_db=-24.0, ratio=2.4, attack=0.005, release=0.11, knee_db=8.0)[0]
    return x


def level_voice(x, target=-16.0):
    """Broadcast VO levelling: known working level, firm compression, look-ahead limiting, then loudness target."""
    from dsp import limiter
    x = x * db(-20.0 - lufs(stereo(x)))
    x = compress(stereo(x), thresh_db=-26.0, ratio=3.0, attack=0.003, release=0.09, knee_db=6.0)[0]
    x = limiter(stereo(x), ceiling_db=-6.0, lookahead=0.004, release=0.05)[0]
    for _ in range(3):  # settle loudness under a -1 dBFS ceiling
        x = x * db(target - lufs(stereo(x)))
        x = limiter(stereo(x), ceiling_db=-1.0, lookahead=0.004, release=0.05)[0]
    return x


def atempo(x, ratio):
    """Tempo change without pitch change (ffmpeg atempo, WSOLA): output length = len(x) / ratio. Keeps UTMOS within ±0.02 at ±5 %."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        a, b = os.path.join(d, "a.wav"), os.path.join(d, "b.wav")
        sf.write(a, x.astype(np.float32), SR, subtype="FLOAT")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a, "-af", f"atempo={ratio:.5f}", b], check=True)
        y, _ = sf.read(b)
    return np.asarray(y, dtype=np.float64)


def pad_pause(x, extra):
    """Lengthen the longest pause inside a line (comma, full stop) by `extra` seconds; None if the line has no pause."""
    fr = int(0.01 * SR)
    n = len(x) // fr
    r = np.sqrt(np.mean(x[: n * fr].reshape(n, fr) ** 2, axis=1))
    quiet = r < r.max() * 10 ** (-38 / 20)
    best, i = (0, 0, 0), 12
    while i < n - 12:
        if quiet[i]:
            j = i
            while j < n - 12 and quiet[j]:
                j += 1
            best = max(best, (j - i, i, j))
            i = j
        else:
            i += 1
    if best[0] < 5:  # no pause of 50 ms or more
        return None
    mid = (best[1] + best[2]) // 2 * fr
    return np.concatenate([x[:mid], np.zeros(int(round(extra * SR))), x[mid:]])


def fit_slot(say, voice, sp, tgt, psp, pcp, legacy):
    """Karaoke line: among takes from 0.66x to 1.3x the asked speed, keep the most natural one that lands in the slot
    (directly, or after lengthening its own pause by <= 0.35 s, or a tempo change within ±5 %). Duration moves in steps
    with speed (frame rounding), so every take is measured rather than predicted."""
    x, s = synth(say, voice, sp, psp, pcp, legacy), sp
    for _ in range(5):  # quick path: speed follows duration; accept a natural take that lands in the slot
        d = len(x) / SR
        if abs(d - tgt) <= slot_tol(tgt):
            if utmos(x / max(1e-9, np.max(np.abs(x))) * 0.7) >= 4.25:
                return s, x, None
            break
        s = float(np.clip(s * d / tgt, sp * 0.66, sp * 1.3))
        x = synth(say, voice, s, psp, pcp, legacy)
    best = None
    for k in np.arange(0.66, 1.301, 0.04):
        x = synth(say, voice, sp * k, psp, pcp, legacy)
        d = len(x) / SR
        adj = None
        if abs(d - tgt) > slot_tol(tgt):
            y = pad_pause(x, tgt - d) if 0 < tgt - d <= 0.35 else None
            if y is not None:
                x, adj = y, f"pause +{tgt - d:.2f} s"
            elif 0.95 <= d / tgt <= 1.05:
                x, adj = atempo(x, d / tgt), f"tempo x{d / tgt:.3f}"
            else:
                continue
        u = utmos(x / max(1e-9, np.max(np.abs(x))) * 0.7)
        score = u - 0.3 * abs(k - 1.0) - (0.05 if adj else 0.0)
        if best is None or score > best[0]:
            best = (score, sp * k, x, adj)
    if best is None:  # nothing lands in the slot: closest take, the gate will flag it
        xs = [(abs(len(xx) / SR - tgt), k, xx) for k in (0.66, 1.0, 1.3) for xx in [synth(say, voice, sp * k, psp, pcp, legacy)]]
        _, k, x = min(xs, key=lambda t: t[0])
        return sp * k, x, None
    return float(best[1]), best[2], best[3]


def slot_tol(tgt):
    """Karaoke slot tolerance: the caption words are spread over the slot, so the voice must end within ±4 % (≥ 50 ms)."""
    return max(0.05, 0.04 * tgt)


def build(reel):
    S = load_spec(reel)
    voice = S["voice"]
    dur_reel = json.load(open(os.path.join(FINAL, reel, reel + ".mp4.log.json")))["meta"]["dur"]
    lines = []
    clips = []
    for i, L in enumerate(S["lines"]):
        legacy = bool(S.get("legacy_pron"))
        say = pron2(L.get("say") or L["text"], legacy)
        for a, b in (voice.get("pron") or {}).items():
            say = say.replace(a, b)
        sp = L.get("speed", voice.get("speed", 1.0))
        x = synth(say, voice, sp, L.get("sp", 0.28), L.get("cp", 0.12), legacy)
        win = L["until"] - L["at"]
        s = sp
        stretched = None
        tgt = L.get("fit_to")
        if tgt:  # karaoke slot: on-screen words are timed to [at, at + fit_to], so match that duration, not just fit under it
            s, x, stretched = fit_slot(say, voice, sp, tgt, L.get("sp", 0.28), L.get("cp", 0.12), legacy)
            win = tgt + slot_tol(tgt)
        while not tgt and len(x) / SR > win and s < sp * MAX_FIT - 1e-6:
            s = min(sp * MAX_FIT, s + 0.02)
            x = synth(say, voice, s, L.get("sp", 0.28), L.get("cp", 0.12), legacy)
        d = len(x) / SR
        clips.append(x)
        lines.append({"i": i, "at": L["at"], "until": L["until"], "t0": round(L["at"], 3), "t1": round(L["at"] + d, 3), "dur": round(d, 3),
                      "text": L["text"], "speed": round(s, 3), "speed_asked": sp, "fits": d <= win + 1e-3, "gain_db": L.get("gain_db", 0.0),
                      "note": L.get("note", "")})
        if tgt:
            lines[-1].update({"slot_dur": tgt, "slot_err": round(d - tgt, 3), "slot_ok": abs(d - tgt) <= slot_tol(tgt)})
            if stretched:
                lines[-1]["slot_adjust"] = stretched
    # level-match lines, then per-line dynamics
    ref = np.median([speech_rms(c) for c in clips])
    total = max(dur_reel, max(l["t1"] for l in lines) + 0.05)
    track = np.zeros(int(np.ceil(total * SR)) + 1)
    for L, c in zip(lines, clips):
        c = c * (ref / speech_rms(c)) * db(L["gain_db"])
        i0 = int(round(L["t0"] * SR))
        track[i0:i0 + len(c)] += c[: len(track) - i0]
    track = voice_chain(track, voice["gender"])
    track = level_voice(track, S.get("vo_lufs", -16.0))
    d = os.path.join(OUT, reel)
    os.makedirs(d, exist_ok=True)
    wav = os.path.join(d, reel + ".vo2.wav")
    sf.write(wav, track, SR, subtype="PCM_24")
    # ---------------------------------------------------------------- QC
    for L, c in zip(lines, clips):
        L["utmos"] = round(utmos(c / max(1e-9, np.max(np.abs(c))) * 0.7), 2) if L["dur"] >= 0.6 else None
        L["wps"] = round(len(V.norm_words(V.pron(L["text"]))) / max(L["dur"], 1e-3), 2)
    ref_text = " ".join(L["text"] for L in lines)
    hyp = V.asr(track)
    wm = max(V.word_match(ref_text, hyp), V.word_match(V.pron(ref_text), hyp))
    med, spread = V.f0_stats(track)
    gaps = [round(lines[i + 1]["t0"] - lines[i]["t1"], 2) for i in range(len(lines) - 1)]
    ut = [L["utmos"] for L in lines if L["utmos"] is not None]
    speech = sum(L["dur"] for L in lines)
    words = sum(len(V.norm_words(V.pron(L["text"]))) for L in lines)
    qc = {"asr_text": hyp, "word_match": round(wm, 3), "utmos_mean": round(float(np.mean(ut)), 2) if ut else None,
          "utmos_min": round(float(np.min(ut)), 2) if ut else None, "f0_median_hz": round(med, 1) if med else None,
          "f0_spread_st": round(spread, 2) if spread else None, "words": words, "speech_s": round(speech, 2),
          "wps": round(words / max(speech, 1e-3), 2), "coverage": round(speech / dur_reel, 2), "gaps": gaps,
          "all_fit": all(L["fits"] for L in lines)}
    qc["gates"] = {
        "ASR word match >= 0.97": qc["word_match"] >= 0.97,
        "every line fits its window": qc["all_fit"],
        "UTMOS mean >= 4.0": bool(qc["utmos_mean"] and qc["utmos_mean"] >= 4.0),
        "no line below UTMOS 3.6": bool(qc["utmos_min"] is None or qc["utmos_min"] >= 3.6),
        "no overlapping lines": all(g >= 0.08 for g in gaps),
    }
    if any("slot_dur" in L for L in lines):
        qc["gates"]["karaoke: every line keeps its original slot"] = all(L.get("slot_ok", True) for L in lines)
    qc["pass"] = all(qc["gates"].values())
    meta = {"reel": reel, "voice": voice, "direction": S.get("direction", {}), "mix": S.get("mix", {}), "lines": lines, "dur": round(total, 3), "wav": wav,
            "sha256": hashlib.sha256(open(wav, "rb").read()).hexdigest(), "qc": qc,
            "provenance": {"engine": "Kokoro-82M v1.0 via kokoro-onnx (local, Apache-2.0)", "model_sha256": MODEL_SHA, "voices_sha256": VOICES_SHA,
                           "voice": voice["id"], "kokoro": voice["kokoro"], "cloning": "none (stock voices / weighted blend of stock voices)",
                           "naturalness_metric": "UTMOS22 strong (tarepan/SpeechMOS, MIT)"}}
    json.dump(meta, open(os.path.join(d, reel + ".vo2.json"), "w"), indent=1, ensure_ascii=False)
    return meta


def report(m):
    q = m["qc"]
    print(f"== {m['reel']} · {m['voice']['id']} ({m['voice']['gender']}, {m['voice']['kokoro']}) · {'PASS' if q['pass'] else 'FAIL'}")
    print(f"   ASR {q['word_match']} · UTMOS mean {q['utmos_mean']} min {q['utmos_min']} · F0 {q['f0_median_hz']} Hz spread {q['f0_spread_st']} st · "
          f"{q['words']} words in {q['speech_s']} s ({q['wps']} w/s) · voice on {int(q['coverage'] * 100)} % of the reel")
    for L in m["lines"]:
        flag = ("" if L["fits"] else "  <-- OVERFLOW") + (f"  slot {L['slot_dur']:.2f}s err {L['slot_err']:+.2f}" + ("" if L["slot_ok"] else " <-- SLOT") if "slot_dur" in L else "")
        print(f"   {L['t0']:6.2f}-{L['t1']:6.2f} (≤{L['until']:5.2f}) x{L['speed']:.2f} {L['wps']:4.2f}w/s UT {L['utmos']}  {L['text']}{flag}")
    if not q["pass"]:
        print("   FAIL:", [k for k, v in q["gates"].items() if not v])


def mix(reel, out_mp4):
    """Audio-only rebuild of the validated reel with this VO; the video stream is copied, never re-encoded."""
    src = os.path.join(FINAL, reel, reel + ".mp4")
    os.makedirs(os.path.dirname(os.path.abspath(out_mp4)), exist_ok=True)
    shutil.copy2(src, out_mp4)
    lj = src + ".log.json"
    if os.path.exists(lj):
        shutil.copy2(lj, out_mp4 + ".log.json")
    env = dict(os.environ, BFYP_VO2=os.path.join(OUT, reel, reel + ".vo2.json"))
    r = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_v2.py"),
                        f"/opt/bfyp/reels/{reel}.js", "--out", out_mp4, "--audio-only"], env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr[-2000:])
    return out_mp4


def qc_mix(reel, mp4):
    """Final-file QC for a VO'd reel: technical gates, identical video, VO intelligibility on the full mix."""
    import qc as Q
    from dsp import true_peak_db
    src = os.path.join(FINAL, reel, reel + ".mp4")
    md5 = lambda f: subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-map", "0:v", "-c", "copy", "-f", "md5", "-"], capture_output=True, text=True).stdout.strip()
    r = Q.probe(mp4)
    wav = mp4 + ".qc.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp4, "-vn", "-ac", "2", "-ar", "48000", wav], check=True)
    import scipy.io.wavfile as wf
    _, x = wf.read(wav)
    os.remove(wav)
    x = x.astype(np.float64) / 32768.0
    J = json.load(open(os.path.join(OUT, reel, reel + ".vo2.json")))
    ref = " ".join(L["text"] for L in J["lines"])
    hyp = V.asr(x.mean(axis=1))
    wm = max(V.word_match(ref, hyp), V.word_match(V.pron(ref), hyp))
    log = json.load(open(mp4 + ".log.json"))["log"]
    r.update({"lufs_i": round(float(lufs(x.T)), 2), "true_peak_dbtp": round(float(true_peak_db(x.T)), 2),
              "rms_first_300ms_db": round(float(20 * np.log10(np.sqrt(np.mean(x[: int(0.3 * SR)].mean(axis=1) ** 2)) + 1e-12)), 1),
              "last_sample_abs": round(float(np.max(np.abs(x[-64:]))), 4), "video_identical": md5(src) == md5(mp4),
              "asr_final_mix": hyp, "vo_word_match_final_mix": round(wm, 3), "vo_over_bed_lu": (log.get("vo2") or {}).get("vo_over_bed_lu"),
              "size_mb": round(os.path.getsize(mp4) / 1e6, 2)})
    g = {"H.264 1080x1920 30 fps": (r.get("vcodec"), r.get("width"), r.get("height"), round(r.get("fps", 0))) == ("h264", 1080, 1920, 30),
         "AAC 48 kHz stereo": (r.get("acodec"), r.get("sample_rate"), r.get("channels")) == ("aac", 48000, "stereo"),
         "video identical to the validated edit": r["video_identical"],
         "loudness -14 ±1 LUFS": abs(r["lufs_i"] + 14) <= 1.0, "true peak <= -1 dBTP": r["true_peak_dbtp"] <= -0.95,
         "sound in first 300 ms": r["rms_first_300ms_db"] > -40, "clean tail": r["last_sample_abs"] < 0.02,
         "VO intelligible on the final mix (ASR >= 0.95)": r["vo_word_match_final_mix"] >= 0.95,
         "VO clear of the bed (>= 7 LU)": (r["vo_over_bed_lu"] or 0) >= 7.0,
         "duration 15-30 s": 15.0 <= r["duration_s"] <= 30.0, "size < 20 MB": r["size_mb"] < 20.0}
    r["gates"] = g
    r["pass"] = all(g.values())
    json.dump(r, open(mp4 + ".qc.json", "w"), indent=1)
    return r


if __name__ == "__main__":
    cmd, reel = sys.argv[1], sys.argv[2]
    if cmd == "build":
        report(build(reel))
    elif cmd == "mix":
        print(mix(reel, sys.argv[3]))
    elif cmd == "qc":
        q = qc_mix(reel, sys.argv[3])
        fails = [k for k, v in q["gates"].items() if not v]
        print(f"{reel:22s} {'PASS' if q['pass'] else 'FAIL'}  {q['duration_s']:.2f}s  {q['lufs_i']} LUFS  TP {q['true_peak_dbtp']}  "
              f"VO/bed {q['vo_over_bed_lu']} LU  ASR {q['vo_word_match_final_mix']}  video identical: {q['video_identical']}" + (f"  FAIL: {fails}" if fails else ""))
