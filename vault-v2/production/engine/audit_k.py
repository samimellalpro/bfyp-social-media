#!/usr/bin/env python3
"""BFYP Vault V2 — keyframe-merge audit.

K(id, prop, keys) MERGES with earlier keys on the same (id, prop). When two calls cover overlapping
time ranges, the merged track can interpolate between them in ways the author did not intend
(e.g. a fade-out followed by a slow fade back in). This lists every (id, prop) whose calls overlap
in time, with the merged opacity/scale track, for review.
"""
import asyncio
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_v2 import CHROME, W, H, build_html  # noqa: E402

WRAP = """<script>(function(){ const orig = window.K; window.__kc = [];
window.K = function(id, prop, kfs){ try { window.__kc.push({id, prop, ts: kfs.map(k=>+k[0]), vs: kfs.map(k=>JSON.stringify(k[1]))}); } catch(e){}
return orig(id, prop, kfs); }; })();</script>
"""


async def audit(reel_js, br):
    tmp = tempfile.mkdtemp(prefix="auditk_")
    html = os.path.join(tmp, "a.html")
    build_html(os.path.abspath(reel_js), "/opt/bfyp/assets", html)
    s = open(html).read()
    tag = f'<script src="file://{os.path.abspath(reel_js)}"></script>'
    assert tag in s
    open(html, "w").write(s.replace(tag, WRAP + tag))
    page = await br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    await page.goto("file://" + html)
    calls = await page.evaluate("window.__kc")
    await page.close()
    groups = {}
    for c in calls:
        if c["prop"] not in ("o",):
            continue
        groups.setdefault((c["id"], c["prop"]), []).append(c)
    flags = []
    for (id_, prop), cs in groups.items():
        if len(cs) < 2:
            continue
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                a, b = cs[i], cs[j]
                if not a["ts"] or not b["ts"]:
                    continue
                a0, a1, b0, b1 = min(a["ts"]), max(a["ts"]), min(b["ts"]), max(b["ts"])
                if b0 < a1 - 1e-6 and b1 > a0 + 1e-6:
                    merged = sorted(zip(a["ts"] + b["ts"], a["vs"] + b["vs"]))
                    flags.append((id_, prop, [(round(t, 2), v) for t, v in merged]))
    return flags


async def main(reels):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"])
        for r in reels:
            fl = await audit(r, br)
            print(f"== {os.path.basename(r)[:-3]}: {len(fl)} overlapping opacity tracks", flush=True)
            for id_, prop, m in fl:
                print(f"   {id_}.{prop}: {m}", flush=True)
        await br.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
