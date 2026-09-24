#!/usr/bin/env python3
"""BFYP Vault V2 — VO casting: same two finance passages in every native-English Kokoro voice (+ blends).

vo_cast.py synth   -> /opt/bfyp/vo2/cast/<voice>_<A|B>.wav + cast.json (duration, rate, F0, ASR)
vo_cast.py score   -> adds UTMOS naturalness (needs torch) to cast.json and prints the ranking
"""
import json
import os
import sys

import numpy as np
import soundfile as sf
from scipy import signal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vo as V  # noqa: E402

OUT = "/opt/bfyp/vo2/cast"
PASSAGES = {
    "A": "Thirty-six percent. That's how much of the fund sits in just ten lines. And the filing shows every one of them, with its date.",
    "B": "A million dollars just moved. Okay... but who moved it? And was it one transfer, or two?",
}
BLENDS = {
    "mix_michael_fenrir": {"am_michael": 0.5, "am_fenrir": 0.5},
    "mix_george_fable": {"bm_george": 0.6, "bm_fable": 0.4},
    "mix_k1": {"am_michael": 0.60, "am_onyx": 0.25, "am_puck": 0.15},
    "mix_puck_michael": {"am_puck": 0.6, "am_michael": 0.4},
    "mix_heart_bella": {"af_heart": 0.6, "af_bella": 0.4},
    "mix_emma_isabella": {"bf_emma": 0.7, "bf_isabella": 0.3},
}


def kokoro():
    from kokoro_onnx import Kokoro
    return Kokoro(os.path.join(V.TTS_DIR, "kokoro-v1.0.onnx"), os.path.join(V.TTS_DIR, "voices-v1.0.bin"))


def style(k, name):
    if name in BLENDS:
        st = None
        for n, w in BLENDS[name].items():
            v = k.get_voice_style(n) * w
            st = v if st is None else st + v
        return st.astype(np.float32)
    return name


def lang_of(name):
    b = BLENDS.get(name)
    first = next(iter(b)) if b else name
    return "en-gb" if first.startswith("b") else "en-us"


def synth_all():
    os.makedirs(OUT, exist_ok=True)
    k = kokoro()
    names = [v for v in sorted(k.get_voices()) if v[:2] in ("af", "am", "bf", "bm")] + list(BLENDS)
    res = {}
    for n in names:
        for pk, txt in PASSAGES.items():
            a, sr = k.create(V.pron(txt), voice=style(k, n), speed=1.0, lang=lang_of(n))
            a = V.trim_silence(np.asarray(a, dtype=np.float64), sr)
            a48 = signal.resample_poly(a, 48000, sr)
            path = os.path.join(OUT, f"{n}_{pk}.wav")
            sf.write(path, a48 / max(1e-9, np.max(np.abs(a48))) * 0.89, 48000, subtype="PCM_16")
            med, spread = V.f0_stats(a48)
            hyp = V.asr(a48)
            words = len(V.norm_words(V.pron(txt)))
            res[f"{n}_{pk}"] = {"voice": n, "passage": pk, "dur": round(len(a48) / 48000, 2), "wps": round(words / (len(a48) / 48000), 2),
                                "f0": round(med, 1) if med else None, "spread_st": round(spread, 2) if spread else None,
                                "asr": round(V.word_match(V.pron(txt), hyp), 3)}
            print(n, pk, res[f"{n}_{pk}"], flush=True)
    json.dump(res, open(os.path.join(OUT, "cast.json"), "w"), indent=1)


def utmos_model():
    import torch
    sys.path.insert(0, "/opt/bfyp/vo2/SpeechMOS")
    from speechmos_utmos import load_utmos  # local shim, see vo2/SpeechMOS
    return load_utmos()


def score_all():
    import torch
    res = json.load(open(os.path.join(OUT, "cast.json")))
    model = utmos_model()
    for key, r in res.items():
        x, sr = sf.read(os.path.join(OUT, key + ".wav"))
        x16 = signal.resample_poly(x, 1, 3).astype(np.float32)
        with torch.no_grad():
            s = float(model(torch.from_numpy(x16).unsqueeze(0), 16000).item())
        r["utmos"] = round(s, 3)
    json.dump(res, open(os.path.join(OUT, "cast.json"), "w"), indent=1)
    by = {}
    for r in res.values():
        by.setdefault(r["voice"], []).append(r)
    rows = []
    for v, rs in by.items():
        rows.append((np.mean([r["utmos"] for r in rs]), v, rs))
    for u, v, rs in sorted(rows, reverse=True):
        a = {r["passage"]: r for r in rs}
        print(f"{v:22s} UTMOS {u:.2f}  A {a['A']['utmos']:.2f} B {a['B']['utmos']:.2f} | F0 {a['A']['f0']} Hz spread {a['A']['spread_st']}/{a['B']['spread_st']} st | wps {a['A']['wps']}/{a['B']['wps']} | ASR {a['A']['asr']}/{a['B']['asr']}")


if __name__ == "__main__":
    {"synth": synth_all, "score": score_all}[sys.argv[1]]()
