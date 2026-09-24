/* V2-08 — "Can't trace it? Can't trust it." */
R.setup({ dur: 20.0, bpm: 140 });
const b = B;
music({ style: 'trap', bpm: 140, key: 'C', mode: 'minor', prog: ['i', 'VI', 'iv', 'v'], seed: 808,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 13, type: 'build' }, { beat: 14, type: 'drop' }, { beat: 36, type: 'cta' }],
  events: [{ type: 'stop', beat: 13, beats: 1 }, { type: 'end', beat: 46, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: a screenshot ------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['This is a', '<span class="g">screenshot.</span>'], { parent: 's1', y: 250, cls: 'h1' });
hookSettle('s1_h');
mk('s1_shot', { parent: 's1', x: 110, y: 620, w: 860, o: 1, origin: '50% 50%', html: `
  <div style="position:relative;width:860px;padding:26px;border-radius:26px;background:#e9edeb;box-shadow:0 50px 140px rgba(0,0,0,0.7);transform:rotate(-2deg)">
    <div style="border-radius:16px;background:#0f1311;padding:34px 34px 30px;border:2px solid #26302d">
      <div class="mono" style="font-size:22px;letter-spacing:.14em;color:#6c7874">SCREENSHOT · ILLUSTRATION</div>
      <div style="font-weight:800;font-size:64px;line-height:1.08;margin-top:18px;color:#eef4f1">🐋 Whale just moved<br><span style="color:#22d3a0">$1.09M</span> of LIT!!</div>
      <div style="margin-top:22px;font-size:30px;color:#7e8b87">no link · no wallet · no time</div>
    </div></div>` });
K('s1_shot', 's', [[0, 0.94, 'linear'], [0.45, 1, 'outBack']]);
flash(0.05, { peak: 0.32, dur: 0.18 });
cue(0, 'shutter'); cue(0.02, 'impact', { size: 0.8 });
wordSwap('s1_w', ['Cropped?', 'Old?', 'Edited?'], b(3), b(1.5), { parent: 's1', y: 1190, cls: 'h1', css: 'font-size:130px;color:#ff5d5d', sfx: 'glitch', sfxOpts: { dur: 0.25 } });
glitchOn('s1_shot', b(3), b(4.5), 9);
shotOut('s1', b(8) - 0.1, 'zoom', 0.25);

// S2 THE POINT --------------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'zoomIn', 0.3);
mk('s2_a', { parent: 's2', x: 72, y: 560, o: 0, html: '<div class="h1" style="font-size:112px">You can’t check<br>a screenshot.</div>' });
slam('s2_a', b(8)); cue(b(8), 'hit');
mk('s2_b', { parent: 's2', x: 72, y: 880, o: 0, html: '<div class="h1" style="font-size:112px">You can check<br><span class="g">a link.</span></div>' });
slam('s2_b', b(10.5)); cue(b(10.5), 'hit');
cue(b(14), 'riser', { dur: b(3) });
shotOut('s2', b(14) - 0.1, 'zoom', 0.2);

// S3 BFYP: whale link -------------------------------------------------
shot('s3'); shotIn('s3', b(14), 'zoomIn', 0.4);
cue(b(14), 'impact', { size: 0.9 }); cue(b(14) + 0.05, 'ding', { note: 87 });
headline('s3_h', ['Every large move,', '<span class="g">linked to the raw tx.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · Whale Activity' });
wordsIn('s3_h', b(14) + 0.1, { stagger: 0.04 });
realScreen('s3_card', 'whale_card', { parent: 's3', w: 944, x: 68, y: 650 });
stamp('s3_stamp', 'whale_card', { parent: 's3', x: 68, y: 570 });
appear('s3_stamp', b(14) + 0.3, { dy: 14, blur: 0 });
scanOver('s3_card', b(14) + 0.3, 0.6);
screenCaption('s3_cap', 'whale_card');
K('s3_cap', 'o', [[b(16) - 0.001, 0, 'linear'], [b(16) + 0.2, 1, 'linear'], [b(24.8), 1, 'linear'], [b(25), 0, 'linear']]);
K('s3_h', 'o', [[b(16), 1, 'linear'], [b(16) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(16), 1, 'linear'], [b(16) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: REG.whale_card.link, key: 'CLICK THROUGH', text: 'View on explorer ↗', t0: b(16), t1: b(20.5) },
  { r: REG.whale_card.when, key: 'SOURCE', text: 'Observed + detected, via etherscan', t0: b(20.5), t1: b(25) },
], { cy: 1000, fit: 600, maxS: 1.55, callY: 330 });
shotOut('s3', b(25) - 0.1, 'left', 0.3);

// S4 BFYP: filings links ----------------------------------------------
shot('s4'); shotIn('s4', b(25), 'left', 0.35);
headline('s4_h', ['Every filing,', '<span class="g">linked to SEC.gov.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · Stocks · NVDA' });
wordsIn('s4_h', b(25) + 0.1, { stagger: 0.04 });
realScreen('s4_card', 'nvda_filings4', { parent: 's4', w: 944, x: 68, y: 650 });
stamp('s4_stamp', 'nvda_filings4', { parent: 's4', x: 68, y: 570 });
appear('s4_stamp', b(25) + 0.3, { dy: 14, blur: 0 });
screenCaption('s4_cap', 'nvda_filings4');
K('s4_cap', 'o', [[b(26.5) - 0.001, 0, 'linear'], [b(26.5) + 0.2, 1, 'linear'], [b(35.8), 1, 'linear'], [b(36), 0, 'linear']]);
K('s4_h', 'o', [[b(27), 1, 'linear'], [b(27) + 0.2, 0, 'linear'], [b(32), 0, 'linear'], [b(32.4), 1, 'linear']]);
K('s4_stamp', 'o', [[b(27), 1, 'linear'], [b(27) + 0.2, 0, 'linear'], [b(32), 0, 'linear'], [b(32.4), 1, 'linear']]);
tour('s4_card', [
  { r: REG.nvda_filings4.links, key: 'ORIGINAL', text: 'Opens the filing on SEC.gov', t0: b(27), t1: b(31.8), s: 1.15 },
], { cy: 1010, fit: 600, maxS: 1.2, callY: 330 });
mk('s4_sum', { parent: 's4', x: 72, y: 1330, o: 0, html: '<div class="h3">Sources <span class="g">one tap away.</span></div>' });
appear('s4_sum', b(32.2), { dy: 30 }); cue(b(32.2), 'hit');
shotOut('s4', b(36) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(36), { lines: ['Don’t trust.', '<span class="g">Click through.</span>'], sub: 'Whale moves and filings, with their sources.',
  visual: { asset: 'whale_card', w: 800 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(36) + 0.4, 'sparkle');
cue(b(46), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Can’t trace it?', '<span class="red">Can’t trust it.</span>'], hY: 420, cls: 'h1', asset: 'whale_card', crop: [180, 380, 660, 190], visW: 900, visY: 860,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1210px">Screenshots can’t be checked.<br><span class="g">Links can →</span></div>' });
