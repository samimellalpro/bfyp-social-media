/* V2-26 — "Alone it's noise." (connected observations) */
R.setup({ dur: 20.6, bpm: 125 });
const b = B;
music({ style: 'techhouse', bpm: 125, key: 'D', mode: 'minor', prog: ['i', 'VII', 'VI', 'v'], seed: 2626,
  sections: [{ beat: 0, type: 'tension' }, { beat: 6, type: 'hook' }, { beat: 15, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 34, type: 'cta' }],
  events: [{ type: 'stop', beat: 15, beats: 1 }, { type: 'end', beat: 42.5, tail: 0.3 }] });
progressBar(); bgLife();

// node graph (abstract illustration)
function node(id, parent, x, y, r, col, label) {
  mk(id, { parent, x: x - r, y: y - r, w: 2 * r, h: 2 * r, o: 0, origin: '50% 50%', html: `<div style="width:${2 * r}px;height:${2 * r}px;border-radius:50%;background:${col};box-shadow:0 0 ${r}px ${col}"></div>${label ? `<div class="mono" style="position:absolute;left:50%;top:${2 * r + 14}px;transform:translateX(-50%);white-space:nowrap;font-size:26px;color:#c6d4cf">${label}</div>` : ''}` });
}
function edge(id, parent, x1, y1, x2, y2, t, col = '#22d3a0') {
  const len = Math.hypot(x2 - x1, y2 - y1), ang = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
  mk(id, { parent, x: x1, y: y1 - 3, w: len, h: 6, o: 0, origin: '0 50%', html: `<div style="width:${len}px;height:6px;border-radius:6px;background:${col};box-shadow:0 0 16px ${col}"></div>` });
  K(id, 'r', [[0, ang, 'linear']]);
  K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
  K(id, 'sx', [[t, 0, 'linear'], [t + 0.35, 1, 'outExpo']]);
}

// S1 HOOK: one lonely dot ----------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 250, w: 936, o: 1, html: '<div class="h1" style="font-size:130px">One signal<br>alone? <span class="m">Noise.</span></div>' });
K('s1_t', 's', [[0, 1.05, 'linear'], [0.5, 1, 'outExpo']]);
node('s1_n0', 's1', 540, 1000, 42, '#8a9a94');
K('s1_n0', 'o', [[0, 1, 'linear']]);
[0.1, b(2), b(4)].forEach((t, k) => {
  const id = `s1_ring${k}`;
  mk(id, { parent: 's1', x: 540 - 70, y: 1000 - 70, w: 140, h: 140, o: 0, origin: '50% 50%', style: { border: '4px solid rgba(170,185,180,0.75)', borderRadius: '50%' } });
  K(id, 's', [[t, 0.4, 'linear'], [t + 1.4, 3.6, 'outCubic']]);
  K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 0.9, 'linear'], [t + 1.4, 0, 'inQuad']]);
});
mk('s1_lbl', { parent: 's1', x: 340, y: 1285, w: 400, o: 1, html: '<div class="mono" style="text-align:center;font-size:28px;letter-spacing:.14em;color:#8a9a94">1 observation</div>' });
K('s1_lbl', 'o', [[b(6) - 0.2, 1, 'linear'], [b(6), 0, 'linear']]);
hook(t => { if (t < b(6)) { const k = 1 + 0.25 * Math.max(0, Math.sin(t * 6.5)); $('s1_n0').style.transform += ` scale(${k.toFixed(3)})`; } });
cue(0, 'impact', { size: 0.8 }); cue(0.1, 'heartbeat'); cue(b(2), 'heartbeat'); cue(b(4), 'heartbeat');
// connection build
const P = { w: [540, 1080], a: [250, 820], b2: [830, 820], a2: [250, 1340], b3: [830, 1340] };
node('s1_w', 's1', P.w[0], P.w[1], 46, '#22d3a0', 'wallet 0xe1ad…1691');
node('s1_a', 's1', P.a[0], P.a[1], 26, '#5cc8ff', 'kind A');
node('s1_b', 's1', P.b2[0], P.b2[1], 26, '#f0b44a', 'kind B');
node('s1_c', 's1', P.a2[0], P.a2[1], 26, '#5cc8ff', 'kind A');
node('s1_d', 's1', P.b3[0], P.b3[1], 26, '#f0b44a', 'kind B');
K('s1_n0', 'o', [[b(6) - 0.2, 1, 'linear'], [b(6), 0, 'linear']]);
[['s1_w', 6], ['s1_a', 7], ['s1_b', 7.5], ['s1_c', 8], ['s1_d', 8.5]].forEach(([id, bt]) => { popIn(id, b(bt), { from: 0.2 }); cue(b(bt), 'pop'); });
edge('s1_e1', 's1', P.a[0], P.a[1], P.w[0], P.w[1], b(9));
edge('s1_e2', 's1', P.b2[0], P.b2[1], P.w[0], P.w[1], b(9.5));
edge('s1_e3', 's1', P.a2[0], P.a2[1], P.w[0], P.w[1], b(10));
edge('s1_e4', 's1', P.b3[0], P.b3[1], P.w[0], P.w[1], b(10.5));
[9, 9.5, 10, 10.5].forEach(x => cue(b(x), 'tick'));
mk('s1_t2', { parent: 's1', x: 72, y: 250, w: 936, o: 0, html: '<div class="h2" style="font-size:96px">Different kinds.<br>Same wallet.<br><span class="g">Same time?</span></div>' });
K('s1_t', 'o', [[b(6) - 0.15, 1, 'linear'], [b(6), 0, 'linear']]);
appear('s1_t2', b(6), { dy: 30 });
mk('s1_ill', { parent: 's1', x: 76, y: 1500, o: 0, html: '<div class="src" style="font-size:21px">Illustration</div>' });
appear('s1_ill', b(7), { dy: 6, blur: 0 });
cue(b(16), 'riser', { dur: b(4) });
shotOut('s1', b(16) - 0.1, 'zoom', 0.22);

