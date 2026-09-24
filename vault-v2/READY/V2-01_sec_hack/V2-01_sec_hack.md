# V2-01 — Even the SEC got faked

**Status: ✅ READY** · Lot 1 — Proof over posts · EN · publish **after 30 Sep 2026** (not scheduled, not in Buffer)

| | |
|---|---|
| Reel (final) | `V2-01_sec_hack-70e4d2b55a.mp4` — 21.40 s · 1080×1920 · 30 fps · H.264 High · AAC 48 kHz stereo · 11.4 MB |
| Cover | `V2-01_sec_hack_cover-1642fba06e.png` — 1080×1920 (key text inside the 3:4 grid-safe area) |
| Format | Directed voice-over over the text-led edit · News timeline → real filing list |
| Music | Original, synthesized for this reel: cinematic · 90 BPM · D minor (no samples, no licensed audio) |
| Voice | **BFYP-K2 · K2-F2 · Correspondent** — female, native English (en-gb) · Kokoro-82M v1.0, local and free (Apache-2.0), stock voice `bf_emma` · no cloning · directed for this reel (see Voice direction) |
| On-screen “AI voice” label | No — visual edit frozen, unchanged |
| Opening hook (from 0 s) | “The SEC’s own account posted fake news.” |
| CTA | Read the filing, not the post. → betterforyourpocket.com |

## Angle / problem
A post is not a source — even an official account was hijacked. Go to the filing.

## Script / on-screen text (beat by beat)
1. HOOK — 'The SEC's own account posted fake news.' + quoted post (9 Jan 2024, 4:11 pm ET): 'Today the SEC grants approval for #Bitcoin ETFs…' — stamped FAKE
2. PROOF — 'Bitcoin rose $1,000+. Then fell $2,000+.' (per U.S. DOJ)
3. PROOF — 4:26 pm ET, Gensler: 'The @SECGov twitter account was compromised… The SEC has not approved…'
4. TWIST — 'The real approval came the next day — in an official SEC order.'
5. WHY IT HURTS — 'If an official account can be faked, any post can.'
6. BFYP — NVDA recent filings, each dated and linked to SEC.gov (spotlight)
7. CTA — 'Read the filing, not the post.' → betterforyourpocket.com

## Voice direction (FR)
- **Intention** : Raconter sobrement un fait réel et daté, puis en tirer la leçon : un post n'est pas une source, un dépôt officiel oui.
- **Interprétation** : Sobre et crédible, presque un bulletin d'info : faits datés et attribués, pas d'adjectifs.
- **Rythme** : Régulier (environ 3 mots/s), phrases courtes et affirmatives.
- **Énergie** : Neutre et posée. Un peu plus chaleureuse sur la solution BFYP.
- **Pauses** : Silences volontaires sous « If an official account can be faked… » et sous « Posts can be faked. Filings are the record. », pour que ces phrases portent seules.
- **Accents** : « own account », « fifteen minutes », « hack », « next day », « dated », « original »

## Voice-over (as rendered) — narration anchored to the edit (cuts, zooms, reveals, CTA)
| start | end | line | lands on (note, FR) |
|---:|---:|---|---|
| 0.10 s | 2.60 s | The SEC's own account posts this. | hook, fake post + FAKE stamp (date is on the card) |
| 2.84 s | 5.07 s | Bitcoin jumps, then drops two thousand. | +$1,000 then −$2,000 (per U.S. DOJ); 'drops' lands near the 3.8 s reveal |
| 5.54 s | 7.50 s | Fifteen minutes later: a hack. | Gensler correction |
| 7.86 s | 9.37 s | Real approval? Next day. | timeline 9 → 10 Jan |
| 10.90 s | 12.69 s | Here, each filing is dated, | BFYP, zoom DATED (silence under 'any post can' before it) |
| 12.78 s | 14.23 s | and linked to the original. | zoom LINKED |
| 16.95 s | 20.36 s | Read the filing, not the post. BetterForYourPocket.com | CTA (silence under 'Posts can be faked.') |

Isolated-voice QC: ASR word match 0.977 (gate ≥ 0.97) · naturalness UTMOS mean 4.32 / min 4.29 (gates ≥ 4.0 / ≥ 3.6) · 3.17 words/s while speaking · every line inside its window → **PASS**. VO file sha256 `b48ff3279d44c789…`

Mix: dynamic ducking (music −12.1 dB, extra −4.0 dB carve at 1–4.5 kHz, SFX −9.1 dB, only while the voice speaks) · voice 9.4 LU over the bed (gate ≥ 7) · ASR on the final mix 0.977 (gate ≥ 0.95)

