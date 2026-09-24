/* V2-25 — "The data pointed both ways." */
R.setup({ dur: 20.4, bpm: 118 });
const b = B;
music({ style: 'minimal', bpm: 118, key: 'B', mode: 'minor', prog: ['i', 'VI', 'iv', 'VII'], seed: 2525,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 15, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 32, type: 'cta' }],
  events: [{ type: 'stop', beat: 15, beats: 1 }, { type: 'end', beat: 40, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK: split arrows ------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_up', { parent: 's1', x: 0, y: 0, w: 540, h: 1920, o: 1, html: '<div style="width:540px;height:1920px;background:linear-gradient(180deg,rgba(23,181,138,0.20),rgba(23,181,138,0.02))"></div>' });
mk('s1_dn', { parent: 's1', x: 540, y: 0, w: 540, h: 1920, o: 1, html: '<div style="width:540px;height:1920px;background:linear-gradient(0deg,rgba(255,93,93,0.18),rgba(255,93,93,0.02))"></div>' });
mk('s1_au', { parent: 's1', x: 150, y: 420, o: 1, origin: '50% 50%', html: '<div class="bigno g" style="font-size:420px;text-shadow:0 0 80px rgba(23,181,138,0.5)">↑</div>' });
mk('s1_ad', { parent: 's1', x: 690, y: 420, o: 1, origin: '50% 50%', html: '<div class="bigno red" style="font-size:420px;text-shadow:0 0 80px rgba(255,93,93,0.45)">↓</div>' });
K('s1_up', 'y', [[0, -300, 'linear'], [0.5, 0, 'outExpo']]);
K('s1_dn', 'y', [[0, 300, 'linear'], [0.5, 0, 'outExpo']]);
K('s1_au', 'y', [[0, 520, 'linear'], [0.5, 420, 'outBack']]);
K('s1_ad', 'y', [[0, 320, 'linear'], [0.5, 420, 'outBack']]);
mk('s1_t', { parent: 's1', x: 72, y: 920, w: 936, o: 1, html: '<div class="h1" style="font-size:112px">On USDC, the data<br>pointed <span class="g">both</span> <span class="red">ways.</span></div>' });
K('s1_t', 's', [[0, 1.05, 'linear'], [0.5, 1, 'outExpo']]);
cue(0, 'impact', { size: 1.0 }); cue(0.05, 'whoosh', { dur: 0.35 });
shotOut('s1', b(8) - 0.1, 'zoom', 0.25);

// S2 WHY IT MATTERS ----------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'zoomIn', 0.3);
mk('s2_a', { parent: 's2', x: 72, y: 600, w: 936, o: 0, html: '<div class="h1" style="font-size:112px">A feed that always<br>picks a side is<br><span class="amber">telling you a story.</span></div>' });
slam('s2_a', b(8)); cue(b(8), 'hit');
cue(b(16), 'riser', { dur: b(3) });
shotOut('s2', b(16) - 0.1, 'zoom', 0.2);

// S3 BFYP Today line ------------------------------------------------------
shot('s3'); shotIn('s3', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.85 }); cue(b(16) + 0.05, 'ding', { note: 86 });
headline('s3_h', ['BFYP says it', '<span class="g">plainly.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · Today' });
wordsIn('s3_h', b(16) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'today_lines', { parent: 's3', w: 940, x: 70, y: 640 });
stamp('s3_stamp', 'today_lines', { parent: 's3', x: 70, y: 560 });
appear('s3_stamp', b(16) + 0.3, { dy: 14, blur: 0 });
scanOver('s3_card', b(16) + 0.3, 0.6);
screenCaption('s3_cap', 'today_lines');
K('s3_cap', 'o', [[b(18) - 0.001, 0, 'linear'], [b(18) + 0.2, 1, 'linear'], [b(31.8), 1, 'linear'], [b(32), 0, 'linear']]);
K('s3_h', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(18), 1, 'linear'], [b(18) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: REG.today_lines.l3, key: 'MIXED, SAID PLAINLY', text: 'Both directions · from one group', t0: b(18), t1: b(25), s: 1.08 },
  { r: REG.today_lines.l4, key: 'NO SPIN', text: 'Computed from observations, not a model', t0: b(25), t1: b(31.8), s: 1.08 },
], { cy: 1000, fit: 900, maxS: 1.15, callY: 330 });
shotOut('s3', b(32) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(32), { lines: ['Mixed is', '<span class="g">information too.</span>'], sub: 'See both sides on the Today page.',
  visual: { asset: 'today_lines', w: 720 }, note: 'Screen from 23 Sep 2026 · live data changes' });
cue(b(32) + 0.4, 'sparkle');
cue(b(40), 'hit');

R.coverSetup = () => coverDesign({ lines: ['The data pointed', '<span class="g">both</span> <span class="red">ways.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:120px', asset: 'today_lines', crop: [56, 342, 878, 110], visW: 940, visY: 900,
  extra: '<div class="bigno g" style="position:absolute;left:260px;top:1080px;font-size:260px">↑</div><div class="bigno red" style="position:absolute;left:620px;top:1080px;font-size:260px">↓</div>' });
