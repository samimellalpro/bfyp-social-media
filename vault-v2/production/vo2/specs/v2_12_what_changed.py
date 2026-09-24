# V2-12 "GREEN. RED. GREEN. RED. — It shows prices. Not what changed." — product / data
SPEC = {
    "reel": "v2_12_what_changed",
    "voice": {"use": "K2-F3", "speed": 1.0},
    "direction": {
        "intent": "Sortir du clignotement vert/rouge pour poser la vraie question (qu'est-ce qui a changé ?), puis montrer les compteurs BFYP du jour.",
        "delivery": "Hôte vive et complice : un brin moqueuse sur le clignotement, puis claire et assurée sur les chiffres.",
        "pace": "Rapide et rythmé sur le hook (calé sur les flashs), plus posé pendant les zooms.",
        "energy": "Haute sur le hook, puis moyenne et régulière.",
        "pauses": "Laisse respirer le zoom CRYPTO · MACRO · STOCKS sans voix.",
        "emphasis": "« actually changed », « what », « counts », « Mostly on-chain », « Facts »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.12, "until": 1.90, "text": "Up, down, up, down.", "speed": 1.06, "cp": 0.06, "note": "hook : GREEN. RED. GREEN. RED."},
        {"at": 2.12, "until": 3.82, "text": "But what actually changed?", "note": "« It shows prices. Not what changed. »"},
        {"at": 4.05, "until": 5.08, "text": "Something moved.", "note": "« Price tells you THAT. »"},
        {"at": 5.24, "until": 7.72, "text": "A price can't tell you what.", "note": "« Not WHAT. »"},
        {"at": 8.00, "until": 10.26, "text": "So BFYP counts activity instead.", "note": "compteur → 354 observations · 10 assets"},
        {"at": 10.36, "until": 11.50, "text": "Mostly on-chain.", "note": "zoom ON-CHAIN · 234 observations"},
        {"at": 11.60, "until": 13.10, "text": "Then companies and themes.", "note": "zoom COMPANIES & THEMES · 101"},
        {"at": 14.06, "until": 15.56, "text": "Facts, not forecasts.", "speed": 0.94, "note": "zoom COUNTS, NOT PRICES"},
        {"at": 15.95, "until": 20.20, "text": "See what changed today. BetterForYourPocket.com", "note": "carte CTA « Start with what changed. »"},
    ],
}
