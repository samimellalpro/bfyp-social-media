/* V2-21 — "Biggest wallet ≠ smartest wallet." */
R.setup({ dur: 20.0, bpm: 174 });
const b = B;
music({ style: 'dnb', bpm: 174, key: 'F', mode: 'minor', prog: ['i', 'VI', 'VII', 'v'], seed: 2121,
  sections: [{ beat: 0, type: 'hook' }, { beat: 14, type: 'tension' }, { beat: 25, type: 'build' }, { beat: 26, type: 'drop' }, { beat: 47, type: 'cta' }],
  events: [{ type: 'stop', beat: 25, beats: 1 }, { type: 'end', beat: 57.5, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK: big bubble vs small bubble -------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['The biggest wallet', 'isn’t the <span class="g">smartest</span> one.'], { parent: 's1', y: 230, cls: 'h1', css: 'font-size:100px' });
hookSettle('s1_h');
mk('s1_big', { parent: 's1', x: 90, y: 620, w: 560, h: 560, o: 1, origin: '50% 50%', html: `<div style="width:560px;height:560px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#3c4d8a,#1b2340 70%);box-shadow:0 0 120px rgba(80,110,220,0.35);display:flex;align-items:center;justify-content:center;flex-direction:column">
  <div class="mono" style="font-size:30px;letter-spacing:.2em;color:#c9d3ff">BIGGEST</div><div style="font-weight:800;font-size:70px;color:#fff">$$$$$</div></div>` });
mk('s1_sm', { parent: 's1', x: 720, y: 900, w: 240, h: 240, o: 1, origin: '50% 50%', html: `<div style="width:240px;height:240px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#22d3a0,#0f8f6c 70%);box-shadow:0 0 80px rgba(34,211,160,0.55);display:flex;align-items:center;justify-content:center;flex-direction:column">
  <div class="mono" style="font-size:22px;letter-spacing:.14em;color:#03140e;font-weight:700">SMARTEST?</div></div>` });
mk('s1_ne', { parent: 's1', x: 640, y: 760, o: 1, html: '<div class="bigno" style="font-size:150px;color:#eef4f1">≠</div>' });
K('s1_big', 's', [[0, 0.8, 'linear'], [0.5, 1, 'outBack']]);
K('s1_sm', 's', [[0.2, 0.3, 'linear'], [0.7, 1, 'outBack']]);
hook(t => { const k = 1 + 0.03 * Math.sin(t * 5.4); $('s1_sm').style.transform += ` scale(${k.toFixed(3)})`; });
cue(0, 'impact', { size: 1.0 }); cue(0.2, 'pop');
mk('s1_n', { parent: 's1', x: 76, y: 1400, o: 0, html: '<div class="src" style="font-size:22px">Illustration</div>' });
appear('s1_n', b(2), { dy: 10, blur: 0 });
mk('s1_l1', { parent: 's1', x: 190, y: 1210, o: 0, html: '<div class="pill" style="font-size:26px;border-color:#6d7fd0"><span class="dot" style="background:#8fa0ff;box-shadow:0 0 12px #8fa0ff"></span>SIZE · OBVIOUS</div>' });
mk('s1_l2', { parent: 's1', x: 640, y: 1170, o: 0, html: '<div class="pill" style="font-size:26px"><span class="dot"></span>SKILL · ?</div>' });
popIn('s1_l1', b(4), { from: 0.6 }); cue(b(4), 'pop'); camPunch(b(4), 0.02);
popIn('s1_l2', b(7), { from: 0.6 }); cue(b(7), 'pop'); camPunch(b(7), 0.02);
K('s1_big', 'bright', [[b(10), 1, 'linear'], [b(10.5), 0.55, 'outCubic']]);
K('s1_sm', 's', [[b(10), 1, 'linear'], [b(10.4), 1.25, 'outBack']]);
cue(b(10), 'ding', { note: 86 });
shotOut('s1', b(14) - 0.1, 'left', 0.28);

// S2 SIZE vs SKILL --------------------------------------------------------
shot('s2'); shotIn('s2', b(14), 'left', 0.3);
mk('s2_a', { parent: 's2', x: 72, y: 600, w: 936, o: 0, html: '<div class="h1" style="font-size:124px">Size is easy<br>to <span class="g">see.</span></div>' });
slam('s2_a', b(14)); cue(b(14), 'hit');
mk('s2_b', { parent: 's2', x: 72, y: 930, w: 936, o: 0, html: '<div class="h1" style="font-size:124px">Skill <span class="red">isn’t.</span></div>' });
slam('s2_b', b(18)); cue(b(18), 'hit');
cue(b(26), 'riser', { dur: b(5) });
shotOut('s2', b(26) - 0.1, 'zoom', 0.2);

// S3 BFYP ---------------------------------------------------------------
shot('s3'); shotIn('s3', b(26), 'zoomIn', 0.4);
cue(b(26), 'impact', { size: 0.9 }); cue(b(26) + 0.05, 'ding', { note: 89 });
headline('s3_h', ['Ranked on', '<span class="g">behavior.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · Smart Money' });
wordsIn('s3_h', b(26) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'sm_rows_12', { parent: 's3', w: 900, x: 90, y: 640 });
stamp('s3_stamp', 'sm_rows_12', { parent: 's3', x: 90, y: 560 });
appear('s3_stamp', b(26) + 0.3, { dy: 14, blur: 0 });
scanOver('s3_card', b(26) + 0.3, 0.6);
screenCaption('s3_cap', 'sm_rows_12');
K('s3_cap', 'o', [[b(29) - 0.001, 0, 'linear'], [b(29) + 0.2, 1, 'linear'], [b(46.8), 1, 'linear'], [b(47), 0, 'linear']]);
K('s3_h', 'o', [[b(29), 1, 'linear'], [b(29) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(29), 1, 'linear'], [b(29) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: REG.sm_rows_12.desc1, key: 'THE RULE', text: 'Never from size alone', t0: b(29), t1: b(38), s: 1.25 },
  { r: [44, 244, 720, 128], key: 'EACH WALLET', text: 'Category · score · confidence', t0: b(38), t1: b(46.8), s: 1.3 },
], { cy: 1000, fit: 860, maxS: 1.4, callY: 330 });
shotOut('s3', b(47) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(47), { lines: ['Ranked on what', '<span class="g">they did.</span>'], sub: 'The Smart Money leaderboard is on the free plan.',
  visual: { asset: 'sm_rows_12', w: 700 }, note: 'Screen from 23 Sep 2026 · live data changes' });
cue(b(47) + 0.4, 'sparkle');
cue(b(57.5), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Biggest wallet', '<span class="red">≠</span> smartest', 'wallet.'], hY: 400, cls: 'h1', hCss: 'font-size:124px', asset: 'sm_rows_12', crop: [6, 40, 790, 90], visW: 940, visY: 900,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1080px">Ranked on <span class="g">behavior →</span></div>' });
