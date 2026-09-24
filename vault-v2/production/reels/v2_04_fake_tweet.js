/* V2-04 — "One fake tweet erased $136.5B." */
R.setup({ dur: 22.0, bpm: 172 });
const b = B;
music({ style: 'dnb', bpm: 172, key: 'A', mode: 'minor', prog: ['i', 'VII', 'VI', 'VII'], seed: 404,
  sections: [{ beat: 0, type: 'hook' }, { beat: 24, type: 'tension' }, { beat: 32, type: 'build' }, { beat: 36, type: 'drop' }, { beat: 50, type: 'cta' }],
  events: [{ type: 'stop', beat: 34, beats: 2 }, { type: 'end', beat: 62, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['One fake tweet', 'erased'], { parent: 's1', y: 250, cls: 'h1' });
hookSettle('s1_h');
mk('s1_n', { parent: 's1', x: 60, y: 520, o: 1, html: '<div class="bigno red" style="font-size:250px;text-shadow:0 0 60px rgba(255,93,93,0.35)">$136.5B</div>' });
K('s1_n', 's', [[0, 1.08, 'linear'], [0.45, 1, 'outExpo']]);
glitchOn('s1_n', 0.0, 0.35, 12);
mk('s1_t', { parent: 's1', x: 72, y: 800, o: 1, html: '<div class="h2">in a <span class="g">3-minute</span> plunge.</div><div class="src" style="font-size:24px;margin-top:28px">S&amp;P 500 value, per Reuters data · 23 Apr 2013</div>' });
cue(0, 'impact', { size: 1.0 }); cue(0.02, 'glitch', { dur: 0.35 });
camShake(0, 0.4, 16);
shotOut('s1', b(12) - 0.1, 'left', 0.28);

// S2 THE TWEET --------------------------------------------------------
shot('s2'); shotIn('s2', b(12), 'left', 0.3);
mk('s2_eb', { parent: 's2', x: 72, y: 330, o: 0, html: '<div class="h3">The tweet, from a <span class="red">hacked</span> news account:</div>' });
appear('s2_eb', b(12) + 0.05, { dy: 20 });
sourceCard('s2_card', { parent: 's2', x: 70, y: 560, w: 940, dark: true, kind: 'Hacked @AP account · fake post', date: '23 Apr 2013',
  quote: '<span style="color:#eef4f1;font-weight:750;font-size:60px;line-height:1.14">“Breaking: Two Explosions in the White House and Barack Obama is injured”</span>',
  url: 'False. Debunked within minutes.' });
popIn('s2_card', b(12.5), { from: 0.85, ease: 'outBackSoft' });
cue(b(12.5), 'notif', { notes: [81, 88] });
stampLabel('s2_fake', 'FAKE', 690, 520, { rot: -9, parent: 's2' });
stampIn('s2_fake', b(15));
shotOut('s2', b(20) - 0.1, 'up', 0.28);

// S3 MARKET REACTION --------------------------------------------------
shot('s3'); shotIn('s3', b(20), 'up', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 560, o: 0, html: '<div class="h1" style="font-size:150px">Dow <span class="red">↓ ~140</span></div><div class="h3 m" style="margin-top:10px">points, within minutes</div>' });
slam('s3_a', b(20)); cue(b(20), 'subdrop'); cue(b(20), 'hit');
mk('s3_b', { parent: 's3', x: 72, y: 930, o: 0, html: '<div class="h2">Then it <span class="g">bounced back.</span></div>' });
appear('s3_b', b(23), { dy: 40 });
cue(b(23), 'whoosh', { dur: 0.35, up: true });
mk('s3_src', { parent: 's3', x: 76, y: 1150, o: 0, html: '<div class="src" style="font-size:22px">Sources: CNBC · Reuters data · 23–24 Apr 2013</div>' });
appear('s3_src', b(23.5), { dy: 10, blur: 0 });
shotOut('s3', b(28) - 0.1, 'zoom', 0.25);

// S4 WHY IT HURTS -----------------------------------------------------
shot('s4'); shotIn('s4', b(28), 'zoomIn', 0.3);
mk('s4_a', { parent: 's4', x: 72, y: 640, o: 0, html: '<div class="h1" style="font-size:120px">Markets react<br><span class="red">first.</span></div>' });
slam('s4_a', b(28)); cue(b(28), 'hit');
mk('s4_b', { parent: 's4', x: 72, y: 960, o: 0, html: '<div class="h1" style="font-size:120px">Verification<br>comes <span class="g">later.</span></div>' });
slam('s4_b', b(30)); cue(b(30), 'hit');
cue(b(36), 'riser', { dur: b(4) });
shotOut('s4', b(36) - 0.1, 'zoom', 0.2);

// S5 BFYP -------------------------------------------------------------
shot('s5'); shotIn('s5', b(36), 'zoomIn', 0.4);
cue(b(36), 'impact', { size: 0.9 }); cue(b(36) + 0.05, 'ding', { note: 88 });
headline('s5_h', ['What was', '<span class="g">actually observed.</span>'], { parent: 's5', y: 250, cls: 'h2', eyebrow: 'On BFYP · Today' });
wordsIn('s5_h', b(36) + 0.1, { stagger: 0.04 });
realScreen('s5_card', 'today_lines', { parent: 's5', w: 940, x: 70, y: 640 });
stamp('s5_stamp', 'today_lines', { parent: 's5', x: 70, y: 560 });
appear('s5_stamp', b(36) + 0.3, { dy: 14, blur: 0 });
scanOver('s5_card', b(36) + 0.3, 0.6);
screenCaption('s5_cap', 'today_lines');
K('s5_cap', 'o', [[b(38) - 0.001, 0, 'linear'], [b(38) + 0.2, 1, 'linear'], [b(42.2), 1, 'linear'], [b(42.4), 0, 'linear']]);
K('s5_h', 'o', [[b(38), 1, 'linear'], [b(38) + 0.2, 0, 'linear']]);
K('s5_stamp', 'o', [[b(38), 1, 'linear'], [b(38) + 0.2, 0, 'linear']]);
tour('s5_card', [
  { r: REG.today_lines.l1, key: 'COUNTED', text: '330 observations · 10 assets · 24h', t0: b(38), t1: b(42.2) },
], { cy: 1000, fit: 900, maxS: 1.35, callY: 330, endT: b(42.2) });
K('s5_card', 'o', [[b(42.2), 1, 'linear'], [b(42.6), 0, 'linear']]);
mk('s5_q', { parent: 's5', x: 72, y: 700, w: 936, o: 0, html: '<div class="h1" style="font-size:88px;line-height:1.0;text-shadow:0 10px 50px rgba(0,0,0,0.9)">“Observed activity,<br>as counted by BFYP.<br><span class="g">Nothing here is<br>a prediction.”</span></div>' });
slam('s5_q', b(42.4)); cue(b(42.4), 'hit');
mk('s5_qs', { parent: 's5', x: 72, y: 1120, o: 0, html: `<div class="capline"><b>●</b> Verbatim · BFYP Today · 23 Sep 2026 · 22:14 UTC</div>` });
appear('s5_qs', b(43), { dy: 10, blur: 0 });
shotOut('s5', b(50) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(50), { lines: ['Check what', '<span class="g">actually happened.</span>'], sub: 'Before you react.',
  visual: { asset: 'today_lines', w: 800 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(50) + 0.4, 'sparkle');
cue(b(62), 'hit');

R.coverSetup = () => coverDesign({ lines: ['One fake tweet', 'erased'], hY: 400, cls: 'h1',
  extra: `<div class="bigno red" style="position:absolute;left:60px;top:640px;font-size:250px;text-shadow:0 0 60px rgba(255,93,93,0.35)">$136.5B</div>
  <div class="h2" style="position:absolute;left:72px;top:920px">in a <span class="g">3-minute</span> plunge.</div>
  <div class="src" style="position:absolute;left:76px;top:1060px;font-size:24px">S&amp;P 500 value · per Reuters data · 23 Apr 2013</div>
  <div class="h4" style="position:absolute;left:76px;top:1330px">Check what <span class="g">actually happened →</span></div>` });
