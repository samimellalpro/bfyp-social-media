/* V2-27 — "If it can't be proven wrong, it's a vibe." — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 92 });
const b = B;
music({ style: 'cinematic', bpm: 92, key: 'E', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 2727,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(4) / b(1)), type: 'build' }, { beat: Math.floor(VT(5) / b(1)), type: 'drop' }, { beat: Math.floor(VT(6) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 MANIFESTO --------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 520, w: 936, o: 1, html: '<div class="h1" style="font-size:124px">If it can’t be proven wrong, it’s just a <span class="amber">vibe.</span></div>' });
karaoke('s1_t', VT(0), VE(0), { dimStart: true });
cue(0, 'impact', { size: 0.9 });
shotOut('s1', VT(1) - 0.12, 'zoom', 0.22);

// S2 THE VIBES (struck through) ------------------------------------------------
shot('s2'); shotIn('s2', VT(1) - 0.1, 'zoomIn', 0.3);
const QUOTES = ['“It’ll pump eventually.”', '“Smart money knows.”', '“Trust me.”'];
QUOTES.forEach((q, i) => {
  const id = `s2_q${i}`, y = 380 + i * 330;
  mk(id, { parent: 's2', x: 72, y, w: 936, o: 0, html: `<div class="h1" style="font-size:100px;color:#dfe7e3">${strikeSpan(q)}</div>` });
  const t = VT(1 + i) - 0.08;
  K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
  K(id, 'x', [[t, 110, 'linear'], [t + 0.3, 72, 'outExpo']]);
  cue(t, 'pop');
  strikeIn(id, VE(1 + i) + 0.05);
  K(id, 'o', [[VE(1 + i) + 0.05, 1, 'linear'], [VE(1 + i) + 0.3, 0.5, 'linear']]);
});
mk('s2_ill', { parent: 's2', x: 76, y: 1360, o: 0, html: '<div class="src" style="font-size:21px">Typical claims · illustration</div>' });
appear('s2_ill', VT(1) + 0.3, { dy: 6, blur: 0 });
shotOut('s2', VT(4) - 0.12, 'left', 0.28);

// S3 WHY -------------------------------------------------------------------
shot('s3'); shotIn('s3', VT(4) - 0.1, 'left', 0.3);
mk('s3_t', { parent: 's3', x: 72, y: 520, w: 936, o: 1, html: '<div class="h1" style="font-size:112px">None of these can ever be wrong. So they tell you <span class="red">nothing.</span></div>' });
karaoke('s3_t', VT(4), VE(4));
cue(VE(4) - 0.3, 'hit');
cue(VT(5), 'riser', { dur: 1.2 });
shotOut('s3', VT(5) - 0.12, 'zoom', 0.22);

// S4 BFYP -------------------------------------------------------------------
shot('s4'); shotIn('s4', VT(5) - 0.1, 'zoomIn', 0.4);
cue(VT(5), 'impact', { size: 0.85 }); cue(VT(5) + 0.05, 'ding', { note: 88 });
realScreen('s4_card', 'today_lines', { parent: 's4', w: 940, x: 70, y: 660 });
stamp('s4_stamp', 'today_lines', { parent: 's4', x: 70, y: 580, o: 1 });
tour('s4_card', [{ r: REG.today_lines.l4, key: 'ON BFYP · TODAY', text: 'Every line names what would prove it', t0: VT(5) + 0.2, t1: VT(6) - 0.15, s: 1.08, move: 0.35 }], { cy: 1000, fit: 900, maxS: 1.1, callY: 330 });
K('s4_stamp', 'o', [[VT(5) + 0.2, 1, 'linear'], [VT(5) + 0.4, 0, 'linear']]);
screenCaption('s4_cap', 'today_lines');
K('s4_cap', 'o', [[VT(5) + 0.3, 0, 'linear'], [VT(5) + 0.5, 1, 'linear'], [VT(6) - 0.2, 1, 'linear'], [VT(6), 0, 'linear']]);
subtitles([{ t0: VT(5), t1: VE(5), html: 'On BFYP, every line names <span class="g">what would prove it.</span>' }], { y: 1290, fs: 48 });
shotOut('s4', VT(6) - 0.15, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(6) - 0.1, { lines: ['Trade vibes', 'for <span class="g">evidence.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'today_lines', w: 720 }, note: 'Screen from 23 Sep 2026 · AI voice' });
cue(VT(6) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['If it can’t be', 'proven wrong,', 'it’s a <span class="amber">vibe.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:124px',
  extra: `<div class="h3" style="position:absolute;left:76px;top:900px;color:#9aa7a2;text-decoration:line-through;text-decoration-color:#ff5d5d;text-decoration-thickness:8px">“It’ll pump eventually.”</div>
  <div class="h3" style="position:absolute;left:76px;top:1010px;color:#9aa7a2;text-decoration:line-through;text-decoration-color:#ff5d5d;text-decoration-thickness:8px">“Smart money knows.”</div>
  <div class="h3" style="position:absolute;left:76px;top:1120px;color:#9aa7a2;text-decoration:line-through;text-decoration-color:#ff5d5d;text-decoration-thickness:8px">“Trust me.”</div>` });
