#!/usr/bin/env python3
"""vault-v2/VO-QC.md: voice, sync and mix QC of the 30 VO reels, one row per reel (from vo2 builds, final QC and the sync audit)."""
import importlib.util
import json
import os
import sys

sys.path.insert(0, "/opt/bfyp/engine")
import vo2_sync  # noqa: E402

s = importlib.util.spec_from_file_location("plan", "/opt/bfyp/plan/plan.py")
P = importlib.util.module_from_spec(s)
s.loader.exec_module(P)
OUT = "/home/user/bfyp-social-media/vault-v2/VO-QC.md"
M = lambda v, f: format(v, f).replace("-", "−")

rows, fails, nF = [], [], 0
for r in P.REELS:
    name = f"v2_{r['id'][3:]}_{r['slug']}"
    J = json.load(open(f"/opt/bfyp/vo2/out/{name}/{name}.vo2.json"))
    Q = json.load(open(f"/opt/bfyp/vo2/final/{name}/{name}_VO.mp4.qc.json"))
    S = vo2_sync.audit(name)
    q, v = J["qc"], J["voice"]
    nF += v["gender"] == "F"
    k = S["karaoke_max_slot_err"]
    ok = q["pass"] and Q["pass"] and S["cta_ok"] and S["tail_ok"]
    if not ok:
        fails.append(r["id"])
    rows.append(f"| {r['id']} | {'♀' if v['gender'] == 'F' else '♂'} {v['id']} | {q['utmos_mean']:.2f} / {q['utmos_min']:.2f} | {q['word_match']:.3f} | "
                f"{Q['vo_word_match_final_mix']:.3f} | {Q['vo_over_bed_lu']:.1f} | {M(Q['lufs_i'], '.1f')} | {M(Q['true_peak_dbtp'], '.1f')} | "
                f"{'yes' if Q['video_identical'] else 'NO'} | {S['anchored']}/{S['lines']} | {'OK' if S['cta_ok'] else 'EARLY'} | "
                f"{('±' + format(k, '.2f') + ' s') if k is not None else '—'} | {'PASS' if ok else 'FAIL'} |")

L = ["# Vault V2 — voice-over QC (30 reels)\n",
     f"**{len(rows) - len(fails)}/30 PASS** · {nF} female / {len(rows) - nF} male voices · 6 voices (BFYP-K2 palette) · measured on the files in `READY/`.\n",
     "| Reel | Voice | Naturalness UTMOS mean / min (voice alone, /5) | ASR word match, voice alone | ASR word match, final mix | Voice over bed (LU) | Loudness (LUFS) | True peak (dBTP) | Video identical to the validated edit | Lines landing on an edit event | CTA line on the CTA card | Karaoke slot error (max) | Verdict |",
     "|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---|"] + rows + [
     "",
     "Gates: UTMOS mean ≥ 4.0 and every line ≥ 3.6; ASR ≥ 0.97 on the voice alone and ≥ 0.95 on the final mix (Whisper small.en); voice ≥ 7 LU over music + SFX while it speaks; "
     "−14 ±1 LUFS; true peak ≤ −1 dBTP; video stream bit-identical to the validated edit (V2-30: its new English edit); every line inside its window, "
     "karaoke lines within ±4 % of their caption slot; the CTA line starts on the CTA card. “Landing on an edit event” = the line starts within 0.45 s after a cut, zoom, headline reveal, "
     "impact/hit/ding or the CTA card (or up to 0.2 s before it).",
     "",
     "The narration of each reel, its direction and the edit event each line lands on are in the reel's sheet (`READY/<reel>/<reel>.md`)."]
open(OUT, "w").write("\n".join(L) + "\n")
print(OUT, f"{len(rows) - len(fails)}/30 PASS", "fails:", fails)
