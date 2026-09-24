/* V2-09 — "NVIDIA's 2026 ended in January." (quiz) */
R.setup({ dur: 20.4, bpm: 126 });
const b = B;
music({ style: 'techhouse', bpm: 126, key: 'B', mode: 'minor', prog: ['i', 'iv', 'VI', 'V'], seed: 909,
  sections: [{ beat: 0, type: 'hook' }, { beat: 4, type: 'tension' }, { beat: 8, type: 'drop' }, { beat: 18, type: 'tension' }, { beat: 25, type: 'build' }, { beat: 26, type: 'drop' }, { beat: 35, type: 'cta' }],
  events: [{ type: 'stop', beat: 7.5, beats: 0.5 }, { type: 'stop', beat: 25, beats: 1 }, { type: 'end', beat: 42, tail: 0.35 }] });
progressBar(); bgLife();

// S1 QUIZ ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['When did NVIDIA’s', '<span class="g">fiscal 2026</span> end?'], { parent: 's1', y: 250, cls: 'h1', css: 'font-size:104px', eyebrow: 'Quick quiz' });
hookSettle('s1_h');
optBoxes('s1_o', ['Dec 31, 2026', 'Dec 31, 2025', 'Jan 25, 2026'], { parent: 's1', x: 90, y: 700, gap: 170 });
['0', '1', '2'].forEach((i, k) => { K(`s1_o_${i}`, 'x', [[0, 90 + 60 * (k + 1), 'linear'], [0.25 + k * 0.08, 90, 'outExpo']]); K(`s1_o_${i}`, 'o', [[0, 0, 'linear'], [0.08 + k * 0.08, 1, 'linear']]); });
cue(0, 'impact', { size: 0.9 });
// countdown ticks
mk('s1_cd', { parent: 's1', x: 72, y: 1250, o: 1, html: '<div class="h3 m" id="cdtxt">Answer in 3…</div>' });
hook(t => { const el = $('cdtxt'); if (t < b(4)) el.textContent = 'Pick one.'; else if (t < b(8)) el.textContent = 'Answer in ' + Math.max(1, 3 - Math.floor((t - b(4)) / b(1.34))) + '…'; else el.textContent = ''; });
[4, 5.33, 6.66].forEach(x => cue(b(x), 'tick'));
optReveal('s1_o', 3, 2, b(8));
mk('s1_ans', { parent: 's1', x: 72, y: 1250, o: 0, html: '<div class="h2">C. <span class="g">January 25, 2026.</span></div>' });
appear('s1_ans', b(8.2), { dy: 30 });
camPunch(b(8), 0.035);
shotOut('s1', b(12) - 0.1, 'left', 0.3);

// S2 SOURCE ------------------------------------------------------------
shot('s2'); shotIn('s2', b(12), 'left', 0.35);
sourceCard('s2_card', { parent: 's2', x: 70, y: 520, w: 940, dark: true, kind: 'NVIDIA · Q4 & fiscal 2026 results', date: '25 Feb 2026',
  quote: '<span style="color:#eef4f1;font-weight:700">“For fiscal 2026, revenue was $215.9 billion, up 65% from a year ago.”</span><br><span style="font-size:36px">Fiscal year ended January 25, 2026.</span>',
  qCss: 'font-size:54px;line-height:1.2', url: 'nvidianews.nvidia.com · Form 10-K on SEC EDGAR' });
popIn('s2_card', b(12.3), { from: 0.85, ease: 'outBackSoft' });
cue(b(12.3), 'pop');
shotOut('s2', b(18) - 0.1, 'up', 0.3);

// S3 WHY IT HURTS -----------------------------------------------------
shot('s3'); shotIn('s3', b(18), 'up', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 540, o: 0, html: '<div class="h1" style="font-size:108px">Fiscal years don’t<br>follow <span class="g">the calendar.</span></div>' });
slam('s3_a', b(18)); cue(b(18), 'hit');
mk('s3_b', { parent: 's3', x: 72, y: 870, o: 0, html: '<div class="h1" style="font-size:108px">Compare the wrong<br>periods, get the<br><span class="red">wrong story.</span></div>' });
slam('s3_b', b(21)); cue(b(21), 'hit');
cue(b(26), 'riser', { dur: b(3) });
shotOut('s3', b(26) - 0.1, 'zoom', 0.2);

// S4 BFYP -------------------------------------------------------------
shot('s4'); shotIn('s4', b(26), 'zoomIn', 0.4);
cue(b(26), 'impact', { size: 0.9 }); cue(b(26) + 0.05, 'ding', { note: 90 });
headline('s4_h', ['Every figure', '<span class="g">with its period.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · NVDA · fundamentals' });
wordsIn('s4_h', b(26) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'nvda_fund', { parent: 's4', w: 900, x: 90, y: 640 });
stamp('s4_stamp', 'nvda_fund', { parent: 's4', x: 90, y: 560 });
appear('s4_stamp', b(26) + 0.3, { dy: 14, blur: 0 });
scanOver('s4_card', b(26) + 0.3, 0.6);
screenCaption('s4_cap', 'nvda_fund');
K('s4_cap', 'o', [[b(27) - 0.001, 0, 'linear'], [b(27) + 0.2, 1, 'linear'], [b(34.8), 1, 'linear'], [b(35), 0, 'linear']]);
K('s4_h', 'o', [[b(27), 1, 'linear'], [b(27) + 0.2, 0, 'linear']]);
K('s4_stamp', 'o', [[b(27), 1, 'linear'], [b(27) + 0.2, 0, 'linear']]);
tour('s4_card', [
  { r: REG.nvda_fund.rev_val, key: 'AS FILED', text: 'Revenue $215.9B', t0: b(27), t1: b(31), s: 1.5 },
  { r: REG.nvda_fund.rev_meta, key: 'THE PERIOD', text: 'FY2026 · ended 2026-01-25 · 10-K', t0: b(31), t1: b(34.8), s: 1.6 },
], { cy: 1000, fit: 700, maxS: 1.6, callY: 330 });
shotOut('s4', b(35) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(35), { lines: ['Every number', '<span class="g">with its period.</span>'], sub: 'Straight from the 10-K on SEC EDGAR.',
  visual: { asset: 'nvda_fund', w: 620 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(35) + 0.4, 'sparkle');
cue(b(42), 'hit');

R.coverSetup = () => coverDesign({ lines: ['NVIDIA’s <span class="g">2026</span>', 'ended in', 'January.'], hY: 400, cls: 'h1', hCss: 'font-size:130px', asset: 'nvda_fund', crop: [28, 70, 350, 290], visW: 560, visY: 950,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1480px">Quiz inside →</div>' });
