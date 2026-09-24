# V2-14 "This whale alert tells you nothing." — TENSION / DATA ALERT prototype
SPEC = {
    "legacy_pron": True,  # validated prototype: keep its exact synthesis path
    "reel": "v2_14_whale_alert",
    "voice": {"id": "K2-M2 · Signal", "gender": "M", "kokoro": "am_fenrir", "lang": "en-us", "speed": 0.98},
    "direction": {
        "intent": "Tension et curiosité face à une alerte brute, résolues par la preuve. Sans hype ni dramatisation.",
        "delivery": "Grave, contenue, un peu feutrée au début, comme en lisant un flux en direct. Plus nette et assurée quand BFYP apporte le contexte.",
        "pace": "Mesuré sur le hook, puis un rythme précis calé sur les six zooms.",
        "energy": "Tension contenue puis résolue : le payoff est plus calme, pas plus fort.",
        "pauses": "Un temps après « just moved » et avant « evidence ».",
        "emphasis": "« a million dollars », « who », « noise », « record », « raw transaction », « evidence »"
    },
    "mix": {"music_duck_db": 8.5, "carve_db": 4.5, "sfx_duck_db": 7.0, "vo_over_bed_target": 8.5},
    "lines": [
        {"at": 0.12, "until": 1.58, "text": "A million dollars just moved.", "speed": 1.04, "note": "alert card, notif"},
        {"at": 1.72, "until": 3.82, "text": "Who's behind it? Where's the proof?", "note": "over the three questions"},
        {"at": 4.05, "until": 5.00, "text": "Just noise.", "speed": 0.92, "gain_db": -0.5, "note": "'Size without context is just noise.'"},
        {"at": 6.34, "until": 8.18, "text": "It's typed, sized, and grouped.", "speed": 1.02, "note": "zooms 1-2"},
        {"at": 8.30, "until": 10.12, "text": "The wallet, and its record.", "speed": 1.0, "note": "zooms 3-4"},
        {"at": 10.24, "until": 12.20, "text": "The raw transaction, and its source.", "speed": 1.02, "note": "zooms 5-6 (PROOF, WHEN + SOURCE)"},
        {"at": 12.45, "until": 15.35, "text": "That's not an alert. That's evidence.", "speed": 0.9, "gain_db": -0.5, "note": "payoff 'Evidence. Not an alert.'"},
        {"at": 15.70, "until": 19.85, "text": "Read the evidence, not the alert. BetterForYourPocket.com", "note": "CTA"},
    ],
}
