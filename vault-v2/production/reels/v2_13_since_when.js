/* V2-13 — "'Whales are buying.' Since when?" — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 130 });
const b = B;
const L = i => V.lines[i];
music({ style: 'garage', bpm: 130, key: 'C', mode: 'minor', prog: ['i7', 'iv7', 'VI', 'v7'], seed: 1313, swing: 0.1,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(3) / b(1)), type: 'drop' }, { beat: Math.floor(VT(6) / b(1)), type: 'break' }, { beat: Math.floor(VT(7) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK --------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
postCard('s1_post', { parent: 's1', x: 70, y: 330, w: 940, name: 'Crypto Buzz', handle: '@example · illustration', o: 1, css: 'padding:44px 46px',
  text: '<span style="font-size:96px;line-height:1.02">🐋 Whales are <span style="color:#22d3a0">buying!</span> 🚀</span>', label: 'TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT' });
K('s1_post', 's', [[0, 0.95, 'linear'], [0.45, 1, 'outBack']]);
cue(0, 'impact', { size: 0.9 }); cue(0.05, 'notif');
mk('s1_q', { parent: 's1', x: 72, y: 880, o: 1, html: '<div class="h1" style="font-size:190px">Since<br><span class="g">when?</span></div>' });
karaoke('s1_q', VT(1), VE(1), { dy: 40 });
cue(VT(1), 'hit'); camPunch(VT(1), 0.03);
shotOut('s1', VT(2) - 0.12, 'zoom', 0.22);

// S2 NOISE --------------------------------------------------------------
shot('s2'); shotIn('s2', VT(2) - 0.1, 'zoomIn', 0.3);
mk('s2_t', { parent: 's2', x: 72, y: 600, w: 936, o: 1, html: '<div class="h1" style="font-size:118px">A number without a timeframe is just <span class="red">noise.</span></div>' });
karaoke('s2_t', VT(2), VE(2));
cue(VE(2) - 0.35, 'glitch', { dur: 0.25 });
glitchOn('s2_t', VE(2) - 0.35, 0.35, 8);
shotOut('s2', VT(3) - 0.1, 'zoom', 0.2);

// S3 BFYP: every number carries its window ---------------------------------
shot('s3'); shotIn('s3', VT(3) - 0.1, 'zoomIn', 0.4);
cue(VT(3), 'impact', { size: 0.85 }); cue(VT(3) + 0.05, 'ding', { note: 88 });
mk('s3_t', { parent: 's3', x: 72, y: 260, w: 936, o: 1, html: '<div class="eyebrow" style="margin-bottom:20px">On BFYP</div><div class="h2">Every number carries <span class="g">its window.</span></div>' });
karaoke('s3_t', VT(3), VE(3));
realScreen('s3_card', 'today_lines', { parent: 's3', w: 940, x: 70, y: 700 });
appear('s3_card', VT(3) + 0.3, { dy: 60 });
stamp('s3_stamp', 'today_lines', { parent: 's3', x: 70, y: 620 });
appear('s3_stamp', VT(3) + 0.5, { dy: 10, blur: 0 });
shotOut('s3', VT(4) - 0.06, 'cut');

// S4 WINDOWS MONTAGE ---------------------------------------------------------
const d4 = VE(4) - VT(4);
const W = [
  { a: 'today_lines', r: REG.today_lines.l1, big: '24 HOURS', k: 'TODAY', s: 1.2, t0: VT(4) - 0.06, t1: VT(4) + d4 * 0.36 },
  { a: 'sm_page', r: [40, 146, 330, 26], big: '7 DAYS', k: 'SMART MONEY', s: 2.2, t0: VT(4) + d4 * 0.36, t1: VT(4) + d4 * 0.68 },
  { a: 'sm_page', r: [40, 116, 580, 32], big: '30 DAYS', k: 'SMART MONEY', s: 1.55, t0: VT(4) + d4 * 0.68, t1: VT(5) - 0.06 },
  { a: 'whale_card', r: REG.whale_card.when, big: '2 HOURS AGO', k: 'WHALE ACTIVITY', s: 1.45, t0: VT(5) - 0.06, t1: VT(6) - 0.12 },
];
W.forEach((w, i) => {
  const sid = `w${i}`;
  shot(sid); shotIn(sid, w.t0, 'cut');
  realScreen(`${sid}_c`, w.a, { parent: sid, w: 940, x: 70, y: 700 });
  tour(`${sid}_c`, [{ r: w.r, t0: w.t0, t1: w.t1 - 0.02, s: w.s, move: 0.01 }], { cy: 1020, fit: 900, maxS: 2.4, callY: 330 });
  mk(`${sid}_big`, { parent: 'fx', x: 72, y: 250, o: 0, html: `<div class="eyebrow" style="margin-bottom:14px">${w.k}</div><div class="bigno g" style="font-size:150px;text-shadow:0 0 50px rgba(0,0,0,0.9)">${w.big}</div>` });
  K(`${sid}_big`, 'o', [[w.t0 - 0.001, 0, 'linear'], [w.t0, 1, 'linear'], [w.t1 - 0.02, 1, 'linear'], [w.t1, 0, 'linear']]);
  K(`${sid}_big`, 's', [[w.t0, 1.15, 'linear'], [w.t0 + 0.25, 1, 'outExpo']]);
  screenCaption(`${sid}_cap`, w.a);
  K(`${sid}_cap`, 'o', [[w.t0 - 0.001, 0, 'linear'], [w.t0, 1, 'linear'], [w.t1 - 0.02, 1, 'linear'], [w.t1, 0, 'linear']]);
  cue(w.t0, 'hit');
  shotOut(sid, w.t1, i === W.length - 1 ? 'zoom' : 'cut', 0.2);
});
subtitles([{ t0: VT(4), t1: VE(4), html: 'Twenty-four hours. Seven days. Thirty days.' }, { t0: VT(5), t1: VE(5), html: 'Observed, two hours ago.' }], { y: 1280, fs: 46 });

// S5 VIBE -----------------------------------------------------------------
shot('s5'); shotIn('s5', VT(6) - 0.1, 'zoomIn', 0.3);
mk('s5_t', { parent: 's5', x: 72, y: 640, w: 936, o: 1, html: '<div class="h1" style="font-size:128px">If it has no window, it’s a <span class="amber">vibe.</span></div>' });
karaoke('s5_t', VT(6), VE(6));
cue(VE(6) - 0.2, 'hit');
shotOut('s5', VT(7) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(7) - 0.1, { lines: ['Numbers with', '<span class="g">a timeframe.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'whale_card', w: 760 }, note: 'Screens from 23 Sep 2026 · AI voice' });
cue(VT(7) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['“Whales are', 'buying.”', '<span class="g">Since when?</span>'], hY: 400, cls: 'h1', hCss: 'font-size:128px', asset: 'whale_card', crop: [180, 470, 620, 100], visW: 900, visY: 1000,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1210px">No window? <span class="amber">It’s a vibe →</span></div>' });
