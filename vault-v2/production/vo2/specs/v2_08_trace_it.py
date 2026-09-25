# V2-08 "This is a screenshot." — POV / conversational
SPEC = {
    "reel": "v2_08_trace_it",
    "voice": {"use": "K2-M1", "speed": 1.14},
    "direction": {
        "intent": "Le réflexe sceptique face à une capture d'écran qui circule, puis le soulagement : sur BFYP, tout se vérifie en un clic.",
        "delivery": "Conversationnel et complice, mais ambitieux et énergique (note de Sami, red team) : questions qui claquent au hook, puis une assurance qui monte jusqu'au CTA.",
        "pace": "Rapide et tonique, questions en rafale au hook.",
        "energy": "Haute tout du long, conquérante sur la solution et le CTA.",
        "pauses": "Micro-pause après « Someone sends you this ».",
        "emphasis": "« when », « cropped », « verify », « follow », « real », « source », « yourself »",
    },
    "mix": {"music_duck_db": 9.5, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.12, "until": 1.28, "text": "Someone sent you this!", "note": "hook : capture « Whale just moved $1.09M of LIT!! »"},
        {"at": 1.38, "until": 3.35, "text": "But when's it from? Who cropped it?", "note": "« Cropped? Old? Edited? »"},
        {"at": 3.55, "until": 6.62, "text": "You can't verify a picture. You can follow a link!", "note": "« You can't check a screenshot. You can check a link. »"},
        {"at": 6.92, "until": 8.76, "text": "Here, you just click through!", "note": "zoom CLICK THROUGH"},
        {"at": 8.88, "until": 10.68, "text": "And there's the real transaction!", "note": "zoom SOURCE (via etherscan)"},
        {"at": 11.62, "until": 13.72, "text": "Filings? They open at the source!", "note": "zoom ORIGINAL"},
        {"at": 15.70, "until": 19.72, "text": "Check it yourself! BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
