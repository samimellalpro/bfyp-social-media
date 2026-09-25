# V2-11 "POV: 11 tabs to check one ticker." — POV / CONVERSATIONAL prototype
SPEC = {
    "legacy_pron": True,  # validated prototype: keep its exact synthesis path
    "reel": "v2_11_eleven_tabs",
    "voice": {"id": "K2-M1 · Peer", "gender": "M", "kokoro": "am_puck", "lang": "en-us", "speed": 1.14},
    "direction": {
        "intent": "Frustration familière, puis la bascule « You know what? » et l'enthousiasme : un seul parcours au lieu de onze onglets.",
        "delivery": "Le Reel le plus énergique du lot (verdict de Sami, red team) : conversationnel mais survolté, un « You know what? » complice juste avant le drop, puis chaque étape annoncée comme une victoire, sur son ding.",
        "pace": "Très vif, phrases courtes calées sur les cuts du montage.",
        "energy": "Maximale : agacée sur le hook, explosive sur « One place! », triomphante sur le CTA.",
        "pauses": "Un temps après « Still no clue what changed! » (buzzer), « You know what? » juste avant la coupure de la musique, puis le drop sur « One place! ».",
        "emphasis": "« eleven tabs », « no clue », « You know what », « one place », « receipts », « Keep one »"
    },
    "mix": {"music_duck_db": 9.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 8.5},
    "lines": [
        {"at": 0.10, "until": 1.55, "text": "One ticker. Eleven tabs!", "note": "hook while the tabs pile up"},
        {"at": 1.64, "until": 2.86, "text": "Still no clue what changed!", "note": "tabs keep piling; ends as '...and you still don't know what changed.' lands (2.91 s)"},
        {"at": 3.60, "until": 4.42, "text": "You know what?", "note": "pivot, just before the music stop (4.45-4.69 s)"},
        {"at": 4.80, "until": 5.56, "text": "One place!", "speed": 1.0, "note": "'One workflow.' slam + ding"},
        {"at": 5.74, "until": 7.22, "text": "First: what changed today!", "note": "m0 Today + ding"},
        {"at": 7.44, "until": 8.90, "text": "Who moved the money!", "speed": 1.06, "note": "m1 Whale Activity + ding"},
        {"at": 9.12, "until": 10.60, "text": "Any track record?", "speed": 1.06, "note": "m2 Smart Money + ding"},
        {"at": 10.82, "until": 12.30, "text": "What was really filed!", "speed": 1.06, "note": "m3 Stock pages + ding"},
        {"at": 12.52, "until": 14.00, "text": "Ask anything. Get receipts!", "note": "m4 AI Research + ding"},
        {"at": 14.22, "until": 15.80, "text": "Every step, sourced!", "note": "'Sources attached. Every step.' + chime"},
        {"at": 16.15, "until": 20.70, "text": "Close ten tabs. Keep one! BetterForYourPocket.com", "gain_db": 0.5, "note": "CTA"},
    ],
}
