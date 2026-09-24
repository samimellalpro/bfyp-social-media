#!/usr/bin/env python3
"""grab.py reel.js outdir t1 t2 ... -> full-res PNG frames at given times (seconds)."""
import asyncio, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_v2 import build_html, CHROME, W, H

async def main(js, outdir, ts):
    os.makedirs(outdir, exist_ok=True)
    outdir = os.path.abspath(outdir)
    html = os.path.join(outdir, '_grab.html')
    build_html(os.path.abspath(js), '/opt/bfyp/assets', html)
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--force-color-profile=srgb", "--hide-scrollbars", "--disable-gpu", "--allow-file-access-from-files"])
        pg = await br.new_page(viewport={"width": W, "height": H})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://" + html)
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(200)
        if errs: print("ERR", errs)
        for t in ts:
            await pg.evaluate(f"R.render({t})")
            await pg.screenshot(path=os.path.join(outdir, f"t{float(t):06.2f}.png"))
        await br.close()
    os.remove(html)

asyncio.run(main(sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]))