## Sources used (external, verified)
- SEC — SECGov X Account (unauthorized post, 9 Jan 2024) — Jan 2024 — https://www.sec.gov/secgov-x-account
- Gary Gensler post, 9 Jan 2024, 4:26 pm ET — 9 Jan 2024 — https://x.com/GenslerArchive/status/1744833049064288387
- U.S. DOJ — sentencing in SEC X account hack (BTC moves: +$1,000 / -$2,000 per BTC) — 16 May 2025 — https://www.justice.gov/opa/pr/alabama-man-sentenced-14-months-connection-securities-and-exchange-commission-x-hack-spiked
- SEC — Gensler statement on spot bitcoin ETP approval — 10 Jan 2024 — https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023

## BFYP assets used (real product, no mockups)
- `nvda_filings5` — Stocks · NVDA: recent filings (5 rows incl. N-PX) · real screen captured **2026-09-23 22:01 UTC** · crop of `public/social/buffer/stories/st_n3_filings-9bd9209208.png`

## Illustrations (labelled on screen where they could be mistaken for real)
- Quote cards in neutral BFYP styling reproducing the unauthorized @SECGov post and Gary Gensler’s correction verbatim, with date, time and source (no platform branding)
- Timeline graphic (9 Jan fake post → 10 Jan official order)

## Cover
`V2-01_sec_hack_cover-1642fba06e.png` — cover line: “The SEC’s own account posted fake news.”

## Caption — Instagram
```text
The SEC's own account once posted fake news. 🔓

9 Jan 2024, 4:11 pm ET: a hijacked @SECGov post said spot bitcoin ETFs were approved. Bitcoin rose $1,000+, then fell $2,000+ after the correction (per the U.S. DOJ). The real approval came the next day, in an official SEC order.

If an official account can be faked, any post can. The filing is the source.

BFYP puts every filing on one page, dated and linked to SEC.gov.
→ betterforyourpocket.com (free plan)

#bitcoin #SEC #crypto #ETF #investing #duediligence

Educational market data. Not financial advice.
```

## Caption — X
```text
The SEC's own account once posted fake news (9 Jan 2024). BTC +$1,000, then −$2,000 (per DOJ). The real approval came the next day, in an SEC order.

Read the filing, not the post → betterforyourpocket.com
```

## Hashtags
#bitcoin #SEC #crypto #ETF #investing #duediligence

## First comment (sources, optional)
```text
Sources: SEC — SECGov X Account (unauthorized post, 9 Jan 2024) (Jan 2024) · Gary Gensler post, 9 Jan 2024, 4:26 pm ET (9 Jan 2024) · U.S. DOJ — sentencing in SEC X account hack (BTC moves: +$1,000 / -$2,000 per BTC) (16 May 2025) · SEC — Gensler statement on spot bitcoin ETP approval (10 Jan 2024)
```

## QC report
### Technical (automated, measured on the final file)
| Check | Result |
|---|---|
| Container / codecs | MP4 (faststart) · h264 High · yuv420p · aac 48000 Hz stereo |
| Resolution / fps | 1080×1920 · 30 fps |
| Duration | 21.40 s |
| Loudness | −14.3 LUFS integrated (target −14) · true peak −1.6 dBTP (≤ −1) |
| Hook audio | sound from frame 0 (−12 dB RMS in the first 300 ms) |
| Tail | clean fade (last sample 0.0) |
| Bitrate / size | 4261 kb/s · 11.4 MB |
| Video stream | bit-identical to the validated edit (stream MD5 compared) — yes |
| Voice intelligibility on the final mix | ASR word match 0.977 (gate ≥ 0.95) |
| Voice over the bed | 9.4 LU (gate ≥ 7) |
| All gates | **PASS** |

### Editorial
- [x] Hook on screen from frame 0, first line readable within 1.5 s: “The SEC’s own account posted fake news.”
- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA
- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen
- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)
- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data
- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)
- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons
- [x] Distinct angle and distinct BFYP payoff within the vault
- [x] End card: CTA + “Educational market data. Not financial advice.”
- [x] Sound: original music + sound design (hit×4, swish×3, click×3, impact×2, notif×2, whoosh×2, tick×2, ding×2, stamp×1, subdrop×1, riser×1, scan×1, pop×1, sparkle×1) + directed voice-over (BFYP-K2, female)
- [x] Voice-over complements the picture instead of reading the on-screen text

**Verdict: READY**
