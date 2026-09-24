# V2-18 — $1.67 trillion. Whose?

**Status: ✅ READY** · Lot 2 — Your research stack is broken · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-18_whose_trillion-77b458a7f8.mp4` — 28.40 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 11.51 MB |
| Cover | `V2-18_whose_trillion_cover-5552c8f363.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Voice-led · Myth → fact |
| Music | Original, synthesized for this reel: minimal · 120 BPM · D minor (no samples, no licensed audio) |
| Voice | Fallback synthetic voice **BFYP-K1** (Kokoro-82M, local, blend am_michael 0.60 + am_onyx 0.25 + am_puck 0.15, speed 0.92). Replace with ElevenLabs Adam when the account is back; timings in `production/reels/v2_18_whose_trillion.vo.json`. |
| Hook (≤ 1.5 s) | “VOO: $1.67 trillion?” |
| CTA | Know what a number covers. → betterforyourpocket.com |

## Angle / problem
The same fund number can cover different scopes. Know what a number covers.

## Script / on-screen text (beat by beat)
1. HOOK — 'VOO:' + counter to '$1.67T' + '?' → 'Not exactly.'
2. FACT — 'VOO is one share class of the Vanguard 500 Index Fund.' (Vanguard prospectus)
3. FACT — diagram of the fund's four share classes: Investor · ETF (VOO) · Admiral · Institutional Select (2026 semi-annual report; not to scale)
4. BFYP — VOO card tour: 'FUND NET ASSETS $1671.23B · period 2026-06-30' → 'whole fund, all share classes' → the scope sits next to the number
5. PAYOFF — 'BFYP labels what every number covers.'
6. CTA — 'Know what a number covers.'

## Voice-over (as rendered)
| start | end | line |
|---:|---:|---|
| 0.15 s | 3.55 s | VOO: $1.67 trillion? |
| 4.25 s | 5.37 s | Not exactly. |
| 6.00 s | 10.83 s | VOO is one share class of the Vanguard 500 Index Fund. |
| 11.50 s | 13.45 s | That fund has four share classes. |
| 14.00 s | 17.91 s | The $1.67 trillion covers the whole fund. |
| 18.50 s | 22.04 s | BFYP labels what every number covers. |
| 22.75 s | 26.97 s | Know what a number covers. Free, at BetterForYourPocket.com. |

Isolated-voice QC: word match 1.000 · 2.83 words/s · median F0 110.7 Hz · F0 spread 7.1 st · min pause 0.55 s · no clipping → **PASS**. VO file sha256 `c48aac823309e7b1…`

## Sources used (external, verified)
- Vanguard S&P 500 ETF prospectus (ETF share class of Vanguard 500 Index Fund) — 28 Apr 2026 — https://fund-docs.vanguard.com/p968.pdf
- Vanguard 500 Index Fund semi-annual report (four share classes) — 2026 — https://www.sec.gov/Archives/edgar/data/0000036405/000110465926102240/tm2620528d8_ncsrs.htm

## BFYP assets used (real product, no mockups)
- `voo_cards` — ETF · VOO: fund net assets / holdings / filed (incl. capture pill) · real screen captured **2026-09-23 22:01 UTC** · crop of `public/social/buffer/carousels/e3_voo-99fee83f3f.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Share-class diagram labelled “not to scale”, per the fund’s 2026 semi-annual report
- Animated counter to $1.67T

## Cover
`V2-18_whose_trillion_cover-5552c8f363.png` — cover line: “$1.67 trillion. Whose?”

## Caption — Instagram
```text
VOO: $1.67 trillion? Not exactly. 🔍

VOO is the ETF share class of the Vanguard 500 Index Fund, which has four share classes. The $1,671.23B in the fund's filing (period 30 Jun 2026) is the whole fund, all share classes.

Same number, different scope.

BFYP labels what every figure covers, right next to the number.
→ betterforyourpocket.com

#VOO #ETF #vanguard #SP500 #investing #indexfunds

Educational market data. Not financial advice.
```

## Caption — X
```text
VOO = one share class of the Vanguard 500 Index Fund. The $1.67T in its N-PORT covers the whole fund, all share classes.

Know what a number covers → betterforyourpocket.com
```

## Hashtags
#VOO #ETF #vanguard #SP500 #investing #indexfunds

## First comment (sources, optional)
```text
Sources: Vanguard S&P 500 ETF prospectus (ETF share class of Vanguard 500 Index Fund) (28 Apr 2026) · Vanguard 500 Index Fund semi-annual report (four share classes) (2026)
```

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 28.40 s |
| Loudness | -14.3 LUFS integrated (target −14) · true peak -1.6 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (-10 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3240 kb/s · 11.51 MB |
| Voice intelligibility on the final mix | ASR word match 1.000 (gate ≥ 0.95) |
| All gates | **PASS** |

### Editorial
- [x] Hook readable within 1.5 s: “VOO: $1.67 trillion?”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (pop×5, swish×3, click×3, impact×2, ticks×1, wrong×1, ding×1, whoosh×1, sparkle×1)

**Verdict: READY**
