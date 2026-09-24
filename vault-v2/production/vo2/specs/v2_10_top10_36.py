# V2-10 "500 companies. 36% in 10 lines." — ANALYTICAL prototype
SPEC = {
    "legacy_pron": True,  # validated prototype: keep its exact synthesis path
    "reel": "v2_10_top10_36",
    "voice": {"id": "K2-F1 · Analyst", "gender": "F", "kokoro": "af_heart", "lang": "en-us", "speed": 0.94},
    "direction": {
        "intent": "Démonter calmement l'idée de fonds « diversifié » avec un seul chiffre, puis montrer où le vérifier.",
        "delivery": "Calme, précise, sûre d'elle. Une analyste qui commente un graphique, sans vendre.",
        "pace": "Sans hâte (environ 3 mots/s pendant la parole), plus lente sur les chiffres.",
        "energy": "Moyenne-basse et régulière. Légère remontée sur BFYP, chaleureuse sur le CTA.",
        "pauses": "Un temps avant chaque chiffre. Le détail Alphabet arrive une fois le graphique posé.",
        "emphasis": "« a third », « two hundred eighty-four billion », « twice », « as filed »"
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 2.25, "text": "Five hundred companies, in one fund.", "note": "hook, over 'You bought 500 companies'"},
        {"at": 2.50, "until": 4.52, "text": "Over a third sits in just ten.", "speed": 0.86, "note": "lands on the 36% reveal"},
        {"at": 4.85, "until": 7.62, "text": "That's two hundred eighty-four billion dollars.", "speed": 0.9, "note": "figure lands with the $284.48B line"},
        {"at": 7.80, "until": 9.12, "text": "One name appears twice.", "note": "ding + 'Alphabet shows up twice.'"},
        {"at": 9.40, "until": 12.05, "text": "Alphabet. Two share classes, one company.", "speed": 0.92, "note": "'10 lines. 9 companies.'"},
        {"at": 12.80, "until": 15.65, "text": "On BFYP: the fund, as filed.", "say": "On B.F.Y.P.: the fund, as filed.", "note": "zooms THE FUND, AS FILED"},
        {"at": 15.85, "until": 17.25, "text": "Top holdings, by weight.", "note": "zoom THE TOP LINES"},
        {"at": 17.55, "until": 20.80, "text": "Know what you own. BetterForYourPocket.com", "speed": 0.9, "gain_db": 0.5, "note": "CTA"},
    ],
}
