#!/usr/bin/env python3
"""BFYP Vault V2 — verify every deliverable against manifest.json, then lock the vault (V2 CLOSED).

lock_vault.py verify   -> recompute the sha256 of the 30 videos and 30 covers; check names and manifest (exit 1 on any mismatch)
lock_vault.py lock     -> verify, then write LOCK.md and the lock + red-team fields into manifest.json
Once LOCK.md exists, engine/package.py refuses to repackage the vault unless BFYP_UNLOCK_V2=1
(to be set only on Sami's explicit request for a new render).
"""
import hashlib
import importlib.util
import json
import os
import sys

VAULT = "/home/user/bfyp-social-media/vault-v2"
RULE = "V2 CLOSED — no new render, re-mix or repackaging without Sami's explicit request."


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load_redteam():
    p = "/opt/bfyp/plan/redteam.py"
    s = importlib.util.spec_from_file_location("redteam", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def verify(M):
    rows, bad = [], []
    for r in M["reels"]:
        row = {"id": r["id"]}
        for kind in ("video", "cover"):
            rel = r[kind]
            p = os.path.join(VAULT, rel)
            if not os.path.exists(p):
                bad.append(f"{r['id']} {kind}: missing {rel}")
                continue
            h = sha(p)
            row[kind] = (rel, h)
            if h != r["sha256_" + kind]:
                bad.append(f"{r['id']} {kind}: sha256 {h[:12]} ≠ manifest {r['sha256_' + kind][:12]}")
            if f"-{h[:10]}." not in os.path.basename(rel):
                bad.append(f"{r['id']} {kind}: file name does not carry its hash ({rel})")
        sp = os.path.join(VAULT, r["sheet"])
        row["sheet"] = (r["sheet"], sha(sp) if os.path.exists(sp) else None)
        if row["sheet"][1] is None:
            bad.append(f"{r['id']} sheet: missing {r['sheet']}")
        # nothing else in the reel folder
        folder = os.path.dirname(os.path.join(VAULT, r["video"]))
        extra = sorted(set(os.listdir(folder)) - {os.path.basename(r["video"]), os.path.basename(r["cover"]), os.path.basename(r["sheet"])})
        if extra:
            bad.append(f"{r['id']}: unexpected files {extra}")
        rows.append(row)
    ready = sorted(d for d in os.listdir(os.path.join(VAULT, "READY")) if os.path.isdir(os.path.join(VAULT, "READY", d)))
    if len(ready) != 30 or len(M["reels"]) != 30:
        bad.append(f"READY holds {len(ready)} folders, manifest lists {len(M['reels'])} reels (expected 30)")
    return rows, bad


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    mp = os.path.join(VAULT, "manifest.json")
    M = json.load(open(mp))
    rows, bad = verify(M)
    for b in bad:
        print("MISMATCH", b)
    print(f"{len(rows)} reels · {2 * len(rows)} files hashed · {'ALL MATCH' if not bad else f'{len(bad)} MISMATCH'}")
    if bad:
        sys.exit(1)
    if cmd != "lock":
        return
    RT = load_redteam()
    date = RT.DATE
    fixed = [k for k, v in RT.VERDICTS.items() if "FAIL" in v[:2]]
    for r in M["reels"]:
        a, d, fix = RT.VERDICTS[r["id"]]
        r["status"] = "LOCKED"
        r["red_team"] = {"aesthetic": a, "data": d, "fixed": bool(fix), "fix": fix or None, "recheck": "PASS" if fix else None}
        r["sha256_sheet"] = next(x["sheet"][1] for x in rows if x["id"] == r["id"])
    lock = {"status": "LOCKED", "closed": True, "locked": date, "rule": RULE, "lock_file": "LOCK.md",
            "red_team": {"date": date, "report": RT.REPORT, "aesthetic_fail": [k for k, v in RT.VERDICTS.items() if v[0] == "FAIL"],
                         "data_fail": [k for k, v in RT.VERDICTS.items() if v[1] == "FAIL"], "fixed_and_rechecked": fixed}}
    out = {"vault": M["vault"], "created": M["created"], "count": M["count"], **lock, "reels": M["reels"]}
    json.dump(out, open(mp, "w"), indent=1, ensure_ascii=False)
    L = ["# 🔒 VAULT V2 — LOCKED · V2 CLOSED\n",
         f"Locked on **{date}**, after the final double red team (aesthetic + accuracy, see [`{RT.REPORT}`]({RT.REPORT})).\n",
         f"**Rule: {RULE}**\n",
         "Nothing here is scheduled or published; the Buffer queue and the planned distribution were not touched. "
         "`engine/package.py` refuses to repackage a locked vault (override `BFYP_UNLOCK_V2=1`, only on that explicit request).\n",
         f"The {len(rows)} videos and {len(rows)} covers below were re-hashed on {date} and match `manifest.json` "
         "(`python3 production/engine/lock_vault.py verify` re-checks them). File names carry the first 10 hex of their sha256.\n",
         "| Reel | Video | sha256 (video) | sha256 (cover) | Red team |", "|---|---|---|---|---|"]
    for x, r in zip(rows, M["reels"]):
        rt = r["red_team"]
        tag = "PASS" if not rt["fixed"] else f"fixed ({'aesthetic' if rt['aesthetic'] == 'FAIL' else 'data'}) → re-check PASS"
        L.append(f"| {r['id']} | `{os.path.basename(x['video'][0])}` | `{x['video'][1]}` | `{x['cover'][1]}` | {tag} |")
    L.append("")
    L.append("Sheets (`READY/*/V2-XX_slug.md`) are hashed in `manifest.json` (`sha256_sheet`).")
    open(os.path.join(VAULT, "LOCK.md"), "w").write("\n".join(L) + "\n")
    print("LOCKED:", os.path.join(VAULT, "LOCK.md"))


if __name__ == "__main__":
    main()
