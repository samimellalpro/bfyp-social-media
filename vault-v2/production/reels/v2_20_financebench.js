/* V2-20 — "Fast doesn't matter if it's wrong." (FinanceBench) */
R.setup({ dur: 21.0, bpm: 170 });
const b = B;
music({ style: 'dnb', bpm: 170, key: 'E', mode: 'minor', prog: ['i', 'VI', 'VII', 'i'], seed: 2020,
  sections: [{ beat: 0, type: 'hook' }, { beat: 16, type: 'tension' }, { beat: 30, type: 'build' }, { beat: 32, type: 'drop' }, { beat: 48, type: 'cta' }],
  events: [{ type: 'stop', beat: 31, beats: 1 }, { type: 'end', beat: 59, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_n', { parent: 's1', x: 50, y: 260, o: 1, html: '<div class="bigno red" style="font-size:400px;text-shadow:0 0 80px rgba(255,93,93,0.35)">81%</div>' });
K('s1_n', 's', [[0, 1.1, 'linear'], [0.5, 1, 'outExpo']]);
glitchOn('s1_n', 0, 0.3, 10);
mk('s1_t', { parent: 's1', x: 72, y: 700, w: 940, o: 1, html: '<div class="h1" style="font-size:100px">of questions on<br>SEC filings:<br><span class="red">wrong or refused.</span></div>' });
mk('s1_src', { parent: 's1', x: 76, y: 1060, o: 1, html: '<div class="src" style="font-size:23px;line-height:1.5">GPT-4-Turbo + retrieval · one test setup<br>FinanceBench · Patronus AI · Nov 2023</div>' });
cue(0, 'impact', { size: 1.0 }); cue(0.02, 'glitch', { dur: 0.3 });
shotOut('s1', b(12) - 0.1, 'left', 0.28);

// S2 SOURCE CARD -----------------------------------------------------
shot('s2'); shotIn('s2', b(12), 'left', 0.3);
sourceCard('s2_card', { parent: 's2', x: 70, y: 520, w: 940, kind: 'Research paper · arXiv 2311.11944', date: 'Nov 2023',
  quote: '“GPT-4-Turbo used with a retrieval system <b>incorrectly answered or refused to answer 81% of questions.</b>”',
  qCss: 'font-size:54px;font-weight:600;color:#141a18;line-height:1.2', url: 'FinanceBench · Patronus AI · 150-question sample' });
popIn('s2_card', b(12.3), { from: 0.85, ease: 'outBackSoft' });
cue(b(12.3), 'pop');
shotOut('s2', b(20) - 0.1, 'up', 0.28);

// S3 FAST. FLUENT. UNCHECKED. ------------------------------------------
shot('s3'); shotIn('s3', b(20), 'up', 0.28);
const ls = lines('s3_l', ['Fast.', 'Fluent.', '<span class="red">Unchecked.</span>'], { parent: 's3', y: 520, cls: 'h1', css: 'font-size:160px', gap: 6 });
ls.forEach((l, i) => { const t = b(20 + i * 2); K(l, 'o', [[t - 0.001, 0, 'linear'], [t, 0, 'linear'], [t + 0.06, 1, 'linear']]); K(l, 's', [[t, 1.25, 'linear'], [t + 0.2, 1, 'outQuart']]); cue(t, 'hit'); });
mk('s3_b', { parent: 's3', x: 72, y: 1160, o: 0, html: '<div class="h2">Finance needs <span class="g">receipts.</span></div>' });
appear('s3_b', b(27), { dy: 30 }); cue(b(27), 'ding', { note: 84 });
cue(b(32), 'riser', { dur: b(4) });
shotOut('s3', b(32) - 0.1, 'zoom', 0.2);

// S4 BFYP: four figures, four receipts -----------------------------------------
shot('s4'); shotIn('s4', b(32), 'zoomIn', 0.4);
cue(b(32), 'impact', { size: 0.9 }); cue(b(32) + 0.05, 'ding', { note: 88 });
headline('s4_h', ['Start from', '<span class="g">the filing.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · NVDA · as filed' });
wordsIn('s4_h', b(32) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'nvda_fund', { parent: 's4', w: 880, x: 100, y: 640 });
stamp('s4_stamp', 'nvda_fund', { parent: 's4', x: 100, y: 560 });
appear('s4_stamp', b(32) + 0.3, { dy: 14, blur: 0 });
scanOver('s4_card', b(32) + 0.3, 0.6);
screenCaption('s4_cap', 'nvda_fund');
K('s4_cap', 'o', [[b(34) - 0.001, 0, 'linear'], [b(34) + 0.2, 1, 'linear'], [b(47.8), 1, 'linear'], [b(48), 0, 'linear']]);
K('s4_h', 'o', [[b(34), 1, 'linear'], [b(34) + 0.2, 0, 'linear']]);
K('s4_stamp', 'o', [[b(34), 1, 'linear'], [b(34) + 0.2, 0, 'linear']]);
tour('s4_card', [
  { r: REG.nvda_fund.rev, key: 'REVENUE · FY2026', text: '$215.9B · 10-K ✓', t0: b(34), t1: b(36.75), s: 1.35 },
  { r: REG.nvda_fund.ni, key: 'NET INCOME · FY2026', text: '$120.1B · 10-K ✓', t0: b(36.75), t1: b(39.5), s: 1.35 },
  { r: REG.nvda_fund.ta, key: 'TOTAL ASSETS', text: '$206.8B · 10-K ✓', t0: b(39.5), t1: b(42.25), s: 1.35 },
  { r: REG.nvda_fund.tl, key: 'TOTAL LIABILITIES', text: '$49.5B · 10-K ✓', t0: b(42.25), t1: b(45), s: 1.35 },
], { cy: 1000, fit: 800, maxS: 1.4, callY: 330, endT: b(45) });
K('s4_card', 'o', [[b(45), 1, 'linear'], [b(45.4), 0.18, 'linear']]);
mk('s4_sum', { parent: 's4', x: 72, y: 800, w: 936, o: 0, html: '<div class="h1" style="font-size:124px;text-shadow:0 10px 50px rgba(0,0,0,0.9)">Four figures.<br><span class="g">Four receipts.</span></div>' });
slam('s4_sum', b(45.3)); cue(b(45.3), 'hit');
shotOut('s4', b(48) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(48), { lines: ['Answers you', '<span class="g">can audit.</span>'], sub: 'Filings first. AI second. Receipts always.',
  visual: { asset: 'nvda_fund', w: 600 }, note: 'Screens from 23 Sep 2026 · live data changes' });
cue(b(48) + 0.4, 'sparkle');
cue(b(59), 'hit');

R.coverSetup = () => coverDesign({ lines: [''], hY: 380, cls: 'h1',
  extra: `<div class="bigno red" style="position:absolute;left:50px;top:300px;font-size:400px;text-shadow:0 0 80px rgba(255,93,93,0.35)">81%</div>
  <div class="h1" style="position:absolute;left:72px;top:740px;font-size:96px">wrong or refused.</div>
  <div class="src" style="position:absolute;left:76px;top:880px;font-size:23px;line-height:1.5">AI on SEC-filing questions · FinanceBench, Nov 2023</div>
  <div class="h2" style="position:absolute;left:72px;top:1080px">Fast doesn’t matter<br>if it’s <span class="red">wrong.</span></div>` });
