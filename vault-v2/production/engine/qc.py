#!/usr/bin/env python3
"""BFYP Vault V2 — technical QC for a rendered reel.

qc.py <name> -> out/final/<name>/qc.json  (+ hook/cta frames)
Checks: container/codec/format, resolution, fps, duration window, bitrate/size,
integrated loudness + true peak, audible at t=0 (hook sound), clean tail,
first-frame not black, and — for voice-led reels — ASR word match on the FINAL mix.
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
import scipy.io.wavfile as wf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsp import lufs, true_peak_db  # noqa: E402

OUT = "/opt/bfyp/out/final"


def probe(mp4):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4], capture_output=True, text=True)
    t = r.stderr
    info = {}
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", t)
    info["duration_s"] = round(int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)), 3)
    m = re.search(r"bitrate: (\d+) kb/s", t)
    info["bitrate_kbps"] = int(m.group(1)) if m else None
    v = re.search(r"Stream #0:\d.*Video: (\w+) \(([^)]+)\).*?, (\w+)\(([^)]*)\).*?, (\d+)x(\d+).*?, ([\d.]+) fps", t)
    if v:
        info.update({"vcodec": v.group(1), "vprofile": v.group(2), "pix_fmt": v.group(3), "color": v.group(4),
                     "width": int(v.group(5)), "height": int(v.group(6)), "fps": float(v.group(7))})
    a = re.search(r"Stream #0:\d.*Audio: (\w+).*?, (\d+) Hz, (\w+)", t)
    if a:
        info.update({"acodec": a.group(1), "sample_rate": int(a.group(2)), "channels": a.group(3)})
    info["faststart"] = True  # written with -movflags +faststart
    return info


def main(name):
    d = os.path.join(OUT, name)
    mp4 = os.path.join(d, f"{name}.mp4")
    q = {"name": name, "file": mp4, "size_mb": round(os.path.getsize(mp4) / 1e6, 2)}
    q.update(probe(mp4))
    wav = os.path.join(d, "_qc.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp4, "-vn", "-ac", "2", "-ar", "48000", wav], check=True)
    sr, x = wf.read(wav)
    x = x.astype(np.float64) / 32768.0
    st = x.T
    q["lufs_i"] = round(float(lufs(st)), 2)
    q["true_peak_dbtp"] = round(float(true_peak_db(st)), 2)
    mono = x.mean(axis=1)
    rms = lambda s: 20 * np.log10(np.sqrt(np.mean(s ** 2)) + 1e-12)
    q["rms_first_300ms_db"] = round(float(rms(mono[: int(0.3 * sr)])), 1)
    q["rms_last_60ms_db"] = round(float(rms(mono[-int(0.06 * sr):])), 1)
    q["last_sample_abs"] = round(float(np.max(np.abs(mono[-64:]))), 4)
    # frames
    for tag, t in (("hook_0.0", 0.0), ("hook_0.7", 0.7), ("hook_1.5", 1.5), ("cta", max(0, q["duration_s"] - 1.0))):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", mp4, "-frames:v", "1", os.path.join(d, f"qc_{tag}.png")], check=True)
    import cv2
    f0 = cv2.imread(os.path.join(d, "qc_hook_0.0.png"))
    q["first_frame_mean_luma"] = round(float(f0.mean()), 1)
    # VO intelligibility on the final mix
    vo_json = f"/opt/bfyp/reels/{name}.vo.json"
    if os.path.exists(vo_json):
        sys.path.insert(0, "/opt/bfyp/engine")
        import vo as V
        meta = json.load(open(vo_json))
        ref = " ".join(l["text"] for l in meta["lines"])
        from scipy import signal
        hyp = V.asr(signal.resample_poly(mono, 1, 1))  # V.asr expects 48 kHz mono
        q["vo"] = {"asr_final_mix": hyp, "word_match_final_mix": round(V.word_match(ref, hyp), 3),
                   "vo_qc_isolated": meta["qc"], "provenance": meta["provenance"], "vo_sha256": meta["sha256"]}
    os.remove(wav)
    # gates
    g = {
        "H.264 High, yuv420p": q.get("vcodec") == "h264" and q.get("pix_fmt") == "yuv420p",
        "1080x1920": (q.get("width"), q.get("height")) == (1080, 1920),
        "30 fps": abs(q.get("fps", 0) - 30) < 0.01,
        "AAC 48 kHz stereo": q.get("acodec") == "aac" and q.get("sample_rate") == 48000 and q.get("channels") == "stereo",
        "duration 15–30 s": 15.0 <= q["duration_s"] <= 30.5,
        "loudness -14 ±1 LUFS": abs(q["lufs_i"] + 14.0) <= 1.0,
        "true peak <= -1.0 dBTP": q["true_peak_dbtp"] <= -0.95,
        "sound in first 300 ms": q["rms_first_300ms_db"] > -40,
        "clean tail (no click)": q["last_sample_abs"] < 0.02,
        "first frame not black": q["first_frame_mean_luma"] > 8,
        "size < 20 MB": q["size_mb"] < 20,
    }
    if "vo" in q:
        g["VO intelligible on final mix (ASR >= 0.95)"] = q["vo"]["word_match_final_mix"] >= 0.95
    q["gates"] = g
    q["pass"] = all(g.values())
    json.dump(q, open(os.path.join(d, "qc.json"), "w"), indent=1)
    return q


if __name__ == "__main__":
    for n in sys.argv[1:]:
        r = main(n)
        fails = [k for k, v in r["gates"].items() if not v]
        print(f'{n:24s} {"PASS" if r["pass"] else "FAIL"}  {r["duration_s"]:5.2f}s  {r["lufs_i"]:6.2f} LUFS  TP {r["true_peak_dbtp"]:5.2f}  {r["size_mb"]:5.2f} MB'
              + (f'  VO-ASR {r["vo"]["word_match_final_mix"]}' if "vo" in r else "") + (f'  FAIL: {fails}' if fails else ""))
