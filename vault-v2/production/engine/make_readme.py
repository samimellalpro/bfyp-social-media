#!/usr/bin/env python3
"""BFYP Vault V2 — README / index generator (reads vault-v2/manifest.json)."""
import json
import os

VAULT = "/home/user/bfyp-social-media/vault-v2"
MAN = M = json.load(open(os.path.join(VAULT, "manifest.json")))
R = M["reels"]

lots = {1: "Proof over posts", 2: "Your research stack is broken", 3: "Bad market habits"}
n_k = sum(1 for r in R if r.get("karaoke"))
n_f = sum(1 for r in R if r["voice"]["gender"] == "F")
voices = {}
for r in R:
    voices.setdefault(r["voice"]["id"], []).append(r["id"][3:])
dur = [r["duration_s"] for r in R]
lu = [r["lufs_i"] for r in R]
tp = [r["true_peak_dbtp"] for r in R]
size = sum(r["size_mb"] for r in R)

M = lambda v, f: format(v, f).replace("-", "−")  # true minus sign

L = []
LOCKED = MAN.get("status") == "LOCKED"
L.append("# BFYP VAULT V2 — 30 Reels, " + ("LOCKED · V2 CLOSED 🔒\n" if LOCKED else "READY\n"))
L.append("New stock of 30 Instagram/TikTok-style Reels for BetterForYourPocket, to be published **after 30 Sep 2026**. "
         "Nothing here is scheduled: the Buffer queue, `public/social/buffer/` and any planned distribution were not touched.\n")
if LOCKED:
    L.append(f"**Status: 🔒 LOCKED — V2 CLOSED on {MAN['locked']}.** No new render, re-mix or repackaging without Sami's explicit request. "
             "The final double red team (aesthetic + accuracy) is in [`RED-TEAM.md`](RED-TEAM.md); every file's sha256 is in [`LOCK.md`](LOCK.md) and `manifest.json`.\n")
L.append(f"**{sum(1 for r in R if r['status'] in ('READY', 'LOCKED'))}/30 {'LOCKED' if LOCKED else 'READY'}** · 30/30 with a directed English voice-over (BFYP-K2: {n_f} female / {30 - n_f} male, {len(voices)} voices, see below) · "
         f"30 EN · {min(dur):.1f}–{max(dur):.1f} s · {M(min(lu), '.1f')} to {M(max(lu), '.1f')} LUFS · true peak ≤ {M(max(tp), '.2f')} dBTP · {size:.0f} MB total\n")
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
L.append("- `V2-XX_slug.md`: the deliverable sheet with internal title, angle, beat-by-beat script and on-screen text, voice (gender, voice, direction) and voice-over lines, sources, "
         "BFYP assets with capture times, illustrations, Instagram caption, X caption, hashtags, CTA, optional sources comment, and the QC report\n")
L.append("File names are content-addressed (`-<first 10 hex of sha256>`), like the rest of this repo. `manifest.json` lists every file with its full sha256. "
         "`VO-QC.md` gives the voice, sync and mix figures of every reel. `archive/` keeps superseded versions (the French V2-30).\n")
L.append("## Index\n")
L.append("| # | Reel | Lot | Voice | Length | Opening hook (from 0 s) |\n|---|---|---|---|---:|---|")
for r in R:
    v = r["voice"]
    fmt = f"{'♀' if v['gender'] == 'F' else '♂'} {v['id']}" + (" · karaoke" if r.get("karaoke") else "")
    L.append(f"| {r['id']} | [{r['title']}]({r['sheet']}) | {r['lot']} | {fmt} | {r['duration_s']:.1f} s | {r['hook']} |")
L.append("")
L.append("Lots: " + " · ".join(f"**{k}** {v}" for k, v in lots.items()) + ".\n")
if LOCKED:
    RTM = MAN["red_team"]
    L.append(f"## Final red team and lock ({RTM['date']})\n")
    L.append("Before the lock, all 30 reels went through a last double red team: **RT1 aesthetic calibration** (contact sheets, full-size zooms on every product screen and spotlight, "
             "voice naturalness/intelligibility/sync, text-safety audit) and **RT2 accuracy** (every figure, date, quote, filing and outside claim re-checked; time-sensitive facts re-verified online on "
             f"{RTM['date']}; every BFYP demo checked against its capture; plan claims against the Pricing captures). Only real defects were fixed; a reel that passed both was not touched.\n")
    L.append(f"- **{30 - len(RTM['fixed_and_rechecked'])} reels PASS/PASS**, untouched: video, cover and sheet are byte-identical to before the red team.")
    L.append(f"- **{len(RTM['fixed_and_rechecked'])} reels fixed, then re-checked (all PASS)**:")
    for r in R:
        if r["red_team"]["fixed"]:
            what = "aesthetic" if r["red_team"]["aesthetic"] == "FAIL" else "data"
            L.append(f"  - {r['id']} ({what}): {r['red_team']['fix']}")
    L.append("- **Sami's review-page notes**: V2-11 and V2-19 (À CORRIGER) and the V2-08 voice note were fixed as above. The V2-06 note came with a VALIDÉ verdict and was kept. "
             "“À poster ASAP” on V2-17 was not acted on: nothing is published from this vault before 30 Sep 2026.")
    L.append("- **SHA-256**: the 30 videos and 30 covers were re-hashed and match `manifest.json`; 21 videos and all 30 covers are unchanged since the pre-red-team package. "
             "`python3 production/engine/lock_vault.py verify` re-checks them, and `production/engine/package.py` refuses to repackage the locked vault.\n")
