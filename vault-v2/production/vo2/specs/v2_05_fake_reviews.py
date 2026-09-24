# V2-05 "The FTC had to ban fake reviews." — product / honesty
SPEC = {
    "reel": "v2_05_fake_reviews",
    "voice": {"use": "K2-F3", "speed": 1.02},
    "direction": {
        "intent": "Partir d'une réalité connue (les faux avis), puis montrer la position honnête de BFYP : zéro témoignage, et « auditez-nous ».",
        "delivery": "Lumineuse et franche, un sourire dans la voix sur « we won't make any up ».",
        "pace": "Vif sur le hook, plus posé sur la page tarifs.",
        "energy": "Positive, confiante, sans ton publicitaire.",
        "pauses": "Un temps avant « It's free to start ».",
        "emphasis": "« banned », « bought », « Zero », « won't », « Check it », « free »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.12, "until": 3.62, "text": "Fake reviews got so bad, the FTC banned them.", "note": "hook : communiqué FTC du 14 août 2024"},
        {"at": 3.92, "until": 6.28, "text": "Because five stars can be bought.", "note": "citation de Lina M. Khan"},
        {"at": 6.50, "until": 8.40, "text": "So here's our pricing page.", "note": "« So here's what our pricing page says. »"},
        {"at": 8.80, "until": 11.60, "text": "Zero testimonials. And we won't make any up.", "note": "zoom IN OUR OWN WORDS"},
        {"at": 11.80, "until": 13.82, "text": "Don't take our word for it. Check it.", "note": "« Don't trust us. Audit us. »"},
        {"at": 13.96, "until": 15.82, "text": "It's free to start.", "speed": 0.96, "note": "« Start at $0. »"},
        {"at": 16.20, "until": 20.10, "text": "Audit us, at BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
