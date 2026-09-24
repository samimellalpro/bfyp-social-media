# V2-07 "'Big fund just bought $XYZ!' 'Just'?" — educational / analytical (13F lag)
SPEC = {
    "reel": "v2_07_just_bought",
    "voice": {"use": "K2-M3", "speed": 1.1},
    "direction": {
        "intent": "Démonter le « just » : expliquer simplement le calendrier des déclarations et montrer les deux dates sur BFYP.",
        "delivery": "Pédagogue et posé, avec un humour britannique discret (« Mind the gap »).",
        "pace": "Mesuré, un temps sur « weeks later » et sur « months old ».",
        "energy": "Calme, sûre, un clin d'œil sur « Mind the gap ».",
        "pauses": "Un temps après « By the time you see it ».",
        "emphasis": "« Not so fast », « weeks later », « months old », « period », « filed », « gap »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 2.68, "text": "Just bought? Not so fast.", "note": "hook : post type « Big fund just bought $XYZ! » (illustration)"},
        {"at": 3.05, "until": 6.52, "text": "It's a snapshot from quarter-end, filed weeks later.", "note": "frise 1 APR → 30 JUN → ~14 AUG (13F : 45 jours)"},
        {"at": 6.85, "until": 10.95, "text": "By the time you see it, it could be months old.", "note": "« You see it mid-August. The trade could be from April. »"},
        {"at": 11.72, "until": 14.95, "text": "BFYP shows the period, and the filing date.", "note": "écran réel SPY · zooms PERIOD (30 Jun) / FILED (28 Aug)"},
        {"at": 15.10, "until": 16.58, "text": "Mind the gap.", "speed": 1.0, "note": "zoom THE GAP"},
        {"at": 16.90, "until": 20.55, "text": "Always check both dates. BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
