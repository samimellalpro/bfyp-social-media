# V2-16 "What did that AI answer actually cost?" — AI Research, price shown before asking
SPEC = {
    "reel": "v2_16_cost_before",
    "voice": {"use": "K2-M1", "speed": 1.04},
    "direction": {
        "intent": "La mauvaise surprise de la facture après coup, puis la transparence : le coût s'affiche avant d'envoyer la question.",
        "delivery": "Pote conversationnel : un peu pince-sans-rire sur la facture, puis concret et rassurant.",
        "pace": "Enumération rythmée sur le hook, puis phrases courtes calées sur les zooms.",
        "energy": "Moyenne-haute au début, détendue ensuite.",
        "pauses": "Un temps avant « Then the bill. » et avant le CTA.",
        "emphasis": "« the bill », « surprise », « before », « seven reports », « Deep ones »",
    },
    "mix": {"music_duck_db": 9.5, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.12, "until": 3.12, "text": "One question. A few follow-ups. Then the bill.", "sp": 0.22, "note": "hook : reçu illustratif « TOTAL ??? »"},
        {"at": 3.40, "until": 6.35, "text": "Nobody likes a surprise bill.", "note": "« You shouldn't find out after. »"},
        {"at": 6.72, "until": 9.62, "text": "Here, the price shows up before you hit send.", "note": "écran réel AI Research · zoom PRICE TAG (36 credits)"},
        {"at": 10.02, "until": 12.48, "text": "Free plan? About seven reports a month.", "note": "écran réel Pricing · zoom INCLUDED (52 crédits ≈ 7 rapports)"},
        {"at": 12.62, "until": 15.40, "text": "Quick questions cost less. Deep ones, more.", "note": "zoom BY DEPTH · 2 à 172 crédits"},
        {"at": 16.55, "until": 20.25, "text": "Know the cost first. BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
