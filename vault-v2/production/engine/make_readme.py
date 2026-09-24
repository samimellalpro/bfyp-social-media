#!/usr/bin/env python3
"""BFYP Vault V2 — README / index generator (reads vault-v2/manifest.json)."""
import json
import os

VAULT = "/home/user/bfyp-social-media/vault-v2"
M = json.load(open(os.path.join(VAULT, "manifest.json")))
R = M["reels"]

lots = {1: "Proof over posts", 2: "Your research stack is broken", 3: "Bad market habits"}
n_vo = sum(1 for r in R if r["format"].startswith("voice"))
dur = [r["duration_s"] for r in R]
lu = [r["lufs_i"] for r in R]
tp = [r["true_peak_dbtp"] for r in R]
size = sum(r["size_mb"] for r in R)

M = lambda v, f: format(v, f).replace("-", "−")  # true minus sign

L = []
L.append("# BFYP VAULT V2 — 30 Reels, READY\n")
L.append("New stock of 30 Instagram/TikTok-style Reels for BetterForYourPocket, to be published **after 30 Sep 2026**. "
         "Nothing here is scheduled: the Buffer queue, `public/social/buffer/` and any planned distribution were not touched.\n")
L.append(f"**Status: {sum(1 for r in R if r['status'] == 'READY')}/30 READY** · {30 - n_vo} text-led · {n_vo} voice-led (fallback voice, see below) · "
         f"29 EN + 1 FR · {min(dur):.1f}–{max(dur):.1f} s · {M(min(lu), '.1f')} to {M(max(lu), '.1f')} LUFS · true peak ≤ {M(max(tp), '.2f')} dBTP · {size:.0f} MB total\n")
L.append("Every reel follows **problem → why it hurts → proof → BFYP solution → CTA**, uses only real BFYP screens "
         "(captured 23 Sep 2026, capture time stamped on screen), cites verifiable external sources where it uses any outside fact, "
         "and ends on the CTA plus “Educational market data. Not financial advice.”\n")
OV = sorted(f for f in os.listdir(VAULT) if f.startswith("covers_overview-") and f.endswith(".jpg"))
if OV:
    L.append(f"![All 30 covers, V2-01 to V2-30]({OV[-1]})\n")
L.append("## How to use\n")
L.append("Each folder in `READY/` contains:\n")
L.append("- `V2-XX_slug-<sha>.mp4`: the final Reel (1080×1920, 30 fps, H.264 High, AAC 48 kHz stereo, −14 LUFS, ≤ −1 dBTP)")
L.append("- `V2-XX_slug_cover-<sha>.png`: the cover (1080×1920; key text sits inside the 3:4 profile-grid area)")
L.append("- `V2-XX_slug.md`: the deliverable sheet with internal title, angle, beat-by-beat script and on-screen text, voice-over (if any), sources, "
         "BFYP assets with capture times, illustrations, Instagram caption, X caption, hashtags, CTA, optional sources comment, and the QC report\n")
L.append("File names are content-addressed (`-<first 10 hex of sha256>`), like the rest of this repo. `manifest.json` lists every file with its full sha256.\n")
L.append("## Index\n")
L.append("| # | Reel | Lot | Format | Length | Opening hook (from 0 s) |\n|---|---|---|---|---:|---|")
for r in R:
    fmt = "Voice (fallback)" if r["format"].startswith("voice") else "Text-led"
    lang = " · FR" if r["lang"] == "FR" else ""
    L.append(f"| {r['id']} | [{r['title']}]({r['sheet']}) | {r['lot']} | {fmt}{lang} | {r['duration_s']:.1f} s | {r['hook']} |")
L.append("")
L.append("Lots: " + " · ".join(f"**{k}** {v}" for k, v in lots.items()) + ".\n")
L.append("## Production standard\n")
L.append("- **Real product only**: 21 BFYP assets. 19 are crops of real product screens (Today, Whale Activity, Smart Money, Stocks/NVDA, ETF/SPY and VOO, AI Research, Pricing). "
         "2 are crops of BFYP’s own Today data card, labelled “BFYP Today data” on screen. All come from the captures of 23 Sep 2026 (21:28–22:14 UTC) already in this repo, "
         "and each is stamped on screen with its capture time. No mockups and no invented figures.")
L.append("- **External facts**: SEC, U.S. DOJ, FTC, FINRA Foundation/CFA Institute, NVIDIA investor relations, Vanguard, court records (Mata v. Avianca), "
         "Reuters/CNBC (AP hack, 2013) and the FinanceBench paper. Each claim is quoted or paraphrased with its source and date on screen, and listed in the reel sheet. "
         "Anything that is only alleged is labelled as such (V2-02).")
