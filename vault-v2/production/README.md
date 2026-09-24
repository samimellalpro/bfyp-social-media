# BFYP Vault V2 — production sources

Everything needed to re-render or edit the 30 Reels in `../READY/`.

## Layout
- `engine/render_v2.py` — renderer: scene script (`reels/*.js`) → frames (headless Chromium, 30 fps, adaptive motion blur, dither) → H.264; audio (music + SFX + optional VO) → master (−14 LUFS, encoded true peak ≤ −1 dBTP) → MP4 + cover PNG.
- `engine/web/` — `brand.css` (BFYP tokens: #080e0d background, #17b58a green, Inter + Geist Mono), `motion.js` (deterministic keyframe engine), `components.js` (real-screen frames, capture stamps, spotlight tours, callouts, quote cards, CTA card, karaoke captions, covers).
- `engine/music.py`, `engine/instruments.py`, `engine/dsp.py` — original music/SFX synthesis (no samples) and mastering chain.
- `engine/vo.py` — fallback voice “BFYP-K1” (Kokoro-82M v1.0 via kokoro-onnx, offline) + objective voice QC (Whisper small.en via sherpa-onnx).
- `engine/qc.py` — technical QC gates. `engine/audit_text.py` — text-safety audit: browser layout checked every 0.1 s, flags text off-frame or under the right-hand Reels buttons. `engine/audit_k.py` — lists opacity keyframes that overlap on one element (the engine merges them). `engine/package.py`, `engine/make_readme.py`, `engine/overview.py` and `engine/make_review.py` — vault packaging, README, covers overview and the local review page (`review.html`).
- `reels/v2_XX_slug.js` — one scene script per Reel (timeline in beats); `reels/*.vo.json` — voice lines, timings, provenance and QC.
- `plan/plan.py` — slate: angles, scripts, captions (IG/X), hashtags, CTA, sources.
- `research/facts.md` — verified external facts with sources.
- `assets/screens/*.png` — 1× crops of the real BFYP screens (captured 23 Sep 2026), `catalog.json` (source file + capture time for each crop), `regions.json` (named regions used by the spotlight tours). Run `python3 engine/upscale_2x.py` to rebuild the `@2x` files the renderer loads.

## Requirements
Python 3.11 with `numpy scipy pillow opencv-python-headless playwright pyloudnorm imageio-ffmpeg` (+ `kokoro-onnx soundfile librosa sherpa-onnx` for voice), Chromium (Playwright), ffmpeg with libx264, and fonts Inter + Geist Mono (Google Fonts, OFL) in `/opt/bfyp/fonts` (paths are set at the top of `render_v2.py`).

## Commands
```bash
python3 engine/render_v2.py reels/v2_14_whale_alert.js --out out/v2_14.mp4 --cover out/v2_14_cover.png   # full render
python3 engine/render_v2.py reels/v2_14_whale_alert.js --out out/v2_14.mp4 --fast out/v2_14_preview       # 3 fps layout sheet
python3 engine/render_v2.py reels/v2_13_since_when.js --out <existing.mp4> --audio-only                    # rebuild audio only (e.g. new VO)
python3 engine/qc.py v2_13_since_when                                                                     # QC gates
python3 engine/audit_text.py reels/v2_13_since_when.js                                                    # text-safety audit
```

Mastering targets −14 LUFS with a −1.5 dBTP limiter ceiling; the AAC encode is then re-checked and trimmed until the encoded true peak is ≤ −1.05 dBTP. If a mix loses loudness in that step (AAC adds inter-sample overs), set a lower ceiling in the reel's `R.setup({ ceiling: -2.8 })` (V2-07 does), or `BFYP_CEILING=-2.8` for one run.

## Swapping the fallback voice for ElevenLabs Adam
1. Generate each line of `reels/<reel>.vo.json` with Adam (Compelling). Keep the text identical.
2. Place each line at its `t0` (the edit is timed to these starts; a take may run up to ~10% longer before the next line).
3. Export mono 48 kHz WAV to the path in `"wav"` and update `sha256` + `provenance`.
4. Run the `--audio-only` command above, then `engine/qc.py` (the intelligibility gate re-checks the final mix).
