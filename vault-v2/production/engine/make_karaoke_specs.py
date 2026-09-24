#!/usr/bin/env python3
"""Write vo2 specs for the 7 karaoke reels: same words and same slots as their captions (reels/<reel>.vo.json),
only the voice, the interpretation and the mix change."""
import json
import os

KARAOKE = {
    "v2_13_since_when": ("K2-M1", 1.04, {
        "intent": "Le pote sceptique qui demande « depuis quand ? » : sans fenêtre de temps, un chiffre ne dit rien.",
        "delivery": "Conversationnel et complice, sourcils levés sur « Since when? », net sur les trois fenêtres.",
        "pace": "Vif, calé sur les créneaux d'origine des sous-titres karaoké (mêmes mots, mêmes instants).",
        "energy": "Moyenne-haute, un sourire sur « it's a vibe ».",
        "pauses": "Celles du montage d'origine ; micro-temps entre « Twenty-four hours. Seven days. Thirty days. »",
        "emphasis": "« Since when », « noise », « window », « two hours ago », « vibe »"}),
    "v2_18_whose_trillion": ("K2-F1", 0.96, {
        "intent": "Recadrer un chiffre spectaculaire : les 1,67 T$ couvrent tout le fonds, pas seulement VOO.",
        "delivery": "Analyste calme et précise, un léger « pas tout à fait » amusé.",
        "pace": "Posé, calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Basse-moyenne et régulière, chaleureuse sur le CTA.",
        "pauses": "Celles du montage d'origine ; un temps avant « Not exactly ».",
        "emphasis": "« Not exactly », « one share class », « four », « whole fund », « covers »"}),
    "v2_19_form_144": ("K2-M3", 1.08, {
        "intent": "Désamorcer la panique « les insiders vendent » : un Form 144 annonce une vente possible, pas une vente faite.",
        "delivery": "Journalistique et pédagogue, flegme britannique sur « Insiders dumping? ».",
        "pace": "Mesuré, calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Sobre, fermeté tranquille sur « Filed is not sold ».",
        "pauses": "Celles du montage d'origine.",
        "emphasis": "« notice », « proposed », « no amendment », « Filed is not sold », « Form 4 »"}),
    "v2_24_three_wins": ("K2-M1", 1.04, {
        "intent": "Trois gains d'affilée : génie ou chance ? Un historique court ne permet pas de trancher, et BFYP le dit.",
        "delivery": "Pote honnête et un peu taquin, franc sur « Honestly? ».",
        "pace": "Vif, calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Moyenne-haute, posée sur la leçon.",
        "pauses": "Celles du montage d'origine ; un temps après « Honestly? ».",
        "emphasis": "« Genius, or luck », « can't tell », « sample », « unproven », « admit »"}),
    "v2_27_prove_it": ("K2-M2", 0.98, {
        "intent": "Une affirmation qui ne peut jamais être fausse ne vaut rien ; BFYP dit ce qui la prouverait.",
        "delivery": "Grave et sèche ; les trois phrases d'« influenceur » dites avec une ironie froide.",
        "pace": "Lent (92 bpm), calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Basse et tendue, assurance sur BFYP.",
        "pauses": "Celles du montage d'origine ; « Trust me. » laissé seul.",
        "emphasis": "« proven wrong », « vibe », « Trust me », « tell you nothing », « prove it »"}),
    "v2_28_no_invented": ("K2-F2", 0.96, {
        "intent": "Mieux vaut un vide qu'une donnée inventée ; citer BFYP mot pour mot pour le prouver.",
        "delivery": "Correspondante posée, qui cite un texte officiel ; sobre sur « Empty is an answer ».",
        "pace": "Lent (88 bpm), calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Basse-moyenne, crédible.",
        "pauses": "Celles du montage d'origine ; un temps avant la citation.",
        "emphasis": "« show nothing », « worse than a blank », « we say so », « not shown », « Empty »"}),
    "v2_29_timestamps": ("K2-F1", 1.0, {
        "intent": "Une capture vieillit dès qu'elle est prise : même page, 46 minutes d'écart, chiffres différents.",
        "delivery": "Analyste claire, un brin complice sur « By the time you watch this ».",
        "pace": "Vif (144 bpm), calé sur les créneaux d'origine des sous-titres karaoké.",
        "energy": "Moyenne, régulière.",
        "pauses": "Celles du montage d'origine ; un temps entre les deux compteurs.",
        "emphasis": "« aging », « Forty-six minutes », « Then », « capture time », « moved on »"}),
}
MIX = {"music_duck_db": 10.0, "carve_db": 4.0, "sfx_duck_db": 7.0, "vo_over_bed_target": 9.0}

for reel, (use, speed, direction) in KARAOKE.items():
    J = json.load(open(f"/opt/bfyp/reels/{reel}.vo.json"))
    lines = [{"at": round(L["t0"], 4), "until": round(L["t1"] + 0.06, 4), "fit_to": round(L["dur"], 4), "text": L["text"],
              "note": f"créneau karaoké d'origine {L['t0']:.2f}–{L['t1']:.2f} s"} for L in J["lines"]]
    spec = {"reel": reel, "karaoke": True, "voice": {"use": use, "speed": speed}, "direction": direction, "mix": MIX, "lines": lines}
    src = (f"# {reel} — karaoke reel: same words, same slots as the on-screen captions ({reel}.vo.json, BFYP-K1);\n"
           f"# only the voice, the interpretation and the mix change.\ntrue, false = True, False\nSPEC = " + json.dumps(spec, ensure_ascii=False, indent=1) + "\n")
    open(f"/opt/bfyp/vo2/specs/{reel}.py", "w").write(src)
    print(reel, use, len(lines), "lines")
