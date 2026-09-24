# V2-23 "31/100 vs 31/100. Same score?" — confidence badges
SPEC = {
    "reel": "v2_23_same_score",
    "voice": {"use": "K2-F1", "speed": 0.96},
    "direction": {
        "intent": "Un jeu des différences : deux scores identiques, deux niveaux de confiance ; la leçon tient en deux phrases.",
        "delivery": "Analyste calme qui fait remarquer un détail, avec un léger sourire sur la révélation.",
        "pace": "Lent et net (106 bpm), chaque badge annoncé sur son surlignage.",
        "energy": "Basse-moyenne, curiosité sur « Look closer », assurance sur la leçon.",
        "pauses": "Un temps entre « only half the story » et « The other half is the badge ».",
        "emphasis": "« both thirty-one », « real », « estimated », « more certain », « half », « badge »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 1.75, "text": "Two wallets, both thirty-one.", "note": "hook : WALLET A 31/100 | WALLET B 31/100"},
        {"at": 2.55, "until": 5.50, "text": "These are two real rows from the leaderboard.", "note": "Wallet #6 / Wallet #7 (écran réel)"},
        {"at": 5.70, "until": 6.76, "text": "Estimated.", "speed": 1.0, "note": "surlignage badge ESTIMATED (impact)"},
        {"at": 6.86, "until": 9.95, "text": "And this one? Much more certain.", "note": "surlignage HIGH CONFIDENCE (ding)"},
        {"at": 10.35, "until": 12.45, "text": "A score is only half the story.", "note": "« Same number. Different confidence. »"},
        {"at": 12.65, "until": 15.70, "text": "The other half is the badge.", "note": "« Read the badge, not just the number. »"},
        {"at": 16.05, "until": 20.20, "text": "Always read both. BetterForYourPocket.com", "note": "carte CTA « Scores with their confidence. »"},
    ],
}