// S2 BFYP Today line ------------------------------------------------------
shot('s2'); shotIn('s2', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.9 }); cue(b(16) + 0.05, 'ding', { note: 88 });
headline('s2_h', ['BFYP flags what’s', '<span class="g">happening together.</span>'], { parent: 's2', y: 250, cls: 'h2', eyebrow: 'On BFYP · Today' });
wordsIn('s2_h', b(16) + 0.1, { stagger: 0.05 });
realScreen('s2_card', 'today_lines', { parent: 's2', w: 940, x: 70, y: 640 });
stamp('s2_stamp', 'today_lines', { parent: 's2', x: 70, y: 560 });
appear('s2_stamp', b(16) + 0.3, { dy: 14, blur: 0 });
scanOver('s2_card', b(16) + 0.3, 0.6);
screenCaption('s2_cap', 'today_lines');
K('s2_cap', 'o', [[b(18) - 0.001, 0, 'linear'], [b(18) + 0.2, 1, 'linear'], [b(27.8), 1, 'linear'], [b(28), 0, 'linear']]);
K('s2_h', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear']]);
K('s2_stamp', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear']]);
tour('s2_card', [
  { r: REG.today_lines.l2, key: 'OCCURRING TOGETHER', text: '4 observations · 2 kinds · 1 wallet', t0: b(18), t1: b(27.8), s: 1.08 },
], { cy: 1000, fit: 900, maxS: 1.12, callY: 330 });
shotOut('s2', b(28) - 0.12, 'zoom', 0.22);

// S3 NOT A SIGNAL ---------------------------------------------------------
shot('s3'); shotIn('s3', b(28), 'zoomIn', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 600, w: 936, o: 0, html: '<div class="h1" style="font-size:112px">Not a trade signal.<br><span class="g">A lead you can check.</span></div>' });
slam('s3_a', b(28)); cue(b(28), 'hit');
shotOut('s3', b(34) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(34), { lines: ['See what’s', '<span class="g">happening together.</span>'], sub: 'Grouped observations, each linked to its evidence.',
  visual: { asset: 'today_lines', w: 720 }, note: 'Screen from 23 Sep 2026 · live data changes' });
cue(b(34) + 0.4, 'sparkle');
cue(b(42.5), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Alone,', 'it’s <span class="m">noise.</span>', '<span class="g">Together?</span>'], hY: 400, cls: 'h1', hCss: 'font-size:130px', asset: 'today_lines', crop: [56, 200, 870, 118], visW: 940, visY: 980,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1160px">See what’s <span class="g">happening together →</span></div>' });
