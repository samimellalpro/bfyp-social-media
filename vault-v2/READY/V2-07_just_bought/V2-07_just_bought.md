# V2-07 — “Just bought” — just?

**Status: ✅ READY** · Lot 1 — Proof over posts · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-07_just_bought-8b2e1509a8.mp4` — 20.80 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 9.32 MB |
| Cover | `V2-07_just_bought_cover-bcaa852730.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Directed voice-over over the text-led edit · Timeline explainer → two dates on a fund page |
| Music | Original, synthesized for this reel: synthwave · 108 BPM · E minor (no samples, no licensed audio) |
| Voice | **BFYP-K2 · K2-M3 · Brit** — male, native English (en-gb) · Kokoro-82M v1.0, local and free (Apache-2.0), stock voice blend `bm_george 0.6 + bm_fable 0.4` · no cloning · directed for this reel (see Voice direction) |
| On-screen “AI voice” label | No — visual edit frozen, unchanged |
| Opening hook (from 0 s) | “Big fund just bought $XYZ!” “Just”? |
| CTA | Check both dates. → betterforyourpocket.com |

## Angle / problem
Holdings disclosures are lagged. 'Just bought' can mean months ago. Check the period and the filing date.

## Script / on-screen text (beat by beat)
1. HOOK — typical post (illustration): 'This fund just bought it!' → 'Just?'
2. TIMELINE — 'Quarter ends 30 Jun' → '13F due within 45 days' → 'You see it mid-August'
3. WHY IT HURTS — 'The trade itself could be from April.'
4. RULE — Form 13F: filed within 45 days after quarter end; holdings as of quarter end (Investor.gov)
5. BFYP — SPY fund page prints two dates: period 2026-06-30 · filed 2026-08-28 (spotlight)
6. CTA — 'Check both dates.'

## Voice direction (FR)
- **Intention** : Démonter le « just » : expliquer simplement le calendrier des déclarations et montrer les deux dates sur BFYP.
- **Interprétation** : Pédagogue et posé, avec un humour britannique discret (« Mind the gap »).
- **Rythme** : Mesuré, un temps sur « weeks later » et sur « months old ».
- **Énergie** : Calme, sûre, un clin d'œil sur « Mind the gap ».
- **Pauses** : Un temps après « By the time you see it ».
- **Accents** : « Not so fast », « weeks later », « months old », « period », « filed », « gap »

## Voice-over (as rendered) — narration anchored to the edit (cuts, zooms, reveals, CTA)
| start | end | line | lands on (note, FR) |
|---:|---:|---|---|
| 0.12 s | 1.95 s | Just bought? Not so fast. | hook : post type « Big fund just bought $XYZ! » (illustration) |
| 3.05 s | 6.31 s | It's a snapshot from quarter-end, filed weeks later. | frise 1 APR → 30 JUN → ~14 AUG (13F : 45 jours) |
| 6.85 s | 9.39 s | By the time you see it, it could be months old. | « You see it mid-August. The trade could be from April. » |
| 11.72 s | 14.93 s | BFYP shows the period, and the filing date. | écran réel SPY · zooms PERIOD (30 Jun) / FILED (28 Aug) |
| 15.10 s | 16.27 s | Mind the gap. | zoom THE GAP |
| 16.90 s | 20.30 s | Always check both dates. BetterForYourPocket.com | carte CTA |

Isolated-voice QC: ASR word match 0.980 (gate ≥ 0.97) · naturalness UTMOS mean 4.38 / min 4.32 (gates ≥ 4.0 / ≥ 3.6) · 3.24 words/s while speaking · every line inside its window → **PASS**. VO file sha256 `aa228461058a941e…`

Mix: dynamic ducking (music −10.4 dB, extra −4.0 dB carve at 1–4.5 kHz, SFX −7.4 dB, only while the voice speaks) · voice 9.5 LU over the bed (gate ≥ 7) · ASR on the final mix 0.980 (gate ≥ 0.95)

## Sources used (external, verified)
- Investor.gov — Form 13F (filed within 45 days of quarter end) — current — https://www.investor.gov/introduction-investing/investing-basics/glossary/form-13f-reports-filed-institutional-investment

## BFYP assets used (real product, no mockups)
- `spy_cards` — ETF · SPY: net assets / holdings / filed · real screen captured **2026-09-23 21:38 UTC** · crop of `public/social/buffer/carousels/s5_etf-2bb66040d5.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Generic post labelled “TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT” (@example handle)
- 13F timeline graphic (45-day rule)

## Cover
`V2-07_just_bought_cover-bcaa852730.png` — cover line: “Just bought it”? Check the date.

## Caption — Instagram
```text
“This fund just bought it!” Just? ⏳

Big-fund holdings reports (Form 13F) show positions as of quarter end, and they can be filed up to 45 days later. A June quarter can surface in mid-August, and the trade itself could be from April.

“Just bought” can mean months ago.

Every BFYP fund page prints both dates: the period the holdings describe and the day the filing went public.
→ betterforyourpocket.com

#investing #stocks #ETF #13F #hedgefunds #SEC

Educational market data. Not financial advice.
```

## Caption — X
```text
“Fund just bought X” — often a 13F: holdings as of quarter end, filed up to 45 days later.

Always check two dates: the period and the filing date → betterforyourpocket.com
```

## Hashtags
#investing #stocks #ETF #13F #hedgefunds #SEC

## First comment (sources, optional)
```text
Sources: Investor.gov — Form 13F (filed within 45 days of quarter end) (current)
```

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 20.80 s |
| Loudness | −14.2 LUFS integrated (target −14) · true peak −2.9 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−13 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3586 kb/s · 9.32 MB |
| Video stream | bit-identical to the validated edit (stream MD5 compared) — yes |
| Voice intelligibility on the final mix | ASR word match 0.980 (gate ≥ 0.95) |
| Voice over the bed | 9.5 LU (gate ≥ 7) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “Big fund just bought $XYZ!” “Just”?
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (tick×3, hit×3, swish×3, click×3, impact×2, notif×1, riser×1, ding×1, scan×1, whoosh×1, pop×1, sparkle×1) + directed voice-over (BFYP-K2, male)
- [x] Voice-over complements the picture instead of reading the on-screen text

**Verdict: READY**
