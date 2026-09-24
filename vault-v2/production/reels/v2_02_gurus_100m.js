/* V2-02 — "Follow filings, not followers." */
R.setup({ dur: 20.6, bpm: 132 });
const b = B;
music({ style: 'garage', bpm: 132, key: 'F', mode: 'minor', prog: ['i7', 'iv7', 'VI', 'v7'], seed: 202, swing: 0.12,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 20, type: 'build' }, { beat: 23, type: 'drop' }, { beat: 35, type: 'cta' }],
  events: [{ type: 'stop', beat: 22, beats: 1 }, { type: 'end', beat: 45, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['8 “trading gurus.”', '<span class="g">$100M.</span>', 'SEC charges.'], { parent: 's1', y: 230, cls: 'h1', css: 'font-size:112px' });
hookSettle('s1_h');
sourceCard('s1_card', { parent: 's1', x: 70, y: 640, w: 940, dark: true, o: 1, kind: 'SEC · Press release 2022-221', date: '14 Dec 2022',
  headline: 'SEC Charges Eight Social Media Influencers in $100 Million Stock Manipulation Scheme Promoted on Discord and Twitter',
  hlCss: 'font-size:54px', url: 'sec.gov/newsroom/press-releases/2022-221' });
K('s1_card', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outBack']]);
cue(0, 'impact', { size: 1.0 });
mk('s1_note', { parent: 's1', x: 76, y: 1120, o: 0, html: '<div class="src" style="font-size:24px">Allegations · related criminal case pending</div>' });
appear('s1_note', b(2), { dy: 10, blur: 0 });
shotOut('s1', b(8) - 0.1, 'left', 0.3);

// S2 THE PLAYBOOK -----------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'left', 0.35);
mk('s2_eb', { parent: 's2', x: 72, y: 300, o: 0, html: '<div class="h3">The playbook, <span class="g">per the SEC:</span></div>' });
appear('s2_eb', b(8) + 0.05, { dy: 20 });
mk('s2_q', { parent: 's2', x: 72, y: 480, w: 936, o: 1, html: `<div class="h2" style="font-size:80px;line-height:1.08">“…posting <span class="g">price targets</span> or indicating they were <span class="g">buying, holding, or adding</span> to their stock positions.”</div>` });
wordsIn('s2_q', b(9), { stagger: 0.035, dy: 30 });
mk('s2_src', { parent: 's2', x: 76, y: 1180, o: 0, html: '<div class="src" style="font-size:24px">SEC press release 2022-221 · 14 Dec 2022</div>' });
appear('s2_src', b(10), { dy: 10, blur: 0 });
shotOut('s2', b(14) - 0.1, 'up', 0.3);

// S3 THEN SOLD --------------------------------------------------------
shot('s3'); shotIn('s3', b(14), 'up', 0.35);
statement('s3_t', '…then sold.<br><span class="red">Without telling<br>their followers.</span>', { parent: 's3', y: 600, cls: 'h1', css: 'font-size:112px' });
slam('s3_t', b(14));
cue(b(14), 'hit'); cue(b(14), 'subdrop');
mk('s3_n', { parent: 's3', x: 76, y: 1010 + 60, o: 0, html: '<div class="small" style="color:#9aa7a2">As alleged by the SEC. Allegations are unproven; the criminal case is pending.</div>' });
appear('s3_n', b(15), { dy: 10, blur: 0 });
shotOut('s3', b(18) - 0.1, 'zoom', 0.25);

// S4 WHY IT HURTS -----------------------------------------------------
shot('s4'); shotIn('s4', b(18), 'zoomIn', 0.3);
mk('s4_a', { parent: 's4', x: 72, y: 600, o: 0, html: '<div class="h1" style="font-size:112px">A post can say<br><span class="g">“I’m buying.”</span></div>' });
slam('s4_a', b(18)); cue(b(18), 'hit');
mk('s4_b', { parent: 's4', x: 72, y: 900, o: 0, html: '<div class="h1" style="font-size:112px">It can’t <span class="g">prove it.</span></div>' });
slam('s4_b', b(20)); cue(b(20), 'hit');
cue(b(23), 'riser', { dur: b(3) });
shotOut('s4', b(23) - 0.1, 'zoom', 0.2);

// S5 BFYP -------------------------------------------------------------
shot('s5'); shotIn('s5', b(23), 'zoomIn', 0.4);
cue(b(23), 'impact', { size: 0.9 }); cue(b(23) + 0.05, 'ding', { note: 89 });
headline('s5_h', ['Insider trades get', '<span class="g">filed. Dated. Linked.</span>'], { parent: 's5', y: 250, cls: 'h2', eyebrow: 'On BFYP · NVDA · insider forms' });
wordsIn('s5_h', b(23) + 0.1, { stagger: 0.05 });
realScreen('s5_card', 'nvda_insider', { parent: 's5', w: 900, x: 90, y: 680 });
stamp('s5_stamp', 'nvda_insider', { parent: 's5', x: 90, y: 600 });
appear('s5_stamp', b(23) + 0.3, { dy: 14, blur: 0 });
scanOver('s5_card', b(23) + 0.3, 0.7);
screenCaption('s5_cap', 'nvda_insider');
K('s5_cap', 'o', [[b(24) - 0.001, 0, 'linear'], [b(24) + 0.2, 1, 'linear'], [b(34.8), 1, 'linear'], [b(35), 0, 'linear']]);
K('s5_h', 'o', [[b(24), 1, 'linear'], [b(24) + 0.2, 0, 'linear'], [b(33), 0, 'linear'], [b(33.4), 1, 'linear']]);
K('s5_stamp', 'o', [[b(24), 1, 'linear'], [b(24) + 0.2, 0, 'linear'], [b(33), 0, 'linear'], [b(33.4), 1, 'linear']]);
tour('s5_card', [
  { r: REG.nvda_insider.desc, key: 'WHO FILES', text: 'Officers, directors, 10%+ owners', t0: b(24), t1: b(27) },
  { r: REG.nvda_insider.r1, key: 'FORM 4', text: 'Due within 2 business days of the trade', t0: b(27), t1: b(30) },
  { r: REG.nvda_insider.notsignal, key: 'NO HYPE', text: 'A reported change, not a signal', t0: b(30), t1: b(33) },
], { cy: 1030, fit: 860, maxS: 1.45, callY: 330 });
mk('s5_src', { parent: 's5', x: 76, y: 1420, o: 0, html: '<div class="src" style="font-size:21px">Form 4 deadline: SEC Form 4 general instructions</div>' });
K('s5_src', 'o', [[b(27.3), 0, 'linear'], [b(27.6), 1, 'linear'], [b(29.8), 1, 'linear'], [b(30), 0, 'linear']]);
shotOut('s5', b(35) - 0.15, 'zoom', 0.25);

// CTA -----------------------------------------------------------------
ctaCard(b(35), { lines: ['Follow filings,', '<span class="g">not followers.</span>'], sub: 'Insider forms on every stock page.',
  visual: { asset: 'nvda_insider', w: 780 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(35) + 0.4, 'sparkle');
cue(b(45), 'hit');

R.coverSetup = () => coverDesign({ lines: ['8 “trading gurus.”', '<span class="g">$100M.</span>', 'SEC charges.'], hY: 400, cls: 'h1',
  extra: `<div class="srccard dark" style="position:absolute;left:70px;top:930px;width:940px"><div class="meta"><span>SEC · Press release 2022-221</span><span>14 Dec 2022</span></div><div class="hl" style="font-size:50px">SEC Charges Eight Social Media Influencers in $100 Million Stock Manipulation Scheme…</div></div>
  <div class="h4" style="position:absolute;left:76px;top:1380px">Follow filings, <span class="g">not followers →</span></div>` });
