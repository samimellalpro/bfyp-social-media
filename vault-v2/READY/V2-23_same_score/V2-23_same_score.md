# V2-23 — Same score. Not the same thing.

**Status: ✅ READY** · Lot 3 — Bad market habits · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-23_same_score-6affc62dc1.mp4` — 20.40 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 7.57 MB |
| Cover | `V2-23_same_score_cover-a54c4a3ee3.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Directed voice-over over the text-led edit · Spot the difference (split screen) |
| Music | Original, synthesized for this reel: synthwave · 106 BPM · C minor (no samples, no licensed audio) |
| Voice | **BFYP-K2 · K2-F1 · Analyst** — female, native English (en-us) · Kokoro-82M v1.0, local and free (Apache-2.0), stock voice `af_heart` · no cloning · directed for this reel (see Voice direction) |
| On-screen “AI voice” label | No — visual edit frozen, unchanged |
| Opening hook (from 0 s) | “31/100 vs 31/100. Same score?” |
| CTA | Scores with their confidence. → betterforyourpocket.com |

## Angle / problem
Two identical scores with different confidence are not equal. Read the badge.

## Script / on-screen text (beat by beat)
1. HOOK — split screen: '31/100' | '31/100' → 'Same score?'
2. REVEAL — badges: 'ESTIMATED' vs 'HIGH CONFIDENCE' (real leaderboard rows 6 and 7)
3. PAYOFF — 'Same number. Different confidence.'
4. LESSON — 'Read the badge, not just the number.'
5. CTA — 'Scores with their confidence.'

## Voice direction (FR)
- **Intention** : Un jeu des différences : deux scores identiques, deux niveaux de confiance ; la leçon tient en deux phrases.
- **Interprétation** : Analyste calme qui fait remarquer un détail, avec un léger sourire sur la révélation.
- **Rythme** : Lent et net (106 bpm), chaque badge annoncé sur son surlignage.
- **Énergie** : Basse-moyenne, curiosité sur « Look closer », assurance sur la leçon.
- **Pauses** : Un temps entre « only half the story » et « The other half is the badge ».
- **Accents** : « both thirty-one », « real », « estimated », « more certain », « half », « badge »

## Voice-over (as rendered) — narration anchored to the edit (cuts, zooms, reveals, CTA)
| start | end | line | lands on (note, FR) |
|---:|---:|---|---|
| 0.12 s | 1.70 s | Two wallets, both thirty-one. | hook : WALLET A 31/100 | WALLET B 31/100 |
| 2.55 s | 4.85 s | These are two real rows from the leaderboard. | Wallet #6 / Wallet #7 (écran réel) |
| 5.70 s | 6.47 s | Estimated. | surlignage badge ESTIMATED (impact) |
| 6.86 s | 8.61 s | And this one? Much more certain. | surlignage HIGH CONFIDENCE (ding) |
| 10.35 s | 12.06 s | A score is only half the story. | « Same number. Different confidence. » |
| 12.65 s | 14.06 s | The other half is the badge. | « Read the badge, not just the number. » |
| 16.05 s | 18.99 s | Always read both. BetterForYourPocket.com | carte CTA « Scores with their confidence. » |

Isolated-voice QC: ASR word match 1.000 (gate ≥ 0.97) · naturalness UTMOS mean 4.38 / min 3.99 (gates ≥ 4.0 / ≥ 3.6) · 3.45 words/s while speaking · every line inside its window → **PASS**. VO file sha256 `17dc179bb242b5b4…`

Mix: dynamic ducking (music −11.2 dB, extra −4.0 dB carve at 1–4.5 kHz, SFX −8.2 dB, only while the voice speaks) · voice 9.4 LU over the bed (gate ≥ 7) · ASR on the final mix 1.000 (gate ≥ 0.95)

## Sources used (external, verified)
- None needed: every claim in this reel is shown on the real BFYP screens below.

## BFYP assets used (real product, no mockups)
- `sm_rows_678` — Smart Money leaderboard: rows 6-8 · real screen captured **2026-09-23 21:38 UTC** · crop of `public/social/buffer/carousels/s4_smart-b1474793d1.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Two neutral 31/100 score cards (hook), then crops of the two real leaderboard rows

## Cover
`V2-23_same_score_cover-a54c4a3ee3.png` — cover line: “Same score. Not the same thing.”

## Caption — Instagram
```text
31/100 vs 31/100. Same score? 👀

Not the same thing. On BFYP's Smart Money leaderboard one is marked ESTIMATED, the other HIGH CONFIDENCE.

Same number, different confidence. Read the badge, not just the number.
→ betterforyourpocket.com

#crypto #smartmoney #onchain #data #investing #trading

Educational market data. Not financial advice.
```

## Caption — X
```text
Two wallets, both 31/100. One ESTIMATED, one HIGH CONFIDENCE.

Read the badge, not just the number → betterforyourpocket.com
```

## Hashtags
#crypto #smartmoney #onchain #data #investing #trading

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 20.40 s |
| Loudness | −14.1 LUFS integrated (target −14) · true peak −1.6 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−12 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 2969 kb/s · 7.57 MB |
| Video stream | bit-identical to the validated edit (stream MD5 compared) — yes |
| Voice intelligibility on the final mix | ASR word match 1.000 (gate ≥ 0.95) |
| Voice over the bed | 9.4 LU (gate ≥ 7) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “31/100 vs 31/100. Same score?”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (whoosh×4, impact×2, hit×2, pop×2, ding×1, sparkle×1) + directed voice-over (BFYP-K2, female)
- [x] Voice-over complements the picture instead of reading the on-screen text

**Verdict: READY**
