# V2-20 — Fast doesn’t matter if it’s wrong

**Status: ✅ READY** · Lot 2 — Your research stack is broken · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-20_financebench-76ac9a26de.mp4` — 21.00 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 10.46 MB |
| Cover | `V2-20_financebench_cover-38ff566a8d.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Directed voice-over over the text-led edit · Stat hook → traced answers |
| Music | Original, synthesized for this reel: dnb · 170 BPM · E minor (no samples, no licensed audio) |
| Voice | **BFYP-K2 · K2-F2 · Correspondent** — female, native English (en-gb) · Kokoro-82M v1.0, local and free (Apache-2.0), stock voice `bf_emma` · no cloning · directed for this reel (see Voice direction) |
| On-screen “AI voice” label | No — visual edit frozen, unchanged |
| Opening hook (from 0 s) | “81% wrong or refused.” |
| CTA | Answers you can audit. → betterforyourpocket.com |

## Angle / problem
A benchmark on SEC filings found a top AI setup wrong or refusing 81% of the time. Finance needs receipts.

## Script / on-screen text (beat by beat)
1. HOOK — '81%' → 'of questions about SEC filings: answered wrong or refused.' (GPT-4-Turbo + retrieval · FinanceBench, Patronus AI, Nov 2023)
2. WHY IT HURTS — 'Fast. Fluent. Unchecked.'
3. TURN — 'Finance needs receipts.'
4. BFYP — 'Start from the filing': NVDA fundamentals as filed, swept card by card: Revenue $215.9B · Net income $120.1B · Total assets $206.8B · Total liabilities $49.5B — each 'FY2026 · period ended 2026-01-25 · 10-K · SEC EDGAR'
5. PAYOFF — 'Four figures. Four receipts.'
6. CTA — 'Answers you can audit.'

## Voice direction (FR)
- **Intention** : Rapporter une étude sérieuse avec un euphémisme britannique, puis montrer l'antidote : partir du dépôt officiel.
- **Interprétation** : Correspondante crédible : factuelle, pince-sans-rire sur « It didn't go well ».
- **Rythme** : Vif (montage à 170 bpm) mais articulé ; laisse les trois coups « Fast. Fluent. Unchecked. » sans voix.
- **Énergie** : Moyenne, plus ferme sur « Sounding right isn't being right ».
- **Pauses** : Silence sur les trois impacts, silence sur « Four figures. Four receipts. ».
- **Accents** : « tested », « didn't go well », « four in five », « isn't », « ten-K », « source », « filing »

## Voice-over (as rendered) — narration anchored to the edit (cuts, zooms, reveals, CTA)
| start | end | line | lands on (note, FR) |
|---:|---:|---|---|
| 0.12 s | 2.91 s | Researchers tested an AI on SEC filings. | hook : 81 % · FinanceBench, Patronus AI, nov. 2023 |
| 3.08 s | 4.22 s | It didn't go well. | euphémisme avant la citation |
| 4.45 s | 6.88 s | More than four in five: wrong, or refused. | citation verbatim de l'étude (81 %) |
| 9.62 s | 11.39 s | Sounding right isn't being right. | « Finance needs receipts. » (silence avant, sous « Fast. Fluent. Unchecked. ») |
| 11.50 s | 13.70 s | Here, every figure comes from the 10-K. | écran réel NVDA as filed · zooms REVENUE / NET INCOME |
| 14.00 s | 15.35 s | Each one, with its source. | zooms TOTAL ASSETS / TOTAL LIABILITIES |
| 17.15 s | 20.12 s | Start from the filing. BetterForYourPocket.com | carte CTA « Answers you can audit. » (silence avant, sous « Four figures. Four receipts. ») |

Isolated-voice QC: ASR word match 1.000 (gate ≥ 0.97) · naturalness UTMOS mean 4.26 / min 4.05 (gates ≥ 4.0 / ≥ 3.6) · 3.48 words/s while speaking · every line inside its window → **PASS**. VO file sha256 `ee57baebe01f1da4…`

Mix: dynamic ducking (music −11.8 dB, extra −4.0 dB carve at 1–4.5 kHz, SFX −9.3 dB, only while the voice speaks) · voice 9.5 LU over the bed (gate ≥ 7) · ASR on the final mix 1.000 (gate ≥ 0.95)

## Sources used (external, verified)
- FinanceBench: A New Benchmark for Financial Question Answering (Patronus AI, arXiv 2311.11944) — 20 Nov 2023 — https://arxiv.org/abs/2311.11944
- NVIDIA — Financial results for Q4 and fiscal 2026 (fiscal year ended 25 Jan 2026) — 25 Feb 2026 — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- NVIDIA FY2026 Form 10-K (SEC EDGAR) — FY ended 25 Jan 2026 — https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm

## BFYP assets used (real product, no mockups)
- `nvda_fund` — Stocks · NVDA: annual fundamentals as filed · real screen captured **2026-09-23 22:01 UTC** · crop of a frame of `public/social/buffer/reels/nvda_record_reel-3266dcd4d2.mp4` (approved Vault V1 reel)

## Illustrations (labelled on screen where they could be mistaken for real)
- Quote card reproducing the FinanceBench abstract sentence verbatim (dated, attributed)

## Cover
`V2-20_financebench_cover-38ff566a8d.png` — cover line: “81% wrong or refused.”

## Caption — Instagram
```text
81% wrong or refused. 🤖📉

In the FinanceBench study (Patronus AI, Nov 2023), GPT-4-Turbo with a retrieval system incorrectly answered or refused 81% of sample questions about public-company filings. (One test setup, 2023 models.)

Fast doesn't matter if it's wrong.

On BFYP, company figures come as filed: every number with its period and the 10-K it came from. Four figures, four receipts. Then ask AI Research, with the evidence attached.
→ betterforyourpocket.com

#AI #LLM #fintech #investing #SEC #research

Educational market data. Not financial advice.
```

## Caption — X
```text
FinanceBench (2023): GPT-4-Turbo + retrieval got 81% of SEC-filing questions wrong or refused.

Start from the filing: every figure with its period and its 10-K → betterforyourpocket.com
```

## Hashtags
#AI #LLM #fintech #investing #SEC #research

## First comment (sources, optional)
```text
Sources: FinanceBench: A New Benchmark for Financial Question Answering (Patronus AI, arXiv 2311.11944) (20 Nov 2023) · NVIDIA — Financial results for Q4 and fiscal 2026 (fiscal year ended 25 Jan 2026) (25 Feb 2026) · NVIDIA FY2026 Form 10-K (SEC EDGAR) (FY ended 25 Jan 2026)
```

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 21.00 s |
| Loudness | −14.3 LUFS integrated (target −14) · true peak −1.5 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−12 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 3984 kb/s · 10.46 MB |
| Video stream | bit-identical to the validated edit (stream MD5 compared) — yes |
| Voice intelligibility on the final mix | ASR word match 1.000 (gate ≥ 0.95) |
| Voice over the bed | 9.5 LU (gate ≥ 7) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “81% wrong or refused.”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (hit×5, swish×4, click×4, glitch×2, impact×2, pop×2, ding×2, riser×1, scan×1, whoosh×1, sparkle×1) + directed voice-over (BFYP-K2, female)
- [x] Voice-over complements the picture instead of reading the on-screen text

**Verdict: READY**
