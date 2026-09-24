/* V2-18 — "$1.67 trillion. Whose?" — VOICE-LED (fallback voice BFYP-K1) */
const V = window.VO;
R.setup({ dur: Math.ceil((V.dur + 0.95) * 30) / 30, bpm: 120 });
const b = B;
music({ style: 'minimal', bpm: 120, key: 'D', mode: 'minor', prog: ['i', 'VI', 'iv', 'VII'], seed: 1818,
  sections: [{ beat: 0, type: 'tension' }, { beat: Math.floor(VT(2) / b(1)), type: 'drop' }, { beat: Math.floor(VT(5) / b(1)), type: 'drop' }, { beat: Math.floor(VT(6) / b(1)), type: 'cta' }],
  events: [{ type: 'end', t: R.dur - 0.25, tail: 0.25 }], level: -17.5 });
progressBar(); bgLife();

// S1 HOOK --------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_t', { parent: 's1', x: 72, y: 300, o: 1, html: '<div class="h1" style="font-size:160px">VOO:</div>' });
mk('s1_n', { parent: 's1', x: 60, y: 500, o: 1, html: '<div class="bigno g" id="tn" style="font-size:250px">$0.00T</div>' });
counter('tn', 0.15, VE(0) - 0.4, 0, 1.67, v => '$' + v.toFixed(2) + 'T');
cue(0.15, 'ticks', { n: 18, dur: VE(0) - 0.6, curve: 0.55 });
mk('s1_q', { parent: 's1', x: 880, y: 500, o: 0, html: '<div class="bigno" style="font-size:250px">?</div>' });
popIn('s1_q', VE(0) - 0.35, { from: 0.3 });
cue(0, 'impact', { size: 0.9 });
mk('s1_no', { parent: 's1', x: 72, y: 860, o: 1, html: '<div class="h1" style="font-size:140px">Not<br><span class="red">exactly.</span></div>' });
karaoke('s1_no', VT(1), VE(1));
cue(VT(1), 'wrong');
shotOut('s1', VT(2) - 0.12, 'left', 0.3);

// S2 SHARE CLASS -------------------------------------------------------
shot('s2'); shotIn('s2', VT(2) - 0.1, 'left', 0.35);
mk('s2_t', { parent: 's2', x: 72, y: 250, w: 936, o: 1, html: '<div class="h2" style="font-size:86px">VOO is <span class="g">one share class</span> of the Vanguard 500 Index Fund.</div>' });
karaoke('s2_t', VT(2), VE(2));
// fund box with 4 share classes (not to scale)
mk('s2_fund', { parent: 's2', x: 72, y: 760, w: 936, o: 0, html: `
  <div style="position:relative;width:936px;border:3px solid #2a3935;border-radius:34px;padding:34px;background:rgba(15,24,22,0.8)">
    <div class="mono" style="font-size:26px;letter-spacing:.16em;color:#9aa7a2">VANGUARD 500 INDEX FUND · ONE PORTFOLIO</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:26px">
      <div id="sc0" class="opt" style="position:relative;width:auto;height:120px;font-size:40px">Investor</div>
      <div id="sc1" class="opt" style="position:relative;width:auto;height:120px;font-size:40px">ETF · <span class="g">VOO</span></div>
      <div id="sc2" class="opt" style="position:relative;width:auto;height:120px;font-size:40px">Admiral</div>
      <div id="sc3" class="opt" style="position:relative;width:auto;height:120px;font-size:40px">Institutional Select</div>
    </div>
    <div class="src" style="margin-top:22px;font-size:20px">Share classes per the fund’s 2026 semi-annual report<br>Not to scale</div></div>` });
appear('s2_fund', VT(3) - 0.2, { dy: 60 });
[0, 1, 2, 3].forEach(i => { reg(`sc${i}`); const t = VT(3) + i * 0.3; K(`sc${i}`, 's', [[t, 0.7, 'linear'], [t + 0.3, 1, 'outBack']]); cue(t, 'pop'); });
hook(t => { const el = $('sc1'); const on = t >= VT(2) + 0.9; el.className = 'opt' + (on ? ' right' : ''); });
mk('s2_src', { parent: 's2', x: 76, y: 1400, o: 0, html: '<div class="src" style="font-size:21px">Vanguard S&amp;P 500 ETF prospectus<br>Vanguard 500 Index Fund semi-annual report (2026)</div>' });
appear('s2_src', VT(2) + 0.6, { dy: 10, blur: 0 });
shotOut('s2', VT(4) - 0.12, 'zoom', 0.25);

// S3 BFYP VOO card ------------------------------------------------------
shot('s3'); shotIn('s3', VT(4) - 0.1, 'zoomIn', 0.4);
cue(VT(4), 'impact', { size: 0.85 }); cue(VT(4) + 0.05, 'ding', { note: 86 });
realScreen('s3_card', 'voo_cards', { parent: 's3', w: 860, x: 110, y: 640 });
screenCaption('s3_cap', 'voo_cards');
K('s3_cap', 'o', [[VT(4) - 0.001, 0, 'linear'], [VT(4) + 0.2, 1, 'linear'], [VT(6) - 0.2, 1, 'linear'], [VT(6), 0, 'linear']]);
tour('s3_card', [
  { r: REG.voo_cards.na_val, key: 'FUND NET ASSETS', text: '$1,671.23B · 30 Jun 2026', t0: VT(4) + 0.1, t1: VT(4) + (VE(4) - VT(4)) * 0.55, s: 1.9 },
  { r: REG.voo_cards.scope, key: 'WHAT IT COVERS', text: 'Whole fund, all share classes', t0: VT(4) + (VE(4) - VT(4)) * 0.55, t1: VT(5) - 0.05, s: 1.9 },
  { r: [0, 0, 736, 624], key: 'ON BFYP', text: 'The scope, next to the number', t0: VT(5) - 0.05, t1: VT(6) - 0.2, s: 1.0 },
], { cy: 1010, fit: 800, maxS: 2.0, callY: 330 });
subtitles([{ t0: VT(4), t1: VE(4), html: 'The $1.67 trillion covers the <span class="g">whole fund.</span>' }, { t0: VT(5), t1: VE(5), html: 'BFYP labels what <span class="g">every number covers.</span>' }], { y: 1290, fs: 46 });
shotOut('s3', VT(6) - 0.15, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(VT(6) - 0.1, { lines: ['Know what a', '<span class="g">number covers.</span>'], sub: 'Free at betterforyourpocket.com',
  visual: { asset: 'voo_cards', w: 560 }, note: 'Screen from 23 Sep 2026 · AI voice' });
cue(VT(6) + 0.3, 'sparkle');

R.coverSetup = () => coverDesign({ lines: ['<span class="g">$1.67 trillion.</span>', 'Whose?'], hY: 420, cls: 'h1', hCss: 'font-size:130px', asset: 'voo_cards', crop: [6, 58, 349, 251], visW: 560, visY: 820,
  extra: '<div class="h4" style="position:absolute;left:76px;top:1420px">VOO is <span class="g">one share class →</span></div>' });
