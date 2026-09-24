# V2-20 "81% wrong or refused." — FinanceBench (Patronus AI, Nov 2023) → BFYP filings first
SPEC = {
    "reel": "v2_20_financebench",
    "voice": {"use": "K2-F2", "speed": 1.02},
    "direction": {
        "intent": "Rapporter une étude sérieuse avec un euphémisme britannique, puis montrer l'antidote : partir du dépôt officiel.",
        "delivery": "Correspondante crédible : factuelle, pince-sans-rire sur « It didn't go well ».",
        "pace": "Vif (montage à 170 bpm) mais articulé ; laisse les trois coups « Fast. Fluent. Unchecked. » sans voix.",
        "energy": "Moyenne, plus ferme sur « Sounding right isn't being right ».",
        "pauses": "Silence sur les trois impacts, silence sur « Four figures. Four receipts. ».",
        "emphasis": "« tested », « didn't go well », « four in five », « isn't », « ten-K », « source », « filing »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.5, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 2.95, "text": "Researchers tested an AI on SEC filings.", "speed": 1.06, "note": "hook : 81 % · FinanceBench, Patronus AI, nov. 2023"},
        {"at": 3.08, "until": 4.32, "text": "It didn't go well.", "speed": 1.0, "note": "euphémisme avant la citation"},
        {"at": 4.45, "until": 6.98, "text": "More than four in five: wrong, or refused.", "note": "citation verbatim de l'étude (81 %)"},
        {"at": 9.62, "until": 11.40, "text": "Sounding right isn't being right.", "note": "« Finance needs receipts. » (silence avant, sous « Fast. Fluent. Unchecked. »)"},
        {"at": 11.50, "until": 13.90, "text": "Here, every figure comes from the 10-K.", "say": "Here, every figure comes from the ten-K.", "note": "écran réel NVDA as filed · zooms REVENUE / NET INCOME"},
        {"at": 14.00, "until": 15.88, "text": "Each one, with its source.", "note": "zooms TOTAL ASSETS / TOTAL LIABILITIES"},
        {"at": 17.15, "until": 20.80, "text": "Start from the filing. BetterForYourPocket.com", "note": "carte CTA « Answers you can audit. » (silence avant, sous « Four figures. Four receipts. »)"},
    ],
}
