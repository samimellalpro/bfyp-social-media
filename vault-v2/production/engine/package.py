#!/usr/bin/env python3
"""BFYP Vault V2 — package READY deliverables into the repo (vault-v2/READY)."""
import collections
import hashlib
import importlib.util
import json
import os
import shutil
import sys

REPO = "/home/user/bfyp-social-media"
VAULT = os.path.join(REPO, "vault-v2")
READY = os.path.join(VAULT, "READY")
OUT = "/opt/bfyp/out/final"
VO2_FINAL = "/opt/bfyp/vo2/final"   # validated edit + directed VO (video stream copied bit for bit)
VO2_OUT = "/opt/bfyp/vo2/out"
REELS_DIR = "/opt/bfyp/reels"
CAT = json.load(open("/opt/bfyp/assets/screens/catalog.json"))

spec = importlib.util.spec_from_file_location("plan", "/opt/bfyp/plan/plan.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

LOTS = {1: "Lot 1 — Proof over posts", 2: "Lot 2 — Your research stack is broken", 3: "Lot 3 — Bad market habits"}

ILLUS = {
    "V2-01": ["Quote cards in neutral BFYP styling reproducing the unauthorized @SECGov post and Gary Gensler’s correction verbatim, with date, time and source (no platform branding)", "Timeline graphic (9 Jan fake post → 10 Jan official order)"],
    "V2-02": ["Quote card reproducing the SEC press-release headline verbatim (dated, attributed)"],
    "V2-03": ["Quote card reproducing the court’s words verbatim (Mata v. Avianca, S.D.N.Y.)", "Animated $5,000 counter"],
    "V2-04": ["Quote card reproducing the fake AP post verbatim, stamped FAKE (dated, attributed)", "Glitch/counter typography"],
    "V2-05": ["Quote card reproducing the FTC press-release headline verbatim", "★★★★★ struck through (graphic)"],
    "V2-06": ["Abstract feed skeleton (no text, no accounts)", "Bar chart built from the FINRA Foundation / CFA Institute percentages"],
    "V2-07": ["Generic post labelled “TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT” (@example handle)", "13F timeline graphic (45-day rule)"],
    "V2-08": ["Generic screenshot labelled “SCREENSHOT · ILLUSTRATION”"],
    "V2-09": ["Quiz cards", "Quote card with NVIDIA’s own FY2026 wording"],
    "V2-10": ["504-dot grid (one dot per holding)", "Bar chart of the ten largest holdings using the filed values shown on the BFYP SPY page"],
    "V2-11": ["Generic browser tabs (descriptive labels only, no logos or brands)"],
    "V2-12": ["Abstract ▲▼ tape and colour flicker (no data)"],
    "V2-13": ["Generic post labelled “TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT” (@example handle)"],
    "V2-14": ["Generic alert labelled “TYPICAL ALERT · ILLUSTRATION · NOT A REAL ACCOUNT” (@example_alerts handle)"],
    "V2-15": ["Generic chat box labelled “GENERIC AI CHAT · ILLUSTRATION” (no product branding)"],
    "V2-16": ["Receipt labelled “RECEIPT · ILLUSTRATION” with unknown (???) amounts"],
    "V2-17": ["Checklist reproducing the free-plan list verbatim from the pricing page"],
    "V2-18": ["Share-class diagram labelled “not to scale”, per the fund’s 2026 semi-annual report", "Animated counter to $1.67T"],
    "V2-19": ["Quote card reproducing SEC staff guidance verbatim (Securities Act Forms C&DI 131.01)", "Amber highlight boxes on the real filings list"],
    "V2-20": ["Quote card reproducing the FinanceBench abstract sentence verbatim (dated, attributed)"],
    "V2-21": ["Bubble graphic (BIGGEST vs SMARTEST?) labelled “Illustration”"],
    "V2-22": ["Abstract two-way flow arrows"],
    "V2-23": ["Two neutral 31/100 score cards (hook), then crops of the two real leaderboard rows"],
    "V2-24": ["W·W·W cards and a coin flip (graphic)"],
    "V2-25": ["Split ↑ / ↓ background (graphic)"],
    "V2-26": ["Node graph labelled “Illustration” (kind A / kind B around wallet 0xe1ad…1691, mirroring the real Today line)"],
    "V2-27": ["Three typical claims labelled “Typical claims · illustration”, struck through"],
    "V2-28": ["Empty-state box (graphic)", "An invented “87% consensus” card stamped MADE UP and labelled “Invented number · illustration of what not to do”"],
    "V2-29": ["Animated “age” counter", "330 → 354 counter using the two real captures"],
    "V2-30": ["Evidence ladder graphic (Rumor → Screenshot → Headline → Official filing)"],
}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fmt_cap(asset):
    m = CAT[asset]
    src = m["src"]
    if src.startswith("/tmp") or "/scratchpad/" in src:
        base = os.path.basename(os.path.dirname(src))
        where = f"crop of a frame of `public/social/buffer/reels/{base}.mp4` (approved Vault V1 reel)"
    else:
        where = "crop of `" + src.replace("home/user/bfyp-social-media/", "") + "`"
    kind = "BFYP data card" if m.get("kind") == "data" else "real screen"
    return f"`{asset}` — {m['page']}: {m['note']} · {kind} captured **{m['captured']}** · {where}"


# BFYP wording reproduced as typeset text (not shown as an image): asset it comes from, how it is used, the exact wording
QUOTED = {
    "V2-04": ("today_footer", "quoted verbatim on screen", "“Observed activity, as counted by BFYP. Nothing here is a prediction.”"),
    "V2-12": ("today_footer", "end-card line shortened from it, not presented as a quote", "“Observed activity, as counted by BFYP. Nothing here is a prediction.”"),
    "V2-17": ("free_list", "the 10 checklist items are typeset verbatim from it", None),
    "V2-28": ("sm_page", "quoted verbatim on screen, over the real line", "“When no scored wallet was active, we say so instead of inventing a consensus.”"),
}
TAPE = {"V2-12": "the decorative ▲▼ tape in the hook", "V2-22": "the decorative ⇄ arrows"}


def main(lots=None):
    if os.path.exists(os.path.join(VAULT, "LOCK.md")) and os.environ.get("BFYP_UNLOCK_V2") != "1":
        sys.exit("Vault V2 is LOCKED (V2 CLOSED, see vault-v2/LOCK.md): no repackaging without Sami's explicit request. "
                 "Set BFYP_UNLOCK_V2=1 only on that request.")
    os.makedirs(READY, exist_ok=True)
    manifest = []
    for r in P.REELS:
        if lots and r["lot"] not in lots:
            continue
        rid, slug = r["id"], r["slug"]
        name = f"v2_{rid[3:]}_{slug}"
        d = os.path.join(OUT, name)
        edit_mp4 = os.path.join(d, f"{name}.mp4")
        cov = os.path.join(d, f"{name}_cover.png")
        edit_qc = json.load(open(os.path.join(d, "qc.json")))
        if not edit_qc["pass"] or os.path.getmtime(os.path.join(d, "qc.json")) < os.path.getmtime(edit_mp4):
            sys.exit(f"{rid}: edit QC missing, failed or older than the render; run engine/qc.py {name} first")
        # the deliverable is the validated edit with its directed VO (BFYP-K2)
        mp4 = os.path.join(VO2_FINAL, name, f"{name}_VO.mp4")
        vo2 = json.load(open(os.path.join(VO2_OUT, name, f"{name}.vo2.json")))
        if not os.path.exists(mp4 + ".qc.json") or os.path.getmtime(mp4 + ".qc.json") < os.path.getmtime(mp4):
            sys.exit(f"{rid}: VO mix QC missing or older than the mix; run engine/vo2.py qc {name} {mp4}")
        qc = json.load(open(mp4 + ".qc.json"))
        if not qc["pass"] or not vo2["qc"]["pass"]:
            sys.exit(f"{rid}: VO build or mix QC failed")
        log = json.load(open(mp4 + ".log.json"))
        if (log["log"].get("vo2") or {}).get("vo_sha256") != vo2["sha256"]:
            sys.exit(f"{rid}: the mix does not carry the current VO build; re-run engine/vo2.py mix")
        karaoke = os.path.exists(os.path.join(REELS_DIR, f"{name}.vo.json"))  # captions timed to the original voice slots
        folder = os.path.join(READY, f"{rid}_{slug}")
        if os.path.isdir(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
        h_mp4, h_cov = sha(mp4), sha(cov)
        f_mp4 = f"{rid}_{slug}-{h_mp4[:10]}.mp4"
        f_cov = f"{rid}_{slug}_cover-{h_cov[:10]}.png"
        shutil.copy2(mp4, os.path.join(folder, f_mp4))
        shutil.copy2(cov, os.path.join(folder, f_cov))
        music = (log.get("meta") or {}).get("music") or {}
        cues = collections.Counter(c["type"] for c in (log.get("cues") or []))
        sfx = ", ".join(f"{k}×{v}" for k, v in sorted(cues.items(), key=lambda kv: -kv[1]))
        lang = r.get("lang", "EN")
        V2 = vo2["voice"]
        kok = V2["kokoro"] if isinstance(V2["kokoro"], str) else " + ".join(f"{k} {w:.1f}" for k, w in V2["kokoro"].items())
        gender = {"F": "female", "M": "male"}[V2["gender"]]
        voice = (f"**BFYP-K2 · {V2['id']}** — {gender}, native English ({V2['lang']}) · Kokoro-82M v1.0, local and free (Apache-2.0), "
                 f"stock voice {'blend ' if not isinstance(V2['kokoro'], str) else ''}`{kok}` · no cloning · directed for this reel (see Voice direction)")
        fmt_line = ("Voice-led, karaoke captions" if karaoke else "Directed voice-over over the text-led edit") + f" · {r['format']}"
        tech = qc
        mx = log["log"]["vo2"]
        g = qc["gates"]
        # ---------------------------------------------------------------- sheet
        L = []
        L.append(f"# {rid} — {r['title']}\n")
        L.append(f"**Status: ✅ READY** · {LOTS[r['lot']]} · {lang} · publish **after 30 Sep 2026** (not scheduled, not in Buffer)\n")
        L.append("| | |\n|---|---|")
        L.append(f"| Reel (final) | `{f_mp4}` — {tech['duration_s']:.2f} s · {tech['width']}×{tech['height']} · {tech['fps']:.0f} fps · H.264 High · AAC 48 kHz stereo · {tech['size_mb']} MB |")
        L.append(f"| Cover | `{f_cov}` — 1080×1920 (key text inside the 3:4 grid-safe area) |")
        L.append(f"| Format | {fmt_line} |")
        L.append(f"| Music | Original, synthesized for this reel: {music.get('style', '?')} · {music.get('bpm', '?')} BPM · {music.get('key', '?')} {music.get('mode', '')} (no samples, no licensed audio) |")
        L.append(f"| Voice | {voice} |")
        L.append(f"| On-screen “AI voice” label | {'Yes — kept from the validated karaoke edit' if karaoke else 'No — visual edit frozen, unchanged'} |")
        qh = r["hook"] if "“" in r["hook"] else f"“{r['hook']}”"
        L.append(f"| Opening hook (from 0 s) | {qh} |")
        L.append(f"| CTA | {r['cta']} → betterforyourpocket.com |\n")
        L.append(f"## Angle / problem\n{r['angle']}\n")
        L.append("## Script / on-screen text (beat by beat)")
        for i, bt in enumerate(r["script"], 1):
            L.append(f"{i}. {bt}")
        L.append("")
        D = vo2.get("direction") or {}
        L.append("## Voice direction (FR)")
        for k, lab in (("intent", "Intention"), ("delivery", "Interprétation"), ("pace", "Rythme"), ("energy", "Énergie"), ("pauses", "Pauses"), ("emphasis", "Accents")):
            if D.get(k):
                L.append(f"- **{lab}** : {D[k]}")
        L.append("")
        L.append("## Voice-over (as rendered)" + (" — same words and same slots as the karaoke captions" if karaoke else " — narration anchored to the edit (cuts, zooms, reveals, CTA)"))
        L.append("| start | end | line | lands on (note, FR) |\n|---:|---:|---|---|")
        for ln in vo2["lines"]:
            L.append(f"| {ln['t0']:.2f} s | {ln['t1']:.2f} s | {ln['text']} | {ln.get('note', '')} |")
        q = vo2["qc"]
        L.append(f"\nIsolated-voice QC: ASR word match {q['word_match']:.3f} (gate ≥ 0.97) · naturalness UTMOS mean {q['utmos_mean']} / min {q['utmos_min']} "
                 f"(gates ≥ 4.0 / ≥ 3.6) · {q['wps']} words/s while speaking · every line inside its window"
                 + (" · every line within ±4 % of its karaoke slot" if karaoke else "") + f" → **PASS**. VO file sha256 `{vo2['sha256'][:16]}…`")
        L.append(f"\nMix: dynamic ducking (music −{mx['music_duck_db']} dB, extra −{mx['carve_db']} dB carve at 1–4.5 kHz, SFX −{mx['sfx_duck_db']} dB, "
                 f"only while the voice speaks) · voice {mx['vo_over_bed_lu']} LU over the bed (gate ≥ 7) · ASR on the final mix {qc['vo_word_match_final_mix']:.3f} (gate ≥ 0.95)\n")
        L.append("## Sources used (external, verified)")
        if r["sources"]:
            for sid in r["sources"]:
                s = P.SRC[sid]
                L.append(f"- {s['name']} — {s['date']} — {s['url']}")
        else:
            L.append("- None needed: every claim in this reel is shown on the real BFYP screens below.")
        L.append("")
        L.append("## BFYP assets used (real product, no mockups)")
        for a in r["bfyp"]:
            L.append(f"- {fmt_cap(a)}")
        if rid in QUOTED:
            qa, how, words = QUOTED[rid]
            L.append(f"- BFYP wording reproduced as text ({how})" + (f": {words}" if words else "") + f" — source: {fmt_cap(qa)}")
        L.append("")
        L.append("## Illustrations (labelled on screen where they could be mistaken for real)")
        for it in ILLUS.get(rid, ["None"]):
            L.append(f"- {it}")
        L.append("")
        qcv = r["cover"] if r["cover"].startswith("“") else f"“{r['cover']}”"
        L.append("## Cover\n" + f"`{f_cov}` — cover line: {qcv}\n")
        L.append("## Caption — Instagram\n```text\n" + r["ig"] + "\n\n" + " ".join(r["tags"]) + "\n\n" +
                 ("Données de marché à visée éducative. Pas un conseil en investissement." if lang == "FR" else "Educational market data. Not financial advice.") + "\n```\n")
        L.append("## Caption — X\n```text\n" + r["x"] + "\n```\n")
        L.append("## Hashtags\n" + " ".join(r["tags"]) + "\n")
        if r["sources"]:
            L.append("## First comment (sources, optional)\n```text\nSources: " + " · ".join(f"{P.SRC[s]['name']} ({P.SRC[s]['date']})" for s in r["sources"]) + "\n```\n")
        L.append("## QC report")
        L.append("### Technical (automated, measured on the final file)")
        L.append("| Check | Result |\n|---|---|")
        L.append(f"| Container / codecs | MP4 (faststart) · {tech['vcodec']} {tech['vprofile']} · {tech['pix_fmt']} · {tech['acodec']} {tech['sample_rate']} Hz {tech['channels']} |")
        L.append(f"| Resolution / fps | {tech['width']}×{tech['height']} · {tech['fps']:.0f} fps |")
        L.append(f"| Duration | {tech['duration_s']:.2f} s |")
        L.append(f"| Loudness | {tech['lufs_i']:.1f} LUFS integrated (target −14) · true peak {tech['true_peak_dbtp']:.1f} dBTP (≤ −1) |".replace("-", "−"))
        L.append(f"| Hook audio | sound from frame 0 ({tech['rms_first_300ms_db']:.0f} dB RMS in the first 300 ms) |".replace("-", "−"))
        L.append(f"| Tail | clean fade (last sample {tech['last_sample_abs']}) |")
        L.append(f"| Bitrate / size | {tech['bitrate_kbps']} kb/s · {tech['size_mb']} MB |")
        L.append(f"| Video stream | bit-identical to the validated edit (stream MD5 compared) — {'yes' if qc['video_identical'] else 'NO'} |")
        L.append(f"| Voice intelligibility on the final mix | ASR word match {qc['vo_word_match_final_mix']:.3f} (gate ≥ 0.95) |")
        L.append(f"| Voice over the bed | {qc['vo_over_bed_lu']} LU (gate ≥ 7) |")
        L.append("| All gates | " + ("**PASS**" if qc["pass"] else "FAIL: " + ", ".join(k for k, v in g.items() if not v)) + " |\n")
        L.append("### Editorial")
        L.append(f"- [x] Hook on screen from frame 0, first line readable within 1.5 s: {qh}")
        L.append("- [x] Structure: problem → why it hurts → proof / context → BFYP solution → CTA")
        L.append("- [x] Every number and quote traced to a primary or reputable source (listed above), or shown on a real BFYP screen")
        L.append("- [x] BFYP screens are real captures, each stamped on screen with its capture date and time (UTC)")
        L.append("- [x] No fake UI, no invented figures; illustrations are labelled where they could be mistaken for real accounts or data")
        L.append("- [x] Short on-screen text, large type, mobile safe zones respected (key text above the bottom UI band)")
        L.append("- [x] Text-safety audit (browser layout checked every 0.1 s): no text leaves the frame and none sits under the right-hand Reels buttons"
                 + (f" (only {TAPE[rid]} bleeds off the edge, by design)" if rid in TAPE else ""))
        L.append("- [x] Distinct angle and distinct BFYP payoff within the vault")
        L.append("- [x] End card: CTA + “Educational market data. Not financial advice.”")
        L.append(f"- [x] Sound: original music + sound design ({sfx}) + directed voice-over (BFYP-K2, {gender})")
        L.append("- [x] Voice-over complements the picture instead of reading the on-screen text" if not karaoke else
                 "- [x] Karaoke captions unchanged: the voice keeps the same words in the same slots")
        L.append("\n**Verdict: READY**\n")
        open(os.path.join(folder, f"{rid}_{slug}.md"), "w").write("\n".join(L))
        manifest.append({
            "id": rid, "slug": slug, "title": r["title"], "lot": r["lot"], "lang": lang,
            "format": "voice-led, karaoke captions (BFYP-K2)" if karaoke else "text-led edit + directed voice-over (BFYP-K2)",
            "voice": {"system": "BFYP-K2", "id": V2["id"], "gender": V2["gender"], "kokoro": V2["kokoro"], "lang": V2["lang"], "speed": V2.get("speed"),
                      "engine": "Kokoro-82M v1.0 (local, kokoro-onnx, Apache-2.0)", "direction": D, "vo_sha256": vo2["sha256"],
                      "utmos_mean": vo2["qc"]["utmos_mean"], "asr_final_mix": qc["vo_word_match_final_mix"], "vo_over_bed_lu": qc["vo_over_bed_lu"]},
            "karaoke": karaoke, "ai_voice_label_on_screen": karaoke, "video_identical_to_validated_edit": qc["video_identical"],
            "duration_s": tech["duration_s"], "lufs_i": tech["lufs_i"], "true_peak_dbtp": tech["true_peak_dbtp"],
            "size_mb": tech["size_mb"], "video": f"READY/{rid}_{slug}/{f_mp4}", "cover": f"READY/{rid}_{slug}/{f_cov}",
            "sheet": f"READY/{rid}_{slug}/{rid}_{slug}.md", "sha256_video": h_mp4, "sha256_cover": h_cov,
            "hook": r["hook"], "cta": r["cta"], "music": {k: music.get(k) for k in ("style", "bpm", "key", "mode")},
            "sources": [P.SRC[s]["url"] for s in r["sources"]], "bfyp_assets": {a: CAT[a]["captured"] for a in r["bfyp"]},
            "qc_pass": qc["pass"], "status": "READY", "publish_after": "2026-09-30",
        })
    if not lots:
        json.dump({"vault": "BFYP VAULT V2", "created": "2026-09-24", "count": len(manifest), "reels": manifest},
                  open(os.path.join(VAULT, "manifest.json"), "w"), indent=1, ensure_ascii=False)
    print(len(manifest), "reels packaged" + (f" (lots {sorted(lots)}; manifest not written)" if lots else ""))


if __name__ == "__main__":
    # package.py            -> all 30 reels + manifest.json
    # package.py 1 [2 ...]  -> only these lots (no manifest)
    main({int(a) for a in sys.argv[1:]} or None)
