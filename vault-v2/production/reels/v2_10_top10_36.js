/* V2-10 — "500 companies. 36% in 10 lines." */
R.setup({ dur: 21.0, bpm: 118 });
const b = B;
music({ style: 'minimal', bpm: 118, key: 'E', mode: 'minor', prog: ['i', 'VI', 'iv', 'VII'], seed: 1010,
  sections: [{ beat: 0, type: 'hook' }, { beat: 4, type: 'drop' }, { beat: 18, type: 'tension' }, { beat: 23, type: 'build' }, { beat: 24, type: 'drop' }, { beat: 34, type: 'cta' }],
  events: [{ type: 'stop', beat: 23, beats: 1 }, { type: 'end', beat: 41, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: 504 dots ----------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['You bought', '<span class="g">500 companies.</span>'], { parent: 's1', y: 250, cls: 'h1' });
hookSettle('s1_h');
dotGrid('s1_g', { parent: 's1', n: 504, cols: 28, size: 26, gap: 6, x: 92, y: 610, color: '#1e4136', radius: 6 });
K('s1_g', 's', [[0, 0.97, 'linear'], [0.6, 1, 'outExpo']]);
cue(0, 'impact', { size: 0.9 });
// top 10 light up
for (let i = 0; i < 10; i++) {
  const d = $(`s1_g_d${i}`);
  hook(t => { const on = t >= b(4) + i * 0.05; d.style.background = on ? '#22d3a0' : '#1e4136'; d.style.boxShadow = on ? '0 0 16px rgba(34,211,160,0.9)' : 'none'; });
}
hook(t => { const dim = t >= b(4.6); for (let i = 10; i < 504; i++) { const d = $(`s1_g_d${i}`); d.style.opacity = dim ? 0.35 : 1; } });
for (let i = 0; i < 10; i++) cue(b(4) + i * 0.05, 'tick');
mk('s1_t', { parent: 's1', x: 72, y: 1270, o: 0, html: '<div class="h2" style="font-size:88px">…<span class="g">36%</span> sits in 10 lines.</div>' });
appear('s1_t', b(4.4), { dy: 30 });
cue(b(4.4), 'hit');
mk('s1_src', { parent: 's1', x: 76, y: 1212, o: 0, html: '<div class="src" style="font-size:22px">SPY · 504 holdings · N-PORT period 30 Jun 2026</div>' });
appear('s1_src', b(1.5), { dy: 10, blur: 0 });
shotOut('s1', b(9) - 0.1, 'left', 0.3);

// S2 BARS --------------------------------------------------------------
shot('s2'); shotIn('s2', b(9), 'left', 0.35);
mk('s2_h', { parent: 's2', x: 72, y: 250, o: 0, html: '<div class="eyebrow" style="margin-bottom:18px">SPY · top 10 holdings, as filed</div><div class="h2"><span class="g" id="pct">0%</span> of the fund.</div>' });
appear('s2_h', b(9) + 0.05, { dy: 20 });
counter('pct', b(9.5), b(12), 0, 36.4, v => v.toFixed(1) + '%');
cue(b(9.5), 'ticks', { n: 16, dur: 2.2, curve: 0.6 });
const rows = [['NVDA', 58.72], ['AAPL', 51.50], ['MSFT', 33.58], ['AMZN', 28.27], ['GOOGL', 25.39], ['AVGO', 21.67], ['GOOG', 20.24], ['MU', 15.77], ['META', 14.99], ['TSLA', 14.35]];
barChart('s2_bars', rows.map(r => ({ label: r[0], v: r[1], val: '$' + r[1].toFixed(2) + 'B', hl: false })), { parent: 's2', x: 72, y: 500, w: 936, rowH: 84, labelW: 190, valW: 210, max: 60, t0: b(9.6), stagger: 0.1, fs: 40, vfs: 32 });
mk('s2_sum', { parent: 's2', x: 72, y: 1360, o: 0, html: '<div class="mono" style="font-size:30px;color:var(--sub)">$284.48B of $781.19B net assets</div>' });
appear('s2_sum', b(12), { dy: 10, blur: 0 });
// Alphabet twice
[4, 6].forEach(i => { hook(t => { const el = $(`s2_bars_bar${i}`); const on = t >= b(15); el.style.background = on ? 'linear-gradient(90deg,#f0b44a,#ffd27a)' : ''; el.style.boxShadow = on ? '0 0 26px rgba(240,180,74,0.7)' : ''; }); });
mk('s2_tw', { parent: 's2', x: 72, y: 1360, o: 0, html: '<div class="h3">Alphabet shows up <span class="amber">twice.</span></div>' });
K('s2_sum', 'o', [[b(14.8), 1, 'linear'], [b(15), 0, 'linear']]);
appear('s2_tw', b(15), { dy: 30 }); cue(b(15), 'ding', { note: 84 });
shotOut('s2', b(18) - 0.1, 'zoom', 0.25);

// S3 10 lines, 9 companies ---------------------------------------------
shot('s3'); shotIn('s3', b(18), 'zoomIn', 0.3);
statement('s3_t', '10 lines.<br><span class="g">9 companies.</span>', { parent: 's3', y: 700, cls: 'h1', css: 'font-size:150px' });
slam('s3_t', b(18)); cue(b(18), 'hit');
mk('s3_s', { parent: 's3', x: 72, y: 1080, o: 0, html: '<div class="small" style="color:#9aa7a2">GOOGL and GOOG are two share classes of Alphabet.</div>' });
appear('s3_s', b(19.5), { dy: 10, blur: 0 });
cue(b(24), 'riser', { dur: b(3) });
shotOut('s3', b(24) - 0.1, 'zoom', 0.2);

// S4 BFYP real table ---------------------------------------------------
shot('s4'); shotIn('s4', b(24), 'zoomIn', 0.4);
cue(b(24), 'impact', { size: 0.9 }); cue(b(24) + 0.05, 'ding', { note: 88 });
headline('s4_h', ['What a fund', '<span class="g">actually holds.</span>'], { parent: 's4', y: 250, cls: 'h2', eyebrow: 'On BFYP · ETF · SPY' });
wordsIn('s4_h', b(24) + 0.1, { stagger: 0.05 });
realScreen('s4_card', 'spy_page', { parent: 's4', w: 960, x: 60, y: 560 });
stamp('s4_stamp', 'spy_page', { parent: 's4', x: 60, y: 480 });
appear('s4_stamp', b(24) + 0.3, { dy: 14, blur: 0 });
screenCaption('s4_cap', 'spy_page');
K('s4_cap', 'o', [[b(25) - 0.001, 0, 'linear'], [b(25) + 0.2, 1, 'linear'], [b(33.8), 1, 'linear'], [b(34), 0, 'linear']]);
K('s4_h', 'o', [[b(25), 1, 'linear'], [b(25) + 0.2, 0, 'linear']]);
K('s4_stamp', 'o', [[b(25), 1, 'linear'], [b(25) + 0.2, 0, 'linear']]);
tour('s4_card', [
  { r: [43, 45, 437, 139], key: 'THE FUND', text: '$781.19B net assets · 30 Jun 2026', t0: b(25), t1: b(28), s: 1.6 },
  { r: REG.spy_page.top_h, key: 'AS FILED', text: '15 of 504 · % of net assets', t0: b(28), t1: b(31), s: 1.7 },
  { r: [66, 486, 870, 225], key: 'THE TOP LINES', text: 'Top 5 rows · values as filed', t0: b(31), t1: b(33.8), s: 1.22 },
], { cy: 1010, fit: 900, maxS: 1.7, callY: 330 });
shotOut('s4', b(34) - 0.12, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(34), { lines: ['See what your fund', '<span class="g">actually holds.</span>'], sub: 'Every ETF page, as filed, with its dates.',
  visual: { asset: 'spy_cards', w: 640 }, note: 'Filing data changes · screens from 23 Sep 2026' });
cue(b(34) + 0.4, 'sparkle');
cue(b(41), 'hit');

R.coverSetup = () => {
  coverDesign({ lines: ['500 companies.', '<span class="g">36%</span> in 10 lines.'], hY: 400, cls: 'h1', hCss: 'font-size:118px',
    extra: '<div id="cg" style="position:absolute;left:92px;top:760px"></div><div class="src" style="position:absolute;left:76px;top:1370px;font-size:22px">SPY · as filed · N-PORT period 30 Jun 2026 · via BFYP</div>' });
  let html = '';
  for (let i = 0; i < 504; i++) { const r = Math.floor(i / 28), c = i % 28; const on = i < 10; html += `<div style="position:absolute;left:${c * 32}px;top:${r * 32}px;width:26px;height:26px;border-radius:6px;background:${on ? '#22d3a0' : '#1e4136'};${on ? 'box-shadow:0 0 16px rgba(34,211,160,0.9)' : 'opacity:0.45'}"></div>`; }
  $('cg').innerHTML = html;
};
