#!/usr/bin/env python3
"""BFYP Vault V2 — local review page.

make_review.py -> vault-v2/review.html (reads vault-v2/manifest.json + plan/plan.py; never touches the reels).
Open the page from a local checkout: videos and covers load from READY/ by relative path.
Verdicts and notes are kept in the browser (localStorage) and exported as text or JSON.
"""
import importlib.util
import json
import os
import subprocess

VAULT = "/home/user/bfyp-social-media/vault-v2"
PLAN = "/opt/bfyp/plan/plan.py"

# One-line problem -> BFYP solution, in French for the reviewer
PS = {
    "V2-01": "Même le compte X de la SEC a publié une fausse info → BFYP renvoie au dépôt officiel, daté et lié à SEC.gov.",
    "V2-02": "Des « gourous » affirment acheter sans preuve (SEC : 8 influenceurs, 100 M$, allégations) → BFYP montre les Form 4 d’initiés, datés et liés.",
    "V2-03": "Une IA sûre d’elle a inventé 6 jurisprudences → l’AI Research de BFYP relie chaque chiffre à sa preuve et dit quand la donnée manque.",
    "V2-04": "Un faux tweet a effacé 136,5 Md$ avant toute vérification → BFYP Today part de ce qui a été observé, sans prédiction.",
    "V2-05": "Les faux avis sont si répandus que la FTC les a interdits → BFYP n’affiche aucun témoignage et invite à l’auditer.",
    "V2-06": "48 % des investisseurs Gen Z apprennent sur des fils faits pour l’engagement → BFYP montre sur quoi repose chaque info.",
    "V2-07": "« Ce fonds vient d’acheter » peut dater de plusieurs mois (13F) → BFYP affiche la période et la date de dépôt.",
    "V2-08": "Une capture peut être recadrée, ancienne ou retouchée → sur BFYP, chaque donnée a un lien vérifiable (explorer, SEC.gov).",
    "V2-09": "L’exercice 2026 de NVIDIA s’est clos en janvier 2026 : mauvaise période, mauvaise conclusion → BFYP date chaque chiffre.",
    "V2-10": "Un fonds S&P 500 « diversifié » : 36 % dans 10 lignes → BFYP montre les principales positions telles que déposées.",
    "V2-11": "11 onglets pour un seul ticker, et on rate encore ce qui a changé → BFYP réunit Today, whales, Smart Money, dépôts et IA.",
    "V2-12": "Le prix dit que ça bouge, pas ce qui a changé → BFYP Today compte les observations réelles des dernières 24 h.",
    "V2-13": "« Les whales achètent »… depuis quand ? → sur BFYP, chaque chiffre porte sa fenêtre de temps (24 h, 7 j, 30 j).",
    "V2-14": "Une alerte whale brute ne donne qu’une taille → BFYP type, regroupe, note et source chaque gros mouvement.",
    "V2-15": "Coller un ticker dans un chatbot oblige à tout réexpliquer → sur BFYP, l’actif ouvre l’AI Research avec son contexte.",
    "V2-16": "Le coût d’une réponse IA se découvre après coup → BFYP l’affiche en crédits avant la question (52 crédits gratuits/mois).",
    "V2-17": "Que donne vraiment le plan gratuit ? → les 10 éléments du plan à 0 $, mot pour mot depuis la page tarifs.",
    "V2-18": "« VOO : 1 670 Md$ ? » Ce montant couvre tout le fonds, toutes classes de parts → BFYP dit ce que couvre chaque chiffre.",
    "V2-19": "3 Form 144 sur NVIDIA ≠ ventes d’initiés : un 144 annonce une vente envisagée → BFYP montre ce qui a été déposé (ventes : Form 4).",
    "V2-20": "Sur des questions de dépôts SEC, une IA testée s’est trompée ou a refusé 81 % du temps → BFYP part du dépôt, chiffres sourcés.",
    "V2-21": "Le plus gros wallet n’est pas le plus malin → BFYP classe les wallets par comportement observé, jamais par taille seule.",
    "V2-22": "Ce « whale » est peut-être un teneur de marché → BFYP étiquette chaque wallet par comportement (Market Maker…).",
    "V2-23": "Deux scores de 31/100 ne se valent pas → BFYP affiche le badge de confiance à côté de chaque score.",
    "V2-24": "3 gains d’affilée : génie ou chance ? → BFYP marque « Unproven » les historiques trop courts.",
    "V2-25": "Sur l’USDC, les données allaient dans les deux sens → BFYP Today montre les deux côtés, pas une seule histoire.",
    "V2-26": "Un signal isolé, c’est du bruit → BFYP signale les observations de natures différentes qui arrivent ensemble.",
    "V2-27": "Une opinion impossible à réfuter n’est qu’une impression → chaque ligne BFYP Today dit ce qui la prouverait.",
    "V2-28": "Sans données, un chiffre inventé est pire qu’un vide → BFYP le dit au lieu d’inventer un consensus.",
    "V2-29": "Une capture vieillit dès qu’elle est prise (330 → 354 observations en 46 min) → BFYP horodate chaque écran publié.",
    "V2-30": "Rumeur, capture, gros titre : ce ne sont pas des sources → BFYP remonte au dépôt officiel, daté et lié.",
}


