#!/usr/bin/env python3
"""BFYP Vault V2 renderer: reel JS scene -> frames (Chromium) + audio (synth) -> MP4 + cover."""
import argparse
import asyncio
import json
import os
import subprocess
import sys
import time

import cv2
import numpy as np
import scipy.io.wavfile as wf
from scipy import signal

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
from dsp import SR, Bus, db, stereo, master, lufs, true_peak_db, butter  # noqa: E402
import instruments as I  # noqa: E402
from music import Track  # noqa: E402

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FONT_DIR = "/opt/bfyp/fonts"
W, H = 1080, 1920


def load_vo(reel_js):
    p = reel_js[:-3] + ".vo.json"
    if not os.path.exists(p):
        return None
    m = json.load(open(p))
    return {"lines": m["lines"], "dur": m["dur"]}


def build_html(reel_js, assets_dir, out_html):
    fonts = []
    for fam, pref in (("Inter", "Inter"), ("Geist", "Geist"), ("Geist Mono", "GeistMono"), ("Inter Tight", "InterTight"), ("JetBrains Mono", "JetBrainsMono")):
        for f in sorted(os.listdir(FONT_DIR)):
            if f.startswith(pref + "-") and f.endswith(".ttf"):
                wt = f[len(pref) + 1:-4]
                if not wt.isdigit():
                    continue
                fonts.append(f"@font-face{{font-family:'{fam}';font-weight:{wt};src:url('file://{FONT_DIR}/{f}') format('truetype');}}")
    html = f"""<!doctype html><html><head><meta charset="utf-8">
<style>{''.join(fonts)}</style>
<link rel="stylesheet" href="file://{ENGINE}/web/brand.css">
<base href="file://{assets_dir}/">
</head><body>
<div id="root"><div id="bg"></div><div id="bggrid"></div><div id="cam" class="abs"></div><div id="fx" class="abs" style="width:1080px;height:1920px;pointer-events:none"></div><div class="vignette"></div></div>
<script>window.VO = {json.dumps(load_vo(reel_js))};
window.ASSET_CATALOG = {json.dumps(json.load(open(os.path.join(assets_dir, 'screens', 'catalog.json'))))};
window.REG = {json.dumps(json.load(open(os.path.join(assets_dir, 'regions.json'))))};</script>
<script src="file://{ENGINE}/web/motion.js"></script>
<script src="file://{ENGINE}/web/components.js"></script>
<script>
mk && (function(){{ R.els['cam'] = {{el: document.getElementById('cam'), tr: {{}}, base: {{x:0,y:0,s:1,sx:1,sy:1,r:0,o:1,blur:0,bright:1,sat:1}}, parent:'root'}}; R.order.push('cam');
document.getElementById('cam').style.transformOrigin = '540px 900px'; }})();
</script>
<script src="file://{reel_js}"></script>
</body></html>"""
    with open(out_html, "w") as f:
        f.write(html)


