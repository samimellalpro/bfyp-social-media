# V2-13 — “Whales are buying.” Since when?

**Status: ✅ READY** · Lot 2 — Your research stack is broken · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-13_since_when-1a6649b072.mp4` — 25.17 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 10.47 MB |
| Cover | `V2-13_since_when_cover-0491d6e303.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Voice-led · Interrogation → windows montage |
| Music | Original, synthesized for this reel: garage · 130 BPM · C minor (no samples, no licensed audio) |
| Voice | Fallback synthetic voice **BFYP-K1** (Kokoro-82M, local, blend am_michael 0.60 + am_onyx 0.25 + am_puck 0.15, speed 0.92). Replace with ElevenLabs Adam when the account is back; timings in `production/reels/v2_13_since_when.vo.json`. |
| Opening hook (from 0 s) | “Whales are buying!” Since when? |
| CTA | Numbers with a timeframe. → betterforyourpocket.com |

## Angle / problem
A number without a time window is noise. Every BFYP figure carries its window.

## Script / on-screen text (beat by beat)
1. HOOK — typical post (illustration): '🐋 Whales are buying! 🚀' + VO → 'Since when?'
2. WHY IT HURTS — 'A number without a timeframe is just noise.'
3. BFYP — 'On BFYP, every number carries its window.' (Today card)
4. BFYP — window montage on real screens: 24 HOURS (Today: 'in the last 24h') · 7 DAYS (Smart Money: '7-day census') · 30 DAYS (Smart Money: '(30D)') · 2 HOURS AGO (Whale Activity: 'observed 2 hours ago')
5. PAYOFF — 'If it has no window, it's a vibe.'
6. CTA — 'Numbers with a timeframe.'

## Voice-over (as rendered)
| start | end | line |
|---:|---:|---|
| 0.15 s | 1.30 s | Whales are buying. |
| 1.85 s | 2.78 s | Since when? |
| 3.46 s | 6.13 s | A number without a timeframe is just noise. |
| 6.69 s | 10.23 s | On BFYP, every number carries its window. |
| 10.85 s | 13.77 s | Twenty-four hours. Seven days. Thirty days. |
| 14.31 s | 15.97 s | Observed, two hours ago. |
| 16.62 s | 18.68 s | If it has no window, it's a vibe. |
| 19.38 s | 23.77 s | Numbers with a timeframe. Free, at BetterForYourPocket.com. |

Isolated-voice QC: word match 1.000 · 2.95 words/s · median F0 109.4 Hz · F0 spread 8.14 st · min pause 0.54 s · no clipping → **PASS**. VO file sha256 `e6d7c526b37c59b7…`

## Sources used (external, verified)
- None needed: every claim in this reel is shown on the real BFYP screens below.

## BFYP assets used (real product, no mockups)
- `today_lines` — Today: observed lines · real screen captured **2026-09-23 21:28 UTC** · crop of `public/social/buffer/carousels/s2_today-560a5b13cf.png`
- `sm_page` — Smart Money: page top: disclaimer, asset consensus, wallet list · real screen captured **2026-09-23 21:38 UTC** · crop of a frame of `public/social/buffer/reels/BFYP_REEL_13_FINAL-f2d9cf7600.mp4` (approved Vault V1 reel)
- `whale_card` — Whale Activity: LIT large transfer card · real screen captured **2026-09-23 21:38 UTC** · crop of `public/social/buffer/carousels/s3_whales-1ae56a5c01.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Generic post labelled “TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT” (@example handle)

## Cover
`V2-13_since_when_cover-0491d6e303.png` — cover line: “Whales are buying.” Since when?

## Caption — Instagram
```text
“Whales are buying.” Since when? 🐋⏱️

A number without a timeframe is just noise. Buying since an hour ago? A month? Which wallets?

On BFYP every figure carries its window: “in the last 24h”, “7-day census”, “30D”, “observed 2 hours ago”.

If it has no window, it's a vibe.
→ betterforyourpocket.com

#crypto #whales #onchain #bitcoin #investing #smartmoney

Educational market data. Not financial advice.
```

## Caption — X
```text
“Whales are buying.” Since when?

On BFYP every number carries its window: 24h, 7-day, 30D, observed time → betterforyourpocket.com
```

## Hashtags
#crypto #whales #onchain #bitcoin #investing #smartmoney

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 25.17 s |
| Loudness | −14.8 LUFS integrated (target −14) · true peak −1.6 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−11 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3327 kb/s · 10.47 MB |
| Voice intelligibility on the final mix | ASR word match 1.000 (gate ≥ 0.95) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “Whales are buying!” Since when?
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (hit×6, swish×4, click×4, impact×2, glitch×2, notif×1, ding×1, whoosh×1, pop×1, sparkle×1)

**Verdict: READY**
