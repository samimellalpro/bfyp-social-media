/* V2-30 — FR — "Pas de source ? C'est du contenu." (échelle de preuve) */
R.setup({ dur: 20.6, bpm: 148 });
const b = B;
music({ style: 'futurebass', bpm: 148, key: 'A', mode: 'major', prog: ['IV', 'V', 'iii', 'vi'], seed: 3030,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 25, type: 'build' }, { beat: 26, type: 'drop' }, { beat: 42, type: 'cta' }],
  events: [{ type: 'stop', beat: 25, beats: 1 }, { type: 'end', beat: 50.5, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_a', { parent: 's1', x: 72, y: 420, w: 936, o: 1, html: '<div class="h1" style="font-size:150px">Pas de<br>source ?</div>' });
K('s1_a', 's', [[0, 1.08, 'linear'], [0.5, 1, 'outExpo']]);
cue(0, 'impact', { size: 1.0 });
mk('s1_b', { parent: 's1', x: 72, y: 800, w: 936, o: 0, html: '<div class="h1" style="font-size:150px"><span class="red">C’est du<br>contenu.</span></div>' });
slam('s1_b', b(3)); cue(b(3), 'hit'); camPunch(b(3), 0.03);
shotOut('s1', b(8) - 0.1, 'up', 0.3);

// S2 ÉCHELLE DE PREUVE ------------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'up', 0.3);
mk('s2_h', { parent: 's2', x: 72, y: 250, w: 936, o: 1, html: '<div class="eyebrow" style="margin-bottom:18px">L’échelle de la preuve</div><div class="h2">Du plus faible au plus solide :</div>' });
const RUNGS = [
  { t: 'Rumeur', ok: false },
  { t: 'Capture d’écran', ok: false },
  { t: 'Gros titre', ok: false },
  { t: 'Dépôt officiel,<br>daté, avec lien', ok: true },
];
RUNGS.forEach((r, i) => {
  const id = `s2_r${i}`;
  const y = 1260 - i * 190, x = 72 + i * 40;
  mk(id, { parent: 's2', x, y, w: 878 - i * 40, o: 0, origin: '0 50%', html: `
    <div style="display:flex;align-items:center;gap:26px;height:150px;padding:0 36px;border-radius:26px;border:3px solid ${r.ok ? '#22d3a0' : '#2a3935'};background:${r.ok ? 'rgba(23,181,138,0.16)' : '#0f1816'};${r.ok ? 'box-shadow:0 0 50px rgba(34,211,160,0.4)' : ''}">
      <div class="mono" style="font-size:34px;color:${r.ok ? '#22d3a0' : '#6c7874'}">0${i + 1}</div>
      <div style="font-weight:800;font-size:${r.ok ? 42 : 56}px;letter-spacing:-0.02em;color:${r.ok ? '#eef4f1' : '#9aa7a2'}">${r.t}</div>
      <div style="margin-left:auto;font-size:56px;font-weight:800;color:${r.ok ? '#22d3a0' : '#ff5d5d'}">${r.ok ? '✓' : '✗'}</div></div>` });
  const t = b(10 + i * 3);
  K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
  K(id, 'sx', [[t, 0.2, 'linear'], [t + 0.35, 1, 'outExpo']]);
  cue(t, r.ok ? 'ding' : 'tick', r.ok ? { note: 88 } : {});
  if (!r.ok) K(id, 'o', [[t + b(2.6), 1, 'linear'], [t + b(2.9), 0.45, 'linear']]);
});
cue(b(26), 'riser', { dur: b(4) });
shotOut('s2', b(26) - 0.1, 'zoom', 0.22);

// S3 BFYP : période + document ---------------------------------------------
shot('s3'); shotIn('s3', b(26), 'zoomIn', 0.4);
cue(b(26), 'impact', { size: 0.9 }); cue(b(26) + 0.05, 'ding', { note: 90 });
headline('s3_h', ['Sur BFYP, chaque', 'chiffre <span class="g">a sa source.</span>'], { parent: 's3', y: 250, cls: 'h2', css: 'font-size:76px', eyebrow: 'BFYP · NVDA · tel que déposé' });
wordsIn('s3_h', b(26) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'nvda_fund', { parent: 's3', w: 860, x: 110, y: 660 });
stamp('s3_stamp', 'nvda_fund', { parent: 's3', x: 110, y: 580, text: 'ÉCRAN RÉEL · CAPTURÉ LE 23 SEPT. 2026 · 22:01 UTC' });
appear('s3_stamp', b(26) + 0.3, { dy: 14, blur: 0 });
K('s3_h', 'o', [[b(28), 1, 'linear'], [b(28) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(28), 1, 'linear'], [b(28) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: REG.nvda_fund.rev_meta, key: 'PÉRIODE + DOCUMENT', text: 'Exercice clos le 25/01/2026 · 10-K · SEC', t0: b(28), t1: b(34), s: 1.6 },
], { cy: 1000, fit: 700, maxS: 1.6, callY: 330 });
shotOut('s3', b(34) - 0.05, 'left', 0.3);

shot('s4'); shotIn('s4', b(34), 'left', 0.3);
headline('s4_h', ['Et le lien', '<span class="g">vers l’original.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'BFYP · ETF · SPY' });
wordsIn('s4_h', b(34) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'spy_note', { parent: 's4', w: 940, x: 70, y: 700 });
K('s4_h', 'o', [[b(35.5), 1, 'linear'], [b(35.5) + 0.2, 0, 'linear']]);
tour('s4_card', [
  { r: REG.spy_note.asfiled, key: 'DÉPÔT ORIGINAL', text: 'N-PORT déposé auprès de la SEC', t0: b(35.5), t1: b(41.8), s: 1.45 },
], { cy: 1000, fit: 900, maxS: 1.5, callY: 330 });
mk('s4_cap', { parent: 'fx', x: 72, y: 1478, o: 0, html: '<div class="capline"><b>●</b> Écran réel BFYP · ETF · SPY · 23 sept. 2026 · 22:01 UTC</div>' });
K('s4_cap', 'o', [[b(35.5), 0, 'linear'], [b(35.7), 1, 'linear'], [b(41.8), 1, 'linear'], [b(42), 0, 'linear']]);
shotOut('s4', b(42) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(42), { lines: ['Remonte', '<span class="g">à la source.</span>'], sub: 'Gratuitement, sur betterforyourpocket.com', button: 'betterforyourpocket.com',
  disc: '<span style="font-size:0.88em">Données de marché à visée éducative. Pas un conseil en investissement.</span>',
  visual: { asset: 'nvda_fund', w: 600 }, note: 'Écrans du 23 sept. 2026 · les données évoluent' });
$('cta_vstamp').innerHTML = '<div class="pill" style="font-size:19px;padding:8px 16px"><span class="dot"></span>CAPTURÉ LE 23 SEPT. 2026 · 22:01 UTC</div>';
cue(b(42) + 0.4, 'sparkle');
cue(b(50.5), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Pas de source ?', '<span class="red">C’est du</span>', '<span class="red">contenu.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:124px',
  extra: '<div class="h3" style="position:absolute;left:76px;top:900px;color:#c6d4cf">Rumeur ✗ · Capture ✗ · Titre ✗</div><div class="h3" style="position:absolute;left:76px;top:1000px">Dépôt officiel, daté, avec lien <span class="g">✓</span></div>' });