# ------------------------------------------------------------------ audio
def render_audio(meta, dur, out_wav, log):
    m = meta.get("music") or {}
    cues = meta.get("cues") or []
    total = dur
    # music
    music = np.zeros((2, int(total * SR) + SR * 3))
    if m:
        T = Track(m.get("style", "techhouse"), m.get("bpm", 120), m.get("key", "A"), m.get("mode", "minor"),
                  m.get("prog", ["i", "VI", "III", "VII"]), dur=total, sections=m.get("sections"), events=m.get("events"),
                  seed=m.get("seed", 1), chords_per_bar=m.get("cpb", 1), swing=m.get("swing", 0.0), gain=m.get("gain"))
        mx = T.render()
        L = lufs(mx[:, : int(total * SR)])
        mx = mx * db(m.get("level", -16.0) - L)
        music[:, : mx.shape[1]] += mx[:, : music.shape[1]]
    sfx = Bus(total, pad=3.0)
    for c in cues:
        t = c["t"]
        typ = c["type"]
        g = db(c.get("db", 0.0)) * c.get("gain", 1.0)
        pan = c.get("pan", None)
        x = None
        if typ == "hit":
            x = I.hit(seed=int(t * 100) % 50); g *= 0.55
        elif typ == "impact":
            x = I.impact(size=c.get("size", 1.0), seed=int(t * 100) % 50); g *= 0.7
        elif typ == "whoosh":
            x = I.whoosh(dur=c.get("dur", 0.5), seed=int(t * 100) % 50, up=c.get("up", True)); g *= 0.5
            t = t - c.get("dur", 0.5) * 0.55  # peak lands on t
        elif typ == "swish":
            x = I.swish(seed=int(t * 100) % 50, dur=c.get("dur", 0.22)); g *= 0.4
            t = t - c.get("dur", 0.22) * 0.5
        elif typ == "riser":
            d = c.get("dur", 2.0)
            x = I.riser(d, seed=int(t * 100) % 50); g *= 0.42
            t = t - d
        elif typ == "downlifter":
            x = I.downlifter(c.get("dur", 1.5)); g *= 0.4
        elif typ == "reverse":
            d = c.get("dur", 1.0)
            x = stereo(I.reverse_crash(dur=d)); g *= 0.35
            t = t - d
        elif typ == "click":
            x = I.click(seed=int(t * 1000) % 50, f=c.get("f", 3200)); g *= 0.5
        elif typ == "tick":
            x = I.tick(seed=int(t * 1000) % 50); g *= 0.4
        elif typ == "key":
            x = I.click(seed=int(t * 1000) % 90, f=2600 + (int(t * 1000) % 7) * 180, gain=0.8); g *= 0.3
        elif typ == "pop":
            x = I.pop(); g *= 0.5
        elif typ == "ding":
            x = I.ding(note=c.get("note", 88)); g *= 0.45
        elif typ == "chime":
            x = I.chime(notes=tuple(c.get("notes", (84, 88)))); g *= 0.4
        elif typ == "wrong":
            x = I.buzz_wrong(); g *= 0.4
        elif typ == "shutter":
            x = I.shutter(); g *= 0.55
        elif typ == "notif":
            x = I.notif(notes=tuple(c.get("notes", (83, 90)))); g *= 0.4
        elif typ == "glitch":
            x = I.glitch(dur=c.get("dur", 0.3), seed=int(t * 100) % 50); g *= 0.3
        elif typ == "scan":
            x = I.scan(dur=c.get("dur", 0.8)); g *= 0.25
        elif typ == "stamp":
            x = I.stamp(); g *= 0.6
        elif typ == "ticks":
            n = c.get("n", 12)
            d = c.get("dur", 1.0)
            u = np.linspace(0, 1, n) ** c.get("curve", 0.6)
            x = I.counter_ticks(list(u * d)); g *= 0.3
        elif typ == "heartbeat":
            x = I.heartbeat(); g *= 0.6
        elif typ == "sparkle":
            x = I.sparkle(); g *= 0.35
        elif typ == "subdrop":
            x = I.sub_drop(); g *= 0.5
        elif typ == "bass":
            x = I.bass_hit(); g *= 0.45
        if x is not None:
            sfx.add(x, t, g, pan=pan)
    n_all = min(music.shape[1], sfx.x.shape[1])
    music_s, sfx_s = music[:, :n_all], sfx.x[:, :n_all]
    vo_path = meta.get("vo_wav")
    if vo_path and os.path.exists(vo_path):
        sr_vo, vo = wf.read(vo_path)
        vo = vo.astype(np.float64) / 32768.0
        if vo.ndim > 1:
            vo = vo.mean(axis=1)
        vo = butter(vo, "hp", 70.0, 2)
        from dsp import compress as _comp, filt as _filt
        vo = _filt(vo, "peak", 3200.0, 0.9, 1.5)      # presence
        vo = _filt(vo, "peak", 250.0, 1.0, -1.5)      # de-box
        vo_st = _comp(np.vstack([vo, vo]), thresh_db=-24, ratio=2.6, attack=0.004, release=0.12)
        Lvo = lufs(vo_st[:, : min(vo_st.shape[1], n_all)])
        vo_st = vo_st * db(-16.0 - Lvo)
        pad = np.zeros((2, n_all))
        m = min(n_all, vo_st.shape[1])
        pad[:, :m] = vo_st[:, :m]
        # ducking envelope from VO activity (music -8 dB, sfx -3 dB under voice)
        from dsp import env_follow
        act = env_follow(pad, attack=0.02, release=0.25)
        act = np.clip((20 * np.log10(act + 1e-9) + 50) / 12.0, 0, 1)
        k = np.exp(-1.0 / (0.08 * SR))
        act = signal.lfilter([1 - k], [1, -k], act)
        music_s = music_s * db(-8.0 * act)
        sfx_s = sfx_s * db(-3.0 * act)
        mix = music_s + sfx_s + pad
        log["vo"] = {"wav": os.path.basename(vo_path), "lufs_vo": -16.0}
    else:
        mix = music_s + sfx_s
    mix = mix[:, : int(total * SR)]
    # final 60 ms fade to avoid end click
    nf = int(0.06 * SR)
    mix[:, -nf:] *= np.linspace(1, 0, nf)
    ceiling = float(os.environ.get("BFYP_CEILING") or meta.get("ceiling") or -1.5)  # per-reel master ceiling (R.setup({ceiling})) when AAC adds large inter-sample overs
    out, info = master(mix, target_lufs=meta.get("lufs", -14.0), ceiling=ceiling)
    log["master_ceiling_dbtp"] = ceiling
    out = out[:, : int(total * SR)]
    # post-master fades: 3 ms in (no DC step), 40 ms out (clean loop point)
    fi, fo = int(0.003 * SR), int(0.04 * SR)
    out[:, :fi] *= np.linspace(0, 1, fi)
    out[:, -fo:] *= np.linspace(1, 0, fo) ** 2
    wf.write(out_wav, SR, (np.clip(out.T, -1, 1) * 32767).astype(np.int16))
    log["audio"] = {"lufs": round(float(info["lufs"]), 2), "true_peak_db": round(float(info["tp"]), 2)}
    return log


