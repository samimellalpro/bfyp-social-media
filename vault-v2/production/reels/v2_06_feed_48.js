/* V2-06 — "48% learn investing on social media." */
R.setup({ dur: 20.4, bpm: 150 });
const b = B;
music({ style: 'futurebass', bpm: 150, key: 'D', mode: 'major', prog: ['IV', 'V', 'vi', 'I'], seed: 606,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'drop' }, { beat: 16, type: 'tension' }, { beat: 27, type: 'build' }, { beat: 29, type: 'drop' }, { beat: 40, type: 'cta' }],
  events: [{ type: 'stop', beat: 28, beats: 1 }, { type: 'end', beat: 50, tail: 0.35 }] });
progressBar(); bgLife();

// feed skeleton background (abstract, no content)
function feedBg(parent, t0, t1) {
  let html = '';
  for (let i = 0; i < 9; i++) {
    html += `<div style="position:absolute;left:0;top:${i * 330}px;width:820px;height:290px;border-radius:28px;background:#0f1614;border:2px solid #1b2724">
      <div style="position:absolute;left:30px;top:30px;width:64px;height:64px;border-radius:50%;background:#1d2a26"></div>
      <div style="position:absolute;left:112px;top:40px;width:240px;height:20px;border-radius:10px;background:#1d2a26"></div>
      <div style="position:absolute;left:112px;top:72px;width:160px;height:16px;border-radius:8px;background:#18231f"></div>
      <div style="position:absolute;left:30px;top:130px;width:${560 + (i % 3) * 70}px;height:24px;border-radius:12px;background:#1a2622"></div>
      <div style="position:absolute;left:30px;top:170px;width:${440 + (i % 2) * 120}px;height:24px;border-radius:12px;background:#1a2622"></div>
      <div style="position:absolute;left:30px;top:226px;width:90px;height:22px;border-radius:11px;background:#1b3a30"></div></div>`;
  }
  mk('feed', { parent, x: 130, y: 0, o: 0.35, html });
  K('feed', 'y', [[t0, 200, 'linear'], [t1, -1500, 'linear']]);
}

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
feedBg('s1', 0, b(16));
mk('s1_n', { parent: 's1', x: 50, y: 300, o: 1, html: '<div class="bigno g" style="font-size:380px;text-shadow:0 0 80px rgba(23,181,138,0.45)">48%</div>' });
K('s1_n', 's', [[0, 1.08, 'linear'], [0.5, 1, 'outExpo']]);
mk('s1_t', { parent: 's1', x: 72, y: 700, w: 940, o: 1, html: '<div class="h1" style="font-size:100px">of Gen Z investors<br>learn investing on<br><span class="g">social media.</span></div>' });
mk('s1_src', { parent: 's1', x: 76, y: 1080, o: 1, html: '<div class="src" style="font-size:24px">FINRA Foundation &amp; CFA Institute<br>Gen Z and Investing · 2023</div>' });
cue(0, 'impact', { size: 1.0 });
shotOut('s1', b(8) - 0.1, 'left', 0.3);

// S2 CONTEXT BARS -----------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'left', 0.35);
mk('s2_h', { parent: 's2', x: 72, y: 330, o: 0, html: '<div class="h2">Where they learn:</div>' });
appear('s2_h', b(8) + 0.05, { dy: 20 });
barChart('s2_bars', [
  { label: 'Social media', v: 48, val: '48%', hl: true },
  { label: 'Internet searches', v: 47, val: '47%' },
  { label: 'Parents / family', v: 45, val: '45%' },
], { parent: 's2', x: 72, y: 600, w: 936, rowH: 210, barH: 96, labelW: 0, valW: 170, max: 52, t0: b(8.6), stagger: 0.25, fs: 50, vfs: 60, labelAbove: true });
mk('s2_src', { parent: 's2', x: 76, y: 1240, o: 0, html: '<div class="src" style="font-size:22px">U.S. Gen Z investors<br>FINRA Foundation &amp; CFA Institute (2023)</div>' });
appear('s2_src', b(10), { dy: 10, blur: 0 });
shotOut('s2', b(16) - 0.1, 'up', 0.3);

// S3 WHY IT HURTS -----------------------------------------------------
shot('s3'); shotIn('s3', b(16), 'up', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 560, o: 0, html: '<div class="h1" style="font-size:118px">Feeds reward<br>what’s <span class="g">engaging.</span></div>' });
slam('s3_a', b(16)); cue(b(16), 'hit');
mk('s3_b', { parent: 's3', x: 72, y: 890, o: 0, html: '<div class="h1" style="font-size:118px">Not what’s<br><span class="red">verified.</span></div>' });
slam('s3_b', b(18.5)); cue(b(18.5), 'hit');
shotOut('s3', b(22) - 0.1, 'zoom', 0.25);

