# V2-17 "$0. Here's everything it gets you." — free-plan speedrun (150 bpm)
SPEC = {
    "reel": "v2_17_free_speedrun",
    "voice": {"use": "K2-F3", "speed": 1.06},
    "direction": {
        "intent": "Un speedrun joyeux du plan gratuit : la voix commente la course sans lire la liste, puis renvoie à la page tarifs comme preuve.",
        "delivery": "Hôte énergique et souriante, façon commentatrice de speedrun.",
        "pace": "Rapide, calé sur le tempo 150 bpm ; les listes groupées en rafales.",
        "energy": "Haute tout du long, un sourire sur « Ten out of ten ».",
        "pauses": "Micro-respirations entre les rafales, pas de silence long.",
        "emphasis": "« Zero dollars », « every month », « Ten out of ten », « pricing page », « free »",
    },
    "mix": {"music_duck_db": 9.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 8.5},
    "lines": [
        {"at": 0.12, "until": 2.30, "text": "Zero dollars. How far does it go?", "note": "hook : $0 · « Here's everything it gets you. »"},
        {"at": 2.72, "until": 5.25, "text": "Markets, whales, smart money, research.", "cp": 0.08, "note": "items 01–04"},
        {"at": 6.25, "until": 7.95, "text": "A watchlist and alerts.", "note": "items 05–06"},
        {"at": 8.05, "until": 9.70, "text": "AI credits, every month.", "note": "items 07–08"},
        {"at": 9.82, "until": 11.95, "text": "Exports, support. Ten out of ten.", "note": "items 09–10"},
        {"at": 12.25, "until": 15.80, "text": "Don't take my word for it. It's on the pricing page.", "note": "écran réel Pricing (23 Sep 2026)"},
        {"at": 16.25, "until": 20.30, "text": "Start free, at BetterForYourPocket.com", "note": "carte CTA"},
    ],
}
