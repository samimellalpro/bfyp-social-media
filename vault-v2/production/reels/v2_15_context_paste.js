/* V2-15 — "Stop pasting tickers into chatbots." */
R.setup({ dur: 20.6, bpm: 115 });
const b = B;
music({ style: 'amapiano', bpm: 115, key: 'Eb', mode: 'minor', prog: ['i7', 'VI', 'iv7', 'v'], seed: 1515,
  sections: [{ beat: 0, type: 'tension' }, { beat: 8, type: 'hook' }, { beat: 14, type: 'build' }, { beat: 16, type: 'drop' }, { beat: 31, type: 'cta' }],
  events: [{ type: 'stop', beat: 15, beats: 1 }, { type: 'end', beat: 39, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: generic chat box, typing a wall of context -------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['Copy. Paste.', '<span class="g">Explain.</span> Repeat.'], { parent: 's1', y: 230, cls: 'h1', css: 'font-size:118px' });
hookSettle('s1_h');
mk('s1_chat', { parent: 's1', x: 70, y: 620, w: 940, o: 1, html: `
  <div style="position:relative;width:940px;border-radius:30px;background:#0f1412;border:2px solid #26302d;box-shadow:0 40px 120px rgba(0,0,0,0.6);padding:34px 36px 30px">
    <div class="mono" style="font-size:22px;letter-spacing:.14em;color:#6c7874">GENERIC AI CHAT · ILLUSTRATION</div>
    <div id="s1_type" style="margin-top:20px;font-weight:600;font-size:44px;line-height:1.24;color:#dfe7e3;min-height:330px"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-top:18px">
      <div class="mono" style="font-size:22px;color:#6c7874">no context · starts from zero</div>
      <div style="width:66px;height:66px;border-radius:50%;background:#26302d;display:flex;align-items:center;justify-content:center;color:#9aa7a2;font-size:34px">↑</div></div></div>` });
K('s1_chat', 's', [[0, 0.96, 'linear'], [0.45, 1, 'outBack']]);
typer('s1_type', "Here's SPY's latest filing, its top holdings, the period it covers, and what changed today… OK, now: what are the risks?", 0.35, 30, { caretOff: b(8) });
cue(0, 'impact', { size: 0.8 });
shotOut('s1', b(8) - 0.1, 'left', 0.3);

// S2 WHY IT HURTS -----------------------------------------------------
shot('s2'); shotIn('s2', b(8), 'left', 0.35);
mk('s2_a', { parent: 's2', x: 72, y: 480, w: 936, o: 0, html: '<div class="h1" style="font-size:112px">Your chatbot<br>doesn’t know<br>what you’re<br><span class="red">looking at.</span></div>' });
slam('s2_a', b(8)); cue(b(8), 'hit');
mk('s2_b', { parent: 's2', x: 72, y: 1000, w: 936, o: 0, html: '<div class="h3 m">So you rebuild the context. Every time.</div>' });
appear('s2_b', b(11), { dy: 20 });
cue(b(16), 'riser', { dur: b(3) });
shotOut('s2', b(16) - 0.1, 'zoom', 0.2);

// S3 BFYP Ask about this ---------------------------------------------
shot('s3'); shotIn('s3', b(16), 'zoomIn', 0.4);
cue(b(16), 'impact', { size: 0.9 }); cue(b(16) + 0.05, 'ding', { note: 87 });
headline('s3_h', ['On BFYP, the asset', '<span class="g">comes with you.</span>'], { parent: 's3', y: 250, cls: 'h2', eyebrow: 'On BFYP · ETF · SPY page' });
wordsIn('s3_h', b(16) + 0.1, { stagger: 0.05 });
realScreen('s3_card', 'ai_ask', { parent: 's3', w: 900, x: 90, y: 640 });
stamp('s3_stamp', 'ai_ask', { parent: 's3', x: 90, y: 560 });
appear('s3_stamp', b(16) + 0.3, { dy: 14, blur: 0 });
scanOver('s3_card', b(16) + 0.3, 0.6);
screenCaption('s3_cap', 'ai_ask');
K('s3_cap', 'o', [[b(17.5) - 0.001, 0, 'linear'], [b(17.5) + 0.2, 1, 'linear'], [b(30.8), 1, 'linear'], [b(31), 0, 'linear']]);
K('s3_h', 'o', [[b(17.5), 1, 'linear'], [b(17.5) + 0.2, 0, 'linear']]);
K('s3_stamp', 'o', [[b(17.5), 1, 'linear'], [b(17.5) + 0.2, 0, 'linear']]);
tour('s3_card', [
  { r: REG.ai_ask.context, key: 'ALREADY IN CONTEXT', text: 'Opens with SPY loaded', t0: b(17.5), t1: b(21.5), s: 1.4 },
  { r: REG.ai_ask.qs, key: 'SUGGESTED', text: 'Questions about this asset', t0: b(21.5), t1: b(25.5), s: 1.35 },
  { r: REG.ai_ask.nothing, key: 'YOUR CALL', text: 'Nothing sent, no credits, until you ask', t0: b(25.5), t1: b(30.8), s: 1.35 },
], { cy: 1010, fit: 860, maxS: 1.45, callY: 330 });
shotOut('s3', b(31) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(31), { lines: ['The asset', '<span class="g">comes with you.</span>'], sub: 'Open AI Research from any fund or company page.',
  visual: { asset: 'ai_ask', w: 700 }, note: 'Screen from 23 Sep 2026 · product may change' });
cue(b(31) + 0.4, 'sparkle');
cue(b(39), 'hit');

R.coverSetup = () => coverDesign({ lines: ['Stop pasting', 'tickers into', '<span class="g">chatbots.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:120px', asset: 'ai_ask', crop: [30, 30, 680, 200], visW: 900, visY: 900,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1250px">The asset <span class="g">comes with you →</span></div>' });
