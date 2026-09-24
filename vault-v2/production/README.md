# BFYP Vault V2 — production sources

Everything needed to re-render or edit the 30 Reels in `../READY/`.

## Layout
- `engine/render_v2.py` — renderer: scene script (`reels/*.js`) → frames (headless Chromium, 30 fps, adaptive motion blur, dither) → H.264; audio (music + SFX + optional VO) → master (−14 LUFS, encoded true peak ≤ −1 dBTP) → MP4 + cover PNG.
- `engine/web/` — `brand.css` (BFYP tokens: #080e0d background, #17b58a green, Inter + Geist Mono), `motion.js` (deterministic keyframe engine), `components.js` (real-screen frames, capture stamps, spotlight tours, callouts, quote cards, CTA card, karaoke captions, covers).
- `engine/music.py`, `engine/instruments.py`, `engine/dsp.py` — original music/SFX synthesis (no samples) and mastering chain.
- `engine/vo2.py` — directed voice-over “BFYP-K2”: one spec per reel (`vo2/specs/<reel>.py`: voice from the 6-voice palette, direction, mix, lines anchored to the edit), Kokoro-82M v1.0 via kokoro-onnx (offline), voice chain + levelling, build QC (Whisper ASR, UTMOS naturalness, window/slot fit), audio-only mix with dynamic ducking, final-file QC. `engine/vo2_batch.sh` / `engine/vo2_mixqc.sh` run it over several reels; `engine/vo2_status.py` shows what is built, mixed and QC'd; `engine/vo2_sync.py` audits each line against the edit map; `engine/make_vo_qc.py` writes `VO-QC.md`.
- `engine/edit_map.py` — edit map of a reel (cuts, text reveals, zooms, sound cues, CTA) → `vo2/maps/<reel>.txt`, used to anchor each voice line. `engine/make_karaoke_specs.py` — specs of the 7 karaoke reels from their caption timings (same words, same slots). `engine/vo_cast.py` — the voice casting (UTMOS).
- `engine/vo.py` — voice QC helpers (pronunciation map, Whisper small.en word match via sherpa-onnx, F0) and the original “BFYP-K1” builder that set the karaoke caption timings (`reels/*.vo.json`).
- `engine/qc.py` — technical QC gates. `engine/audit_text.py` — text-safety audit: browser layout checked every 0.1 s, flags text off-frame or under the right-hand Reels buttons. `engine/audit_k.py` — lists opacity keyframes that overlap on one element (the engine merges them). `engine/package.py`, `engine/make_readme.py`, `engine/overview.py` and `engine/make_review.py` — vault packaging, README, covers overview and the local review page (`review.html`).
- `reels/v2_XX_slug.js` — one scene script per Reel (timeline in beats); `reels/*.vo.json` — caption timings of the 7 karaoke reels (the words and slots the voice keeps).
- `vo2/specs/*.py` — the 30 voice-over scripts and directions; `vo2/maps/*.txt` — the 30 edit maps; `vo2/SpeechMOS/speechmos_utmos.py` — loader for the UTMOS22 strong naturalness model (MIT; code from tarepan/SpeechMOS, weights `utmos22_strong_step7459_v1.pt` from its v1.0.0 GitHub release).
- `plan/plan.py` — slate: angles, scripts, captions (IG/X), hashtags, CTA, sources.
- `research/facts.md` — verified external facts with sources.
- `assets/screens/*.png` — 1× crops of the real BFYP screens (captured 23 Sep 2026), `catalog.json` (source file + capture time for each crop), `regions.json` (named regions used by the spotlight tours). Run `python3 engine/upscale_2x.py` to rebuild the `@2x` files the renderer loads.

## Requirements
Python 3.11 with `numpy scipy pillow opencv-python-headless playwright pyloudnorm imageio-ffmpeg` (+ `kokoro-onnx soundfile librosa sherpa-onnx torch` for voice and its QC), Chromium (Playwright), ffmpeg with libx264, and fonts Inter + Geist Mono (Google Fonts, OFL) in `/opt/bfyp/fonts` (paths are set at the top of `render_v2.py`).

## Commands
```bash
python3 engine/render_v2.py reels/v2_14_whale_alert.js --out out/v2_14.mp4 --cover out/v2_14_cover.png   # full render
python3 engine/render_v2.py reels/v2_14_whale_alert.js --out out/v2_14.mp4 --fast out/v2_14_preview       # 3 fps layout sheet
python3 engine/render_v2.py reels/v2_13_since_when.js --out <existing.mp4> --audio-only                    # rebuild audio only (e.g. new VO)
python3 engine/qc.py v2_13_since_when                                                                     # QC gates
python3 engine/audit_text.py reels/v2_13_since_when.js                                                    # text-safety audit
```

Mastering targets −14 LUFS with a −1.5 dBTP limiter ceiling; the AAC encode is then re-checked and trimmed until the encoded true peak is ≤ −1.05 dBTP. If a mix loses loudness in that step (AAC adds inter-sample overs), set a lower ceiling in the reel's `R.setup({ ceiling: -2.8 })` (V2-07 does), or `BFYP_CEILING=-2.8` for one run.

## Directed voice-over (BFYP-K2)
```bash
python3 engine/edit_map.py reels/v2_14_whale_alert.js > vo2/maps/v2_14_whale_alert.txt   # edit map (+ vo2/maps/*.json): where each line can land
python3 engine/vo2.py build v2_14_whale_alert                    # voice from vo2/specs/v2_14_whale_alert.py -> vo2/out/ (+ build QC)
python3 engine/vo2.py mix v2_14_whale_alert vo2/final/v2_14_whale_alert/v2_14_whale_alert_VO.mp4   # validated edit + this voice
python3 engine/vo2.py qc v2_14_whale_alert vo2/final/v2_14_whale_alert/v2_14_whale_alert_VO.mp4    # final-file QC
```
- A line is `{"at": start, "until": latest end, "text": script, "say": synthesis text (optional), "speed", "gain_db", "note"}`; karaoke lines add `"fit_to"` (the slot length). A line that does not fit is sped up by at most 10 %; beyond that, rewrite it.
- Build gates: ASR word match ≥ 0.97 on the isolated voice, UTMOS mean ≥ 4.0 and every line ≥ 3.6, every line inside its window (karaoke: ±4 % of its slot), no overlap.
- The mix copies the validated MP4 and rebuilds only its audio (same music and SFX, deterministic), ducking music and SFX while the voice speaks. Final gates: video stream bit-identical to the validated edit, ASR ≥ 0.95 on the full mix, voice ≥ 7 LU over the bed, −14 ±1 LUFS, true peak ≤ −1 dBTP.
- `"legacy_pron": True` in a spec keeps the exact synthesis path of the 4 validated prototypes (dotted acronyms); new specs say “BFYP” as one quick acronym.