# ------------------------------------------------------------------ video
async def render_video(html, out_mp4, log, cover_png=None, preview_dir=None, only_cover=False, fast_dir=None):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--force-color-profile=srgb", "--hide-scrollbars",
                                                                    "--disable-gpu", "--font-render-hinting=none", "--allow-file-access-from-files"])
        page = await br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        errs = []
        page.on("pageerror", lambda e: errs.append(str(e)))
        page.on("console", lambda m: errs.append("console:" + m.text) if m.type == "error" else None)
        await page.goto("file://" + html)
        await page.evaluate("document.fonts.ready")
        await page.evaluate("Promise.all(Array.from(document.images).map(i => i.decode ? i.decode().catch(()=>{}) : 0))")
        await page.wait_for_timeout(200)
        if errs:
            raise RuntimeError("page errors: " + "; ".join(errs[:5]))
        meta = await page.evaluate("({dur: R.dur, fps: R.fps, bpm: R.bpm, cues: R.cues, music: R.music, meta: R.meta, coverT: R.coverT, lufs: R.lufs || -14.0, ceiling: R.ceiling || null})")
        fps = meta["fps"]
        nfr = int(round(meta["dur"] * fps))
        cdp = await page.context.new_cdp_session(page)

        async def grab(t):
            await page.evaluate(f"R.render({t:.6f})")
            r = await cdp.send("Page.captureScreenshot", {"format": "png", "optimizeForSpeed": True})
            import base64
            buf = np.frombuffer(base64.b64decode(r["data"]), np.uint8)
            img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
            return img  # BGR

        if fast_dir:
            os.makedirs(fast_dir, exist_ok=True)
            step = max(1, int(fps / 3))
            tiles = []
            for i in range(0, nfr, step):
                img = await grab(i / fps)
                tiles.append(cv2.resize(img, (270, 480)))
                cv2.putText(tiles[-1], f"{i / fps:.1f}", (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            while len(tiles) % 10:
                tiles.append(np.zeros_like(tiles[0]))
            sheet = np.vstack([np.hstack(tiles[k:k + 10]) for k in range(0, len(tiles), 10)])
            cv2.imwrite(os.path.join(fast_dir, "sheet.jpg"), sheet, [cv2.IMWRITE_JPEG_QUALITY, 82])
            await br.close()
            return meta
        if not only_cover:
            rng = np.random.RandomState(1234)
            # static dither/grain pattern: breaks gradient banding without costing bitrate
            grain = cv2.GaussianBlur(rng.normal(0, 1.0, (H, W)).astype(np.float32), (0, 0), 0.6)[..., None]
            grain *= 1.0 / (grain.std() + 1e-6)
            ff = subprocess.Popen([
                "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
                "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
                "-c:v", "libx264", "-preset", "slow", "-crf", "19", "-maxrate", "9M", "-bufsize", "18M", "-profile:v", "high", "-level", "4.2",
                "-x264-params", "keyint=60:min-keyint=15:aq-mode=3:aq-strength=0.8:deblock=-1,-1:psy-rd=1.0,0.10",
                "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
                "-movflags", "+faststart", out_mp4 + ".video.mp4"], stdin=subprocess.PIPE)
            t0 = time.time()
            mb_frames = 0
            for i in range(nfr):
                t = i / fps
                mot = await page.evaluate(f"R.motion({t:.6f})")
                nsub = 1 if mot < 6 else (3 if mot < 30 else 5)
                if nsub == 1:
                    img = (await grab(t)).astype(np.float32)
                else:
                    mb_frames += 1
                    acc = None
                    shutter = 0.5  # 180-degree shutter
                    for k in range(nsub):
                        tt = t + (k / (nsub - 1) - 0.5) * shutter / fps
                        im = (await grab(max(0.0, tt))).astype(np.float32)
                        acc = im if acc is None else acc + im
                    img = acc / nsub
                # film grain + dither (luma), stronger in darks
                lum = img.mean(axis=2, keepdims=True)
                amp = 1.25 - 0.6 * (lum / 255.0)
                img = img + grain * amp
                ff.stdin.write(np.clip(img + 0.5, 0, 255).astype(np.uint8).tobytes())
                if preview_dir and i % int(fps) == 0:
                    cv2.imwrite(os.path.join(preview_dir, f"f{i // int(fps):03d}.jpg"), np.clip(img, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
            ff.stdin.close()
            ff.wait()
            log["video"] = {"frames": nfr, "fps": fps, "motion_blur_frames": mb_frames, "render_s": round(time.time() - t0, 1)}
        if cover_png:
            ct = meta.get("coverT")
            has_cover = await page.evaluate("typeof R.coverSetup === 'function'")
            if has_cover:
                await page.evaluate("R.coverSetup()")
            await page.evaluate(f"R.render({(ct if ct is not None else 1.0):.4f})")
            if has_cover:
                await page.evaluate("R.coverPost && R.coverPost()")
            await page.wait_for_timeout(50)
            await page.screenshot(path=cover_png, type="png")
        await br.close()
        return meta


def encode_aac_guarded(wav, m4a, log=None, target_tp=-1.05, tries=5):
    """Encode AAC, decode it back, and trim gain until the ENCODED true peak <= target_tp."""
    tp = None
    for i in range(tries):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2", m4a], check=True)
        dec = m4a + ".dec.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", m4a, "-ac", "2", "-ar", "48000", dec], check=True)
        _, y = wf.read(dec)
        os.remove(dec)
        tp = float(true_peak_db(y.T.astype(np.float64) / 32768.0))
        if tp <= target_tp:
            break
        sr, x = wf.read(wav)
        x = x.astype(np.float64) / 32768.0 * db(target_tp - 0.2 - tp)
        wf.write(wav, sr, (np.clip(x, -1, 1) * 32767).astype(np.int16))
    if log is not None:
        log.setdefault("audio", {})["true_peak_aac_dbtp"] = round(tp, 2)
    return tp


def mux(out_mp4, wav, dur=None, video=None, log=None):
    video = video or (out_mp4 + ".video.mp4")
    m4a = out_mp4 + ".m4a"
    encode_aac_guarded(wav, m4a, log)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", m4a, "-map", "0:v:0", "-map", "1:a:0", "-c", "copy"]
    if dur:
        cmd += ["-t", f"{dur:.6f}"]
    tmp = out_mp4 + ".mux.mp4"
    subprocess.run(cmd + ["-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, out_mp4)
    os.remove(m4a)
    if video.endswith(".video.mp4") and os.path.exists(video):
        os.remove(video)


def video_frames(mp4):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-map", "0:v:0", "-c", "copy", "-f", "null", "-"], capture_output=True, text=True)
    import re as _re
    m = _re.findall(r"frame=\s*(\d+)", r.stderr)
    return int(m[-1]) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel_js")
    ap.add_argument("--out", required=True)
    ap.add_argument("--assets", default="/opt/bfyp/assets")
    ap.add_argument("--preview", default=None)
    ap.add_argument("--cover", default=None)
    ap.add_argument("--only-cover", action="store_true")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--fast", default=None, help="write a 3fps layout contact sheet to this dir and exit")
    ap.add_argument("--audio-only", action="store_true", help="re-render audio and remux into existing --out mp4 (video copied)")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    if a.preview:
        os.makedirs(a.preview, exist_ok=True)
    html = os.path.abspath(a.out) + ".html"
    build_html(os.path.abspath(a.reel_js), a.assets, html)
    log = {"reel": os.path.basename(a.reel_js)}
    if a.audio_only:
        meta = asyncio.run(render_video(html, os.path.abspath(a.out), log, only_cover=True))
        vo = load_vo(os.path.abspath(a.reel_js))
        if vo:
            meta["vo_wav"] = json.load(open(os.path.abspath(a.reel_js)[:-3] + ".vo.json"))["wav"]
        outp = os.path.abspath(a.out)
        nfr = video_frames(outp) or int(round(meta["dur"] * meta["fps"]))
        dur = nfr / meta["fps"]
        log["video_frames_existing"] = nfr
        wav = outp + ".wav"
        render_audio(meta, dur, wav, log)
        src = outp + ".src.mp4"
        os.replace(outp, src)
        mux(outp, wav, dur=dur, video=src, log=log)
        os.remove(src)
        os.remove(wav)
        os.remove(html)
        lj = outp + ".log.json"
        if os.path.exists(lj):
            L = json.load(open(lj)); L["log"]["audio"] = log["audio"]
            if "vo" in log: L["log"]["vo"] = log["vo"]
            json.dump(L, open(lj, "w"), indent=1)
        print(json.dumps(log))
        return
    meta = asyncio.run(render_video(html, os.path.abspath(a.out), log, cover_png=a.cover, preview_dir=a.preview, only_cover=a.only_cover, fast_dir=a.fast))
    vo = load_vo(os.path.abspath(a.reel_js))
    if vo:
        meta["vo_wav"] = json.load(open(os.path.abspath(a.reel_js)[:-3] + ".vo.json"))["wav"]
    if a.fast:
        os.remove(html)
        print(json.dumps({"fast": a.fast, "dur": meta["dur"]}))
        return
    if not a.only_cover:
        dur = int(round(meta["dur"] * meta["fps"])) / meta["fps"]
        wav = os.path.abspath(a.out) + ".wav"
        if not a.no_audio:
            render_audio(meta, dur, wav, log)
            mux(os.path.abspath(a.out), wav, dur=dur, log=log)
            os.remove(wav)
        else:
            os.rename(os.path.abspath(a.out) + ".video.mp4", os.path.abspath(a.out))
    with open(os.path.abspath(a.out) + ".log.json", "w") as f:
        json.dump({"log": log, "meta": {k: meta[k] for k in ("dur", "fps", "bpm", "music", "meta") if k in meta}, "cues": meta.get("cues")}, f, indent=1)
    os.remove(html) if os.path.exists(html) and not os.environ.get("KEEP_HTML") else None
    print(json.dumps(log))


if __name__ == "__main__":
    main()
