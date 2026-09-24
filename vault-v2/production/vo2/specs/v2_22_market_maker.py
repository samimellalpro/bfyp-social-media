# V2-22 "That 'whale'? Might be a market maker." — Smart Money behaviour labels
SPEC = {
    "reel": "v2_22_market_maker",
    "voice": {"use": "K2-M2", "speed": 1.0},
    "direction": {
        "intent": "Semer le doute sur la « baleine », expliquer le métier de teneur de marché, puis montrer les étiquettes de comportement.",
        "delivery": "Grave, un peu de suspense sur le hook, puis explicatif et net.",
        "pace": "Posé (112 bpm), chaque étiquette annoncée sur son zoom.",
        "energy": "Moyenne, légère tension au début.",
        "pauses": "Un temps avant « Or just someone doing their job? ».",
        "emphasis": "« Big move », « job », « liquidity », « makes markets », « accumulates », « story »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 1.55, "text": "Big wallet. Big move.", "note": "hook : « That “whale”? »"},
        {"at": 1.72, "until": 4.12, "text": "Or just someone doing their job?", "note": "« Might be a market maker. » + flux ⇄"},
        {"at": 4.40, "until": 5.82, "text": "Huge volume, every day.", "note": "« Market makers move size all day. »"},
        {"at": 6.00, "until": 8.42, "text": "That's liquidity. Not a bet on the price.", "note": "« It's their job — not a conviction bet. »"},
        {"at": 9.70, "until": 11.72, "text": "This one makes markets.", "note": "zoom WALLET #6 · Market maker"},
        {"at": 11.85, "until": 13.82, "text": "This one accumulates.", "note": "zoom WALLET #8 · Whale accumulator"},
        {"at": 14.22, "until": 16.00, "text": "Both big. Not the same story.", "note": "« Different behavior. Same leaderboard. »"},
        {"at": 16.30, "until": 20.10, "text": "Check the label first. BetterForYourPocket.com", "note": "carte CTA « Know who you're watching. »"},
    ],
}
