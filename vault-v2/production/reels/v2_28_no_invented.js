/* V2-28 — "We won't invent a consensus." — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 88 });
const b = B;
music({ style: 'cinematic', bpm: 88, key: 'G', mode: 'minor', prog: ['i', 'iv', 'VI', 'V'], seed: 2828,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(2) / b(1)), type: 'build' }, { beat: Math.floor(VT(3) / b(1)), type: 'drop' }, { beat: Math.floor(VT(6) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK: an honest empty state ------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 250, w: 936, o: 1, html: '<div class="h1" style="font-size:124px">No data?<br>Then show <span class="g">nothing.</span></div>' });
karaoke('s1_t', VT(0), VE(0), { dimStart: true });
mk('s1_box', { parent: 's1', x: 90, y: 700, w: 900, o: 1, html: `<div style="position:relative;width:900px;height:420px;border-radius:32px;border:3px dashed #2f413c;background:rgba(15,24,22,0.6);display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div class="mono" style="font-size:28px;letter-spacing:.2em;color:#6c7874">CONSENSUS</div>
  <div class="bigno" id="s1_dash" style="font-size:170px;color:#3a4b46;margin-top:6px">—</div>
  <div class="mono" style="font-size:24px;color:#6c7874">no data · nothing to show</div></div>` });
K('s1_box', 's', [[0, 0.96, 'linear'], [0.5, 1, 'outExpo']]);
hook(t => { $('s1_dash').style.opacity = (0.55 + 0.45 * Math.abs(Math.sin(t * 2.2))).toFixed(3); });
cue(0, 'impact', { size: 0.8 });
shotOut('s1', VT(1) - 0.12, 'left', 0.28);

// S2 THE GUESS (illustration) ---------------------------------------------------
shot('s2'); shotIn('s2', VT(1) - 0.1, 'left', 0.3);
mk('s2_t', { parent: 's2', x: 72, y: 250, w: 936, o: 1, html: '<div class="h2" style="font-size:88px">A guess dressed up as data is <span class="red">worse than a blank.</span></div>' });
karaoke('s2_t', VT(1), VE(1));
mk('s2_g', { parent: 's2', x: 90, y: 720, w: 900, o: 0, origin: '50% 50%', html: `<div style="position:relative;width:900px;height:420px;border-radius:32px;background:#101a17;border:3px solid #26302d;display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div class="mono" style="font-size:28px;letter-spacing:.2em;color:#8a9a94">"CONSENSUS"</div>
  <div class="bigno g" style="font-size:170px;margin-top:6px">87%</div>
  <div class="mono" style="font-size:26px;color:#22d3a0">BULLISH · "HIGH CONVICTION"</div></div>` });
popIn('s2_g', VT(1) + 0.4, { from: 0.8, ease: 'outBackSoft' });
stampLabel('s2_stamp', 'MADE UP', 330, 860, { parent: 's2', rot: -9 });
stampIn('s2_stamp', VE(1) - 0.5);
mk('s2_ill', { parent: 's2', x: 76, y: 1180, o: 0, html: '<div class="src" style="font-size:21px">Invented number · illustration of what not to do</div>' });
appear('s2_ill', VT(1) + 0.6, { dy: 6, blur: 0 });
shotOut('s2', VT(2) - 0.12, 'zoom', 0.22);

// S3 BFYP Smart Money page -------------------------------------------------------
shot('s3'); shotIn('s3', VT(2) - 0.1, 'zoomIn', 0.4);
cue(VT(2), 'ding', { note: 86 });
mk('s3_t', { parent: 's3', x: 72, y: 250, w: 936, o: 1, html: '<div class="eyebrow" style="margin-bottom:18px">On BFYP · Smart Money</div><div class="h2">The Smart Money page puts it <span class="g">plainly:</span></div>' });
karaoke('s3_t', VT(2), VE(2));
realScreen('s3_card', 'sm_page', { parent: 's3', w: 960, x: 60, y: 560 });
appear('s3_card', VT(2) + 0.2, { dy: 60 });
K('s3_t', 'o', [[VT(3) - 0.1, 1, 'linear'], [VT(3) + 0.1, 0, 'linear']]);
tour('s3_card', [{ r: [370, 144, 586, 30], t0: VT(3) - 0.05, t1: VE(3) + 0.2, s: 1.75, move: 0.4 }], { cy: 900, fit: 900, maxS: 1.8 });
mk('s3_qbg', { parent: 'fx', x: 0, y: 1010, w: 1080, h: 420, o: 0, style: { background: 'linear-gradient(180deg, rgba(6,11,10,0) 0%, rgba(6,11,10,0.88) 18%, rgba(6,11,10,0.88) 82%, rgba(6,11,10,0) 100%)' } });
K('s3_qbg', 'o', [[VT(3) - 0.1, 0, 'linear'], [VT(3) + 0.1, 1, 'linear'], [VE(3) + 0.2, 1, 'linear'], [VE(3) + 0.4, 0, 'linear']]);
mk('s3_q', { parent: 'fx', x: 72, y: 1060, w: 936, o: 1, html: '<div class="h2" style="font-size:66px;line-height:1.14;text-shadow:0 6px 30px rgba(0,0,0,0.9)">“When no scored wallet was active, we say so <span class="g">instead of inventing a consensus.</span>”</div>' });
karaoke('s3_q', VT(3), VE(3));
K('s3_q', 'o', [[0, 1, 'linear'], [VE(3) + 0.2, 1, 'linear'], [VE(3) + 0.4, 0, 'linear']]);
mk('s3_src', { parent: 'fx', x: 72, y: 330, o: 0, html: `<div class="capline"><b>●</b> Verbatim · ${capText('sm_page')}</div>` });
K('s3_src', 'o', [[VT(3), 0, 'linear'], [VT(3) + 0.2, 1, 'linear'], [VE(3) + 0.2, 1, 'linear'], [VE(3) + 0.4, 0, 'linear']]);
shotOut('s3', VT(4) - 0.1, 'left', 0.3);

// S4 BFYP Today note ---------------------------------------------------------------
shot('s4'); shotIn('s4', VT(4) - 0.1, 'left', 0.3);
realScreen('s4_card', 'today_cats', { parent: 's4', w: 900, x: 90, y: 560 });
tour('s4_card', [{ r: REG.today_cats.none, key: 'ON BFYP · TODAY', text: 'Empty groups aren’t padded', t0: VT(4) + 0.1, t1: VE(4) + 0.25, s: 1.25, move: 0.35 }], { cy: 950, fit: 900, maxS: 1.3, callY: 330 });
subtitles([{ t0: VT(4), t1: VE(4), html: 'On Today, a group with none in it <span class="g">is not shown.</span>' }], { y: 1290, fs: 48 });
screenCaption('s4_cap', 'today_cats');
K('s4_cap', 'o', [[VT(4), 0, 'linear'], [VT(4) + 0.2, 1, 'linear'], [VT(5) - 0.2, 1, 'linear'], [VT(5), 0, 'linear']]);
shotOut('s4', VT(5) - 0.12, 'zoom', 0.22);

// S5 EMPTY IS AN ANSWER ------------------------------------------------------------
shot('s5'); shotIn('s5', VT(5) - 0.1, 'zoomIn', 0.3);
mk('s5_t', { parent: 's5', x: 72, y: 700, w: 936, o: 1, html: '<div class="h1" style="font-size:150px">Empty is<br>an <span class="g">answer.</span></div>' });
karaoke('s5_t', VT(5), VE(5));
cue(VT(5), 'hit');
shotOut('s5', VT(6) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(6) - 0.1, { lines: ['Data that', '<span class="g">doesn’t pretend.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'today_cats', w: 620 }, note: 'Screens from 23 Sep 2026 · AI voice' });
cue(VT(6) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['We won’t', 'invent a', '<span class="g">consensus.</span>'], hY: 400, cls: 'h1', hCss: 'font-size:132px',
  extra: `<div style="position:absolute;left:90px;top:960px;width:900px;height:360px;border-radius:32px;border:3px dashed #2f413c;background:rgba(15,24,22,0.6);display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div class="mono" style="font-size:28px;letter-spacing:.2em;color:#6c7874">CONSENSUS</div><div class="bigno" style="font-size:150px;color:#3a4b46">—</div><div class="mono" style="font-size:24px;color:#6c7874">no data · nothing to show</div></div>` });
