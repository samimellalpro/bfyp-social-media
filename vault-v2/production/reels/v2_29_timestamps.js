/* V2-29 — "Why every screen we post is timestamped." — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 144 });
const b = B;
music({ style: 'trap', bpm: 144, key: 'D', mode: 'minor', prog: ['i', 'VI', 'iv', 'v'], seed: 2929,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(1) / b(1)), type: 'drop' }, { beat: Math.floor(VT(4) / b(1)), type: 'break' }, { beat: Math.floor(VT(5) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK: a screenshot ageing ----------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 230, w: 936, o: 1, html: '<div class="h1" style="font-size:104px">Every screenshot starts <span class="amber">aging</span> the second it’s taken.</div>' });
karaoke('s1_t', VT(0), VE(0), { dimStart: true });
realScreen('s1_card', 'today_lines', { parent: 's1', w: 900, x: 90, y: 760, o: 1 });
K('s1_card', 'sat', [[0, 1, 'linear'], [VE(0), 0.15, 'linear']]);
K('s1_card', 'bright', [[0, 1, 'linear'], [VE(0), 0.75, 'linear']]);
K('s1_card', 'r', [[0, 0, 'linear'], [VE(0), -1.5, 'inOutQuad']]);
mk('s1_clock', { parent: 's1', x: 72, y: 1360, o: 1, html: '<div class="mono" id="s1_age" style="font-size:40px;color:#f0b44a">age: 00:00</div>' });
hook(t => { const s = Math.floor(t * 17); $('s1_age').textContent = `age: ${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`; });
for (let i = 0; i < 6; i++) cue(0.2 + i * 0.5, 'tick');
cue(0, 'shutter'); flash(0.04, { peak: 0.25, dur: 0.16 });
shotOut('s1', VT(1) - 0.12, 'left', 0.28);

// S2 SAME PAGE, 46 MINUTES APART -----------------------------------------------------
shot('s2'); shotIn('s2', VT(1) - 0.1, 'left', 0.3);
mk('s2_t', { parent: 's2', x: 72, y: 230, w: 936, o: 1, html: '<div class="h2" style="font-size:84px">Same BFYP Today page. <span class="g">Forty-six minutes apart.</span></div>' });
karaoke('s2_t', VT(1), VE(1));
paneCrop('s2_A', 'today_lines', REG.today_lines.l1, 60, 560, 960, 250, { parent: 's2', scale: 1.05 });
paneCrop('s2_B', 'today_head', [0, 60, 940, 300], 60, 960, 960, 330, { parent: 's2', scale: 1.0 });
mk('s2_pa', { parent: 's2', x: 76, y: 500, o: 1, html: `<div class="pill" style="font-size:22px;padding:9px 18px"><span class="dot"></span>${capText('today_lines')}</div>` });
mk('s2_pb', { parent: 's2', x: 76, y: 900, o: 1, html: `<div class="pill" style="font-size:22px;padding:9px 18px"><span class="dot"></span>${capText('today_head')}</div>` });
appear('s2_A', VT(1) + 0.2, { dy: 50 }); appear('s2_pa', VT(1) + 0.3, { dy: 10, blur: 0 });
appear('s2_B', VT(1) + 1.2, { dy: 50 }); appear('s2_pb', VT(1) + 1.3, { dy: 10, blur: 0 });
cue(VT(1) + 0.2, 'whoosh', { dur: 0.3 }); cue(VT(1) + 1.2, 'whoosh', { dur: 0.3 });
mk('s2_d', { parent: 's2', x: 660, y: 840, o: 0, origin: '50% 50%', html: '<div class="callout" style="position:relative"><span class="k">Δ TIME</span>+46 min</div>' });
calloutIn('s2_d', VT(1) + 2.0); cue(VT(1) + 2.0, 'ding', { note: 86 });
shotOut('s2', VT(2) - 0.12, 'zoom', 0.22);

// S3 330 → 354 ---------------------------------------------------------------------
shot('s3'); shotIn('s3', VT(2) - 0.1, 'zoomIn', 0.3);
mk('s3_eb', { parent: 's3', x: 72, y: 330, o: 1, html: '<div class="eyebrow">Observations · last 24h · 10 assets</div>' });
mk('s3_a', { parent: 's3', x: 60, y: 460, o: 1, html: '<div class="bigno" style="font-size:230px;color:#9aa7a2">330</div><div class="mono" style="font-size:30px;color:#9aa7a2">21:28 UTC</div>' });
mk('s3_arrow', { parent: 's3', x: 470, y: 560, o: 0, html: '<div class="bigno g" style="font-size:150px">→</div>' });
mk('s3_b', { parent: 's3', x: 640, y: 460, o: 0, html: '<div class="bigno g" id="s3_bn" style="font-size:230px">330</div><div class="mono" style="font-size:30px;color:#22d3a0">22:14 UTC</div>' });
appear('s3_arrow', VT(2) + 1.3, { dx: -40, dy: 0 });
appear('s3_b', VT(2) + 1.6, { dy: 30 });
counter('s3_bn', VT(2) + 1.8, VE(2), 330, 354, v => Math.round(v).toString());
cue(VT(2) + 1.8, 'ticks', { n: 12, dur: VE(2) - VT(2) - 1.9, curve: 0.6 });
mk('s3_n', { parent: 's3', x: 72, y: 900, w: 936, o: 0, html: '<div class="h3">Same page. Same day.<br><span class="g">Different number.</span></div>' });
appear('s3_n', VE(2) - 0.2, { dy: 30 });
subtitles([{ t0: VT(2), t1: VE(2), html: '330 observations. Then <span class="g">354.</span>' }], { y: 1290, fs: 46 });
mk('s3_src', { parent: 's3', x: 76, y: 1180, o: 1, html: '<div class="src" style="font-size:21px">BFYP Today · 23 Sep 2026 · rolling 24h window</div>' });
shotOut('s3', VT(3) - 0.12, 'left', 0.28);

// S4 WE STAMP OURS ---------------------------------------------------------------------
shot('s4'); shotIn('s4', VT(3) - 0.1, 'left', 0.3);
mk('s4_t', { parent: 's4', x: 72, y: 230, w: 936, o: 1, html: '<div class="h2" style="font-size:88px">That’s why every screen we post carries its <span class="g">capture time.</span></div>' });
karaoke('s4_t', VT(3), VE(3));
const CAPS = ['today_lines', 'whale_card', 'nvda_filings4', 'spy_page', 'ai_ask', 'today_cats'];
CAPS.forEach((a, i) => {
  const id = `s4_p${i}`;
  mk(id, { parent: 's4', x: 72 + (i % 2) * 18, y: 640 + i * 118, o: 0, noMax: true, html: `<div class="pill" style="font-size:21px;letter-spacing:.08em;padding:12px 22px"><span class="dot"></span>${capText(a)}</div>` });
  const t = VT(3) + 0.35 + i * 0.3;
  K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
  K(id, 'x', [[t, 1100, 'linear'], [t + 0.35, 72 + (i % 2) * 18, 'outExpo']]);
  cue(t, 'click');
});
shotOut('s4', VT(4) - 0.12, 'zoom', 0.22);

// S5 MOVED ON -----------------------------------------------------------------------
shot('s5'); shotIn('s5', VT(4) - 0.1, 'zoomIn', 0.3);
mk('s5_t', { parent: 's5', x: 72, y: 560, w: 936, o: 1, html: '<div class="h1" style="font-size:112px">By the time you watch this, the live page has <span class="g">moved on.</span></div>' });
karaoke('s5_t', VT(4), VE(4));
shotOut('s5', VT(5) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(5) - 0.1, { lines: ['Check the', '<span class="g">live page.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'today_lines', w: 720 }, note: 'Screens from 23 Sep 2026 · AI voice' });
cue(VT(5) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['Every screenshot', 'starts <span class="amber">aging.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:120px',
  extra: `<div class="bigno" style="position:absolute;left:60px;top:760px;font-size:200px;color:#9aa7a2">330</div><div class="bigno g" style="position:absolute;left:470px;top:790px;font-size:140px">→</div><div class="bigno g" style="position:absolute;left:640px;top:760px;font-size:200px">354</div>
  <div class="mono" style="position:absolute;left:72px;top:980px;font-size:28px;color:#9aa7a2">21:28 UTC</div><div class="mono" style="position:absolute;left:652px;top:980px;font-size:28px;color:#22d3a0">22:14 UTC</div>
  <div class="h4" style="position:absolute;left:76px;top:1120px">Same page. <span class="g">46 minutes apart →</span></div>` });
