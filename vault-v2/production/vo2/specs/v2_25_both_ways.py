# V2-25 "On USDC, the data pointed both ways." — mixed is information too
SPEC = {
    "reel": "v2_25_both_ways",
    "voice": {"use": "K2-F1", "speed": 0.96},
    "direction": {
        "intent": "Assumer une donnée partagée au lieu de raconter une histoire, puis montrer que BFYP l'affiche telle quelle.",
        "delivery": "Analyste posée et honnête, sans dramatiser.",
        "pace": "Calme (118 bpm), phrases en miroir (up / down, easy / full picture).",
        "energy": "Basse-moyenne, constante ; chaleur sur le CTA.",
        "pauses": "Un temps entre « pointed up » et « Some pointed down ».",
        "emphasis": "« up », « down », « easy », « full picture », « as it is », « No model »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 3.90, "text": "Some of the data pointed up. Some pointed down.", "note": "hook : ↑ ↓ « On USDC, the data pointed both ways. »"},
        {"at": 4.25, "until": 5.88, "text": "Picking a side is easy.", "note": "« A feed that always picks a side… »"},
        {"at": 6.05, "until": 7.98, "text": "It just isn't the full picture.", "note": "« …is telling you a story. »"},
        {"at": 9.25, "until": 12.55, "text": "BFYP shows the split as it is.", "note": "écran réel Today · zoom MIXED, SAID PLAINLY"},
        {"at": 12.85, "until": 16.10, "text": "No model deciding which way to lean.", "note": "zoom NO SPIN · « Computed from observations, not a model »"},
        {"at": 16.50, "until": 20.20, "text": "Mixed? You should know. BetterForYourPocket.com", "note": "carte CTA « Mixed is information too. »"},
    ],
}