L.append("## Review page\n")
L.append("The final review runs on a private claude.ai page that plays the 30 VO reels on a phone and records a VALIDÉ / À CORRIGER verdict and a note per reel "
         "(voice, gender and direction shown for each). `review.html` is the same review for a local checkout of this branch: it loads the videos and covers from `READY/` next to it, "
         "and its verdicts stay in the browser (text recap or JSON export).\n")
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
L.append("- **Mix**: master at −14 LUFS integrated. True peak is ≤ −1 dBTP measured on the encoded AAC. Every reel has sound from frame 0 and ends on a clean fade for seamless loops. "
         "Music and SFX duck dynamically under the voice only while it speaks (music −8 to −12 dB, an extra carve at 1–4.5 kHz, SFX −5 to −9 dB), so the voice sits 8.4–9.5 LU above the bed.")
L.append("- **Legibility**: large type (≥ 44 px body, 84–190 px headlines), short lines, and a spotlight + callout on every product detail. "
         "A browser-layout audit checks every text element every 0.1 s: nothing leaves the frame and nothing sits under the right-hand Reels buttons (x > 960 px, y 1100–1760 px).\n")
L.append("## Voice-over: BFYP-K2, a directed English voice on all 30 reels\n")
L.append("Every reel now carries an English voice-over written and directed for that reel. It is not one uniform read: each reel has its own intent, delivery, pace, energy, pauses and emphasis "
         "(listed in its sheet, in French for the reviewer). The narration is anchored to the frozen edit: lines land on the cuts, zooms, reveals and the CTA card, and they complement the picture "
         "instead of reading the on-screen text.\n")
L.append("- **Local and free only**: Kokoro-82M v1.0 (Apache-2.0) run offline through kokoro-onnx. Stock native-English voices, one weighted blend of two stock voices, no cloning, no paid service.")
L.append(f"- **Palette of {len(voices)} recurring voices, {n_f} female / {30 - n_f} male reels**, picked from a 34-voice casting scored for naturalness (UTMOS, out of 5):\n")
L.append("| Voice | Gender | Accent | Kokoro | Register | Reels |\n|---|---|---|---|---|---|")
REG = {"K2-F1": "analytical, calm, precise", "K2-F2": "correspondent, journalistic", "K2-F3": "host, bright and friendly",
       "K2-M1": "peer, conversational / POV", "K2-M2": "signal, low and tense (data alerts)", "K2-M3": "British explainer, dry wit"}
seen = {}
for r in R:
    seen.setdefault(r["voice"]["id"], r["voice"])
for vid, v in sorted(seen.items()):
    k = v["kokoro"] if isinstance(v["kokoro"], str) else " + ".join(f"{n} {w:.1f}" for n, w in v["kokoro"].items())
    L.append(f"| {vid} | {'female' if v['gender'] == 'F' else 'male'} | {'US' if v['lang'] == 'en-us' else 'UK'} | `{k}` | {REG.get(vid.split(' ')[0], '')} | {', '.join(voices[vid])} ({len(voices[vid])}) |")
L.append("")
L.append(f"- **Karaoke reels ({n_k})**: V2-13, 18, 19, 24, 27, 28 and 29 show their words on screen as they are spoken. They keep the same words in the same slots; only the voice, the delivery and the mix changed. "
         "Their end card already said “AI voice” and still does. The other reels were not given that mention: their visual edit is frozen.")
L.append("- **Frozen edits**: the video stream of every VO reel is bit-identical to its validated edit (stream MD5 compared). V2-30 was converted to English (screens, cover, captions) before its voice was added. "
         "The final red team re-rendered the edits of V2-02, V2-19, V2-23 and V2-30 to fix real defects (see RED-TEAM.md); their mixes copy the new edits bit for bit.")
L.append("- **QC gates, per reel**: on the isolated voice, speech recognition (Whisper small.en) recovers ≥ 97 % of the script, naturalness UTMOS ≥ 4.0 on average and ≥ 3.6 on every line, every line fits its window "
         "(karaoke: within ±4 % of its slot), no overlaps. On the final file, speech recognition on the full mix ≥ 0.95, voice ≥ 7 LU over the bed, −14 ±1 LUFS, true peak ≤ −1 dBTP, video identical.")
