/* V2-17 — "$0. Here's everything it gets you." (speed-run) */
R.setup({ dur: 20.4, bpm: 150 });
const b = B;
music({ style: 'futurebass', bpm: 150, key: 'E', mode: 'major', prog: ['I', 'V', 'vi', 'IV'], seed: 1717,
  sections: [{ beat: 0, type: 'hook' }, { beat: 6, type: 'drop' }, { beat: 30, type: 'tension' }, { beat: 39, type: 'build' }, { beat: 40, type: 'cta' }],
  events: [{ type: 'stop', beat: 39, beats: 1 }, { type: 'end', beat: 51, tail: 0.35 }] });
progressBar(); bgLife();

// S1 HOOK ------------------------------------------------------------
shot('s1'); shotIn('s1', 0, 'cut');
mk('s1_n', { parent: 's1', x: 40, y: 330, o: 1, html: '<div class="bigno g" style="font-size:520px;text-shadow:0 0 90px rgba(23,181,138,0.5)">$0</div>' });
K('s1_n', 's', [[0, 1.12, 'linear'], [0.5, 1, 'outExpo']]);
mk('s1_t', { parent: 's1', x: 72, y: 900, o: 1, html: '<div class="h1" style="font-size:108px">Here’s everything<br>it gets you.</div>' });
cue(0, 'impact', { size: 1.0 }); cue(0.05, 'sparkle');
shotOut('s1', b(6) - 0.08, 'up', 0.25);

// S2 CHECKLIST SPEED-RUN (verbatim from the pricing page) -------------------
const ITEMS = ['Dashboard & live market overview', 'Whale activity feed', 'Smart Money leaderboard', 'Token, stock & ETF research pages', '3 watchlist entries',
  '3 alert rules · 10 whale alerts/month', '52 AI credits/month (=\u00a07\u00a0reports)', 'AI Research: 2–172 credits/question by depth', 'CSV export preview (100 rows)', 'Community support'];
shot('s2'); shotIn('s2', b(6), 'up', 0.3);
mk('s2_eb', { parent: 's2', x: 72, y: 250, o: 1, html: '<div class="eyebrow">BFYP free plan · $0/month</div>' });
mk('s2_ct', { parent: 's2', x: 760, y: 236, o: 1, html: '<div class="mono" id="s2_cnt" style="font-size:44px;color:var(--green2);font-weight:600">00/10</div>' });
[0, 1].forEach(pg => {
  const pid = `s2_p${pg}`;
  let html = '';
  for (let j = 0; j < 5; j++) {
    const i = pg * 5 + j;
    html += `<div id="it${i}" class="chk" style="position:absolute;left:0;top:${j * 196}px;width:930px"><div class="ic">${CHECK}</div><div style="font-size:58px;font-weight:750;letter-spacing:-0.02em;line-height:1.08">${ITEMS[i]}</div></div>`;
  }
  mk(pid, { parent: 's2', x: 76, y: 380, w: 930, o: 1, html });
  for (let j = 0; j < 5; j++) {
    const i = pg * 5 + j;
    reg(`it${i}`);
    const ti = b(6.6 + i * 2.2);
    K(`it${i}`, 'o', [[ti - 0.001, 0, 'linear'], [ti, 0, 'linear'], [ti + 0.06, 1, 'linear']]);
    K(`it${i}`, 'x', [[ti, 60, 'linear'], [ti + 0.3, 0, 'outExpo']]);
    cue(ti, 'tick'); cue(ti + 0.02, 'pop');
  }
});
hook(t => { const n = ITEMS.filter((_, i) => t >= b(6.6 + i * 2.2)).length; $('s2_cnt').textContent = String(n).padStart(2, '0') + '/10'; });
K('s2_p0', 'y', [[b(6.6 + 5 * 2.2) - 0.25, 380, 'linear'], [b(6.6 + 5 * 2.2) - 0.02, -1400, 'inExpo']]);
K('s2_p0', 'o', [[b(6.6 + 5 * 2.2) - 0.12, 1, 'linear'], [b(6.6 + 5 * 2.2) - 0.02, 0, 'linear']]);
K('s2_p1', 'y', [[0, 380, 'linear']]);
cue(b(6.6 + 5 * 2.2) - 0.2, 'whoosh', { dur: 0.3 });
shotOut('s2', b(30) - 0.1, 'zoom', 0.25);

// S3 PROOF: the real pricing screens -----------------------------------------
shot('s3'); shotIn('s3', b(30), 'zoomIn', 0.35);
headline('s3_h', ['Straight from', 'the <span class="g">pricing page.</span>'], { parent: 's3', y: 250, cls: 'h2' });
wordsIn('s3_h', b(30) + 0.05, { stagger: 0.05 });
realScreen('s3_a', 'free_card', { parent: 's3', w: 640, x: 72, y: 640 });
realScreen('s3_b', 'free_list', { parent: 's3', w: 560, x: 450, y: 760 });
stamp('s3_st', 'free_list', { parent: 's3', x: 72, y: 560 });
appear('s3_a', b(30.5), { dy: 60 }); appear('s3_b', b(31.5), { dy: 60 }); appear('s3_st', b(31), { dy: 10, blur: 0 });
cue(b(30.5), 'whoosh', { dur: 0.3 }); cue(b(31.5), 'whoosh', { dur: 0.3 });
K('s3_b', 's', [[b(31.5), 1, 'linear'], [b(40), 1.04, 'linear']]);
cue(b(40), 'riser', { dur: b(3) });
shotOut('s3', b(40) - 0.1, 'zoom', 0.22);

// CTA -----------------------------------------------------------------
ctaCard(b(40), { lines: ['Create a', '<span class="g">free account.</span>'], sub: 'Ten things. Zero dollars.', button: 'betterforyourpocket.com',
  visual: { asset: 'free_card', w: 700 }, note: 'Plan details as of 23 Sep 2026 · may change' });
cue(b(40) + 0.4, 'sparkle');
cue(b(51), 'hit');

R.coverSetup = () => coverDesign({ lines: [''], hY: 380, cls: 'h1',
  extra: `<div class="bigno g" style="position:absolute;left:40px;top:330px;font-size:520px;text-shadow:0 0 90px rgba(23,181,138,0.5)">$0</div>
  <div class="h1" style="position:absolute;left:72px;top:880px;font-size:108px">Here’s everything<br>it gets you.</div>
  <div class="h4" style="position:absolute;left:76px;top:1180px">10 things, <span class="g">verbatim from pricing →</span></div>` });