L.append("- **Illustrations** (typical posts, alerts, chats, receipts) use `@example` handles and say “ILLUSTRATION · NOT A REAL ACCOUNT”. They never imitate a real brand or person.")
L.append("- **Music and sound**: every track is original and synthesized for its reel (tech house, UK garage, trap, future bass, synthwave, minimal, amapiano-lite, drum & bass, cinematic). "
         "No samples and no licensed audio. The edit is cut to the beat, with sound design on the moments that matter (impacts, whooshes, risers, dings, clicks, stamps, glitches).")
L.append("- **Mix**: master at −14 LUFS integrated. True peak is ≤ −1 dBTP measured on the encoded AAC. Every reel has sound from frame 0 and ends on a clean fade for seamless loops.")
L.append("- **Legibility**: large type (≥ 44 px body, 84–190 px headlines), short lines, and a spotlight + callout on every product detail. "
         "A browser-layout audit checks every text element every 0.1 s: nothing leaves the frame and nothing sits under the right-hand Reels buttons (x > 960 px, y 1100–1760 px).\n")
L.append("## Voice-over: ElevenLabs “Adam” was not available\n")
L.append("This environment could not reach `api.elevenlabs.io` (network policy), and the BFYP MARKETING session reported that the ElevenLabs subscription has a failed payment. "
         f"As instructed for this case, **{n_vo} reels use the local fallback voice “BFYP-K1”** (Kokoro-82M v1.0, Apache-2.0, run offline; blend of stock voices am_michael 0.60 + am_onyx 0.25 + am_puck 0.15, speed 0.92; no voice cloning). "
         "The other 23 reels are text-led by design.\n")
L.append("The end card of these reels says “AI voice” (honest disclosure, still accurate after a swap to Adam). "
         "Each fallback take passed objective QC gates: word match ≥ 0.97, 2.30–3.30 words/s, median F0 85–120 Hz, pitch spread ≥ 6.4 st, pauses at sentence ends, no clipping. "
         "Intelligibility was re-checked by speech recognition on the final mix with music (≥ 0.95).\n")
L.append("**To swap in Adam later:** generate the same lines with ElevenLabs Adam (Compelling), then fit them to the timings in `production/reels/<reel>.vo.json`. "
         "Re-run `production/engine/render_v2.py <reel>.js --out <mp4> --audio-only` to rebuild the audio. The video stays identical.\n")
L.append("## Blockers met, and what was done\n")
L.append("1. **Network policy** blocked betterforyourpocket.com, google.com, sec.gov, elevenlabs.io and image hosts. "
         "Workaround: the vault uses the real screens already captured on 23 Sep 2026, each stamped with its capture time. Facts were verified through web search against primary sources. "
         "Charts are built from verified numbers instead of downloading third-party images. "
         "To enable fresh captures or ElevenLabs next time, allow those domains in the cloud environment's network settings.")
L.append("2. **ElevenLabs unavailable**: fallback voice on 7 reels, as described above.")
L.append("3. **No video toolchain in the image**: installed a static ffmpeg (x264/AAC) and headless Chromium rendering. The whole pipeline is in `production/`.\n")
L.append("## Self-QC: what was rejected or reworked before READY\n")
L.append("- **V2-14 pilot v1 rejected.** The hook frame was too sparse, the cover had no product and the callout text was too small. It was rebuilt with larger type, a product visual on the cover and spotlight tours.")
L.append("- **V2-04, V2-06 and V2-20 payoffs rebuilt for distinctness.** They repeated the same Today / AI Research shots as other reels. New payoffs: "
         "BFYP’s verbatim “Nothing here is a prediction.” (V2-04), a “built on” triptych of Today, Whales and Stocks (V2-06), and a four-figures / four-receipts sweep of NVIDIA’s as-filed numbers (V2-20).")
L.append("- **Layout bugs fixed:** the FAKE stamp leaking into later scenes (V2-01); orphaned words in hooks (V2-11, V2-20); lines overflowing the safe edge (V2-11, V2-12, V2-15, V2-23, V2-29); "
         "an unreadable full-table zoom replaced by targeted zooms (V2-10); a checklist page not clearing (V2-17); strike-through that missed wrapped lines (V2-27); "
         "callouts colliding with capture stamps, fixed by rebuilding the split screen (V2-23); a coin covering text (V2-24).")
