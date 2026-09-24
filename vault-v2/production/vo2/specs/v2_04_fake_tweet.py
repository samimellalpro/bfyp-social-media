# V2-04 "One fake tweet erased $136.5B." — revelation, tight rhythm then a pause before the payoff
SPEC = {
    "reel": "v2_04_fake_tweet",
    "voice": {"use": "K2-M3", "speed": 1.1},
    "direction": {
        "intent": "Raconter la panique de 2013 en quelques secondes, puis opposer la réaction du marché à ce qui a été réellement observé.",
        "delivery": "Récit serré, presque un flash info, puis un payoff posé.",
        "pace": "Rapide et haché jusqu'à « Facts, later », puis ralenti.",
        "energy": "Tendue au début, calme et sûre sur BFYP.",
        "pauses": "Pause nette avant le payoff « Observed. Not predicted. »",
        "emphasis": "« hacked », « White House », « recovered », « first », « later », « counted », « Observed »",
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0},
    "lines": [
        {"at": 0.12, "until": 4.05, "text": "April 2013. One tweet, from a hacked news account.", "say": "April, twenty thirteen. One tweet, from a hacked news account.", "note": "hook : 136,5 Md$ effacés (S&P 500, Reuters)"},
        {"at": 4.42, "until": 6.88, "text": "It claimed explosions at the White House.", "note": "le faux tweet @AP (piraté)"},
        {"at": 7.08, "until": 9.70, "text": "Stocks dropped, then recovered.", "note": "« ↓ ~140 points, within minutes » / « Then it bounced back. »"},
        {"at": 9.92, "until": 12.45, "text": "Markets move first. Facts, later.", "note": "« Markets react first. Verification comes later. »"},
        {"at": 12.72, "until": 14.80, "text": "Here, activity is counted.", "note": "écran réel Today · zoom COUNTED (330 observations · 10 assets · 24h)"},
        {"at": 15.00, "until": 17.35, "text": "Observed. Not predicted.", "speed": 1.0, "note": "payoff sous la citation verbatim BFYP"},
        {"at": 17.70, "until": 21.75, "text": "Check before you react. BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
