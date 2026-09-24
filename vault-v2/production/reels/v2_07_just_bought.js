/* V2-07 — "'Just bought' — just?" (13F lag → two dates) */
R.setup({ dur: 20.8, bpm: 108, ceiling: -2.8 });  // AAC adds ~1.3 dB of inter-sample overs on this mix
const b = B;
music({ style: 'synthwave', bpm: 108, key: 'E', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 707,
  sections: [{ beat: 0, type: 'hook' }, { beat: 5, type: 'tension' }, { beat: 18, type: 'build' }, { beat: 20, type: 'drop' }, { beat: 30, type: 'cta' }],
  events: [{ type: 'stop', beat: 19, beats: 1 }, { type: 'end', beat: 37, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
postCard('s1_post', { parent: 's1', x: 70, y: 250, w: 940, name: 'Market Buzz', handle: '@example · illustration', o: 1,
  text: '🚨 Big fund <span style="color:#22d3a0">just bought</span> $XYZ! 🚀', label: 'TYPICAL POST · ILLUSTRATION · NOT A REAL ACCOUNT' });
K('s1_post', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outBack']]);
mk('s1_q', { parent: 's1', x: 72, y: 760, o: 1, html: '<div class="bigno" style="font-size:250px">“Just”<span class="g">?</span></div>' });
K('s1_q', 's', [[0, 1.06, 'linear'], [0.5, 1, 'outExpo']]);
cue(0, 'impact', { size: 1.0 }); cue(0.05, 'notif');
mk('s1_sub', { parent: 's1', x: 72, y: 1110, o: 0, html: '<div class="h3 m">Check when it actually happened.</div>' });
appear('s1_sub', b(2), { dy: 20 });
shotOut('s1', b(5) - 0.1, 'left', 0.3);

// S2 TIMELINE ---------------------------------------------------------
shot('s2'); shotIn('s2', b(5), 'left', 0.35);
headline('s2_h', ['How a fund-holdings', 'report <span class="g">really works:</span>'], { parent: 's2', y: 280, cls: 'h2' });
wordsIn('s2_h', b(5) + 0.05, { stagger: 0.04 });
timelineH('s2_tl', [
  { x: 0.0, label: '1 APR', sub: 'Quarter starts', color: '#8a9a94', above: true },
  { x: 0.5, label: '30 JUN', sub: 'Holdings snapshot', color: '#22d3a0', above: false },
  { x: 1.0, label: '~14 AUG', sub: '13F due (45 days)', color: '#f0b44a', above: true },
], { parent: 's2', y: 900, x0: 170, x1: 910, t0: b(6), draw: 1.6, labW: 330, subFs: 44, labFs: 30, aboveH: 190 });
mk('s2_src', { parent: 's2', x: 76, y: 1220, o: 0, html: '<div class="src" style="font-size:22px">Form 13F: filed within 45 days after quarter end<br>Investor.gov</div>' });
appear('s2_src', b(8), { dy: 10, blur: 0 });
shotOut('s2', b(12) - 0.1, 'up', 0.3);

// S3 WHY IT HURTS -----------------------------------------------------
shot('s3'); shotIn('s3', b(12), 'up', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 560, o: 0, html: '<div class="h1" style="font-size:112px">You see it<br><span class="amber">mid-August.</span></div>' });
slam('s3_a', b(12)); cue(b(12), 'hit');
mk('s3_b', { parent: 's3', x: 72, y: 880, o: 0, html: '<div class="h1" style="font-size:112px">The trade could be<br><span class="red">from April.</span></div>' });
slam('s3_b', b(14.5)); cue(b(14.5), 'hit');
cue(b(20), 'riser', { dur: b(3) });
shotOut('s3', b(20) - 0.1, 'zoom', 0.2);

// S4 BFYP -------------------------------------------------------------
shot('s4'); shotIn('s4', b(20), 'zoomIn', 0.4);
cue(b(20), 'impact', { size: 0.85 }); cue(b(20) + 0.05, 'ding', { note: 88 });
headline('s4_h', ['Every fund page', 'prints <span class="g">two dates.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · ETF · SPY' });
wordsIn('s4_h', b(20) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'spy_cards', { parent: 's4', w: 880, x: 100, y: 640 });
stamp('s4_stamp', 'spy_cards', { parent: 's4', x: 100, y: 560 });
appear('s4_stamp', b(20) + 0.3, { dy: 14, blur: 0 });
scanOver('s4_card', b(20) + 0.3, 0.6);
screenCaption('s4_cap', 'spy_cards');
K('s4_cap', 'o', [[b(21) - 0.001, 0, 'linear'], [b(21) + 0.2, 1, 'linear'], [b(29.8), 1, 'linear'], [b(30), 0, 'linear']]);
K('s4_h', 'o', [[b(21), 1, 'linear'], [b(21) + 0.2, 0, 'linear']]);
K('s4_stamp', 'o', [[b(21), 1, 'linear'], [b(21) + 0.2, 0, 'linear']]);
tour('s4_card', [
  { r: REG.spy_cards.period, key: 'PERIOD', text: 'What the holdings describe: 30 Jun', t0: b(21), t1: b(24) },
  { r: REG.spy_cards.filed_val, key: 'FILED', text: 'When it went public: 28 Aug', t0: b(24), t1: b(27) },
  { r: REG.spy_cards.nport, key: 'THE GAP', text: 'Public with a statutory delay', t0: b(27), t1: b(29.8) },
], { cy: 1000, fit: 700, maxS: 1.6, callY: 330 });
shotOut('s4', b(30) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(30), { lines: ['Check', '<span class="g">both dates.</span>'], sub: 'Period + filing date, on every fund page.',
  visual: { asset: 'spy_cards', w: 700 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(30) + 0.4, 'sparkle');
cue(b(37), 'hit');

R.coverSetup = () => coverDesign({ lines: ['“Just bought it”?', 'Check <span class="g">the date.</span>'], hY: 420, cls: 'h1', hCss: 'font-size:112px', asset: 'spy_cards', visW: 820, visY: 820 });
