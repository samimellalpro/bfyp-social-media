/* V2-05 — "No testimonials. On purpose." (FTC hook) */
R.setup({ dur: 20.4, bpm: 113 });
const b = B;
music({ style: 'amapiano', bpm: 113, key: 'Bb', mode: 'minor', prog: ['i7', 'iv7', 'VI', 'v'], seed: 505,
  sections: [{ beat: 0, type: 'hook' }, { beat: 7, type: 'tension' }, { beat: 13, type: 'build' }, { beat: 15, type: 'drop' }, { beat: 30, type: 'cta' }],
  events: [{ type: 'stop', beat: 14, beats: 1 }, { type: 'end', beat: 38, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['The FTC', 'had to ban', '<span class="red">fake reviews.</span>'], { parent: 's1', y: 230, cls: 'h1', css: 'font-size:118px' });
hookSettle('s1_h');
mk('s1_stars', { parent: 's1', x: 72, y: 600, o: 1, html: '<div style="font-size:96px;letter-spacing:10px;color:#f0b44a;text-shadow:0 0 40px rgba(240,180,74,0.45)">★★★★★</div>' });
strikeOver('s1_strike', 's1', 60, 660, 560, b(1.2));
sourceCard('s1_card', { parent: 's1', x: 70, y: 790, w: 940, o: 1, kind: 'Federal Trade Commission · press release', date: '14 Aug 2024',
  headline: 'Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials', hlCss: 'font-size:56px', url: 'ftc.gov · rule effective 21 Oct 2024' });
K('s1_card', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outBack']]);
cue(0, 'impact', { size: 1.0 });
shotOut('s1', b(7) - 0.1, 'left', 0.3);

// S2 KHAN QUOTE -------------------------------------------------------
shot('s2'); shotIn('s2', b(7), 'left', 0.35);
mk('s2_q', { parent: 's2', x: 72, y: 470, w: 936, o: 1, html: `<div class="h2" style="font-size:84px;line-height:1.08">“Fake reviews not only waste people’s time and money, but also <span class="g">pollute the marketplace</span>…”</div>` });
wordsIn('s2_q', b(7.2), { stagger: 0.04, dy: 30 });
mk('s2_src', { parent: 's2', x: 76, y: 1080, o: 0, html: '<div class="src" style="font-size:24px">Lina M. Khan, FTC Chair<br>FTC press release · 14 Aug 2024</div>' });
appear('s2_src', b(8.5), { dy: 10, blur: 0 });
shotOut('s2', b(12) - 0.1, 'zoom', 0.25);

// S3 TURN -------------------------------------------------------------
shot('s3'); shotIn('s3', b(12), 'zoomIn', 0.3);
statement('s3_t', 'So here’s what<br><span class="g">our</span> pricing page says.', { parent: 's3', y: 720, cls: 'h1', css: 'font-size:104px' });
slam('s3_t', b(12)); cue(b(12), 'hit');
cue(b(15), 'riser', { dur: b(2.5) });
shotOut('s3', b(15) - 0.1, 'zoom', 0.2);

// S4 BFYP HONESTY -----------------------------------------------------
shot('s4'); shotIn('s4', b(15), 'zoomIn', 0.4);
cue(b(15), 'impact', { size: 0.85 }); cue(b(15) + 0.05, 'ding', { note: 85 });
headline('s4_h', ['No made-up praise.', '<span class="g">An audit invite.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · pricing page' });
wordsIn('s4_h', b(15) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'honesty', { parent: 's4', w: 960, x: 60, y: 720 });
stamp('s4_stamp', 'honesty', { parent: 's4', x: 60, y: 640 });
appear('s4_stamp', b(15) + 0.3, { dy: 14, blur: 0 });
scanOver('s4_card', b(15) + 0.3, 0.6);
screenCaption('s4_cap', 'honesty');
K('s4_cap', 'o', [[b(16) - 0.001, 0, 'linear'], [b(16) + 0.2, 1, 'linear'], [b(25.7), 1, 'linear'], [b(26), 0, 'linear']]);
K('s4_h', 'o', [[b(16.5), 1, 'linear'], [b(16.5) + 0.2, 0, 'linear'], [b(21), 0, 'linear'], [b(21.3), 1, 'linear']]);
tour('s4_card', [
  { r: REG.honesty.body, key: 'IN OUR OWN WORDS', text: 'Zero testimonials. None made up.', t0: b(16.5), t1: b(21), s: 1.08 },
], { cy: 960, fit: 900, maxS: 1.1, callY: 330 });
mk('s4_a', { parent: 's4', x: 72, y: 1150, o: 0, html: '<div class="h1" style="font-size:104px">Don’t trust us.</div>' });
slam('s4_a', b(22)); cue(b(22), 'hit');
mk('s4_b', { parent: 's4', x: 72, y: 1270, o: 0, html: '<div class="h1 g" style="font-size:104px">Audit us.</div>' });
slam('s4_b', b(23.5)); cue(b(23.5), 'hit');
K('s4_card', 'o', [[b(21.8), 1, 'linear'], [b(22), 0.5, 'linear'], [b(25.7), 0.5, 'linear'], [b(26), 0, 'linear']]);
['s4_a', 's4_b'].forEach(id => K(id, 'o', [[b(25.7), 1, 'linear'], [b(26), 0, 'linear']]));
K('s4_h', 'o', [[b(25.7), 1, 'linear'], [b(26), 0, 'linear']]);
mk('s4_c', { parent: 's4', x: 72, y: 400, o: 0, html: '<div class="h1">Start at <span class="g">$0.</span></div>' });
appear('s4_c', b(26), { dy: 30 });
realScreen('s4_free', 'free_card', { parent: 's4', w: 936, x: 72, y: 720, o: 0 });
appear('s4_free', b(26.2), { dy: 60, s: 0.94 });
stamp('s4_fstamp', 'free_card', { parent: 's4', x: 72, y: 640 });
appear('s4_fstamp', b(26.5), { dy: 10, blur: 0 });
cue(b(26), 'pop'); cue(b(26.2), 'whoosh', { dur: 0.35 });
shotOut('s4', b(30) - 0.15, 'zoom', 0.25);

// CTA -----------------------------------------------------------------
ctaCard(b(30), { lines: ['Don’t trust us.', '<span class="g">Audit us.</span>'], sub: 'Public pages that have to agree with each other.',
  visual: { asset: 'honesty', w: 860 }, note: 'Screen from 23 Sep 2026 · pricing may change' });
cue(b(30) + 0.4, 'sparkle');
cue(b(38), 'hit');

R.coverSetup = () => coverDesign({ lines: ['The FTC had to ban', '<span class="red">fake reviews.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:108px',
  extra: `<div style="position:absolute;left:72px;top:690px;font-size:110px;letter-spacing:10px;color:#f0b44a;text-shadow:0 0 40px rgba(240,180,74,0.45)">★★★★★</div>
  <div class="strike" style="position:absolute;left:60px;top:760px;width:640px"></div>
  <div class="h2" style="position:absolute;left:72px;top:960px">Zero testimonials.<br><span class="g">Audit us instead.</span></div>` });
