#!/usr/bin/env python3
"""BFYP Vault V2 — DOM text audit.

audit_text.py <reel.js>... -> prints text that leaves the 1080x1920 frame (hard fail) or sits under
the Instagram Reels right-rail icons (x > 960, 1100 < y < 1760; warning), sampled every 0.1 s.
Only text that is visible (effective opacity >= 0.25) for >= 0.3 s is reported, so shot
transitions (0.2-0.4 s zooms) do not trigger it.
"""
import asyncio
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_v2 import CHROME, W, H, build_html  # noqa: E402

JS = r"""(t) => {
  R.render(t);
  const out = [];
  const walker = document.createTreeWalker(document.getElementById('root'), NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const txt = n.nodeValue.trim();
    if (!txt) continue;
    let op = 1, e = n.parentElement;
    while (e && e.id !== 'root') { const cs = getComputedStyle(e); if (cs.display === 'none') { op = 0; break; } op *= parseFloat(cs.opacity); e = e.parentElement; }
    if (op < 0.25 || getComputedStyle(n.parentElement).visibility === 'hidden') continue;
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) {
      if (r.width < 2 || r.height < 2) continue;
      const hard = r.right > 1080 - 4 || r.left < 4 || r.top < 0 || r.bottom > 1920;
      const rail = r.right > 960 && r.bottom > 1100 && r.top < 1760;
      if (hard || rail) out.push({k: hard ? 'OUT' : 'RAIL', txt: txt.slice(0, 60), l: Math.round(r.left), r: Math.round(r.right), t: Math.round(r.top), b: Math.round(r.bottom)});
    }
  }
  return out;
}"""


async def audit(reel_js, br):
    tmp = tempfile.mkdtemp(prefix="audit_")
    html = os.path.join(tmp, "a.html")
    build_html(os.path.abspath(reel_js), "/opt/bfyp/assets", html)
    page = await br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    await page.goto("file://" + html)
    await page.evaluate("document.fonts.ready")
    await page.wait_for_timeout(150)
    dur = await page.evaluate("R.dur")
    hits = {}
    steps = int(dur / 0.1)
    for i in range(steps + 1):
        t = min(i * 0.1, dur - 0.01)
        for h in await page.evaluate(JS, t):
            key = (h["k"], h["txt"])
            hits.setdefault(key, []).append((round(t, 1), h))
    await page.close()
    rep = []
    for (k, txt), lst in hits.items():
        ts = sorted({x[0] for x in lst})
        if len(ts) >= 3:
            worst = max(lst, key=lambda x: x[1]["r"])[1]
            rep.append({"kind": k, "text": txt, "t0": ts[0], "t1": ts[-1], "n": len(ts), "rect": [worst["l"], worst["t"], worst["r"], worst["b"]]})
    return rep


async def main(reels):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--hide-scrollbars", "--disable-gpu", "--allow-file-access-from-files"])
        res = {}
        for r in reels:
            rep = await audit(r, br)
            name = os.path.basename(r)[:-3]
            res[name] = rep
            print(f"== {name}: {sum(1 for x in rep if x['kind'] == 'OUT')} OUT, {sum(1 for x in rep if x['kind'] == 'RAIL')} RAIL", flush=True)
            for x in sorted(rep, key=lambda x: (x["kind"], x["t0"])):
                print(f"   {x['kind']:4s} {x['t0']:5.1f}-{x['t1']:5.1f}s rect={x['rect']}  {x['text']!r}", flush=True)
        await br.close()
    return res


if __name__ == "__main__":
    out = asyncio.run(main(sys.argv[1:]))
    json.dump(out, open(os.environ.get("AUDIT_JSON", "/opt/bfyp/test/audit_text.json"), "w"), indent=1)
