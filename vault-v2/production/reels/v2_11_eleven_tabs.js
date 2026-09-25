/* V2-11 — "POV: 11 tabs to check one ticker." */
R.setup({ dur: 21.0, bpm: 128 });
const b = B;
music({ style: 'techhouse', bpm: 128, key: 'G', mode: 'minor', prog: ['i', 'VI', 'VII', 'v'], seed: 1111,
  sections: [{ beat: 0, type: 'tension' }, { beat: 6, type: 'build' }, { beat: 10, type: 'drop' }, { beat: 30, type: 'break' }, { beat: 34, type: 'cta' }],
  events: [{ type: 'stop', beat: 9.5, beats: 0.5 }, { type: 'end', beat: 44.5, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK: tab chaos ---------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
headline('s1_h', ['POV: 11 tabs', 'to check', '<span class="g">one ticker.</span>'], { parent: 's1', y: 210, cls: 'h1', css: 'font-size:112px' });
hookSettle('s1_h');
const TABS = ['Price chart', 'X search: $XYZ', 'Forum thread', 'EDGAR search', 'Block explorer', 'News site', 'AI chatbot', 'Discord', 'Spreadsheet', 'Earnings PDF', 'Another chart'];
const COLS = ['#3b4b8a', '#2a2a2a', '#8a4b2a', '#2a5a8a', '#3a6a4a', '#7a2a3a', '#5a3a8a', '#4a4aa0', '#2a7a3a', '#8a2a2a', '#3b4b8a'];
TABS.forEach((t, i) => {
  const id = `tab${i}`;
  const x = 60 + (i % 3) * 22 + (i * 37) % 180, y = 600 + i * 70;
  mk(id, { parent: 's1', x, y, o: 0, origin: '0 100%', html: `<div class="tab" style="position:relative;width:${520 + (i * 53) % 300}px"><div class="fav" style="background:${COLS[i]}"></div>${t}<span style="margin-left:auto;color:#6c7874">✕</span></div>` });
  const ti = i < 1 ? 0 : b(0.5 + i * 0.5);
  K(id, 'o', [[ti - 0.001, 0, 'linear'], [ti, 1, 'linear']]);
  K(id, 'y', [[ti, y + 40, 'linear'], [ti + 0.25, y, 'outExpo']]);
  K(id, 'r', [[ti, (i % 2 ? 3 : -3), 'linear'], [ti + 0.3, (i % 2 ? 1 : -1) * (i % 4) * 0.6, 'outBack']]);
  if (i > 0) cue(ti, 'click', { f: 2800 + i * 90 });
});
cue(0, 'impact', { size: 0.8 });
mk('s1_q', { parent: 's1', x: 72, y: 1400, w: 936, o: 0, html: '<div class="h3">…and you still don’t know <span class="red">what changed.</span></div>' });
appear('s1_q', b(6.2), { dy: 30 }); cue(b(6.2), 'wrong');
camShake(b(6.2), 0.3, 10);
// collapse all tabs into one point
TABS.forEach((t, i) => {
  const id = `tab${i}`;
  K(id, 's', [[b(9.4), 1, 'linear'], [b(10), 0.1, 'inExpo']]);
  K(id, 'x', [[b(9.4), R.els[id].base.x, 'linear'], [b(10), 480, 'inExpo']]);
  K(id, 'o', [[b(9.8), 1, 'linear'], [b(10), 0, 'linear']]);
});
cue(b(10), 'riser', { dur: b(3) });
shotOut('s1', b(10), 'cut');

// S2 ONE WORKFLOW ----------------------------------------------------
shot('s2'); shotIn('s2', b(10), 'zoomIn', 0.3);
statement('s2_t', 'One<br><span class="g">workflow.</span>', { parent: 's2', y: 700, cls: 'h1', css: 'font-size:170px' });
slam('s2_t', b(10)); cue(b(10), 'impact', { size: 1.0 }); cue(b(10) + 0.02, 'ding', { note: 86 }); flash(b(10), { peak: 0.25, dur: 0.2, color: '#22d3a0' });
shotOut('s2', b(12) - 0.08, 'zoom', 0.2);

// S3 MONTAGE ---------------------------------------------------------
const STEPS = [
  { a: 'today_cats', n: '01', k: 'WHAT CHANGED', h: 'Today', w: 820 },
  { a: 'whale_card', n: '02', k: 'WHO MOVED', h: 'Whale Activity', w: 900 },
  { a: 'sm_rows_678', n: '03', k: 'WHO HAS A RECORD', h: 'Smart Money', w: 860 },
  { a: 'nvda_filings4', n: '04', k: 'WHAT WAS FILED', h: 'Stock pages', w: 900 },
  { a: 'ai_prompt', n: '05', k: 'ASK, WITH RECEIPTS', h: 'AI Research', w: 820 },
];
STEPS.forEach((st, i) => {
  const t0 = b(12 + i * 3.6), t1 = b(12 + (i + 1) * 3.6);
  const sid = `m${i}`;
  shot(sid); shotIn(sid, t0, i % 2 ? 'left' : 'right', 0.32);
  mk(`${sid}_n`, { parent: sid, x: 72, y: 250, o: 1, html: `<div class="mono" style="font-size:34px;letter-spacing:.2em;color:var(--green2)">${st.n} / 05</div>` });
  mk(`${sid}_k`, { parent: sid, x: 72, y: 310, o: 1, html: `<div class="h2">${st.k.charAt(0) + st.k.slice(1).toLowerCase()}</div>` });
  mk(`${sid}_p`, { parent: sid, x: 72, y: 420, o: 1, html: `<div class="h4 g">${st.h}</div>` });
  const meta = window.ASSET_CATALOG[st.a];
  let w = st.w; const maxH = 800; if (meta.h * w / meta.w > maxH) w = maxH * meta.w / meta.h;
  realScreen(`${sid}_c`, st.a, { parent: sid, w, x: (1080 - w) / 2, y: 600 });
  stamp(`${sid}_s`, st.a, { parent: sid, x: (1080 - w) / 2, y: 530, size: 20, pad: '8px 16px', text: capText(st.a, false) });
  K(`${sid}_c`, 's', [[t0, 0.96, 'linear'], [t1, 1.03, 'linear']]);
  cue(t0, 'whoosh', { dur: 0.3 }); cue(t0 + 0.05, 'hit'); cue(t0 + 0.02, 'ding', { note: [79, 82, 84, 86, 89][i], db: -2 });
  if (i < STEPS.length - 1) shotOut(sid, t1 - 0.02, i % 2 ? 'left' : 'right', 0.3);
  else shotOut(sid, t1 - 0.02, 'zoom', 0.25);
});

// S4 SOURCES ATTACHED ------------------------------------------------
shot('s4'); shotIn('s4', b(30), 'zoomIn', 0.3);
statement('s4_t', 'Sources attached.<br><span class="g">Every step.</span>', { parent: 's4', y: 740, cls: 'h1', css: 'font-size:118px' });
slam('s4_t', b(30)); cue(b(30), 'hit'); cue(b(30) + 0.05, 'chime', { notes: [86, 91] });
shotOut('s4', b(34) - 0.1, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(34), { lines: ['Close', '<span class="g">10 tabs.</span>'], sub: 'Today, whales, Smart Money, filings and AI in one place.',
  visual: { asset: 'today_cats', w: 640 }, note: 'Free plan available · screens from 23 Sep 2026' });
cue(b(34) + 0.4, 'sparkle');
cue(b(44.5), 'hit');

R.coverSetup = () => {
  coverDesign({ lines: ['POV: 11 tabs', 'to check', '<span class="g">one ticker.</span>'], hY: 380, cls: 'h1', hCss: 'font-size:112px', extra: '<div id="ctabs"></div>' });
  let html = '';
  TABS.forEach((t, i) => { const x = 60 + (i % 3) * 22 + (i * 37) % 180, y = 760 + i * 66; html += `<div class="tab" style="position:absolute;left:${x}px;top:${y}px;width:${520 + (i * 53) % 300}px;transform:rotate(${(i % 2 ? 1 : -1) * (i % 4) * 0.6}deg)"><div class="fav" style="background:${COLS[i]}"></div>${t}<span style="margin-left:auto;color:#6c7874">✕</span></div>`; });
  $('ctabs').innerHTML = html;
};
