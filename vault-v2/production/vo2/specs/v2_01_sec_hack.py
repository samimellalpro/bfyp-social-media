# V2-01 "The SEC's own account posted fake news." — EDUCATIONAL / JOURNALISTIC prototype
SPEC = {
    "legacy_pron": True,  # validated prototype: keep its exact synthesis path
    "reel": "v2_01_sec_hack",
    "voice": {"id": "K2-F2 · Correspondent", "gender": "F", "kokoro": "bf_emma", "lang": "en-gb", "speed": 0.98},
    "direction": {
        "intent": "Raconter sobrement un fait réel et daté, puis en tirer la leçon : un post n'est pas une source, un dépôt officiel oui.",
        "delivery": "Sobre et crédible, presque un bulletin d'info : faits datés et attribués, pas d'adjectifs.",
        "pace": "Régulier (environ 3 mots/s), phrases courtes et affirmatives.",
        "energy": "Neutre et posée. Un peu plus chaleureuse sur la solution BFYP.",
        "pauses": "Silences volontaires sous « If an official account can be faked… » et sous « Posts can be faked. Filings are the record. », pour que ces phrases portent seules.",
        "emphasis": "« own account », « fifteen minutes », « hack », « next day », « dated », « original »"
    },
    "mix": {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.5},
    "lines": [
        {"at": 0.10, "until": 2.64, "text": "The SEC's own account posts this.", "say": "The S.E.C.'s own account posts this.", "note": "hook, fake post + FAKE stamp (date is on the card)"},
        {"at": 2.84, "until": 5.30, "text": "Bitcoin jumps, then drops two thousand.", "note": "+$1,000 then −$2,000 (per U.S. DOJ); 'drops' lands near the 3.8 s reveal"},
        {"at": 5.54, "until": 7.62, "text": "Fifteen minutes later: a hack.", "note": "Gensler correction"},
        {"at": 7.86, "until": 9.40, "text": "Real approval? Next day.", "note": "timeline 9 → 10 Jan"},
        {"at": 10.90, "until": 12.70, "text": "Here, each filing is dated,", "note": "BFYP, zoom DATED (silence under 'any post can' before it)"},
        {"at": 12.78, "until": 14.30, "text": "and linked to the original.", "note": "zoom LINKED"},
        {"at": 16.95, "until": 21.05, "text": "Read the filing, not the post. BetterForYourPocket.com", "note": "CTA (silence under 'Posts can be faked.')"},
    ],
}
