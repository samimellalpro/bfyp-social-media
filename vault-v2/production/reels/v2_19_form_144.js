/* V2-19 — "A Form 144 isn't a sale." — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 140 });
const b = B;
music({ style: 'trap', bpm: 140, key: 'G', mode: 'minor', prog: ['i', 'VI', 'iv', 'v'], seed: 1919,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(2) / b(1)), type: 'drop' }, { beat: Math.floor(VT(4) / b(1)), type: 'break' }, { beat: Math.floor(VT(5) / b(1)), type: 'drop' }, { beat: Math.floor(VT(6) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK: the real filings list -------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 230, w: 936, o: 1, html: '<div class="h2" style="font-size:84px">Three <span class="amber">Form 144</span> filings on NVIDIA in September.</div>' });
karaoke('s1_t', VT(0), VE(0), { dimStart: true });
realScreen('s1_card', 'nvda_filings5', { parent: 's1', w: 860, x: 110, y: 640, o: 1 });
stamp('s1_stamp', 'nvda_filings5', { parent: 's1', x: 110, y: 565, o: 1 });
K('s1_card', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outExpo']]);
cue(0, 'impact', { size: 0.9 });
['r1', 'r2', 'r4'].forEach((r, i) => {
  const rg = REG.nvda_filings5[r];
  glowBox(`s1_g${i}`, "s1_card", [rg[0], rg[1], 380, rg[3]], { color: 'rgba(240,180,74,0.14)', border: '#f0b44a' });
  const t = VT(0) + 1.2 + i * 0.45;
  K(`s1_g${i}`, 'o', [[t - 0.001, 0, 'linear'], [t + 0.1, 1, 'linear']]);
  K(`s1_g${i}`, 's', [[t, 1.2, 'linear'], [t + 0.3, 1, 'outBack']]);
  cue(t, 'click');
});
mk('s1_q', { parent: 's1', x: 72, y: 1210, w: 936, o: 0, html: '<div class="h1 red" style="font-size:104px">Insiders dumping?</div>' });
slam('s1_q', VT(1) - 0.05); cue(VT(1), 'hit'); camPunch(VT(1), 0.03);
shotOut('s1', VT(2) - 0.12, 'left', 0.3);

// S2 WHAT IT IS ----------------------------------------------------------
shot('s2'); shotIn('s2', VT(2) - 0.1, 'left', 0.35);
mk('s2_t', { parent: 's2', x: 72, y: 280, w: 936, o: 1, html: '<div class="h1" style="font-size:104px">A Form 144 is a notice of a <span class="g">proposed</span> sale.</div>' });
karaoke('s2_t', VT(2), VE(2));
mk('s2_src', { parent: 's2', x: 76, y: 700, o: 0, html: '<div class="src" style="font-size:22px">Investor.gov · Form 144</div>' });
appear('s2_src', VT(2) + 0.8, { dy: 10, blur: 0 });
sourceCard('s2_card', { parent: 's2', x: 70, y: 820, w: 940, dark: true, kind: 'SEC staff guidance · Securities Act Forms C&amp;DI', date: 'Form 144',
  quote: '“If a person who has filed a Form 144 <b style="color:#eef4f1">does not sell</b> the securities referred to therein, <b style="color:#eef4f1">no amendment</b> reflecting this fact need be filed.”',
  qCss: 'font-size:46px;line-height:1.24', url: 'Compliance & Disclosure Interpretations, Section 131' });
popIn('s2_card', VT(3) - 0.15, { from: 0.85, ease: 'outBackSoft' });
cue(VT(3) - 0.15, 'pop');
shotOut('s2', VT(4) - 0.12, 'zoom', 0.22);

// S3 FILED ≠ SOLD -------------------------------------------------------
shot('s3'); shotIn('s3', VT(4) - 0.1, 'zoomIn', 0.3);
mk('s3_t', { parent: 's3', x: 72, y: 700, w: 936, o: 0, html: '<div class="h1" style="font-size:190px">Filed <span class="g">≠</span><br>sold.</div>' });
slam('s3_t', VT(4)); cue(VT(4), 'impact', { size: 0.8 });
shotOut('s3', VT(5) - 0.12, 'zoom', 0.22);

// S4 FORM 4 on BFYP ------------------------------------------------------
shot('s4'); shotIn('s4', VT(5) - 0.1, 'zoomIn', 0.4);
cue(VT(5), 'ding', { note: 88 });
mk('s4_t', { parent: 's4', x: 72, y: 250, w: 936, o: 1, html: '<div class="eyebrow" style="margin-bottom:18px">On BFYP · NVDA · insider forms</div><div class="h2" style="font-size:84px">Completed insider trades show up on <span class="g">Form 4.</span></div>' });
karaoke('s4_t', VT(5), VE(5));
realScreen('s4_card', 'nvda_insider', { parent: 's4', w: 900, x: 90, y: 700 });
appear('s4_card', VT(5) + 0.2, { dy: 60 });
tour('s4_card', [{ r: REG.nvda_insider.rows, t0: VT(5) + 0.9, t1: VT(6) - 0.2, s: 1.0, move: 0.3 }], { cy: 1060, fit: 900, maxS: 1.1, callY: 330 });
screenCaption('s4_cap', 'nvda_insider');
K('s4_cap', 'o', [[VT(5) + 0.3, 0, 'linear'], [VT(5) + 0.5, 1, 'linear'], [VT(6) - 0.2, 1, 'linear'], [VT(6), 0, 'linear']]);
shotOut('s4', VT(6) - 0.15, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(6) - 0.1, { lines: ['Read what was', '<span class="g">actually filed.</span>'], sub: 'Every filing dated and linked to SEC.gov.',
  visual: { asset: 'nvda_filings5', w: 600 }, note: 'Screens from 23 Sep 2026 · AI voice' });
cue(VT(6) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['A Form 144', '<span class="g">isn’t a sale.</span>'], hY: 420, cls: 'h1', hCss: 'font-size:128px', asset: 'nvda_filings5', crop: [40, 140, 712, 330], visW: 920, visY: 820,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1300px">Filed <span class="g">≠</span> sold →</div>' });
