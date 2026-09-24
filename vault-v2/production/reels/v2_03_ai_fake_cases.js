/* V2-03 — "Fluent isn't true." */
R.setup({ dur: 20.8, bpm: 120 });
const b = B;
music({ style: 'minimal', bpm: 120, key: 'G', mode: 'dorian', prog: ['i', 'IV', 'i', 'VII'], seed: 303,
  sections: [{ beat: 0, type: 'hook' }, { beat: 10, type: 'tension' }, { beat: 16, type: 'build' }, { beat: 18, type: 'drop' }, { beat: 31, type: 'cta' }],
  events: [{ type: 'stop', beat: 17, beats: 1 }, { type: 'end', beat: 41, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['An AI invented', '<span class="g">6 court cases.</span>'], { parent: 's1', y: 250, cls: 'h1' });
hookSettle('s1_h');
sourceCard('s1_card', { parent: 's1', x: 70, y: 620, w: 940, o: 1, kind: 'U.S. District Court · S.D.N.Y.', date: 'Mata v. Avianca · 2023',
  quote: '“…<b>non-existent judicial opinions</b> with fake quotes and citations created by the artificial intelligence tool ChatGPT…”',
  qCss: 'font-size:52px;font-weight:600;color:#141a18;line-height:1.2', url: 'Sanctions opinion · 22 Jun 2023' });
K('s1_card', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outBack']]);
cue(0, 'impact', { size: 1.0 });
mk('s1_b', { parent: 's1', x: 72, y: 1250, o: 0, html: '<div class="h2">A lawyer <span class="red">filed them.</span></div>' });
slam('s1_b', b(2.5)); cue(b(2.5), 'hit'); camPunch(b(2.5), 0.03);
shotOut('s1', b(6) - 0.1, 'left', 0.3);

// S2 SANCTION ---------------------------------------------------------
shot('s2'); shotIn('s2', b(6), 'left', 0.35);
mk('s2_eb', { parent: 's2', x: 72, y: 430, o: 0, html: '<div class="h3 m">The result:</div>' });
appear('s2_eb', b(6) + 0.05, { dy: 20 });
bigNumber('s2_n', { parent: 's2', y: 560, t0: b(6.3), t1: b(8), from: 0, to: 5000, fmt: v => '$' + Math.round(v).toLocaleString('en-US'), size: 250, color: 'var(--red)', o: 1 });
mk('s2_t', { parent: 's2', x: 72, y: 860, o: 0, html: '<div class="h2">in sanctions.</div><div class="src" style="font-size:24px;margin-top:26px">Judge P. Kevin Castel · S.D.N.Y. · 22 June 2023</div>' });
appear('s2_t', b(7.5), { dy: 30 });
shotOut('s2', b(10) - 0.1, 'up', 0.3);

// S3 CONFIDENT FLUENT WRONG -------------------------------------------
shot('s3'); shotIn('s3', b(10), 'up', 0.3);
const ls = lines('s3_l', ['Confident.', 'Fluent.', '<span class="red">Wrong.</span>'], { parent: 's3', y: 520, cls: 'h1', css: 'font-size:150px', gap: 10 });
ls.forEach((l, i) => { K(l, 'o', [[b(10 + i) - 0.001, 0, 'linear'], [b(10 + i), 0, 'linear'], [b(10 + i) + 0.06, 1, 'linear']]); K(l, 's', [[b(10 + i), 1.25, 'linear'], [b(10 + i) + 0.22, 1, 'outQuart']]); cue(b(10 + i), 'hit'); });
glitchOn('s3_l_l2', b(12), 0.45, 12);
shotOut('s3', b(14) - 0.1, 'zoom', 0.25);

// S4 WHY IT HURTS -----------------------------------------------------
shot('s4'); shotIn('s4', b(14), 'zoomIn', 0.3);
statement('s4_t', 'In markets, a made-up<br>number <span class="g">costs money.</span>', { parent: 's4', y: 700, cls: 'h1', css: 'font-size:108px' });
slam('s4_t', b(14)); cue(b(14), 'hit');
cue(b(18), 'riser', { dur: b(3) });
shotOut('s4', b(18) - 0.1, 'zoom', 0.2);

// S5 BFYP -------------------------------------------------------------
shot('s5'); shotIn('s5', b(18), 'zoomIn', 0.4);
cue(b(18), 'impact', { size: 0.9 }); cue(b(18) + 0.05, 'ding', { note: 86 });
headline('s5_h', ['AI answers that', '<span class="g">admit the gaps.</span>'], { parent: 's5', y: 250, cls: 'h2', eyebrow: 'On BFYP · AI Research' });
wordsIn('s5_h', b(18) + 0.1, { stagger: 0.05 });
realScreen('s5_card', 'ai_prompt', { parent: 's5', w: 900, x: 90, y: 640 });
stamp('s5_stamp', 'ai_prompt', { parent: 's5', x: 90, y: 560 });
appear('s5_stamp', b(18) + 0.3, { dy: 14, blur: 0 });
scanOver('s5_card', b(18) + 0.3, 0.7);
screenCaption('s5_cap', 'ai_prompt');
K('s5_cap', 'o', [[b(19) - 0.001, 0, 'linear'], [b(19) + 0.2, 1, 'linear'], [b(26.8), 1, 'linear'], [b(27), 0, 'linear']]);
K('s5_h', 'o', [[b(19), 1, 'linear'], [b(19) + 0.2, 0, 'linear']]);
K('s5_stamp', 'o', [[b(19), 1, 'linear'], [b(19) + 0.2, 0, 'linear']]);
tour('s5_card', [
  { r: REG.ai_prompt.traced, key: 'TRACED', text: 'Every figure → the evidence it came from', t0: b(19), t1: b(23) },
  { r: REG.ai_prompt.saysso, key: 'HONEST', text: 'No data? The answer says so.', t0: b(23), t1: b(27) },
], { cy: 1000, fit: 880, maxS: 1.4, callY: 330 });
K('s5_card', 'o', [[b(27), 1, 'linear'], [b(27) + 0.25, 0, 'linear']]);
realScreen('s5_label', 'ai_label', { parent: 's5', w: 900, x: 90, y: 760, o: 0 });
appear('s5_label', b(27.2), { dy: 60 });
mk('s5_lt', { parent: 's5', x: 72, y: 470, o: 0, html: '<div class="h2">Automated —<br><span class="g">and it says so.</span></div>' });
appear('s5_lt', b(27.2), { dy: 30 });
cue(b(27.2), 'whoosh', { dur: 0.4 });
shotOut('s5', b(31) - 0.15, 'zoom', 0.25);

// CTA -----------------------------------------------------------------
ctaCard(b(31), { lines: ['Ask with', '<span class="g">receipts.</span>'], sub: 'Free plan: 52 AI credits a month.',
  visual: { asset: 'ai_prompt', w: 760 }, note: 'Live product may differ · screen from 23 Sep 2026' });
cue(b(31) + 0.4, 'sparkle');
cue(b(41), 'hit');

R.coverSetup = () => coverDesign({ lines: ['An AI invented', '<span class="g">6 court cases.</span>', 'A lawyer filed them.'], hY: 400, cls: 'h1', hCss: 'font-size:108px',
  extra: `<div class="srccard" style="position:absolute;left:70px;top:900px;width:940px"><div class="meta"><span>U.S. District Court · S.D.N.Y.</span><span>2023</span></div><div class="q" style="font-size:48px;font-weight:600;color:#141a18">“…non-existent judicial opinions with fake quotes and citations…”</div></div>
  <div class="h4" style="position:absolute;left:76px;top:1340px">Fluent isn't <span class="g">true →</span></div>` });
