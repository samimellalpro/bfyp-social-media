#!/usr/bin/env python3
"""Sync audit of the directed VO against the frozen edit (vo2/maps/<reel>.json).

vo2_sync.py <reel>... -> per reel: how many lines start on an edit event (cut, zoom, headline reveal, CTA, impact/hit/ding),
lines that run across a hard cut, the CTA line vs the CTA card, the tail margin, karaoke slot errors.
"""
import json
import sys

ANCHOR = 0.45  # a line "lands" on an event when it starts within 0.45 s after it (or 0.2 s before)


def audit(reel):
    M = json.load(open(f"/opt/bfyp/vo2/maps/{reel}.json"))
    J = json.load(open(f"/opt/bfyp/vo2/out/{reel}/{reel}.vo2.json"))
    ev = [(s["t"], "cut " + s["shot"]) for s in M["shots"]]
    ev += [(t["t0"], "zoom " + t["key"]) for t in M["tours"]]
    ev += [(x["t_in"], "text “" + x["text"][:28] + "”") for x in M["texts"] if x.get("headline") or x.get("size", 0) >= 60]
    ev += [(c["t"], c["type"]) for c in M["cues"] if c["type"] in ("impact", "hit", "ding", "whoosh", "notif", "stamp", "subdrop", "riser")]
    ev.append((M["cta"], "CTA card"))
    cuts = [s["t"] for s in M["shots"] if s["t"] > 0.05]
    rows, anchored = [], 0
    for L in J["lines"]:
        near = [(abs(L["t0"] - t), t, n) for t, n in ev if -0.2 <= L["t0"] - t <= ANCHOR]
        a = min(near) if near else None
        anchored += bool(a)
        cross = [round(c, 2) for c in cuts if L["t0"] + 0.2 < c < L["t1"] - 0.2]
        rows.append({"t0": L["t0"], "t1": L["t1"], "text": L["text"], "on": (f"{a[2]} @ {a[1]:.2f}" if a else None), "crosses_cut": cross,
                     "slot_err": L.get("slot_err")})
    last = J["lines"][-1]
    cta_ok = last["t0"] >= M["cta"] - 0.05
    tail = round(M["dur"] - last["t1"], 2)
    return {"reel": reel, "lines": len(rows), "anchored": anchored, "rows": rows, "cta_card": M["cta"], "cta_line_t0": last["t0"],
            "cta_ok": cta_ok, "tail_s": tail, "tail_ok": tail >= 0.1, "first_t0": J["lines"][0]["t0"],
            "karaoke_max_slot_err": max((abs(r["slot_err"]) for r in rows if r["slot_err"] is not None), default=None)}


if __name__ == "__main__":
    out = []
    for reel in sys.argv[1:]:
        r = audit(reel)
        out.append(r)
        k = f" · karaoke max slot error {r['karaoke_max_slot_err']:.2f} s" if r["karaoke_max_slot_err"] is not None else ""
        print(f"{reel:22s} {r['anchored']}/{r['lines']} lines land on an edit event · CTA line at {r['cta_line_t0']:.2f} s (card {r['cta_card']:.2f} s) "
              f"{'OK' if r['cta_ok'] else 'EARLY'} · tail {r['tail_s']:.2f} s {'OK' if r['tail_ok'] else 'SHORT'}{k}")
        for x in r["rows"]:
            flag = "" if x["on"] else "   (free)"
            cc = f"   crosses cut {x['crosses_cut']}" if x["crosses_cut"] else ""
            print(f"    {x['t0']:6.2f}-{x['t1']:6.2f}  {x['text'][:52]:52s} {x['on'] or ''}{flag}{cc}")
    json.dump(out, open("/opt/bfyp/vo2/logs/sync_audit.json", "w"), indent=1, ensure_ascii=False)
