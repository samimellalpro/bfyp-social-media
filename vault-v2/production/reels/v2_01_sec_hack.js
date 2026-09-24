/* V2-01 — "Even the SEC got faked." */
R.setup({ dur: 21.4, bpm: 90 });
const b = B;
music({ style: 'cinematic', bpm: 90, key: 'D', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 101,
  sections: [{ beat: 0, type: 'hook' }, { beat: 4, type: 'tension' }, { beat: 15, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 25, type: 'cta' }],
  events: [{ type: 'stop', beat: 15.5, beats: 0.5 }, { type: 'end', beat: 32, tail: 0.4 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ["The SEC's own account", 'posted <span class="red">fake news.</span>'], { parent: 's1', y: 250, cls: 'h2' });
hookSettle('s1_h');
sourceCard('s1_card', { parent: 's1', x: 70, y: 700, w: 940, o: 1, kind: 'X post · @SECGov · unauthorized', date: '9 Jan 2024 · 4:11 pm ET',
  quote: '“Today the SEC grants approval for #Bitcoin ETFs for listing on all registered national securities exchanges.”',
  qCss: 'font-size:54px;font-weight:700;color:#141a18;line-height:1.18', url: 'Source: sec.gov/secgov-x-account' });
K('s1_card', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outBack']]);
K('s1_card', 'r', [[0, -1.5, 'linear'], [0.8, 0, 'outElastic']]);
stampLabel('s1_fake', 'FAKE', 700, 640, { rot: -10, parent: 's1' });
stampIn('s1_fake', b(1.5));
cue(0, 'impact', { size: 1.0 }); cue(0.05, 'notif');
camPunch(b(1.5), 0.03);
shotOut('s1', b(4) - 0.1, 'left', 0.3);

// S2 PRICE MOVES ------------------------------------------------------
shot('s2'); shotIn('s2', b(4), 'left', 0.35);
mk('s2_a', { parent: 's2', x: 72, y: 560, o: 0, html: '<div class="h1" style="font-size:150px">Bitcoin <span class="g">↑</span></div><div class="h1 g" style="font-size:190px">+$1,000</div>' });
appear('s2_a', b(4) + 0.05, { dy: 60 });
cue(b(4), 'whoosh', { dur: 0.4, up: true });
mk('s2_b', { parent: 's2', x: 72, y: 1010, o: 0, html: '<div class="h1" style="font-size:110px">then <span class="red">↓ −$2,000</span></div>' });
appear('s2_b', b(5.6), { dy: -40 });
cue(b(5.6), 'subdrop'); cue(b(5.6), 'hit');
mk('s2_src', { parent: 's2', x: 76, y: 1290, o: 0, html: '<div class="src" style="font-size:24px">Per BTC · per U.S. Department of Justice</div>' });
appear('s2_src', b(6), { dy: 10, blur: 0 });
camShake(b(5.6), 0.35, 14);
shotOut('s2', b(8) - 0.1, 'up', 0.3);

// S3 CORRECTION -------------------------------------------------------
shot('s3'); shotIn('s3', b(8), 'up', 0.35);
mk('s3_eb', { parent: 's3', x: 72, y: 380, o: 0, html: '<div class="h3">15 minutes later…</div>' });
appear('s3_eb', b(8) + 0.1, { dy: 16, blur: 0 });
sourceCard('s3_card', { parent: 's3', x: 70, y: 560, w: 940, dark: true, kind: 'X post · SEC Chair Gary Gensler', date: '9 Jan 2024 · 4:26 pm ET',
  quote: '“The @SECGov twitter account was compromised, and an unauthorized tweet was posted. <span style="color:#eef4f1;font-weight:700">The SEC has not approved</span> the listing and trading of spot bitcoin exchange-traded products.”',
  qCss: 'font-size:52px;line-height:1.24', url: 'Source: x.com/GenslerArchive' });
popIn('s3_card', b(8) + 0.15, { from: 0.85, ease: 'outBackSoft' });
cue(b(8) + 0.15, 'notif', { notes: [79, 86] });
shotOut('s3', b(11.5) - 0.1, 'fade', 0.25);

// S4 TWIST ------------------------------------------------------------
shot('s4'); shotIn('s4', b(11.5), 'zoom', 0.35);
headline('s4_h', ['The real approval', 'came <span class="g">the next day.</span>'], { parent: 's4', y: 430, cls: 'h2' });
wordsIn('s4_h', b(11.5) + 0.05, { stagger: 0.05 });
timelineH('s4_tl', [{ x: 0.08, label: '9 JAN 2024', sub: 'Fake post', color: '#ff5d5d', above: false }, { x: 0.92, label: '10 JAN 2024', sub: 'Official SEC order', color: '#22d3a0', above: false }],
  { parent: 's4', y: 900, t0: b(12.2), draw: 0.9 });
cue(b(13.1), 'ding', { note: 86 });
shotOut('s4', b(14) - 0.1, 'zoom', 0.25);

// S5 WHY IT HURTS -----------------------------------------------------
shot('s5'); shotIn('s5', b(14), 'zoomIn', 0.3);
statement('s5_t', 'If an official account<br>can be faked,<br><span class="g">any post can.</span>', { parent: 's5', y: 640, cls: 'h1', css: 'font-size:112px' });
slam('s5_t', b(14));
cue(b(14), 'hit');
cue(b(16), 'riser', { dur: b(1.8) });
shotOut('s5', b(16) - 0.08, 'zoom', 0.2);

// S6 BFYP -------------------------------------------------------------
shot('s6'); shotIn('s6', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.9 }); cue(b(16) + 0.05, 'ding', { note: 88 });
headline('s6_h', ['The filing itself.', '<span class="g">Dated. Linked.</span>'], { parent: 's6', y: 250, cls: 'h2', eyebrow: 'The source · on BFYP' });
wordsIn('s6_h', b(16) + 0.1, { stagger: 0.05 });
realScreen('s6_card', 'nvda_filings5', { parent: 's6', w: 880, x: 100, y: 640 });
stamp('s6_stamp', 'nvda_filings5', { parent: 's6', x: 100, y: 562 });
appear('s6_stamp', b(16) + 0.3, { dy: 14, blur: 0 });
scanOver('s6_card', b(16) + 0.3, 0.7);
screenCaption('s6_cap', 'nvda_filings5');
K('s6_cap', 'o', [[b(17) - 0.001, 0, 'linear'], [b(17) + 0.2, 1, 'linear'], [b(24.8), 1, 'linear'], [b(25), 0, 'linear']]);
K('s6_h', 'o', [[b(17), 1, 'linear'], [b(17) + 0.2, 0, 'linear'], [b(23), 0, 'linear'], [b(23.4), 1, 'linear']]);
K('s6_stamp', 'o', [[b(17), 1, 'linear'], [b(17) + 0.2, 0, 'linear'], [b(23), 0, 'linear'], [b(23.4), 1, 'linear']]);
tour('s6_card', [
  { r: REG.nvda_filings5.r1_date, key: 'DATED', text: 'Every filing shows its date', t0: b(17), t1: b(19) },
  { r: REG.nvda_filings5.r1_link, key: 'LINKED', text: 'Opens the original on SEC.gov', t0: b(19), t1: b(21) },
  { r: REG.nvda_filings5.r3_date, key: 'BOTH DATES', text: 'Event period + filing date', t0: b(21), t1: b(23) },
], { cy: 1010, fit: 820, maxS: 1.6, callY: 330 });
mk('s6_sum', { parent: 's6', x: 72, y: 1330, o: 0, html: '<div class="h3">Posts can be faked.<br><span class="g">Filings are the record.</span></div>' });
appear('s6_sum', b(23.2), { dy: 40 });
cue(b(23.2), 'hit');
shotOut('s6', b(25) - 0.15, 'zoom', 0.25);

// CTA -----------------------------------------------------------------
ctaCard(b(25), { lines: ['Read the filing,', '<span class="g">not the post.</span>'], sub: 'Every NVIDIA filing, dated and linked.',
  visual: { asset: 'nvda_filings5', w: 760 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(25) + 0.4, 'sparkle');
cue(b(32), 'hit');

R.coverSetup = () => coverDesign({ lines: ["The SEC's own", 'account posted', '<span class="red">fake news.</span>'], hY: 400, cls: 'h1',
  extra: `<div class="srccard" style="position:absolute;left:90px;top:900px;width:900px"><div class="meta"><span>X post · @SECGov · unauthorized</span><span>9 Jan 2024</span></div><div class="q" style="font-size:44px;font-weight:650;color:#141a18">“Today the SEC grants approval for #Bitcoin ETFs…”</div></div>
  <div class="stamp" style="position:absolute;left:640px;top:860px;transform:rotate(-10deg)">FAKE</div>
  <div class="h4" style="position:absolute;left:76px;top:1320px">Here's where the <span class="g">real record</span> lives →</div>` });