L.append("- **Engine bugs fixed before the final renders:** the spotlight ring snapped back to the first target between steps. "
         "In voice-led hooks, karaoke words not yet spoken were pre-scaled and ate the spaces between words (“ThreeForm144filings”); "
         "V2-19 and V2-24 were re-rendered with the fix.")
L.append("- **Voice-reel end card:** the small print said “voice: synthetic (fallback)”, which is internal jargon. It now reads “AI voice”; 6 reels were re-rendered.")
L.append("- **Hook clarity:** V2-26 opened on a lone small dot, the sparsest first second in the vault; it now has a heartbeat radar pulse. "
         "V2-12 relied on a GREEN/RED flicker for ~2 s before naming the problem. It now says “Your dashboard, all day:” from frame 0. "
         "The V2-18 cover crop clipped an in-screen capture pill and was tightened.")
L.append("- **Text-safety audit (added late, caught real defects):** the capture caption under product screens ran past the right edge in 20 reels "
         "(a third of it off-frame in V2-21 and V2-24). A few source lines ran long, including one in V2-18 by ~300 px. Subtitles and some source lines sat under the like/comment buttons. "
         "Fixes: shorter captions (“Real BFYP screen · page · date · time UTC”), long sources split onto two lines, and subtitles narrowed to 840 px. "
         "28 reels were re-rendered, and the audit now reports nothing off-frame or under the buttons.")
L.append("- **Quote accuracy:** every BFYP sentence shown as text was checked word for word against its capture. V2-04 showed a shortened line labelled “Verbatim”. "
         "It now shows BFYP’s exact footer, “Observed activity, as counted by BFYP. Nothing here is a prediction.”, with more time on screen (the reel went from 20.6 to 22.0 s). "
         "Four sheets listed a screen the reel never shows; the lists now match what is on screen.")
L.append("- **Keyframe audit:** repeated opacity keyframes on the same element are merged by the engine. In V2-04 and V2-05 this made a screen caption fade back in after its screen had left. "
         "Both were fixed. A new check (`engine/audit_k.py`) lists every such overlap, and the rest are intentional.")
L.append("- **Audio:** after AAC encoding, 4 reels had a true peak above −1 dBTP, and `-shortest` muxing clipped the tail on 3. "
         "The mux was rebuilt (exact duration + encoded-peak guard) and all 30 reels were remastered and re-verified.")
L.append("- **Fact precision:** the Dow drop is shown as “~140 points” because sources give 130–145. V2-02 says “allegations · criminal case pending” "
         "(dismissed in March 2024, reinstated by the 5th Circuit in October 2025). FinanceBench is labelled “one test setup, 2023 models”. Plan wording matches the pricing page verbatim, e.g. “(= 7 reports)”.\n")
L.append("## Posting notes\n")
L.append("- Publish from **1 Oct 2026** onward. The screens are dated 23 Sep 2026 and the stamp says so, which suits the V2-29 “timestamps” message.")
ORDER = ["V2-14", "V2-01", "V2-11", "V2-21", "V2-12", "V2-02", "V2-23", "V2-04", "V2-15", "V2-26", "V2-10", "V2-22", "V2-18", "V2-03", "V2-07",
         "V2-27", "V2-16", "V2-19", "V2-24", "V2-05", "V2-13", "V2-25", "V2-09", "V2-17", "V2-28", "V2-08", "V2-20", "V2-29", "V2-06", "V2-30"]
L.append("- Suggested order, one per day. It mixes the lots and keeps similar reels at least two slots apart "
         "(Smart Money: 21/22/23/24 · Today: 04/12/25/26/27/29 · AI: 03/15/16/20 · pricing: 05/16/17 · ETF: 07/10/18): " + " → ".join(ORDER) + ".")
L.append("- For reels that cite outside facts, the sheet has an optional first comment listing the sources.")
L.append("- Pricing and plan details are as of 23 Sep 2026. Re-check `/pricing` before posting V2-05, V2-16 and V2-17.\n")
L.append("## Reproduce / edit\n")
L.append("`production/` contains the engine (`engine/`: renderer, motion + component library, synth/DSP music engine, fallback VO, QC, packaging), "
         "the 30 scene scripts (`reels/`), the voice-over timings (`reels/*.vo.json`), the slate with scripts and captions (`plan/plan.py`), "
         "the verified-facts log (`research/facts.md`) and the 1× crops of the real screens (`assets/screens/`). "
         "`engine/qc.py` (technical gates), `engine/audit_text.py` (text safety) and `engine/audit_k.py` (keyframe overlaps) re-check any edit. See `production/README.md`.\n")
open(os.path.join(VAULT, "README.md"), "w").write("\n".join(L))
print("README written")