def main():
    spec = importlib.util.spec_from_file_location("plan", PLAN)
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    plan = {r["id"]: r for r in P.REELS}
    man = json.load(open(os.path.join(VAULT, "manifest.json")))
    commit = subprocess.run(["git", "-C", VAULT, "log", "-1", "--format=%h", "--", "READY"], capture_output=True, text=True).stdout.strip()
    reels = []
    for m in man["reels"]:
        p = plan[m["id"]]
        voiced = m["format"].startswith("voice")
        reels.append({
            "id": m["id"], "title": m["title"], "lot": m["lot"], "lang": m["lang"], "dur": m["duration_s"],
            "voice": "BFYP-K1" if voiced else "Text-led", "ps": PS[m["id"]], "cta": p["cta"],
            "video": m["video"], "cover": m["cover"], "sheet": m["sheet"], "sha": m["sha256_video"],
        })
    assert len(reels) == 30 and all(r["ps"] for r in reels)
    data = json.dumps(reels, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", data).replace("__COMMIT__", commit or "?")
    out = os.path.join(VAULT, "review.html")
    open(out, "w").write(html)
    print(out, round(os.path.getsize(out) / 1024, 1), "KB · commit", commit)


TEMPLATE = r"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Revue Vault V2</title>
<style>
:root {
  --bg: #080e0d; --panel: #0d1614; --panel2: #111c19; --line: #1d2b27; --line2: #2a3b36;
  --ink: #eef4f1; --sub: #a3b1ac; --dim: #6f7e79;
  --green: #17b58a; --green2: #22d3a0; --green-bg: rgba(23,181,138,0.14);
  --red: #ff5d5d; --red-bg: rgba(255,93,93,0.13); --amber: #f0b44a; --amber-bg: rgba(240,180,74,0.13);
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { background: var(--bg); }
body { margin: 0; background: var(--bg); color: var(--ink);
  font: 15px/1.45 Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
.mono { font-family: ui-monospace, "SF Mono", "Geist Mono", Menlo, Consolas, monospace; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 16px; }
a { color: var(--green2); }
button { font: inherit; color: inherit; }

/* header */
header { position: sticky; top: 0; z-index: 20; background: rgba(8,14,13,0.94); backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }
.top { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 18px; padding-top: 12px; padding-bottom: 12px; }
.brand { font-weight: 800; letter-spacing: -0.01em; font-size: 18px; margin-right: auto; }
.brand small { display: block; font-weight: 500; font-size: 12px; color: var(--dim); letter-spacing: 0.02em; }
.stats { display: flex; gap: 14px; font-size: 14px; color: var(--sub); white-space: nowrap; }
.stats b { font-variant-numeric: tabular-nums; color: var(--ink); }
.stats .s-ok b { color: var(--green2); } .stats .s-fix b { color: var(--red); }
.bar { flex-basis: 100%; height: 4px; border-radius: 4px; background: var(--line); overflow: hidden; display: flex; }
.bar i { display: block; height: 100%; }
.bar .b-ok { background: var(--green); } .bar .b-fix { background: var(--red); }
.toolbar { padding-top: 12px; padding-bottom: 4px; }
.tools { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.seg { display: inline-flex; border: 1px solid var(--line2); border-radius: 10px; overflow: hidden; }
.seg button { background: transparent; border: 0; padding: 7px 12px; cursor: pointer; color: var(--sub); font-size: 13px; }
.seg button + button { border-left: 1px solid var(--line2); }
.seg button[aria-pressed="true"] { background: var(--panel2); color: var(--ink); }
.tools .sp { flex: 1; }
.btn { background: var(--panel2); border: 1px solid var(--line2); border-radius: 10px; padding: 7px 12px; cursor: pointer; font-size: 13px; color: var(--ink); }
.btn:hover { border-color: var(--green); }
.btn.primary { background: var(--green); border-color: var(--green); color: #04110d; font-weight: 700; }
.btn.ghost { background: transparent; color: var(--sub); }
.toast { font-size: 13px; color: var(--green2); min-width: 1em; }

/* intro */
.intro { color: var(--sub); font-size: 14px; margin: 18px auto 6px; }
.intro b { color: var(--ink); font-weight: 600; }

/* cards */
#list { display: grid; gap: 14px; padding-top: 10px; padding-bottom: 20px; }
.card { display: grid; grid-template-columns: 288px 162px minmax(0, 1fr); gap: 18px; align-items: start;
  background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 16px; scroll-margin-top: 96px; }
.card[data-v="ok"] { border-color: rgba(23,181,138,0.55); }
.card[data-v="fix"] { border-color: rgba(255,93,93,0.6); }
.card[hidden] { display: none; }
.player { width: 100%; aspect-ratio: 9 / 16; background: #000; border-radius: 12px; display: block; }
.mcol { min-width: 0; }
.vfail { margin: 8px 0 0; font-size: 12px; color: var(--amber); }
.cover { display: block; }
.cover img { width: 100%; aspect-ratio: 9 / 16; object-fit: cover; border-radius: 10px; border: 1px solid var(--line2); display: block; background: #050908; }
.cover span { display: block; margin-top: 6px; font-size: 12px; color: var(--dim); text-align: center; }
.info { min-width: 0; display: flex; flex-direction: column; gap: 10px; }
.idrow { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.id { font-weight: 800; font-size: 13px; letter-spacing: 0.04em; color: var(--green2); margin-right: 4px; }
.chip { font-size: 12px; color: var(--sub); border: 1px solid var(--line2); border-radius: 999px; padding: 2px 9px; white-space: nowrap; }
.chip.voice { color: var(--amber); border-color: rgba(240,180,74,0.45); background: var(--amber-bg); }
.chip.text { color: var(--sub); }
h3 { margin: 0; font-size: 21px; line-height: 1.2; letter-spacing: -0.015em; }
.lbl { display: block; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--dim); margin-bottom: 3px; }
.ps, .cta { margin: 0; }
.cta span.v { font-weight: 650; }
.verdict { display: flex; gap: 8px; flex-wrap: wrap; }
.vb { flex: 1 1 140px; border-radius: 12px; padding: 10px 12px; cursor: pointer; font-weight: 800; letter-spacing: 0.03em;
  background: transparent; border: 2px solid var(--line2); color: var(--sub); }
.vb.ok:hover { border-color: var(--green); color: var(--green2); }
.vb.fix:hover { border-color: var(--red); color: var(--red); }
.vb.ok[aria-pressed="true"] { background: var(--green); border-color: var(--green); color: #04110d; }
.vb.fix[aria-pressed="true"] { background: var(--red); border-color: var(--red); color: #1a0505; }
textarea { width: 100%; min-height: 76px; resize: vertical; background: #070c0b; color: var(--ink); border: 1px solid var(--line2);
  border-radius: 12px; padding: 10px 12px; font-family: inherit; font-size: 14px; line-height: 1.45; }
textarea:focus, .btn:focus-visible, .vb:focus-visible, .seg button:focus-visible { outline: 2px solid var(--green2); outline-offset: 2px; }
.note-tools { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; font-size: 12px; color: var(--dim); }
.note-tools .btn { padding: 4px 9px; font-size: 12px; }
.stale { display: none; font-size: 12px; color: var(--amber); border: 1px solid rgba(240,180,74,0.45); background: var(--amber-bg); border-radius: 10px; padding: 6px 10px; }
.card.is-stale .stale { display: block; }
.saved { margin-left: auto; }

/* recap */
.recap { padding-top: 8px; padding-bottom: 40px; }
.recap h2 { font-size: 16px; margin: 10px 0 8px; }
.recap textarea { min-height: 200px; font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; font-size: 13px; }
.recap p { color: var(--sub); font-size: 13px; margin: 8px 0 0; }
.recap .recap-actions { margin: 0 0 10px; display: flex; gap: 10px; align-items: center; }
footer { color: var(--dim); font-size: 12px; padding-bottom: 30px; }

@media (max-width: 900px) {
  .card { grid-template-columns: minmax(0, 1fr) 132px; }
  .info { grid-column: 1 / -1; }
  .player { max-height: 70vh; }
}
@media (max-width: 560px) {
  .card { grid-template-columns: minmax(0, 1fr) 96px; gap: 12px; padding: 12px; }
  h3 { font-size: 19px; }
  .stats { gap: 10px; font-size: 13px; }
  .top { gap: 6px 12px; padding-top: 8px; padding-bottom: 8px; }
  .brand { font-size: 16px; }
  .brand small { display: none; }
  .card { scroll-margin-top: 80px; }
}
</style>
</head>
<body>
<header>
  <div class="wrap top">
    <div class="brand">BFYP · Vault V2 — Revue<small>30 reels · commit __COMMIT__ · aucun fichier du vault n’est modifié par cette page</small></div>
    <div class="stats" aria-live="polite">
      <span class="s-ok"><b id="nOk">0</b> validés</span>
      <span class="s-fix"><b id="nFix">0</b> à corriger</span>
      <span><b id="nTodo">30</b> sans verdict</span>
    </div>
    <div class="bar" aria-hidden="true"><i class="b-ok" id="barOk"></i><i class="b-fix" id="barFix"></i></div>
  </div>
</header>
<div class="wrap toolbar">
    <div class="tools">
      <div class="seg" role="group" aria-label="Filtrer">
        <button data-f="all" aria-pressed="true">Tous</button>
        <button data-f="todo" aria-pressed="false">Sans verdict</button>
        <button data-f="ok" aria-pressed="false">Validés</button>
        <button data-f="fix" aria-pressed="false">À corriger</button>
      </div>
      <span class="sp"></span>
      <span class="toast" id="toast" role="status"></span>
      <button class="btn primary" id="copy">Copier le récap</button>
      <button class="btn" id="dl">Télécharger .json</button>
      <button class="btn ghost" id="imp">Importer</button>
      <input type="file" id="impFile" accept=".json,application/json" hidden>
      <button class="btn ghost" id="reset">Tout effacer</button>
    </div>
</div>

<p class="wrap intro">Pour chaque reel : regarde la vidéo, choisis <b>VALIDÉ</b> ou <b>À CORRIGER</b>, et note ce qui doit changer (le bouton ⏱ ajoute le moment de la vidéo). Tout s’enregistre dans ce navigateur. À la fin, <b>Copier le récap</b> puis colle-le dans la conversation. Seuls les reels marqués À CORRIGER seront retouchés.</p>

<main class="wrap" id="list"></main>

<section class="wrap recap" aria-labelledby="recapTitle">
  <h2 id="recapTitle">Récap à m’envoyer</h2>
  <p class="recap-actions"><button class="btn primary" id="copy2" type="button">Copier le récap</button> <span class="toast" id="toast2" role="status"></span></p>
  <textarea id="recap" readonly aria-label="Récap des verdicts"></textarea>
  <p>Voix : <b>Text-led</b> = texte à l’écran, musique et sound design, sans voix. <b>BFYP-K1</b> = voix IA de secours (Kokoro, locale), utilisée à la place d’ElevenLabs Adam indisponible. Le carton de fin de ces 7 reels indique « AI voice ».</p>
</section>
<footer class="wrap">Vidéos et couvertures lues depuis <span class="mono">READY/</span> à côté de cette page. Ouvre-la depuis un clone local de la branche <span class="mono">claude/bfyp-vault-v2-reels-l883ff</span>.</footer>

<script>
const REELS = __DATA__;
const COMMIT = "__COMMIT__";
const KEY = "bfyp-vault-v2-review";
const LABEL = { ok: "VALIDÉ", fix: "À CORRIGER" };

function load() {
  try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; }
}
let state = load();
function save() {
  try { localStorage.setItem(KEY, JSON.stringify(state)); return true; } catch (e) { return false; }
}
// an entry only counts for the exact video it was given on (file hash); a new render needs a new verdict
function entry(r) { const e = state[r.id]; return e || { verdict: "", note: "", sha: r.sha }; }
function verdictOf(r) { const e = state[r.id]; return e && e.sha === r.sha ? (e.verdict || "") : ""; }
function fmtTime(s) { const m = Math.floor(s / 60), x = s - m * 60; return m + ":" + (x < 10 ? "0" : "") + x.toFixed(1); }
const $ = (s, el = document) => el.querySelector(s);

const list = $("#list");
for (const r of REELS) {
  const card = document.createElement("article");
  card.className = "card"; card.id = r.id;
  card.innerHTML = `
    <div class="mcol"><video class="player" controls preload="metadata" playsinline></video>
      <p class="vfail" hidden>Ce navigateur ne lit pas ce MP4 ici. <a class="vlink" target="_blank" rel="noopener">Ouvrir la vidéo</a></p></div>
    <a class="cover" target="_blank" rel="noopener"><img loading="lazy" alt=""><span>Couverture</span></a>
    <div class="info">
      <div class="idrow"><span class="id"></span><span class="chip c-lot"></span><span class="chip c-dur"></span><span class="chip c-voice"></span><span class="chip c-lang"></span></div>
      <h3></h3>
      <div class="stale" role="note">Nouvelle version depuis ton verdict : à revoir.</div>
      <p class="ps"><span class="lbl">Problème → Solution</span><span class="v"></span></p>
      <p class="cta"><span class="lbl">CTA</span><span class="v"></span></p>
      <div class="verdict" role="group">
        <button class="vb ok" type="button" aria-pressed="false">✓ VALIDÉ</button>
        <button class="vb fix" type="button" aria-pressed="false">✕ À CORRIGER</button>
      </div>
      <div>
        <label class="lbl"></label>
        <textarea placeholder="Note libre : ce qui doit changer (texte, timing, son, visuel…)"></textarea>
      </div>
      <div class="note-tools">
        <button class="btn t-time" type="button" title="Ajoute le moment actuel de la vidéo dans la note">⏱ Ajouter le moment</button>
        <a class="t-sheet" target="_blank" rel="noopener">Fiche complète</a>
        <span class="saved"></span>
      </div>
    </div>`;
  const v = $("video", card);
  v.src = r.video + "#t=0.05";
  $(".vlink", card).href = r.video;
  v.addEventListener("error", () => { $(".vfail", card).hidden = false; });
  v.setAttribute("aria-label", `Vidéo ${r.id}`);
  $(".cover", card).href = r.cover;
  $(".cover img", card).src = r.cover;
  $(".cover img", card).alt = `Couverture ${r.id}`;
  $(".id", card).textContent = r.id;
  $(".c-lot", card).textContent = "Lot " + r.lot;
  $(".c-dur", card).textContent = r.dur.toFixed(1).replace(".", ",") + " s";
  const cv = $(".c-voice", card);
  cv.textContent = r.voice === "Text-led" ? "Text-led" : "Voix IA · BFYP-K1";
  cv.classList.add(r.voice === "Text-led" ? "text" : "voice");
  $(".c-lang", card).textContent = r.lang;
  $("h3", card).textContent = r.title;
  $(".ps .v", card).textContent = r.ps;
  $(".cta .v", card).textContent = r.cta;
  $(".verdict", card).setAttribute("aria-label", `Verdict ${r.id}`);
  const ta = $("textarea", card), lab = $("label.lbl", card);
  ta.id = "note-" + r.id; lab.htmlFor = ta.id; lab.textContent = "Note";
  $(".t-sheet", card).href = r.sheet;

  const e = state[r.id];
  if (e) {
    ta.value = e.note || "";
    if (e.sha !== r.sha && (e.verdict || e.note)) card.classList.add("is-stale");
  }
  $(".vb.ok", card).addEventListener("click", () => setVerdict(r, "ok"));
  $(".vb.fix", card).addEventListener("click", () => setVerdict(r, "fix"));
  let tmr;
  ta.addEventListener("input", () => {
    clearTimeout(tmr);
    tmr = setTimeout(() => { setNote(r, ta.value); }, 250);
  });
  $(".t-time", card).addEventListener("click", () => {
    const stamp = "[" + fmtTime(v.currentTime || 0) + "] ";
    const pos = ta.selectionStart ?? ta.value.length;
    const before = ta.value.slice(0, pos), after = ta.value.slice(pos);
    const sep = before && !before.endsWith("\n") ? "\n" : "";
    ta.value = before + sep + stamp + after;
    ta.focus(); const at = (before + sep + stamp).length; ta.setSelectionRange(at, at);
    setNote(r, ta.value);
  });
  v.addEventListener("play", () => { document.querySelectorAll("video").forEach(o => { if (o !== v) o.pause(); }); });
  list.appendChild(card);
}

function touch(r) {
  const e = state[r.id];
  if (!e || e.sha !== r.sha) state[r.id] = { verdict: "", note: e ? e.note || "" : "", sha: r.sha };
  return state[r.id];
}
function setVerdict(r, val) {
  const e = touch(r);
  e.verdict = e.verdict === val ? "" : val;
  e.at = new Date().toISOString();
  document.getElementById(r.id).classList.remove("is-stale");
  persist(r);
}
function setNote(r, text) {
  const e = touch(r);
  e.note = text; e.at = new Date().toISOString();
  persist(r);
}
function persist(r) {
  const ok = save();
  const card = document.getElementById(r.id);
  $(".saved", card).textContent = ok ? "Enregistré" : "Non enregistré (stockage bloqué) : exporte avant de fermer";
  render();
}

let filter = "all";
document.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
  filter = b.dataset.f;
  document.querySelectorAll(".seg button").forEach(x => x.setAttribute("aria-pressed", String(x === b)));
  render();
}));

function recapText() {
  const now = new Date();
  const d = now.toLocaleDateString("fr-FR") + " " + now.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
  const by = { ok: [], fix: [], "": [] };
  for (const r of REELS) by[verdictOf(r)].push(r);
  const note = r => { const n = (state[r.id] && state[r.id].sha === r.sha ? state[r.id].note : "").trim(); return n ? "\n    note : " + n.replace(/\n/g, "\n    ") : ""; };
  const L = [];
  L.push(`VAULT V2 — revue du ${d} (commit ${COMMIT})`);
  L.push(`Validés : ${by.ok.length} · À corriger : ${by.fix.length} · Sans verdict : ${by[""].length}`);
  L.push("");
  L.push("À CORRIGER");
  if (!by.fix.length) L.push("- (aucun)");
  for (const r of by.fix) L.push(`- ${r.id} ${r.title}${note(r)}`);
  L.push("");
  L.push("VALIDÉ");
  if (!by.ok.length) L.push("- (aucun)");
  for (const r of by.ok) L.push(`- ${r.id} ${r.title}${note(r)}`);
  if (by[""].length) {
    L.push("");
    L.push("SANS VERDICT");
    for (const r of by[""]) L.push(`- ${r.id} ${r.title}${note(r)}`);
  }
  return L.join("\n");
}
function exportJson() {
  return {
    vault: "BFYP VAULT V2", reviewed_commit: COMMIT, exported_at: new Date().toISOString(),
    summary: { valide: REELS.filter(r => verdictOf(r) === "ok").length, a_corriger: REELS.filter(r => verdictOf(r) === "fix").length,
               sans_verdict: REELS.filter(r => !verdictOf(r)).length },
    reels: REELS.map(r => {
      const e = state[r.id] && state[r.id].sha === r.sha ? state[r.id] : {};
      return { id: r.id, title: r.title, verdict: LABEL[e.verdict] || "", note: e.note || "", video: r.video, sha256_video: r.sha, at: e.at || null };
    }),
  };
}

function render() {
  let ok = 0, fix = 0;
  for (const r of REELS) {
    const v = verdictOf(r);
    if (v === "ok") ok++; else if (v === "fix") fix++;
    const card = document.getElementById(r.id);
    card.dataset.v = v;
    $(".vb.ok", card).setAttribute("aria-pressed", String(v === "ok"));
    $(".vb.fix", card).setAttribute("aria-pressed", String(v === "fix"));
    card.hidden = !(filter === "all" || (filter === "todo" && !v) || filter === v);
  }
  $("#nOk").textContent = ok; $("#nFix").textContent = fix; $("#nTodo").textContent = REELS.length - ok - fix;
  $("#barOk").style.width = (ok / REELS.length * 100) + "%";
  $("#barFix").style.width = (fix / REELS.length * 100) + "%";
  $("#recap").value = recapText();
}

function toast(msg) {
  for (const t of [$("#toast"), $("#toast2")]) t.textContent = msg;
  clearTimeout(toast.t); toast.t = setTimeout(() => { $("#toast").textContent = ""; $("#toast2").textContent = ""; }, 3500);
}
async function copyRecap() {
  const text = recapText();
  try { await navigator.clipboard.writeText(text); toast("Récap copié"); }
  catch (e) {
    const ta = $("#recap"); ta.value = text; ta.focus(); ta.select();
    try { document.execCommand("copy"); toast("Récap copié"); } catch (e2) { toast("Sélectionne le récap en bas de page et copie-le"); }
  }
}
$("#copy").addEventListener("click", copyRecap);
$("#copy2").addEventListener("click", copyRecap);
$("#dl").addEventListener("click", () => {
  const blob = new Blob([JSON.stringify(exportJson(), null, 1)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "vault-v2-verdicts-" + new Date().toISOString().slice(0, 16).replace(/[:T]/g, "-") + ".json";
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  toast("Fichier téléchargé");
});
$("#imp").addEventListener("click", () => $("#impFile").click());
$("#impFile").addEventListener("change", async ev => {
  const f = ev.target.files[0]; if (!f) return;
  try {
    const j = JSON.parse(await f.text());
    const inv = { "VALIDÉ": "ok", "À CORRIGER": "fix" };
    let n = 0;
    for (const x of j.reels || []) {
      const r = REELS.find(y => y.id === x.id); if (!r) continue;
      state[r.id] = { verdict: inv[x.verdict] || "", note: x.note || "", sha: x.sha256_video || r.sha, at: x.at || null };
      const card = document.getElementById(r.id);
      $("textarea", card).value = state[r.id].note;
      card.classList.toggle("is-stale", state[r.id].sha !== r.sha && !!(state[r.id].verdict || state[r.id].note));
      n++;
    }
    save(); render(); toast(n + " verdicts importés");
  } catch (e) { toast("Fichier illisible"); }
  ev.target.value = "";
});
$("#reset").addEventListener("click", () => {
  if (!confirm("Effacer tous les verdicts et notes de ce navigateur ?")) return;
  state = {}; save();
  document.querySelectorAll("#list textarea").forEach(t => t.value = "");
  document.querySelectorAll(".card").forEach(c => c.classList.remove("is-stale"));
  render(); toast("Tout est effacé");
});
render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
