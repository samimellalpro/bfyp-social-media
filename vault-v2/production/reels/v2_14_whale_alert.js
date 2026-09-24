/* V2-14 — "This whale alert tells you nothing." */
R.setup({ dur: 20.0, bpm: 124 });
const b = B;
music({ style: 'techhouse', bpm: 124, key: 'A', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 14,
  sections: [{ beat: 0, type: 'hook' }, { beat: 8, type: 'tension' }, { beat: 12, type: 'drop' }, { beat: 28, type: 'break' }, { beat: 32, type: 'cta' }],
  events: [{ type: 'stop', beat: 10.5, beats: 1.5 }, { type: 'end', beat: 40, tail: 0.45 }] });
progressBar(); bgLife();

// ---------------------------------------------------------------- S1 HOOK (b0-b8)
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['This whale alert', 'tells you <span class="g">nothing.</span>'], { parent: 's1', y: 250 });
postCard('s1_alert', { parent: 's1', x: 70, y: 660, w: 940, name: 'Alert Feed', handle: '@example_alerts · illustration', o: 1,
  text: '🚨🐋 <span style="color:#fff">$1.09M $LIT</span><br>just moved!', label: 'TYPICAL ALERT · ILLUSTRATION · NOT A REAL ACCOUNT' });
K('s1_h', 's', [[0, 1.05, 'linear'], [0.5, 1, 'outExpo']]);
K('s1_alert', 's', [[0, 0.95, 'linear'], [0.5, 1, 'outBack']]);
K('s1_alert', 'r', [[0, -2.2, 'linear'], [0.7, 0, 'outElastic']]);
cue(0, 'impact', { size: 1.0 }); cue(0.05, 'notif');
const qs = lines('s1_q', ['Who is the <span class="g">wallet?</span>', 'One transfer or <span class="g">many?</span>', 'Where is the <span class="g">proof?</span>'], { parent: 's1', y: 1130, cls: 'h2', gap: 20, css: 'font-size:78px' });
qs.forEach((q, i) => {
  K(q, 'o', [[b(3 + i * 1.5) - 0.001, 0, 'linear'], [b(3 + i * 1.5), 0, 'linear'], [b(3 + i * 1.5) + 0.08, 1, 'linear']]);
  K(q, 'x', [[b(3 + i * 1.5), -40, 'linear'], [b(3 + i * 1.5) + 0.35, 0, 'outExpo']]);
  cue(b(3 + i * 1.5), 'pop');
});
K('s1_alert', 'bright', [[b(3), 1, 'linear'], [b(3) + 0.3, 0.6, 'outCubic']]);
K('s1_alert', 'y', [[b(3), 660, 'linear'], [b(3) + 0.4, 620, 'outExpo']]);
camPunch(b(3), 0.015); camPunch(b(4.5), 0.015); camPunch(b(6), 0.02);
shotOut('s1', b(8), 'zoom', 0.28);

// ---------------------------------------------------------------- S2 STATEMENT (b8-b12)
shot('s2'); shotIn('s2', b(8), 'zoomIn', 0.35);
statement('s2_t', 'Size without<br>context is<br>just <span class="g">noise.</span>', { parent: 's2', y: 560, cls: 'h1', css: 'font-size:132px' });
slam('s2_t', b(8));
cue(b(8), 'hit'); cue(b(8), 'whoosh', { dur: 0.35 });
mk('s2_sub', { parent: 's2', x: 72, y: 1090, html: '<div class="h3 m">Same move, <span class="g">on BFYP</span> →</div>', o: 0 });
appear('s2_sub', b(10), { dy: 30 });
cue(b(12), 'riser', { dur: b(2.2) });
cue(b(10.5), 'reverse', { dur: b(1.5) });
shotOut('s2', b(12) - 0.12, 'zoom', 0.2);

// ---------------------------------------------------------------- S3 PROOF (b12-b28)
shot('s3'); shotIn('s3', b(12), 'zoomIn', 0.4);
cue(b(12), 'impact', { size: 0.85 }); cue(b(12) + 0.05, 'ding', { note: 88 });
headline('s3_h', ['Every large move,', '<span class="g">typed and sourced.</span>'], { parent: 's3', y: 236, cls: 'h3', eyebrow: 'Same move · on BFYP' });
wordsIn('s3_h', b(12) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'whale_card', { parent: 's3', w: 944, x: 68, y: 640 });
stamp('s3_stamp', 'whale_card', { parent: 's3', x: 68, y: 560 });
appear('s3_stamp', b(12) + 0.3, { dy: 16, blur: 0 });
K('s3_stamp', 'o', [[b(13) - 0.1, 1, 'linear'], [b(13) + 0.1, 0, 'linear'], [b(25), 0, 'linear'], [b(25.5), 1, 'linear']]);
scanOver('s3_card', b(12) + 0.35, 0.7);
screenCaption('s3_cap', 'whale_card');
K('s3_cap', 'o', [[b(13) - 0.001, 0, 'linear'], [b(13) + 0.2, 1, 'linear'], [b(31.5), 1, 'linear'], [b(32), 0, 'linear']]);
K('s3_h', 'o', [[b(13), 1, 'linear'], [b(13) + 0.2, 0, 'linear'], [b(25), 0, 'linear'], [b(25.4), 1, 'linear']]);
const steps = [
  { r: [186, 62, 650, 64], key: 'TYPED + SIZED', text: 'Large transfer · $1.09M LIT', beat: 13 },
  { r: [186, 186, 620, 116], key: 'GROUPED', text: '2 similar transfers', beat: 15 },
  { r: [186, 312, 510, 58], key: 'WHO + WHERE', text: 'The wallet + its chain', beat: 17 },
  { r: [452, 390, 380, 64], key: 'TRACK RECORD', text: "Wallet score · ROI", beat: 19 },
  { r: [186, 394, 250, 56], key: 'PROOF', text: 'Raw transaction, 1 click', beat: 21 },
  { r: [186, 478, 600, 86], key: 'WHEN + SOURCE', text: 'Observed · detected · via', beat: 23 },
].map(s => Object.assign(s, { t0: b(s.beat), t1: b(s.beat + 2) - 0.02 }));
tour('s3_card', steps, { cy: 1000, fit: 860, maxS: 1.45, endT: b(25), callY: 330 });
mk('s3_sum', { parent: 's3', x: 72, y: 1300, o: 0, html: '<div class="h2">Not an alert. <span class="g">Evidence.</span></div>' });
appear('s3_sum', b(26), { dy: 40 });
cue(b(26), 'hit');
camPunch(b(12), 0.03); camPunch(b(26), 0.025);
shotOut('s3', b(32) - 0.15, 'zoom', 0.25);

// ---------------------------------------------------------------- CTA (b32-end)
ctaCard(b(32), { lines: ['Read the evidence,', '<span class="g">not the alert.</span>'],
  sub: 'The whale feed is on the free plan.', button: 'betterforyourpocket.com',
  visual: { asset: 'whale_card', w: 800 }, note: 'Live data changes · screen from 23 Sep 2026' });
cue(b(32) + 0.4, 'sparkle');
cue(b(40), 'hit');

R.coverT = 1.2;
R.coverSetup = () => coverDesign({ lines: ['This whale alert', 'tells you <span class="g">nothing.</span>'], asset: 'whale_card', visW: 900, visY: 880, hY: 420,
  extra: '<div style="position:absolute;left:90px;top:1500px" class="h4">Here is what it <span class="g">left out →</span></div>' });
