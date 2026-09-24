# V2-29 — Why every screen we post is timestamped

**Status: ✅ READY** · Lot 3 — Bad market habits · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-29_timestamps-d24baad097.mp4` — 27.43 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 11.15 MB |
| Cover | `V2-29_timestamps_cover-c9974d6b07.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Voice-led · Brand manifesto |
| Music | Original, synthesized for this reel: trap · 144 BPM · D minor (no samples, no licensed audio) |
| Voice | Fallback synthetic voice **BFYP-K1** (Kokoro-82M, local, blend am_michael 0.60 + am_onyx 0.25 + am_puck 0.15, speed 0.92). Replace with ElevenLabs Adam when the account is back; timings in `production/reels/v2_29_timestamps.vo.json`. |
| Opening hook (from 0 s) | “Every screenshot starts aging the second it’s taken.” |
| CTA | See today's version live. → betterforyourpocket.com |

## Angle / problem
Screenshots age instantly. We stamp ours so you know when, and check the live page for now.

## Script / on-screen text (beat by beat)
1. HOOK — 'Every screenshot starts aging the second it's taken.' (a real Today card slowly desaturates, age counter ticking)
2. PROOF — same BFYP Today page, 46 minutes apart: '330 observations' (21:28 UTC) vs '354 observations' (22:14 UTC)
3. PROOF — counter 330 → 354: 'Same page. Same day. Different number.'
4. BFYP — 'That's why every screen we post carries its capture time.' Capture pills fly in: 21:28 · 21:38 · 21:39 · 22:01 · 22:09 · 22:14 UTC
5. TRUTH — 'By the time you watch this, the live page has moved on.'
6. CTA — 'Check the live page.'

## Voice-over (as rendered)
| start | end | line |
|---:|---:|---|
| 0.15 s | 3.26 s | Every screenshot starts aging the second it's taken. |
| 3.96 s | 8.08 s | Same BFYP Today page. Forty-six minutes apart. |
| 8.75 s | 13.26 s | Three hundred thirty observations. Then three hundred fifty-four. |
| 13.96 s | 17.15 s | That's why every screen we post carries its capture time. |
| 17.71 s | 21.07 s | By the time you watch this, the live page has moved on. |
| 21.67 s | 26.02 s | So check the live page. Free, at BetterForYourPocket.com. |

Isolated-voice QC: word match 1.000 · 2.83 words/s · median F0 109.4 Hz · F0 spread 7.9 st · min pause 0.56 s · no clipping → **PASS**. VO file sha256 `2ada85099adad96f…`

## Sources used (external, verified)
- None needed: every claim in this reel is shown on the real BFYP screens below.

## BFYP assets used (real product, no mockups)
- `today_lines` — Today: observed lines · real screen captured **2026-09-23 21:28 UTC** · crop of `public/social/buffer/carousels/s2_today-560a5b13cf.png`
- `today_head` — Today: headline: 354 observations in the last 24h · BFYP data card captured **2026-09-23 22:14 UTC** · crop of `public/social/buffer/fresh/today_story-68bc826c3a.png`
- `whale_card` — Whale Activity: LIT large transfer card · real screen captured **2026-09-23 21:38 UTC** · crop of `public/social/buffer/carousels/s3_whales-1ae56a5c01.png`
- `nvda_filings4` — Stocks · NVDA: recent filings (4 rows) · real screen captured **2026-09-23 21:39 UTC** · crop of `public/social/buffer/carousels/s6_stocks-3955eff09a.png`
- `spy_page` — ETF · SPY: page top: cards, asset mix, top holdings 1-13 · real screen captured **2026-09-23 22:01 UTC** · crop of a frame of `public/social/buffer/reels/BFYP_REEL_15_FINAL-9c99d7a370.mp4` (approved Vault V1 reel)
- `ai_ask` — ETF · SPY: Ask BFYP about this · real screen captured **2026-09-23 22:09 UTC** · crop of `public/social/buffer/carousels/g3_context-f554c41ec8.png`
- `today_cats` — Today: category counts card · BFYP data card captured **2026-09-23 22:14 UTC** · crop of `public/social/buffer/fresh/today_story-68bc826c3a.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Animated “age” counter
- 330 → 354 counter using the two real captures

## Cover
`V2-29_timestamps_cover-c9974d6b07.png` — cover line: “Every screenshot starts aging.”

## Caption — Instagram
```text
Every screenshot starts aging the second it's taken. ⏱️

Same BFYP Today page, 46 minutes apart: 330 observations, then 354. That's why every BFYP screen we post carries its capture time, down to the minute (these were captured 23 Sep 2026, UTC).

By the time you watch this, the live pages have moved on. That's the point: check the live page, not our screenshot.
→ betterforyourpocket.com

#investing #data #fintech #crypto #stocks #transparency

Educational market data. Not financial advice.
```

## Caption — X
```text
Every screenshot starts aging the second it's taken. We timestamp ours to the minute.

Check the live page, not the screenshot → betterforyourpocket.com
```

## Hashtags
#investing #data #fintech #crypto #stocks #transparency

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 27.43 s |
| Loudness | −14.3 LUFS integrated (target −14) · true peak −1.6 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−16 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3250 kb/s · 11.15 MB |
| Voice intelligibility on the final mix | ASR word match 1.000 (gate ≥ 0.95) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “Every screenshot starts aging the second it’s taken.”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (tick×6, click×6, whoosh×3, shutter×1, ding×1, ticks×1, pop×1, sparkle×1)

**Verdict: READY**
