/* V2-23 — "Same score. Not the same thing." (spot the difference) */
R.setup({ dur: 20.4, bpm: 106 });
const b = B;
music({ style: 'synthwave', bpm: 106, key: 'C', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 2323,
  sections: [{ beat: 0, type: 'hook' }, { beat: 4, type: 'tension' }, { beat: 9, type: 'build' }, { beat: 10, type: 'drop' }, { beat: 28, type: 'cta' }],
  events: [{ type: 'stop', beat: 9, beats: 1 }, { type: 'end', beat: 36, tail: 0.3 }] });
progressBar(); bgLife();

// S1 HOOK: 31/100 vs 31/100 ------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['Same score?'], { parent: 's1', y: 250, cls: 'h1', css: 'font-size:150px' });
hookSettle('s1_h');
['L', 'R'].forEach((side, i) => {
  mk(`s1_${side}`, { parent: 's1', x: i ? 560 : 60, y: 560, w: 460, o: 1, origin: '50% 50%', html: `
    <div style="width:460px;height:520px;border-radius:34px;background:#0f1816;border:3px solid #2a3935;display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div class="mono" style="font-size:28px;letter-spacing:.18em;color:#8a9a94">WALLET ${i ? 'B' : 'A'}</div>
      <div class="bigno" style="font-size:190px;margin-top:10px">31</div><div class="mono" style="font-size:40px;color:#8a9a94">/100</div></div>` });
  K(`s1_${side}`, 'x', [[0, i ? 1100 : -500, 'linear'], [0.45, i ? 560 : 60, 'outExpo']]);
});
cue(0, 'impact', { size: 0.9 }); cue(0.05, 'whoosh', { dur: 0.35 });
mk('s1_q', { parent: 's1', x: 72, y: 1150, w: 936, o: 0, html: '<div class="h3 m">Look closer.</div>' });
appear('s1_q', b(3), { dy: 20 });
shotOut('s1', b(4) - 0.08, 'zoom', 0.22);

// S2 REVEAL: the real rows, split screen --------------------------------------
shot('s2'); shotIn('s2', b(4), 'zoomIn', 0.35);
mk('s2_eb', { parent: 's2', x: 72, y: 250, o: 1, html: '<div class="eyebrow">Two real rows · Smart Money</div>' });
mk('s2_la', { parent: 's2', x: 72, y: 330, o: 1, html: '<div class="h4">Wallet #6</div>' });
paneCrop('s2_A', 'sm_rows_678', [435, 100, 450, 88], 60, 410, 960, 190, { parent: 's2', scale: 2.13 });
mk('s2_lb', { parent: 's2', x: 72, y: 680, o: 1, html: '<div class="h4">Wallet #7</div>' });
paneCrop('s2_B', 'sm_rows_678', [380, 296, 450, 89], 60, 760, 960, 190, { parent: 's2', scale: 2.13 });
appear('s2_A', b(4.2), { dy: 60 }); appear('s2_B', b(5), { dy: 60 });
appear('s2_la', b(4.2), { dy: 20 }); appear('s2_lb', b(5), { dy: 20 });
cue(b(4.2), 'whoosh', { dur: 0.3 }); cue(b(5), 'whoosh', { dur: 0.3 });
stamp('s2_st', 'sm_rows_678', { parent: 's2', x: 72, y: 990 });
appear('s2_st', b(5.5), { dy: 10, blur: 0 });
// glow boxes on the real badges (pane coordinates)
mk('s2_ga', { parent: 's2_A', x: 408, y: 19, w: 425, h: 135, o: 0, origin: '50% 50%', style: { border: '5px solid #c6d4cf', borderRadius: '22px', boxShadow: '0 0 30px rgba(198,212,207,0.55)' } });
mk('s2_gb', { parent: 's2_B', x: 318, y: 19, w: 632, h: 135, o: 0, origin: '50% 50%', style: { border: '5px solid #22d3a0', borderRadius: '22px', boxShadow: '0 0 34px rgba(34,211,160,0.7)' } });
[['s2_ga', 10], ['s2_gb', 12]].forEach(([id, bt]) => { K(id, 'o', [[b(bt) - 0.001, 0, 'linear'], [b(bt) + 0.08, 1, 'linear']]); K(id, 's', [[b(bt), 1.3, 'linear'], [b(bt) + 0.3, 1, 'outExpo']]); });
cue(b(10), 'impact', { size: 0.8 }); cue(b(12), 'ding', { note: 88 });
mk('s2_ka', { parent: 's2', x: 72, y: 1100, w: 936, o: 0, html: '<div class="h3"><span style="color:#c6d4cf">Estimated</span> vs <span class="g">high confidence.</span></div>' });
appear('s2_ka', b(12.3), { dy: 30 });
K('s2_A', 'bright', [[b(12), 1, 'linear'], [b(12.3), 0.75, 'linear']]);
shotOut('s2', b(18) - 0.1, 'zoom', 0.22);

// S3 LESSON -------------------------------------------------------------
shot('s3'); shotIn('s3', b(18), 'zoomIn', 0.3);
mk('s3_a', { parent: 's3', x: 72, y: 560, w: 936, o: 0, html: '<div class="h1" style="font-size:120px">Same number.<br><span class="g">Different confidence.</span></div>' });
slam('s3_a', b(18)); cue(b(18), 'hit');
mk('s3_b', { parent: 's3', x: 72, y: 1000, w: 936, o: 0, html: '<div class="h3">Read the badge,<br>not just the number.</div>' });
appear('s3_b', b(22), { dy: 30 }); cue(b(22), 'pop');
shotOut('s3', b(28) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(28), { lines: ['Scores with', '<span class="g">their confidence.</span>'], sub: 'Every Smart Money score sits next to its badge.',
  visual: { asset: 'sm_rows_678', w: 680 }, note: 'Screen from 23 Sep 2026 · live data changes' });
cue(b(28) + 0.4, 'sparkle');
cue(b(36), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Same score.', '<span class="g">Not the same</span>', 'thing.'], hY: 400, cls: 'h1', hCss: 'font-size:128px',
  extra: `<div style="position:absolute;left:60px;top:900px;width:460px;height:420px;border-radius:34px;background:#0f1816;border:3px solid #2a3935;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="bigno" style="font-size:170px">31</div><div class="mono" style="font-size:30px;color:#8a9a94;margin-top:8px">ESTIMATED</div></div>
  <div style="position:absolute;left:560px;top:900px;width:460px;height:420px;border-radius:34px;background:rgba(23,181,138,0.12);border:3px solid #22d3a0;display:flex;flex-direction:column;align-items:center;justify-content:center"><div class="bigno" style="font-size:170px">31</div><div class="mono" style="font-size:30px;color:#22d3a0;margin-top:8px">HIGH CONFIDENCE</div></div>
  <div class="src" style="position:absolute;left:76px;top:1350px;font-size:21px">Two real rows · BFYP Smart Money leaderboard · 23 Sep 2026</div>` });
