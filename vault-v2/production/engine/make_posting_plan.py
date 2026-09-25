#!/usr/bin/env python3
"""BFYP Vault V2 — posting plan for the Buffer session (distribution aid; never touches the reels).

make_posting_plan.py -> vault-v2/posting_plan.json + vault-v2/HANDOFF-BUFFER.md
Captions, hashtags and first comments are copied verbatim from the locked sheets (READY/*/V2-XX_slug.md);
the order is the README's suggested order (engine/make_readme.py, ORDER).
"""
import ast
import datetime
import json
import os
import re

VAULT = "/home/user/bfyp-social-media/vault-v2"
ENGINE = os.path.dirname(os.path.abspath(__file__))
START = datetime.date(2026, 10, 1)
PRICING_RECHECK = {"V2-05", "V2-16", "V2-17"}   # reels showing pricing-page details (as of 23 Sep 2026)
UTM = "https://betterforyourpocket.com/?utm_source={platform}&utm_medium=social&utm_campaign=vault_v2&utm_content={rid}"


def order():
    src = open(os.path.join(ENGINE, "make_readme.py")).read()
    node = next(n for n in ast.parse(src).body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "ORDER")
    return ast.literal_eval(node.value)


def block(md, heading):
    """Text of the ```text block right under `## heading`, or None."""
    m = re.search(r"^## " + re.escape(heading) + r"\s*\n```text\n(.*?)\n```", md, re.S | re.M)
    return m.group(1) if m else None


def main():
    M = json.load(open(os.path.join(VAULT, "manifest.json")))
    R = {r["id"]: r for r in M["reels"]}
    ORDER = order()
    assert sorted(ORDER) == sorted(R), "ORDER must list the 30 reels once"
    plan = []
    for i, rid in enumerate(ORDER):
        r = R[rid]
        md = open(os.path.join(VAULT, r["sheet"])).read()
        hm = re.search(r"^## Hashtags\s*\n(.+)$", md, re.M)
        ig, x = block(md, "Caption — Instagram"), block(md, "Caption — X")
        assert ig and x and hm, rid
        plan.append({
            "slot": i + 1, "suggested_date": (START + datetime.timedelta(days=i)).isoformat(), "id": rid, "title": r["title"],
            "hook": r["hook"], "cta": r["cta"], "duration_s": r["duration_s"],
            "video": r["video"], "cover": r["cover"], "sheet": r["sheet"], "sha256_video": r["sha256_video"],
            "caption_instagram": ig, "caption_x": x, "hashtags": hm.group(1).strip(),
            "first_comment": block(md, "First comment (sources, optional)"),
            "pricing_recheck": rid in PRICING_RECHECK,
            "tracking_link_optional": UTM.replace("{rid}", rid.lower()),
        })
    out = {
        "vault": "BFYP VAULT V2", "status": M.get("status", "READY"), "locked": M.get("locked"), "publish_from": START.isoformat(),
        "cadence": "one reel per day, in this order, around the posts already scheduled (do not move or replace them)",
        "rules": [
            "Post the files as they are: no re-encode, trim, crop or overlay (V2 is locked; hashes in LOCK.md).",
            "Captions, hashtags and first comments are verbatim from the locked sheets.",
            "Re-check betterforyourpocket.com/pricing before posting the reels marked pricing_recheck (plan details as of 23 Sep 2026).",
            "tracking_link_optional: fill {platform} (instagram, tiktok, youtube, facebook, x) where a clickable link is possible, to measure traffic per reel.",
        ],
        "reels": plan,
    }
    json.dump(out, open(os.path.join(VAULT, "posting_plan.json"), "w"), indent=1, ensure_ascii=False)

    L = ["# Vault V2 — passation à la session Buffer\n",
         f"**30 Reels prêts, verrouillés le {M.get('locked')} (V2 CLOSED).** À publier à partir du **1er octobre 2026**. "
         "Tout est dans ce dossier, sur la branche `claude/bfyp-vault-v2-reels-l883ff`.\n",
         "## Fichiers\n",
         "- `posting_plan.json` : les 30 Reels dans l'ordre de diffusion, chacun avec sa vidéo, sa cover, sa légende Instagram, sa légende X, "
         "ses hashtags et son premier commentaire (sources). Tout est copié mot pour mot des fiches verrouillées.",
         "- `READY/V2-XX_slug/` : la vidéo MP4 (1080×1920, 20–28 s, −14 LUFS), la cover PNG et la fiche complète.",
         "- `manifest.json` et `LOCK.md` : les SHA-256 de chaque fichier.\n",
         "## Règles\n",
         "- Publier les fichiers tels quels : pas de ré-encodage, de coupe, de recadrage ni d'incrustation. V2 est verrouillé.",
         "- Ne pas déplacer ni remplacer ce qui est déjà programmé dans Buffer : les Reels V2 s'ajoutent autour.",
         "- Revérifier betterforyourpocket.com/pricing avant de poster V2-05, V2-16 et V2-17 (détails du plan au 23/09/2026).\n",
         "## Pour ramener le maximum de trafic\n",
         "- Un Reel par jour, dans l'ordre ci-dessous. Il alterne les thèmes et garde les Reels proches à au moins deux jours d'écart. "
         "V2-17 (« Everything $0 gets you ») passe en premier, suivant la note de Sami « à poster ASAP ».",
         "- Publier chaque Reel sur tous les formats verticaux connectés à Buffer (Instagram Reels, TikTok, YouTube Shorts, Facebook Reels), "
         "et sur X avec la légende X. Le même fichier convient partout.",
         "- Sur Instagram, mettre la cover fournie (grille du profil). Ajouter le premier commentaire « sources » quand la fiche en a un.",
         "- Là où un lien est cliquable (bio, X, description YouTube), utiliser le lien de suivi `tracking_link_optional` en remplaçant {platform}. "
         "On saura ainsi quel Reel et quelle plateforme amènent du trafic sur le site.",
         "- Relever pour chaque Reel, à J+7 : vues, durée moyenne de visionnage, partages, enregistrements, visites du profil, clics et sessions UTM. "
         "Ces chiffres serviront à choisir les formats de la V3.\n",
         "## Ordre de diffusion\n",
         "| Jour | Date | Reel | Titre | Hook (0 s) | Durée | Revérifier /pricing |", "|---:|---|---|---|---|---:|---|"]
    for p in plan:
        L.append(f"| {p['slot']} | {p['suggested_date']} | {p['id']} | {p['title']} | {p['hook']} | {p['duration_s']:.1f} s | {'oui' if p['pricing_recheck'] else ''} |")
    open(os.path.join(VAULT, "HANDOFF-BUFFER.md"), "w").write("\n".join(L) + "\n")
    print(f"posting plan: {len(plan)} reels, {plan[0]['suggested_date']} → {plan[-1]['suggested_date']}, first {plan[0]['id']}")


if __name__ == "__main__":
    main()