shot('s3b'); shotIn('s3b', b(22), 'zoomIn', 0.3);
mk('s3b_a', { parent: 's3b', x: 72, y: 600, o: 0, html: '<div class="h2 m">So ask one thing:</div>' });
appear('s3b_a', b(22), { dy: 30 });
mk('s3b_b', { parent: 's3b', x: 72, y: 730, o: 0, html: '<div class="h1" style="font-size:128px">What is this<br><span class="g">built on?</span></div>' });
slam('s3b_b', b(24)); cue(b(24), 'hit');
cue(b(29), 'riser', { dur: b(4) });
shotOut('s3b', b(29) - 0.1, 'zoom', 0.2);

// S4 BFYP: every claim shows what it's built on (triptych of real screens) -----------
shot('s4'); shotIn('s4', b(29), 'zoomIn', 0.4);
cue(b(29), 'impact', { size: 0.9 }); cue(b(29) + 0.05, 'ding', { note: 90 });
headline('s4_h', ['On BFYP, you see', '<span class="g">what it’s built on.</span>'], { parent: 's4', y: 250, cls: 'h2', css: 'font-size:84px' });
wordsIn('s4_h', b(29) + 0.1, { stagger: 0.04 });
const TRI = [
  { a: 'today_lines', r: REG.today_lines.l1, y: 500, h: 190, k: 'TODAY · BUILT ON', v: '330 observations', t: 30.5 },
  { a: 'whale_card', r: [186, 392, 600, 170], y: 740, h: 240, k: 'WHALES · BUILT ON', v: 'the raw transaction', t: 33 },
  { a: 'nvda_fund', r: [24, 85, 734, 245], y: 1030, h: 320, k: 'STOCKS · BUILT ON', v: 'the 10-K on SEC EDGAR', t: 35.5, fill: 1.0 },
];
TRI.forEach((p, i) => {
  const id = `s4_p${i}`;
  paneCrop(id, p.a, p.r, 60, p.y, 960, p.h, { parent: 's4', fill: p.fill || 0.94, o: 0 });
  appear(id, b(p.t), { dy: 50 });
  mk(`${id}_k`, { parent: 's4', x: 84, y: p.y - 26, o: 0, html: `<div class="pill" style="font-size:22px;padding:8px 16px;background:#0a110f"><span class="dot"></span>${p.k} <span style="color:#22d3a0;margin-left:6px">${p.v}</span></div>` });
  appear(`${id}_k`, b(p.t) + 0.12, { dy: 10, blur: 0 });
  cue(b(p.t), 'whoosh', { dur: 0.3 }); cue(b(p.t) + 0.12, 'click');
});
K('s4_h', 'o', [[b(30.3), 1, 'linear'], [b(30.5), 0.35, 'linear']]);
mk('s4_cap', { parent: 'fx', x: 72, y: 1400, o: 0, html: '<div class="capline"><b>●</b> Real BFYP screens · 23 Sep 2026 · 21:28–22:01 UTC</div>' });
K('s4_cap', 'o', [[b(30.5), 0, 'linear'], [b(30.7), 1, 'linear'], [b(39.8), 1, 'linear'], [b(40), 0, 'linear']]);
shotOut('s4', b(40) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(40), { lines: ['Learn from', '<span class="g">evidence.</span>'], sub: 'Not from the loudest post.',
  visual: { asset: 'today_lines', w: 800 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(40) + 0.4, 'sparkle');
cue(b(50), 'hit');

R.coverSetup = () => coverDesign({ lines: [''], hY: 380, cls: 'h1',
  extra: `<div class="bigno g" style="position:absolute;left:50px;top:360px;font-size:380px;text-shadow:0 0 80px rgba(23,181,138,0.45)">48%</div>
  <div class="h1" style="position:absolute;left:72px;top:760px;font-size:100px">of Gen Z investors<br>learn investing on<br><span class="g">social media.</span></div>
  <div class="src" style="position:absolute;left:76px;top:1140px;font-size:24px">FINRA Foundation &amp; CFA Institute · 2023</div>
  <div class="h4" style="position:absolute;left:76px;top:1330px">Ask what it's <span class="g">built on →</span></div>` });