L.append("- **QC report**: `VO-QC.md`, one row per reel: naturalness, speech recognition on the voice and on the final mix, voice over the bed, loudness, true peak, identical video, lines landing on the edit, CTA timing, karaoke slot error.")
L.append("- **Rebuild a voice**: edit `production/vo2/specs/<reel>.py`, then `engine/vo2.py build <reel>`, `engine/vo2.py mix <reel> <out.mp4>` and `engine/vo2.py qc <reel> <out.mp4>`.\n")
L.append("## Blockers met, and what was done\n")
L.append("1. **Network policy** blocked betterforyourpocket.com, google.com, sec.gov, elevenlabs.io and image hosts. "
         "Workaround: the vault uses the real screens already captured on 23 Sep 2026, each stamped with its capture time. Facts were verified through web search against primary sources. "
         "Charts are built from verified numbers instead of downloading third-party images. "
         "To enable fresh captures or ElevenLabs next time, allow those domains in the cloud environment's network settings.")
L.append("2. **Voice**: ElevenLabs was out of reach (network policy and a failed subscription payment). By decision, every voice is now made with a local, free TTS (BFYP-K2, above).")
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
L.append("- **Voice-over pass:** 4 prototypes (2 female, 2 male) were validated before the other 26. The first builds were too dense for their windows: scripts were cut to about 3 words/s and re-timed to the edit. "
         "The British voice speaks slower, so its lines were rewritten shorter. “BFYP” was said as four stopped letters; it is now one quick acronym. "
         "Speech recognition caught lines a listener could mishear (“hype a stock” heard as “hyper stock”, “sends” heard as “send”); they were reworded. "
         "An old pronunciation rule made the voice spell “NVIDIA” as “en-V-I-D”; the engine's own reading is used now. "
         "Lines that only repeated the on-screen text were rewritten to add something the picture does not say.")
L.append("- **Audio encoding of the VO mixes:** ffmpeg's AAC encoder added short noise bursts (up to 8 dB above the source) to 3 mixes, and on V2-29 the limiter missed inter-sample peaks, so the master stopped at −15 LUFS. "
         "Each encode is now decoded and compared with its source, window by window. The encoder runs without noise substitution, and a 320 kb/s or 19.5 kHz setting is used when a burst remains. "
         "The master lowers its limiter when it detects inter-sample overs. All 26 new mixes were redone with this chain; the 4 validated prototypes were checked and have no burst.")
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
L.append("- **Fact precision:** the Dow drop is shown as “~140 points” because sources give 130–145. V2-02 says “allegations · criminal case pending” and “As alleged by the SEC. The related criminal case is pending.” "
         "(one of the eight pleaded guilty in 2023; the indictment of the other seven was dismissed in March 2024, reinstated by the 5th Circuit in October 2025, trial set for May 2027). FinanceBench is labelled “one test setup, 2023 models”. Plan wording matches the pricing page verbatim, e.g. “(= 7 reports)”.\n")
L.append("## Posting notes\n")
L.append("- Publish from **1 Oct 2026** onward. The screens are dated 23 Sep 2026 and the stamp says so, which suits the V2-29 “timestamps” message.")
ORDER = ["V2-14", "V2-01", "V2-11", "V2-21", "V2-12", "V2-02", "V2-23", "V2-04", "V2-15", "V2-26", "V2-10", "V2-22", "V2-18", "V2-03", "V2-07",
         "V2-27", "V2-16", "V2-19", "V2-24", "V2-05", "V2-13", "V2-25", "V2-09", "V2-17", "V2-28", "V2-08", "V2-20", "V2-29", "V2-06", "V2-30"]
L.append("- Suggested order, one per day. It mixes the lots and keeps similar reels at least two slots apart "
         "(Smart Money: 21/22/23/24 · Today: 04/12/25/26/27/29 · AI: 03/15/16/20 · pricing: 05/16/17 · ETF: 07/10/18): " + " → ".join(ORDER) + ".")
L.append("- For reels that cite outside facts, the sheet has an optional first comment listing the sources.")
L.append("- Pricing and plan details are as of 23 Sep 2026 (re-checked against the Pricing captures on 25 Sep 2026; a live check was not possible because the production environment cannot reach the site). "
         "Re-check `/pricing` before posting V2-05, V2-16 and V2-17.\n")
L.append("## Reproduce / edit\n")
L.append("`production/` contains the engine (`engine/`: renderer, motion + component library, synth/DSP music engine, directed VO `vo2.py`, QC, packaging), "
         "the 30 scene scripts (`reels/`), the karaoke caption timings (`reels/*.vo.json`), the directed voice-over scripts (`vo2/specs/`) and edit maps (`vo2/maps/`), the slate with scripts and captions (`plan/plan.py`), "
         "the verified-facts log (`research/facts.md`) and the 1× crops of the real screens (`assets/screens/`). "
         "`engine/qc.py` (technical gates), `engine/audit_text.py` (text safety) and `engine/audit_k.py` (keyframe overlaps) re-check any edit. See `production/README.md`.\n")
open(os.path.join(VAULT, "README.md"), "w").write("\n".join(L))
print("README written")
