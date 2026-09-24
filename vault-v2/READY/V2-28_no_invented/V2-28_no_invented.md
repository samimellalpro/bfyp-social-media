# V2-28 — We won’t invent a consensus

**Status: ✅ READY** · Lot 3 — Bad market habits · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-28_no_invented-9c65317ef6.mp4` — 26.73 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 11.73 MB |
| Cover | `V2-28_no_invented_cover-a343f8fe82.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Voice-led · Empty-state manifesto |
| Music | Original, synthesized for this reel: cinematic · 88 BPM · G minor (no samples, no licensed audio) |
| Voice | Fallback synthetic voice **BFYP-K1** (Kokoro-82M, local, blend am_michael 0.60 + am_onyx 0.25 + am_puck 0.15, speed 0.92). Replace with ElevenLabs Adam when the account is back; timings in `production/reels/v2_28_no_invented.vo.json`. |
| Opening hook (from 0 s) | “No data? Then show nothing.” |
| CTA | Data that doesn't pretend. → betterforyourpocket.com |

## Angle / problem
When there's no data, the honest output is nothing. BFYP says so instead of inventing a number.

## Script / on-screen text (beat by beat)
1. HOOK — 'No data? Then show nothing.' + an honest empty consensus box
2. WHY IT HURTS — 'A guess dressed up as data is worse than a blank.' + an invented '87% consensus' card stamped MADE UP (illustration of what not to do)
3. BFYP — Smart Money page, verbatim: 'When no scored wallet was active, we say so instead of inventing a consensus.' (spotlight on the real line)
4. BFYP — Today: 'A group with none in it is not shown.' (spotlight)
5. PAYOFF — 'Empty is an answer.'
6. CTA — 'Data that doesn't pretend.'

## Voice-over (as rendered)
| start | end | line |
|---:|---:|---|
| 0.15 s | 1.96 s | No data? Then show nothing. |
| 2.73 s | 5.67 s | A guess dressed up as data is worse than a blank. |
| 6.48 s | 8.72 s | The Smart Money page puts it plainly: |
| 9.55 s | 14.66 s | When no scored wallet was active, we say so instead of inventing a consensus. |
| 15.34 s | 18.13 s | On Today, a group with none in it is not shown. |
| 18.75 s | 20.18 s | Empty is an answer. |
| 20.80 s | 25.31 s | Data that doesn't pretend. Free, at BetterForYourPocket.com. |

Isolated-voice QC: word match 0.984 · 3.12 words/s · median F0 108.2 Hz · F0 spread 7.8 st · min pause 0.62 s · no clipping → **PASS**. VO file sha256 `ad8fbc0143792abd…`

## Sources used (external, verified)
- None needed: every claim in this reel is shown on the real BFYP screens below.

## BFYP assets used (real product, no mockups)
- `sm_page` — Smart Money: page top: disclaimer, asset consensus, wallet list · real screen captured **2026-09-23 21:38 UTC** · crop of a frame of `public/social/buffer/reels/BFYP_REEL_13_FINAL-f2d9cf7600.mp4` (approved Vault V1 reel)
- `today_cats` — Today: category counts card · BFYP data card captured **2026-09-23 22:14 UTC** · crop of `public/social/buffer/fresh/today_story-68bc826c3a.png`
- BFYP wording reproduced as text (quoted verbatim on screen, over the real line): “When no scored wallet was active, we say so instead of inventing a consensus.” — source: `sm_page` — Smart Money: page top: disclaimer, asset consensus, wallet list · real screen captured **2026-09-23 21:38 UTC** · crop of a frame of `public/social/buffer/reels/BFYP_REEL_13_FINAL-f2d9cf7600.mp4` (approved Vault V1 reel)

## Illustrations (labelled on screen where they could be mistaken for real)
- Empty-state box (graphic)
- An invented “87% consensus” card stamped MADE UP and labelled “Invented number · illustration of what not to do”

## Cover
`V2-28_no_invented_cover-a343f8fe82.png` — cover line: “We won’t invent a consensus.”

## Caption — Instagram
```text
When there's no data, what does your dashboard show? 🫥

BFYP's Smart Money page: “When no scored wallet was active, we say so instead of inventing a consensus.”

Today page: “A group with none in it is not shown.”

Empty is an answer. Data that doesn't pretend.
→ betterforyourpocket.com

#data #crypto #smartmoney #investing #fintech #onchain

Educational market data. Not financial advice.
```

## Caption — X
```text
“When no scored wallet was active, we say so instead of inventing a consensus.”

Empty is an answer → betterforyourpocket.com
```

## Hashtags
#data #crypto #smartmoney #investing #fintech #onchain

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 26.73 s |
| Loudness | −14.3 LUFS integrated (target −14) · true peak −1.8 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−9 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3510 kb/s · 11.73 MB |
| Voice intelligibility on the final mix | ASR word match 0.984 (gate ≥ 0.95) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “No data? Then show nothing.”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (swish×2, click×2, impact×1, stamp×1, ding×1, hit×1, whoosh×1, pop×1, sparkle×1)

**Verdict: READY**
