# V2-09 "When did NVIDIA's fiscal 2026 end?" — analytical quiz
SPEC = {
    "reel": "v2_09_fiscal_2026",
    "voice": {"use": "K2-F1", "speed": 0.98},
    "direction": {
        "intent": "Un quiz qui piège gentiment, puis la leçon : un chiffre ne veut rien dire sans sa période.",
        "delivery": "Analyste complice : joueuse sur le quiz, précise sur la leçon.",
        "pace": "Laisse le compte à rebours vivre, puis un rythme posé.",
        "energy": "Légère sur le hook, calme et sûre ensuite.",
        "pauses": "Silence pendant « Answer in 3… 2… 1… ».",
        "emphasis": "« guess », « Late January », « Fiscal isn't calendar », « as filed », « exact period »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.12, "until": 1.95, "text": "Quick quiz. Take a guess.", "note": "hook : « When did NVIDIA's fiscal 2026 end? »"},
        {"at": 4.08, "until": 5.92, "text": "Late January. Surprised?", "note": "réponse « January 25, 2026. » (silence avant, sous le compte à rebours)"},
        {"at": 6.05, "until": 8.48, "text": "That's the year this revenue figure refers to.", "note": "citation NVIDIA : 215,9 Md$ sur l'exercice 2026"},
        {"at": 8.75, "until": 10.04, "text": "Fiscal isn't calendar.", "note": "« Fiscal years don't follow the calendar. »"},
        {"at": 10.15, "until": 12.28, "text": "Mix them up, and the story's wrong.", "note": "« Compare the wrong periods, get the wrong story. »"},
        {"at": 12.72, "until": 14.82, "text": "BFYP shows the number as filed,", "note": "zoom AS FILED"},
        {"at": 14.92, "until": 16.62, "text": "with the exact period it covers.", "note": "zoom THE PERIOD"},
        {"at": 16.90, "until": 20.24, "text": "Every number, with its period. BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
