/* V2-12 — "Prices move. What changed?" */
R.setup({ dur: 20.4, bpm: 122 });
const b = B;
music({ style: 'minimal', bpm: 122, key: 'F#', mode: 'minor', prog: ['i', 'VII', 'VI', 'VII'], seed: 1212,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 15, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 32, type: 'cta' }],
  events: [{ type: 'stop', beat: 15, beats: 1 }, { type: 'end', beat: 41, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: colour flicker ---------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
const W8 = ['<span class="g">GREEN.</span>', '<span class="red">RED.</span>', '<span class="g">GREEN.</span>', '<span class="red">RED.</span>'];
wordSwap('s1_w', W8, 0, b(1), { parent: 's1', y: 640, cls: 'h1', css: 'font-size:210px', sfx: 'tick', hideLast: true });
// ticker-like tape (abstract, no data)
mk('s1_top', { parent: 's1', x: 72, y: 300, w: 936, o: 1, html: '<div class="h2">Your dashboard,<br>all day:</div>' });
K('s1_top', 's', [[0, 1.05, 'linear'], [0.45, 1, 'outExpo']]);
mk('s1_tape', { parent: 's1', x: 0, y: 540, w: 1080, o: 1, html: '<div class="mono" style="white-space:nowrap;font-size:34px;letter-spacing:.12em;color:#3a4b46">▲ ▼ ▲ ▲ ▼ ▲ ▼ ▼ ▲ ▲ ▼ ▲ ▼ ▲ ▲ ▼ ▲ ▼ ▼ ▲ ▲ ▼ ▲ ▼ ▲ ▲ ▼ ▲</div>' });
K('s1_tape', 'x', [[0, 0, 'linear'], [b(8), -500, 'linear']]);
hook(t => { $('bg').style.filter = t < b(4) ? `hue-rotate(${Math.floor(t / b(1)) % 2 ? 200 : 0}deg)` : 'none'; });
mk('s1_t', { parent: 's1', x: 72, y: 960, w: 936, o: 0, html: '<div class="h2">It shows <span class="g">prices.</span><br>Not <span class="red">what changed.</span></div>' });
appear('s1_t', b(4), { dy: 40 }); cue(b(4), 'hit');
cue(0, 'impact', { size: 0.9 });
shotOut('s1', b(8) - 0.1, 'zoom', 0.25);

// S2 THAT vs WHAT ------------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'zoomIn', 0.3);
mk('s2_a', { parent: 's2', x: 72, y: 600, o: 0, html: '<div class="h1" style="font-size:120px">Price tells you<br><span class="g">THAT.</span></div>' });
slam('s2_a', b(8)); cue(b(8), 'hit');
mk('s2_b', { parent: 's2', x: 72, y: 930, o: 0, html: '<div class="h1" style="font-size:120px">Not <span class="red">WHAT.</span></div>' });
slam('s2_b', b(10.5)); cue(b(10.5), 'hit');
cue(b(16), 'riser', { dur: b(3) });
shotOut('s2', b(16) - 0.1, 'zoom', 0.2);

// S3 BFYP Today counts -------------------------------------------------
shot('s3'); shotIn('s3', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.9 }); cue(b(16) + 0.05, 'ding', { note: 88 });
mk('s3_eb', { parent: 's3', x: 72, y: 250, o: 1, html: '<div class="eyebrow">On BFYP · Today · last 24h</div>' });
mk('s3_n', { parent: 's3', x: 60, y: 300, o: 1, html: '<div class="bigno g" id="obs" style="font-size:210px">0</div>' });
counter('obs', b(16.2), b(18.5), 0, 354, v => Math.round(v).toString());
cue(b(16.2), 'ticks', { n: 18, dur: b(2.2), curve: 0.55 });
mk('s3_l', { parent: 's3', x: 72, y: 520, o: 0, html: '<div class="h3">observations. <span class="m">10 assets.</span></div>' });
appear('s3_l', b(17.5), { dy: 20 });
realScreen('s3_card', 'today_cats', { parent: 's3', w: 860, x: 110, y: 660 });
appear('s3_card', b(18), { dy: 60 });
stamp('s3_stamp', 'today_cats', { parent: 's3', x: 110, y: 610, size: 20, pad: '8px 16px' });
appear('s3_stamp', b(18.3), { dy: 10, blur: 0 });
screenCaption('s3_cap', 'today_cats');
K('s3_cap', 'o', [[b(20) - 0.001, 0, 'linear'], [b(20) + 0.2, 1, 'linear'], [b(31.8), 1, 'linear'], [b(32), 0, 'linear']]);
['s3_eb', 's3_n', 's3_l', 's3_stamp'].forEach(id => K(id, 'o', [[b(20.8), 1, 'linear'], [b(21), 0, 'linear'], [b(29.6), 0, 'linear'], [b(30), 1, 'linear']]));
tour('s3_card', [
  { r: REG.today_cats.r1, key: 'ON-CHAIN', text: '234 observations', t0: b(21), t1: b(23.5) },
  { r: REG.today_cats.r2, key: 'COMPANIES & THEMES', text: '101 observations', t0: b(23.5), t1: b(26) },
  { r: [40, 230, 784, 226], key: 'CRYPTO · MACRO · STOCKS & ETFs', text: '11 · 5 · 3', t0: b(26), t1: b(28.5) },
  { r: REG.today_cats.note, key: 'COUNTS, NOT PRICES', text: 'Not price movement. Not size.', t0: b(28.5), t1: b(31.6), s: 1.2 },
], { cy: 1030, fit: 860, maxS: 1.3, callY: 330 });
shotOut('s3', b(32) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(32), { lines: ['Start with', '<span class="g">what changed.</span>'], sub: 'Observed activity. Nothing here is a prediction.',
  visual: { asset: 'today_cats', w: 620 }, note: 'BFYP Today data from 23 Sep 2026 · live data changes' });
cue(b(32) + 0.4, 'sparkle');
cue(b(41), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Prices move.', '<span class="g">What changed?</span>'], hY: 400, cls: 'h1', hCss: 'font-size:120px', asset: 'today_cats', visW: 760, visY: 800 });
