#!/usr/bin/env python3
"""BFYP Vault V2 — edit map: what the viewer sees and hears, and when.

edit_map.py <reel.js>... -> /opt/bfyp/vo2/maps/<reel>.json + a readable timeline on stdout.
Records shot cuts (shotIn/shotOut), text reveals (first time each text block becomes readable),
tours/zooms on real screens, SFX cues, music sections, and the CTA start. Nothing is rendered.
"""
import asyncio
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_v2 import CHROME, W, H, build_html  # noqa: E402

OUT = "/opt/bfyp/vo2/maps"
WRAP = """<script>(function(){
  window.__ev = [];
  const wrap = (name) => { const f = window[name]; if (typeof f !== 'function') return;
    window[name] = function(...a) { try { window.__ev.push({fn: name, args: JSON.parse(JSON.stringify(a.slice(0, 4), (k, v) => (typeof v === 'number' || typeof v === 'string' || typeof v === 'boolean' || v === null || Array.isArray(v) || (typeof v === 'object')) ? v : undefined))}); } catch (e) {}
      return f.apply(this, a); }; };
  ['shotIn', 'shotOut', 'tour', 'ctaCard', 'camPunch', 'slam', 'popIn', 'wordsIn', 'karaoke', 'counter', 'stampIn', 'strikeIn', 'glitchOn'].forEach(wrap);
})();</script>
"""

# visible, readable text blocks at time t (top-level text containers only)
JS = r"""(t) => {
  R.render(t);
  const out = [];
  const seen = new Set();
  const walker = document.createTreeWalker(document.getElementById('root'), NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const txt = n.nodeValue.replace(/\s+/g, ' ').trim();
    if (!txt || txt.length < 2) continue;
    let op = 1, e = n.parentElement, host = null;
    while (e && e.id !== 'root') {
      const cs = getComputedStyle(e);
      if (cs.display === 'none') { op = 0; break; }
      op *= parseFloat(cs.opacity);
      if (!host && e.id && R.els[e.id]) host = e.id;
      e = e.parentElement;
    }
    if (op < 0.6 || getComputedStyle(n.parentElement).visibility === 'hidden') continue;
    const r = n.parentElement.getBoundingClientRect();
    if (r.bottom < 0 || r.top > 1920 || r.right < 0 || r.left > 1080) continue;
    const key = (host || '?') + '|' + txt;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push({host: host || '?', txt: txt.slice(0, 90), y: Math.round(r.top), size: Math.round(parseFloat(getComputedStyle(n.parentElement).fontSize))});
  }
  return out;
}"""


async def map_reel(reel_js, br):
    tmp = tempfile.mkdtemp(prefix="emap_")
    html = os.path.join(tmp, "a.html")
    build_html(os.path.abspath(reel_js), "/opt/bfyp/assets", html)
    s = open(html).read()
    tag = f'<script src="file://{os.path.abspath(reel_js)}"></script>'
    open(html, "w").write(s.replace(tag, WRAP.replace("window[name] = function", "window[name] = function") + tag))
    page = await br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    await page.goto("file://" + html)
    await page.evaluate("document.fonts.ready")
    meta = await page.evaluate("({dur: R.dur, bpm: R.bpm, cues: R.cues, music: R.music})")
    ev = await page.evaluate("window.__ev")
    dur = meta["dur"]
    first = {}
    last = {}
    step = 0.1
    i = 0
    while i * step < dur:
        t = round(i * step, 2)
        for b in await page.evaluate(JS, t):
            k = (b["host"], b["txt"])
            if k not in first:
                first[k] = {"t": t, **b}
            last[k] = t
        i += 1
    await page.close()
    texts = []
    for k, v in first.items():
        big = v["size"] >= 40
        texts.append({"t_in": v["t"], "t_out": round(last[k] + step, 2), "host": v["host"], "text": v["txt"], "size": v["size"], "y": v["y"], "headline": big})
    texts.sort(key=lambda x: (x["t_in"], x["y"]))
    shots = []
    for e in ev:
        if e["fn"] == "shotIn":
            shots.append({"shot": e["args"][0], "t": round(float(e["args"][1]), 3), "kind": e["args"][2] if len(e["args"]) > 2 else ""})
    shots.sort(key=lambda x: x["t"])
    tours = []
    for e in ev:
        if e["fn"] == "tour":
            for st in (e["args"][1] or []):
                if isinstance(st, dict) and "t0" in st:
                    tours.append({"screen": e["args"][0], "t0": round(float(st["t0"]), 3), "t1": round(float(st.get("t1", st["t0"])), 3), "key": st.get("key", ""), "text": st.get("text", "")})
    cta = [round(float(e["args"][0]), 3) for e in ev if e["fn"] == "ctaCard"]
    kara = [{"id": e["args"][0], "t0": round(float(e["args"][1]), 3), "t1": round(float(e["args"][2]), 3)} for e in ev if e["fn"] == "karaoke"]
    cues = sorted([{"t": round(c["t"], 3), "type": c["type"]} for c in meta["cues"]], key=lambda c: c["t"])
    m = {"reel": os.path.basename(reel_js)[:-3], "dur": dur, "bpm": meta["bpm"], "music": {k: meta["music"].get(k) for k in ("style", "bpm", "key", "mode", "sections")} if meta["music"] else None,
         "shots": shots, "texts": texts, "tours": tours, "cta": cta[0] if cta else None, "karaoke": kara, "cues": cues}
    return m


def show(m):
    L = [f"== {m['reel']}  dur {m['dur']:.2f}s  bpm {m['bpm']}  CTA at {m['cta']}"]
    ev = []
    for s in m["shots"]:
        ev.append((s["t"], 0, f"--- CUT {s['shot']} ({s['kind']})"))
    for x in m["texts"]:
        ev.append((x["t_in"], 1, f"{'TXT' if x['headline'] else 'txt'} [{x['t_in']:.1f}-{x['t_out']:.1f}] {x['text']}"))
    for x in m["tours"]:
        ev.append((x["t0"], 2, f"ZOOM [{x['t0']:.2f}-{x['t1']:.2f}] {x['key']} · {x['text']}"))
    for c in m["cues"]:
        if c["type"] in ("impact", "hit", "ding", "riser", "stamp", "subdrop", "whoosh", "glitch", "notif"):
            ev.append((c["t"], 3, f"sfx {c['type']}"))
    for t, _, s in sorted(ev):
        L.append(f"{t:6.2f}  {s}")
    return "\n".join(L)


async def main(reels):
    from playwright.async_api import async_playwright
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"])
        for r in reels:
            m = await map_reel(r, br)
            json.dump(m, open(os.path.join(OUT, m["reel"] + ".json"), "w"), indent=1, ensure_ascii=False)
            open(os.path.join(OUT, m["reel"] + ".txt"), "w").write(show(m))
            print(show(m), flush=True)
        await br.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
