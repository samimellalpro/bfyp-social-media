#!/usr/bin/env python3
"""Status of the 30 directed VOs: build QC, mix freshness (mix carries the current VO build), final QC.

vo2_status.py           -> table
vo2_status.py --to-mix  -> reels whose build passes but whose final mix is missing or stale (space-separated)
"""
import json
import os
import sys

FIN = "/opt/bfyp/vo2/final"
OUT = "/opt/bfyp/vo2/out"
REELS = sorted(d for d in os.listdir("/opt/bfyp/out/final") if d.startswith("v2_") and d != "v2_30_fr_source"
               and os.path.exists(f"/opt/bfyp/out/final/{d}/{d}.mp4"))


def status(r):
    s = {"reel": r, "build": None, "mix": "missing", "qc": None}
    j = f"{OUT}/{r}/{r}.vo2.json"
    if not os.path.exists(j) or not os.path.exists(f"/opt/bfyp/vo2/specs/{r}.py"):
        return s
    J = json.load(open(j))
    s.update(build=J["qc"]["pass"], voice=J["voice"]["id"], gender=J["voice"]["gender"])
    s["frozen"] = '"legacy_pron": True' in open(f"/opt/bfyp/vo2/specs/{r}.py").read()
    if not s["frozen"] and os.path.getmtime(f"/opt/bfyp/vo2/specs/{r}.py") > os.path.getmtime(j):
        s["build"] = "stale"
    mp4 = f"{FIN}/{r}/{r}_VO.mp4"
    if os.path.exists(mp4):
        LL = json.load(open(mp4 + ".log.json"))["log"]
        L = LL.get("vo2") or {}
        # a mix is current when it carries this VO build and the no-PNS AAC encode (validated prototypes are kept as they are)
        A = LL.get("audio") or {}
        clean = "aac_pns 0" in A.get("aac", "") and (A.get("aac_worst_overshoot_db") or 99) <= 1.5  # no encoder burst
        s["mix"] = "ok" if L.get("vo_sha256") == J["sha256"] and (s["frozen"] or clean) else "stale"
        if os.path.exists(mp4 + ".qc.json") and os.path.getmtime(mp4 + ".qc.json") >= os.path.getmtime(mp4):
            Q = json.load(open(mp4 + ".qc.json"))
            s["qc"] = Q["pass"]
            s.update(lufs=Q["lufs_i"], tp=Q["true_peak_dbtp"], vob=Q["vo_over_bed_lu"], asr=Q["vo_word_match_final_mix"], same=Q["video_identical"])
    return s


if __name__ == "__main__":
    S = [status(r) for r in REELS]
    if "--to-mix" in sys.argv:
        # validated prototypes are never re-mixed: their final is the validated file (only re-QC'd)
        print(" ".join(x["reel"] for x in S if x["build"] is True and not x.get("frozen") and (x["mix"] != "ok" or x["qc"] is None)))
        sys.exit()
    for x in S:
        extra = f"  {x['lufs']:6.2f} LUFS  TP {x['tp']:5.2f}  VO/bed {x['vob']:4.1f}  ASR {x['asr']:.3f}  same video {x['same']}" if x.get("qc") is not None else ""
        print(f"{x['reel']:22s} {x.get('gender', '?')} {x.get('voice', '-'):24s} build {str(x['build']):5s}  mix {x['mix']:7s}  qc {str(x['qc']):5s}{extra}")
    done = [x for x in S if x["build"] is True and x["mix"] == "ok" and x["qc"] is True]
    print(f"\n{len(done)}/{len(S)} final · F {sum(1 for x in S if x.get('gender') == 'F')} / M {sum(1 for x in S if x.get('gender') == 'M')}")
