# V2-11 "POV: 11 tabs to check one ticker." — POV / CONVERSATIONAL prototype
SPEC = {
    "legacy_pron": True,  # validated prototype: keep its exact synthesis path
    "reel": "v2_11_eleven_tabs",
    "voice": {"id": "K2-M1 · Peer", "gender": "M", "kokoro": "am_puck", "lang": "en-us", "speed": 1.06},
    "direction": {
        "intent": "Frustration familière, puis soulagement : un seul parcours au lieu de onze onglets.",
        "delivery": "Conversationnel, comme un ami qui est passé par là. Un peu agacé sur le hook, puis détendu et sûr de lui.",
        "pace": "Vif (environ 3,4 mots/s), phrases courtes calées sur les cuts du montage.",
        "energy": "Moyenne-haute sur le hook, détendue pendant le montage, enthousiaste sur le CTA.",
        "pauses": "Micro-pause après « Eleven tabs ». Chaque ligne du montage démarre sur son whoosh.",
        "emphasis": "« eleven tabs », « no clue », « one place », « receipts », « Keep one »"
    },
    "mix": {"music_duck_db": 9.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.10, "until": 1.72, "text": "One ticker. Eleven tabs.", "note": "hook while the tabs pile up"},
        {"at": 1.86, "until": 2.95, "text": "You know the drill.", "speed": 1.1, "note": "tabs keep piling"},
        {"at": 3.08, "until": 4.62, "text": "Still no clue what changed.", "note": "'...and you still don't know what changed.'"},
        {"at": 4.82, "until": 5.58, "text": "One place.", "speed": 1.0, "note": "'One workflow.'"},
        {"at": 5.74, "until": 7.28, "text": "First: what changed today.", "note": "m0 Today"},
        {"at": 7.44, "until": 8.96, "text": "Who moved the money.", "note": "m1 Whale Activity"},
        {"at": 9.12, "until": 10.66, "text": "Any track record?", "note": "m2 Smart Money"},
        {"at": 10.82, "until": 12.35, "text": "What was really filed.", "note": "m3 Stock pages"},
        {"at": 12.52, "until": 14.03, "text": "Ask anything. Get receipts.", "note": "m4 AI Research"},
        {"at": 14.22, "until": 15.90, "text": "Every step, sourced.", "note": "'Every step. Sources attached.'"},
        {"at": 16.15, "until": 20.70, "text": "Close ten tabs. Keep one. BetterForYourPocket.com", "gain_db": 0.5, "note": "CTA"},
    ],
}
