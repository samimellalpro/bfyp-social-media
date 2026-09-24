/* V2-24 — "3 wins. Genius or luck?" — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 134 });
const b = B;
music({ style: 'garage', bpm: 134, key: 'A', mode: 'minor', prog: ['i7', 'VI', 'iv7', 'v'], seed: 2424, swing: 0.1,
  sections: [{ beat: 0, type: 'hook' }, { beat: Math.floor(VT(2) / b(1)), type: 'tension' }, { beat: Math.floor(VT(4) / b(1)), type: 'drop' }, { beat: Math.floor(VT(5) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK: W W W ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
[0, 1, 2].forEach(i => {
  mk(`s1_w${i}`, { parent: 's1', x: 90 + i * 310, y: 330, w: 280, h: 320, o: 0, origin: '50% 50%', html: `<div style="width:280px;height:320px;border-radius:30px;background:rgba(23,181,138,0.16);border:4px solid #22d3a0;box-shadow:0 0 40px rgba(34,211,160,0.4);display:flex;align-items:center;justify-content:center"><div class="bigno g" style="font-size:200px">W</div></div>` });
  const t = 0.05 + i * 0.32;
  K(`s1_w${i}`, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
  K(`s1_w${i}`, 'sx', [[t, 0.05, 'linear'], [t + 0.28, 1, 'outBack']]);
  cue(t, 'pop'); cue(t, 'tick');
});
mk('s1_t', { parent: 's1', x: 72, y: 720, w: 936, o: 1, html: '<div class="h1" style="font-size:120px">Three wins<br>in a row.</div>' });
karaoke('s1_t', VT(0), VE(0), { dimStart: true });
cue(0, 'impact', { size: 0.8 });
mk('s1_q', { parent: 's1', x: 72, y: 1060, w: 936, o: 1, html: '<div class="h1" style="font-size:130px"><span class="g">Genius,</span> or <span class="amber">luck?</span></div>' });
karaoke('s1_q', VT(1), VE(1));
// coin flip
mk('s1_coin', { parent: 's1', x: 450, y: 1260, w: 180, h: 180, o: 0, origin: '50% 50%', html: '<div style="width:180px;height:180px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe29a,#c8922e 70%);box-shadow:0 0 40px rgba(240,180,74,0.5)"></div>' });
K('s1_coin', 'o', [[VE(1) - 0.2, 0, 'linear'], [VE(1), 1, 'linear'], [VT(2) - 0.15, 1, 'linear'], [VT(2), 0, 'linear']]);
hook(t => { if (t > VE(1) - 0.2 && t < VT(2)) { const k = Math.cos((t - VE(1)) * 26); $('s1_coin').style.transform += ` scaleX(${k.toFixed(3)})`; } });
cue(VE(1) - 0.1, 'swish');
shotOut('s1', VT(2) - 0.12, 'zoom', 0.22);

// S2 CAN'T TELL ------------------------------------------------------------
shot('s2'); shotIn('s2', VT(2) - 0.1, 'zoomIn', 0.3);
mk('s2_t', { parent: 's2', x: 72, y: 560, w: 936, o: 1, html: '<div class="h1" style="font-size:112px">Honestly? A short track record <span class="red">can’t tell you.</span></div>' });
karaoke('s2_t', VT(2), VE(2));
shotOut('s2', VT(3) - 0.12, 'left', 0.28);

// S3 SAMPLE vs STYLE ---------------------------------------------------------
shot('s3'); shotIn('s3', VT(3) - 0.1, 'left', 0.3);
mk('s3_t', { parent: 's3', x: 72, y: 560, w: 936, o: 1, html: '<div class="h1" style="font-size:112px">Three good calls is a <span class="amber">sample,</span> not a <span class="g">style.</span></div>' });
karaoke('s3_t', VT(3), VE(3));
cue(VE(3) - 0.3, 'hit');
shotOut('s3', VT(4) - 0.12, 'zoom', 0.22);

// S4 BFYP -------------------------------------------------------------------
shot('s4'); shotIn('s4', VT(4) - 0.1, 'zoomIn', 0.4);
cue(VT(4), 'impact', { size: 0.85 }); cue(VT(4) + 0.05, 'ding', { note: 88 });
realScreen('s4_card', 'sm_rows_12', { parent: 's4', w: 900, x: 90, y: 660 });
stamp('s4_stamp', 'sm_rows_12', { parent: 's4', x: 90, y: 580, o: 1 });
tour('s4_card', [{ r: REG.sm_rows_12.desc2, key: 'ON BFYP · SMART MONEY', text: 'Thin history reads “Unproven”', t0: VT(4) + 0.2, t1: VT(5) - 0.15, s: 1.45, move: 0.35 }], { cy: 1000, fit: 900, maxS: 1.5, callY: 330 });
K('s4_stamp', 'o', [[VT(4) + 0.2, 1, 'linear'], [VT(4) + 0.4, 0, 'linear']]);
screenCaption('s4_cap', 'sm_rows_12');
K('s4_cap', 'o', [[VT(4) + 0.3, 0, 'linear'], [VT(4) + 0.5, 1, 'linear'], [VT(5) - 0.2, 1, 'linear'], [VT(5), 0, 'linear']]);
subtitles([{ t0: VT(4), t1: VE(4), html: 'On BFYP, thin history reads <span class="g">unproven.</span>' }], { y: 1290, fs: 48 });
shotOut('s4', VT(5) - 0.15, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(5) - 0.1, { lines: ['Scores that admit', '<span class="g">what they don’t know.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'sm_rows_12', w: 700 }, note: 'Screen from 23 Sep 2026 · AI voice' });
cue(VT(5) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['3 wins in a row.', '<span class="g">Genius</span> or', '<span class="amber">luck?</span>'], hY: 400, cls: 'h1', hCss: 'font-size:128px',
  extra: `<div style="position:absolute;left:90px;top:900px;display:flex;gap:30px">${[0, 1, 2].map(() => '<div style="width:280px;height:300px;border-radius:30px;background:rgba(23,181,138,0.16);border:4px solid #22d3a0;display:flex;align-items:center;justify-content:center"><div class="bigno g" style="font-size:190px">W</div></div>').join('')}</div>
  <div class="h4" style="position:absolute;left:76px;top:1270px">A short record <span class="red">can’t tell you →</span></div>` });
