/* V2-22 — "That 'whale' might be a market maker." */
R.setup({ dur: 20.4, bpm: 112 });
const b = B;
music({ style: 'amapiano', bpm: 112, key: 'A', mode: 'minor', prog: ['i7', 'iv7', 'VI', 'v'], seed: 2222,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 15, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 30, type: 'cta' }],
  events: [{ type: 'stop', beat: 15, beats: 1 }, { type: 'end', beat: 37.5, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_a', { parent: 's1', x: 72, y: 330, w: 936, o: 1, html: '<div class="h1" style="font-size:150px">That<br>“whale”?</div>' });
K('s1_a', 's', [[0, 1.08, 'linear'], [0.5, 1, 'outExpo']]);
cue(0, 'impact', { size: 1.0 });
mk('s1_b', { parent: 's1', x: 72, y: 780, w: 936, o: 0, html: '<div class="h1" style="font-size:118px">Might be a<br><span class="amber">market maker.</span></div>' });
slam('s1_b', b(3)); cue(b(3), 'hit'); camPunch(b(3), 0.03);
// flow arrows (two-way traffic), abstract
mk('s1_flow', { parent: 's1', x: 72, y: 1160, w: 936, o: 0, html: `<div class="mono" style="font-size:44px;letter-spacing:.1em;color:#5f6d69;white-space:nowrap">⇄ ⇄ ⇄ ⇄ ⇄ ⇄ ⇄ ⇄ ⇄ ⇄</div>` });
appear('s1_flow', b(4), { dy: 10, blur: 0 });
K('s1_flow', 'x', [[b(4), 72, 'linear'], [b(8), -60, 'linear']]);
shotOut('s1', b(8) - 0.1, 'left', 0.3);

// S2 WHY IT MATTERS ----------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'left', 0.35);
mk('s2_a', { parent: 's2', x: 72, y: 560, w: 936, o: 0, html: '<div class="h1" style="font-size:110px">Market makers move size <span class="g">all day.</span></div>' });
slam('s2_a', b(8)); cue(b(8), 'hit');
mk('s2_b', { parent: 's2', x: 72, y: 900, w: 936, o: 0, html: '<div class="h1" style="font-size:110px">It’s their job —<br><span class="m">not a conviction bet.</span></div>' });
slam('s2_b', b(11)); cue(b(11), 'hit');
cue(b(16), 'riser', { dur: b(3) });
shotOut('s2', b(16) - 0.1, 'zoom', 0.2);

// S3 BFYP labels -------------------------------------------------------
shot('s3'); shotIn('s3', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.9 }); cue(b(16) + 0.05, 'ding', { note: 86 });
headline('s3_h', ['Labelled by', '<span class="g">what they do.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · Smart Money leaderboard' });
wordsIn('s3_h', b(16) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'sm_rows_678', { parent: 's3', w: 880, x: 100, y: 640 });
stamp('s3_stamp', 'sm_rows_678', { parent: 's3', x: 100, y: 560 });
appear('s3_stamp', b(16) + 0.3, { dy: 14, blur: 0 });
scanOver('s3_card', b(16) + 0.3, 0.6);
screenCaption('s3_cap', 'sm_rows_678');
K('s3_cap', 'o', [[b(18) - 0.001, 0, 'linear'], [b(18) + 0.2, 1, 'linear'], [b(29.8), 1, 'linear'], [b(30), 0, 'linear']]);
K('s3_h', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear'], [b(26), 0, 'linear'], [b(26.3), 1, 'linear']]);
K('s3_stamp', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear'], [b(26), 0, 'linear'], [b(26.3), 1, 'linear']]);
tour('s3_card', [
  { r: REG.sm_rows_678.row6, key: 'WALLET #6', text: 'Market maker', t0: b(18), t1: b(22), s: 1.12 },
  { r: REG.sm_rows_678.row8, key: 'WALLET #8', text: 'Whale accumulator', t0: b(22), t1: b(25.8), s: 1.12 },
], { cy: 1000, fit: 900, maxS: 1.2, callY: 330 });
mk('s3_sum', { parent: 's3', x: 72, y: 1300, w: 936, o: 0, html: '<div class="h3">Same leaderboard.<br><span class="g">Different behavior.</span></div>' });
appear('s3_sum', b(26.2), { dy: 30 }); cue(b(26.2), 'hit');
shotOut('s3', b(30) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(30), { lines: ['Know who you’re', '<span class="g">watching.</span>'], sub: 'Every wallet with a behavior label, a score and a confidence badge.',
  visual: { asset: 'sm_rows_678', w: 680 }, note: 'Screen from 23 Sep 2026 · live data changes' });
cue(b(30) + 0.4, 'sparkle');
cue(b(37.5), 'hit');

R.coverSetup = () => coverDesign({ lines: ['That “whale”', 'might be a', '<span class="amber">market maker.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:118px', asset: 'sm_rows_678', crop: [6, 6, 860, 193], visW: 920, visY: 900,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1180px">Know who you’re <span class="g">watching →</span></div>' });
