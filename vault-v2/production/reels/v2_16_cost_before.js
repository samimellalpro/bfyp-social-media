/* V2-16 — "Know the cost before you ask." */
R.setup({ dur: 20.4, bpm: 110 });
const b = B;
music({ style: 'synthwave', bpm: 110, key: 'F', mode: 'minor', prog: ['i', 'VI', 'III', 'VII'], seed: 1616,
  sections: [{ beat: 0, type: 'hook' }, { beat: 6, type: 'tension' }, { beat: 11, type: 'build' }, { beat: 12, type: 'drop' }, { beat: 30, type: 'cta' }],
  events: [{ type: 'stop', beat: 11, beats: 1 }, { type: 'end', beat: 37, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: receipt with unknown total ---------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['What did that', 'AI answer', '<span class="red">actually cost?</span>'], { parent: 's1', y: 230, cls: 'h1', css: 'font-size:112px' });
hookSettle('s1_h');
mk('s1_rc', { parent: 's1', x: 250, y: 660, w: 580, o: 1, origin: '50% 0%', html: `
  <div style="position:relative;width:580px;background:#eef1ef;color:#131816;border-radius:14px 14px 0 0;padding:34px 38px 50px;box-shadow:0 50px 140px rgba(0,0,0,0.7);font-family:'Geist Mono',monospace">
    <div style="text-align:center;font-size:26px;letter-spacing:.2em">RECEIPT · ILLUSTRATION</div>
    <div style="border-top:3px dashed #9aa5a1;margin:22px 0"></div>
    <div style="display:flex;justify-content:space-between;font-size:30px;margin:10px 0"><span>1 × AI answer</span><span>???</span></div>
    <div style="display:flex;justify-content:space-between;font-size:30px;margin:10px 0"><span>context</span><span>???</span></div>
    <div style="display:flex;justify-content:space-between;font-size:30px;margin:10px 0"><span>follow-ups</span><span>???</span></div>
    <div style="border-top:3px dashed #9aa5a1;margin:22px 0"></div>
    <div style="display:flex;justify-content:space-between;font-size:40px;font-weight:700"><span>TOTAL</span><span style="color:#c93b3b">???</span></div>
  </div>
  <div style="width:580px;height:26px;background:linear-gradient(135deg,#eef1ef 50%,transparent 50%) 0 0/26px 26px,linear-gradient(225deg,#eef1ef 50%,transparent 50%) 0 0/26px 26px"></div>` });
K('s1_rc', 'sy', [[0, 0.3, 'linear'], [0.6, 1, 'outBack']]);
K('s1_rc', 'r', [[0, -2, 'linear'], [0.8, 1.5, 'outElastic']]);
cue(0, 'impact', { size: 0.8 }); cue(0.05, 'scan', { dur: 0.5 });
shotOut('s1', b(6) - 0.1, 'left', 0.3);

// S2 WHY IT HURTS -----------------------------------------------------
shot('s2'); shotIn('s2', b(6), 'left', 0.35);
statement('s2_t', 'You shouldn’t<br>find out <span class="red">after.</span>', { parent: 's2', y: 720, cls: 'h1', css: 'font-size:130px' });
slam('s2_t', b(6)); cue(b(6), 'hit');
cue(b(12), 'riser', { dur: b(3) });
shotOut('s2', b(12) - 0.1, 'zoom', 0.2);

// S3 BFYP: cost shown up front ----------------------------------------------
shot('s3'); shotIn('s3', b(12), 'zoomIn', 0.4);
cue(b(12), 'impact', { size: 0.9 }); cue(b(12) + 0.05, 'ding', { note: 86 });
headline('s3_h', ['The cost is on screen', '<span class="g">before you ask.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · AI Research' });
wordsIn('s3_h', b(12) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'ai_prompt', { parent: 's3', w: 900, x: 90, y: 640 });
stamp('s3_stamp', 'ai_prompt', { parent: 's3', x: 90, y: 560 });
appear('s3_stamp', b(12) + 0.3, { dy: 14, blur: 0 });
screenCaption('s3_cap', 'ai_prompt');
K('s3_cap', 'o', [[b(13.5) - 0.001, 0, 'linear'], [b(13.5) + 0.2, 1, 'linear'], [b(17.8), 1, 'linear'], [b(18), 0, 'linear']]);
K('s3_h', 'o', [[b(13.5), 1, 'linear'], [b(13.5) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(13.5), 1, 'linear'], [b(13.5) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: [18, 398, 752, 160], key: 'PRICE TAG', text: '36 credits per question', t0: b(13.5), t1: b(17.8), s: 1.25 },
], { cy: 1000, fit: 900, maxS: 1.3, callY: 330 });
shotOut('s3', b(18) - 0.05, 'left', 0.3);

// S4 BFYP: free plan credits ------------------------------------------------
shot('s4'); shotIn('s4', b(18), 'left', 0.35);
headline('s4_h', ['Free plan:', '<span class="g">52 AI credits a month.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · pricing' });
wordsIn('s4_h', b(18) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'free_list', { parent: 's4', w: 760, x: 160, y: 600 });
stamp('s4_stamp', 'free_list', { parent: 's4', x: 160, y: 520 });
appear('s4_stamp', b(18) + 0.3, { dy: 14, blur: 0 });
screenCaption('s4_cap', 'free_list');
K('s4_cap', 'o', [[b(19.5) - 0.001, 0, 'linear'], [b(19.5) + 0.2, 1, 'linear'], [b(29.8), 1, 'linear'], [b(30), 0, 'linear']]);
K('s4_h', 'o', [[b(19.5), 1, 'linear'], [b(19.5) + 0.2, 0, 'linear'], [b(27), 0, 'linear'], [b(27.4), 1, 'linear']]);
K('s4_stamp', 'o', [[b(19.5), 1, 'linear'], [b(19.5) + 0.2, 0, 'linear'], [b(27), 0, 'linear'], [b(27.4), 1, 'linear']]);
tour('s4_card', [
  { r: REG.free_list.i7, key: 'INCLUDED', text: '≈ 7 reports a month', t0: b(19.5), t1: b(23), s: 1.6 },
  { r: REG.free_list.i8, key: 'BY DEPTH', text: '2 to 172 credits per question', t0: b(23), t1: b(27), s: 1.5 },
], { cy: 1000, fit: 800, maxS: 1.7, callY: 330 });
shotOut('s4', b(30) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(30), { lines: ['52 free AI credits', '<span class="g">every month.</span>'], sub: 'And the cost is on screen before you ask.',
  visual: { asset: 'free_card', w: 720 }, note: 'Plan details as of 23 Sep 2026 · may change' });
cue(b(30) + 0.4, 'sparkle');
cue(b(37), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Know the cost', '<span class="g">before you ask.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:116px', asset: 'ai_prompt', crop: [10, 390, 770, 180], visW: 920, visY: 820,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1100px">AI research with the <span class="g">price tag up front →</span></div>' });
