/* BFYP Vault V2 — reusable, brand-consistent components built on motion.js */
(function () {
  const CAT = window.ASSET_CATALOG || {};
  const MON = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
  function capParts(asset) {
    const cap = (CAT[asset] || {}).captured || '';
    const d = cap.split(' ');
    const [yy, mm, dd] = (d[0] || '').split('-');
    return { day: parseInt(dd, 10), mon: MON[parseInt(mm, 10) - 1], year: yy, time: d[1] || '' };
  }
  window.capText = function (asset, long = true) {
    const c = capParts(asset);
    const meta = CAT[asset] || {};
    const lead = meta.kind === 'data' ? `BFYP ${(meta.page || '').toUpperCase()} DATA` : 'REAL SCREEN';
    return long ? `${lead} · CAPTURED ${c.day} ${c.mon} ${c.year} · ${c.time} UTC` : `CAPTURED ${c.day} ${c.mon} ${c.year} · ${c.time} UTC`;
  };

  // background life: slow grid drift + glow breathing on the beat
  window.bgLife = function (o = {}) {
    const g = $('bggrid');
    hook(t => {
      g.style.transform = `translate3d(0, ${(-(t * (o.speed || 14)) % 72).toFixed(2)}px, 0)`;
      if (o.gridO !== undefined) g.style.opacity = o.gridO;
    });
  };

  // headline block: lines = array of strings, may contain <span class="g">..</span>
  window.headline = function (id, lines, o = {}) {
    const cls = o.cls || 'h1';
    const html = (o.eyebrow ? `<div class="eyebrow" style="margin-bottom:${o.ebGap || 22}px">${o.eyebrow}</div>` : '') +
      `<div class="${cls}" style="${o.css || ''}">${lines.join('<br>')}</div>` +
      (o.sub ? `<div class="body" style="margin-top:${o.subGap || 26}px;max-width:${o.subW || 900}px">${o.sub}</div>` : '');
    return mk(id, { parent: o.parent, html, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 250 : o.y, w: o.w || 936, style: Object.assign({ textShadow: '0 10px 40px rgba(0,0,0,0.55)' }, o.style || {}), o: o.o });
  };

  window.statement = function (id, html, o = {}) {
    return mk(id, { parent: o.parent, html: `<div class="${o.cls || 'h2'}" style="text-align:${o.align || 'left'};${o.css || ''}">${html}</div>`, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 760 : o.y, w: o.w || 936, o: o.o, style: { textShadow: '0 10px 40px rgba(0,0,0,0.6)' } });
  };

  // real screen: framed crop at display width w; region coords are in asset 1x px
  window.realScreen = function (id, asset, o = {}) {
    const meta = CAT[asset] || { w: 900, h: 600 };
    const w = o.w || meta.w;
    const bs = w / meta.w;
    const h = meta.h * bs;
    const glow = o.glow === false ? '' : 'box-shadow:0 60px 160px rgba(0,0,0,0.75),0 0 0 2px rgba(23,181,138,0.30),0 0 90px rgba(23,181,138,0.12);';
    mk(id, {
      parent: o.parent, origin: '0 0', x: o.x === undefined ? (1080 - w) / 2 : o.x, y: o.y === undefined ? 700 : o.y, o: o.o,
      html: `<div style="position:relative;width:${w}px;height:${h}px;border-radius:${o.radius === undefined ? 26 : o.radius}px;overflow:hidden;background:#0b1311;${glow}">` +
        `<img src="screens/${asset}@2x.png" style="display:block;width:${w}px;height:${h}px">` +
        `<div style="position:absolute;inset:0;border-radius:inherit;background:linear-gradient(180deg,rgba(255,255,255,0.035),rgba(255,255,255,0) 30%);pointer-events:none"></div></div>`,
    });
    Object.assign(R.els[id], { bs, W: w, H: h, asset });
    return { id, bs, W: w, H: h };
  };

  // capture stamp pill
  window.stamp = function (id, asset, o = {}) {
    return mk(id, { parent: o.parent, html: `<div class="pill${o.dim ? ' dim' : ''}" style="font-size:${o.size || 23}px;padding:${o.pad || '11px 22px'}"><span class="dot"></span>${o.text || capText(asset)}</div>`, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 640 : o.y, o: o.o });
  };
  // small persistent caption line (bottom of safe area); short enough to clear the Reels right rail (x < 960)
  const SHORT_PAGE = { 'Smart Money · Scored wallet universe': 'Smart Money', 'Smart Money leaderboard': 'Smart Money' };
  window.screenCaption = function (id, asset, o = {}) {
    const meta = CAT[asset] || {};
    const page = SHORT_PAGE[meta.page] || meta.page || '';
    const c = capParts(asset);
    const lead = meta.kind === 'data' ? 'BFYP ' + page + ' data' : 'Real BFYP screen' + (page ? ' · ' + page : '');
    return mk(id, { parent: o.parent || 'fx', x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 1478 : o.y, o: 0,
      html: `<div class="capline"><b>●</b> ${lead} · ${c.day} ${c.mon} ${c.year} · ${c.time} UTC</div>` });
  };

  // focus brackets drawn inside a screen container at region [x,y,w,h] (asset px)
  window.brackets = function (id, parent, region, o = {}) {
    const bs = (R.els[parent] && R.els[parent].bs) || 1;
    const pad = o.pad === undefined ? 10 : o.pad;
    const [x, y, w, h] = [region[0] * bs - pad, region[1] * bs - pad, region[2] * bs + 2 * pad, region[3] * bs + 2 * pad];
    const c = o.color || '#22d3a0';
    const L = Math.min(o.len || 34, w / 3, h / 2);
    const sw = o.stroke || 5;
    const svg = `<svg width="${w + 20}" height="${h + 20}" viewBox="-10 -10 ${w + 20} ${h + 20}" style="overflow:visible;filter:drop-shadow(0 0 10px ${c})">
      <g fill="none" stroke="${c}" stroke-width="${sw}" stroke-linecap="round">
      <path d="M0 ${L} V0 H${L}"/><path d="M${w - L} 0 H${w} V${L}"/><path d="M${w} ${h - L} V${h} H${w - L}"/><path d="M${L} ${h} H0 V${h - L}"/></g>
      ${o.fill ? `<rect x="0" y="0" width="${w}" height="${h}" rx="10" fill="${o.fill}"/>` : ''}</svg>`;
    return mk(id, { parent, html: svg, x: x - 10, y: y - 10, o: 0, origin: `${w / 2 + 10}px ${h / 2 + 10}px` });
  };
  window.bracketsIn = function (id, t, o = {}) {
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + 0.08, 1, 'linear']]);
    K(id, 's', [[t, o.from || 1.35, 'linear'], [t + (o.dur || 0.32), 1, 'outExpo']]);
    if (o.out) K(id, 'o', [[o.out, 1, 'linear'], [o.out + 0.18, 0, 'inQuad']]);
  };

  // highlight (marker) inside a screen container
  window.glowBox = function (id, parent, region, o = {}) {
    const bs = (R.els[parent] && R.els[parent].bs) || 1;
    const pad = o.pad === undefined ? 8 : o.pad;
    const c = o.color || 'rgba(34,211,160,0.16)';
    const b = o.border || '#22d3a0';
    return mk(id, { parent, x: region[0] * bs - pad, y: region[1] * bs - pad, w: region[2] * bs + 2 * pad, h: region[3] * bs + 2 * pad, o: 0,
      style: { borderRadius: (o.radius || 14) + 'px', background: c, border: `4px solid ${b}`, boxShadow: `0 0 26px ${b}66` }, origin: '50% 50%' });
  };

  // callout label (screen space)
  window.callout = function (id, key, text, x, y, o = {}) {
    return mk(id, { parent: o.parent || 'fx', x, y, o: 0, origin: o.origin || '0% 50%',
      html: `<div class="callout${o.red ? ' red' : ''}" style="position:relative;${o.css || ''}">${key ? `<span class="k">${key}</span>` : ''}${text}</div>` });
  };
  window.calloutIn = function (id, t, o = {}) {
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + 0.1, 1, 'linear']]);
    K(id, 's', [[t, 0.6, 'linear'], [t + 0.34, 1, 'outBack']]);
    K(id, 'blur', [[t, 8, 'linear'], [t + 0.2, 0, 'outCubic']]);
    if (o.out) K(id, 'o', [[o.out, 1, 'linear'], [o.out + 0.16, 0, 'inQuad']]);
  };

  /* Spotlight tour over a real screen.
     steps: [{r:[x,y,w,h] (asset px), t0, t1, key, text, red, callY}]
     Camera zoom is capped so focused text stays sharp and fully visible. */
  window.tour = function (cardId, steps, o = {}) {
    const e = R.els[cardId];
    const bs = e.bs, Wd = e.W, Hd = e.H;
    const bx = e.base.x, by = e.base.y;
    const cy = o.cy || 930, fit = o.fit || 900, maxS = o.maxS || 1.55, minS = o.minS || 1.0, pad = o.pad || 14;
    const X = [], Y = [], S = [];
    const ringId = cardId + '_spot';
    mk(ringId, { parent: 'fx', cls: 'spotring' + (o.red ? ' red' : ''), x: 0, y: 0, w: 10, h: 10, o: 0 });
    const t0 = steps[0].t0;
    X.push([t0 - 0.001, bx, 'linear']); Y.push([t0 - 0.001, by, 'linear']); S.push([t0 - 0.001, 1, 'linear']);
    const RX = [], RY = [], RW = [], RH = [], RO = [];
    steps.forEach((st, i) => {
      const r = st.r;
      const rw = r[2] * bs, rh = r[3] * bs;
      let s = Math.max(minS, Math.min(maxS, st.s || fit / rw));
      s = Math.min(s, Math.max(0.6, (o.maxW || 1000) / rw));   // the focused region always fits on screen
      let x = 540 - (r[0] * bs + rw / 2) * s;
      const cw = Wd * s;
      if (cw <= 1000) x = (1080 - cw) / 2; else x = Math.min(40, Math.max(1040 - cw, x));
      const ycen = st.cy || cy;
      let y = ycen - (r[1] * bs + rh / 2) * s;
      const move = st.move || 0.42;
      X.push([st.t0, X[X.length - 1][1], 'linear']); Y.push([st.t0, Y[Y.length - 1][1], 'linear']); S.push([st.t0, S[S.length - 1][1], 'linear']);
      X.push([st.t0 + move, x, 'inOutExpo']); Y.push([st.t0 + move, y, 'inOutExpo']); S.push([st.t0 + move, s, 'inOutExpo']);
      const sx = x + r[0] * bs * s - pad, sy = y + r[1] * bs * s - pad, sw = rw * s + 2 * pad, sh = rh * s + 2 * pad;
      const ta = st.t0 + move * 0.85;
      RX.push([ta - 0.001, sx, 'hold'], [ta, sx, 'hold'], [st.t1, sx, 'hold']); RY.push([ta - 0.001, sy, 'hold'], [ta, sy, 'hold'], [st.t1, sy, 'hold']);
      RW.push([ta - 0.001, sw, 'hold'], [ta, sw, 'hold'], [st.t1, sw, 'hold']); RH.push([ta - 0.001, sh, 'hold'], [ta, sh, 'hold'], [st.t1, sh, 'hold']);
      RO.push([ta - 0.001, 0, 'linear'], [ta + 0.12, 1, 'outCubic'], [st.t1 - 0.12, 1, 'linear'], [st.t1, 0, 'inQuad']);
      cue(st.t0, 'swish');
      cue(ta, st.sfx || 'click');
      if (st.text || st.key) {
        const cid = `${cardId}_co${i}`;
        let cyp = st.callY !== undefined ? st.callY : (o.callY !== undefined ? o.callY : (sy + sh + 34));
        if (st.callY === undefined && o.callY === undefined && cyp + 140 > 1460) cyp = Math.max(420, sy - 170);
        callout(cid, st.key || '', st.text || '', st.callX || 72, cyp, { red: st.red || o.red });
        calloutIn(cid, ta + 0.08, { out: st.t1 - 0.1 });
      }
    });
    const tend = o.endT || (steps[steps.length - 1].t1 + 0.05);
    X.push([tend, X[X.length - 1][1], 'linear'], [tend + 0.5, bx, 'inOutExpo']);
    Y.push([tend, Y[Y.length - 1][1], 'linear'], [tend + 0.5, by, 'inOutExpo']);
    S.push([tend, S[S.length - 1][1], 'linear'], [tend + 0.5, 1, 'inOutExpo']);
    K(cardId, 'x', X); K(cardId, 'y', Y); K(cardId, 's', S);
    K(ringId, 'x', RX); K(ringId, 'y', RY); K(ringId, 'w', RW); K(ringId, 'h', RH); K(ringId, 'o', RO);
    return tend + 0.5;
  };

  // scanline sweep over a card (child element)
  window.scanOver = function (cardId, t, d = 0.8) {
    const e = R.els[cardId];
    const id = cardId + '_scan' + Math.round(t * 100);
    mk(id, { parent: cardId, cls: 'scanline', x: 0, y: -220, w: e.W, o: 0 });
    K(id, 'y', [[t, -220, 'linear'], [t + d, e.H, 'inOutQuad']]);
    K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear'], [t + d * 0.8, 1, 'linear'], [t + d, 0, 'linear']]);
    cue(t, 'scan', { dur: d });
  };

  // stamp label (FAKE / VERIFIED / NOTICE)
  window.stampLabel = function (id, text, x, y, o = {}) {
    return mk(id, { parent: o.parent, x, y, o: 0, origin: '50% 50%', html: `<div class="stamp ${o.kind || ''}" style="position:relative;transform:rotate(${o.rot === undefined ? -8 : o.rot}deg);${o.css || ''}">${text}</div>` });
  };
  window.stampIn = function (id, t) {
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + 0.05, 1, 'linear']]);
    K(id, 's', [[t, 2.2, 'linear'], [t + 0.2, 1, 'outQuart']]);
    K(id, 'blur', [[t, 10, 'linear'], [t + 0.15, 0, 'linear']]);
    cue(t + 0.12, 'stamp');
  };

  // external source card (neutral design; quotes public sources with attribution)
  window.sourceCard = function (id, o) {
    const html = `<div class="srccard ${o.dark ? 'dark' : ''}" style="position:relative;width:${o.w || 900}px;${o.css || ''}">
      <div class="meta"><span>${o.kind || 'SOURCE'}</span><span>${o.date || ''}</span></div>
      ${o.headline ? `<div class="hl" style="${o.hlCss || ''}">${o.headline}</div>` : ''}
      ${o.quote ? `<div class="q" style="${o.qCss || ''}">${o.quote}</div>` : ''}
      ${o.url ? `<div class="url">${o.url}</div>` : ''}</div>`;
    return mk(id, { parent: o.parent, html, x: o.x === undefined ? 90 : o.x, y: o.y === undefined ? 700 : o.y, o: o.o === undefined ? 0 : o.o, origin: '50% 50%' });
  };

  // generic social post illustration (clearly labelled)
  window.postCard = function (id, o) {
    const html = `<div class="post" style="position:relative;width:${o.w || 900}px;${o.css || ''}">
      <div class="hd"><div class="av" style="${o.avCss || ''}"></div><div><div>${o.name || 'Alert Feed'}</div><div class="handle">${o.handle || '@example · illustration'}</div></div></div>
      <div class="tx">${o.text}</div>
      <div class="ill">${o.label || 'ILLUSTRATION · NOT A REAL ACCOUNT'}</div></div>`;
    return mk(id, { parent: o.parent, html, x: o.x === undefined ? 90 : o.x, y: o.y === undefined ? 700 : o.y, o: o.o === undefined ? 0 : o.o, origin: '50% 50%' });
  };

  window.brandBar = function (id, o = {}) {
    return mk(id, { parent: o.parent, html: BRAND, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 150 : o.y, o: o.o === undefined ? 0 : o.o });
  };

  window.progressBar = function () {
    mk('progress', { parent: 'fx', cls: 'progress', o: 0.9 });
    K('progress', 'sx', [[0, 0.0, 'linear'], [R.dur, 1, 'linear']]);
  };

  /* End CTA: brand, headline, product visual, button, disclaimer, capture note */
  window.ctaCard = function (t, o = {}) {
    const sid = o.id || 'cta';
    shot(sid);
    shotIn(sid, t, o.inKind || 'zoom', 0.5);
    brandBar(sid + '_brand', { parent: sid, x: 72, y: 210, o: 1 });
    headline(sid + '_h', o.lines || ['Check it', '<span class="g">yourself.</span>'], { parent: sid, x: 72, y: 300, cls: o.cls || 'h2', sub: o.sub, subGap: 24 });
    const btnY = o.btnY || 1236;
    if (o.visual) {
      const v = o.visual;
      const meta = CAT[v.asset] || { w: 900, h: 600 };
      let w = v.w || 800;
      const maxH = v.maxH || 470;
      if (meta.h * (w / meta.w) > maxH) w = maxH * meta.w / meta.h;
      const h = meta.h * (w / meta.w);
      const vy = v.y || (btnY - 70 - h);
      realScreen(sid + '_vis', v.asset, { parent: sid, w, x: (1080 - w) / 2, y: vy, o: 0 });
      stamp(sid + '_vstamp', v.asset, { parent: sid, x: (1080 - w) / 2 + 18, y: vy - 26, size: 19, pad: '8px 16px', text: capText(v.asset, false) });
      appear(sid + '_vis', t + 0.25, { dy: 60, s: 0.94 });
      appear(sid + '_vstamp', t + 0.45, { dy: 10, blur: 0 });
      const fy = vy;
      hook(tt => {
        if (tt < t + 0.8) return;
        const k = Math.sin((tt - t) * 1.6) * 7;
        $(sid + '_vis').style.transform = `translate3d(${((1080 - w) / 2).toFixed(1)}px, ${(fy + k).toFixed(2)}px, 0)`;
      });
    }
    mk(sid + '_btn', { parent: sid, x: 72, y: btnY, o: 1, origin: '0 50%', html: `<div class="btn">${o.button || 'betterforyourpocket.com'} <span style="font-size:44px">→</span></div>` });
    mk(sid + '_disc', { parent: sid, x: 76, y: btnY + 138, o: 1, html: `<div class="disc">${o.disc || 'Educational market data. Not financial advice.'}</div>` });
    if (o.note) mk(sid + '_note', { parent: sid, x: 76, y: btnY + 182, o: 1, html: `<div class="src" style="font-size:22px;color:#95a39e">${o.note}</div>` });
    appear(sid + '_brand', t + 0.05, { dy: 20 });
    wordsIn(sid + '_h', t + 0.12, { stagger: 0.06, dy: 50 });
    popIn(sid + '_btn', t + 0.6, { from: 0.7 });
    appear(sid + '_disc', t + 0.8, { dy: 10, blur: 0 });
    if (o.note) appear(sid + '_note', t + 0.9, { dy: 10, blur: 0 });
    hook(tt => {
      if (tt < t + 1.0) return;
      const ph = ((tt - t) * (R.bpm / 60)) % 1;
      const k = Math.exp(-ph * 5);
      $(sid + '_btn').firstChild.style.boxShadow = `0 0 ${60 + 50 * k}px rgba(23,181,138,${(0.45 + 0.35 * k).toFixed(3)}), 0 20px 50px rgba(0,0,0,0.5)`;
    });
    cue(t, 'whoosh', { dur: 0.45, up: true });
    cue(t + 0.6, 'pop');
    return sid;
  };

  // lines stack
  window.lines = function (id, arr, o = {}) {
    const html = arr.map((l, i) => `<div id="${id}_l${i}" class="${o.cls || 'h3'}" style="margin-bottom:${o.gap || 22}px;${o.css || ''}">${l}</div>`).join('');
    mk(id, { parent: o.parent, html, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 700 : o.y, w: o.w || 936, style: { textShadow: '0 10px 40px rgba(0,0,0,0.6)' } });
    arr.forEach((l, i) => reg(`${id}_l${i}`));
    return arr.map((l, i) => `${id}_l${i}`);
  };

  // big counter number
  window.bigNumber = function (id, o) {
    mk(id, { parent: o.parent, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 600 : o.y, w: o.w || 936, o: o.o === undefined ? 0 : o.o,
      html: `<div class="bigno ${o.cls || ''}" id="${id}_n" style="font-size:${o.size || 260}px;color:${o.color || 'var(--ink)'};${o.css || ''}">${o.fmt(o.from)}</div>` });
    counter(id + '_n', o.t0, o.t1, o.from, o.to, o.fmt, o.ease || 'outExpo');
    if (o.ticks !== false) cue(o.t0, 'ticks', { n: o.nticks || 14, dur: Math.max(0.2, (o.t1 - o.t0) * 0.85), curve: 0.55 });
  };
  // strike-through bar over an element region (screen/parent coords)
  window.strikeOver = function (id, parent, x, y, w, t, o = {}) {
    mk(id, { parent, cls: 'strike', x, y, w, o: 0, origin: '0 50%' });
    K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
    K(id, 'sx', [[t, 0, 'linear'], [t + (o.dur || 0.25), 1, 'outExpo']]);
    cue(t, 'swish', { dur: 0.18 });
  };
  // strike-through that follows wrapped lines: wrap text in this span, animate --p 0→1
  window.strikeSpan = (html, color = '#ff5d5d') => `<span style="background:linear-gradient(${color},${color}) no-repeat 0 58% / calc(var(--p, 0) * 100%) 0.11em;-webkit-box-decoration-break:clone;box-decoration-break:clone">${html}</span>`;
  window.strikeIn = function (id, t, d = 0.3) { K(id, 'p', [[t - 0.001, 0, 'linear'], [t, 0, 'linear'], [t + d, 1, 'outExpo']]); cue(t, 'swish', { dur: 0.18 }); };
  // underline sweep
  window.underline = function (id, parent, x, y, w, t, o = {}) {
    mk(id, { parent, cls: 'uline', x, y, w, o: 0, origin: '0 50%' });
    K(id, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
    K(id, 'sx', [[t, 0, 'linear'], [t + (o.dur || 0.35), 1, 'outExpo']]);
  };
  // rapid word swap in one slot: words appear one after another
  window.wordSwap = function (id, words, t0, step, o = {}) {
    const html = words.map((w, i) => `<div id="${id}_s${i}" class="abs ${o.cls || 'h1'}" style="white-space:nowrap;${o.css || ''}">${w}</div>`).join('');
    mk(id, { parent: o.parent, x: o.x === undefined ? 72 : o.x, y: o.y === undefined ? 800 : o.y, w: o.w || 936, html, style: { textShadow: '0 10px 40px rgba(0,0,0,0.6)' } });
    words.forEach((w, i) => {
      reg(`${id}_s${i}`);
      const ta = t0 + i * step, tb = ta + step;
      const last = i === words.length - 1;
      K(`${id}_s${i}`, 'o', [[ta - 0.001, 0, 'linear'], [ta, 1, 'linear']].concat(last && !o.hideLast ? [] : [[tb - 0.001, 1, 'linear'], [tb, 0, 'linear']]));
      K(`${id}_s${i}`, 's', [[ta, 1.12, 'linear'], [ta + 0.18, 1, 'outCubic']]);
      if (o.sfx !== false) cue(ta, o.sfx || 'hit', o.sfxOpts || {});
    });
  };
  // horizontal bar chart (values in same unit)
  window.barChart = function (id, rows, o) {
    const x = o.x || 72, y = o.y || 700, w = o.w || 936, rh = o.rowH || 78, max = o.max || Math.max(...rows.map(r => r.v));
    mk(id, { parent: o.parent, x: 0, y: 0, w: 1080, h: 1920, o: 1 });
    rows.forEach((r, i) => {
      const ry = y + i * rh;
      const bw = Math.max(8, (w - (o.labelW || 250) - (o.valW || 190)) * r.v / max);
      const bh = o.barH || (rh - 26);
      const labY = o.labelAbove ? ry - (o.fs || 38) * 1.35 : ry + 6;
      mk(`${id}_lab${i}`, { parent: id, x, y: labY, o: 0, html: `<div style="font-weight:700;font-size:${o.fs || 38}px;color:var(--ink);white-space:nowrap">${r.label}</div>` });
      mk(`${id}_bar${i}`, { parent: id, cls: 'bar' + (r.dim ? ' dim' : ''), x: x + (o.labelW || 250), y: ry + 8, w: bw, h: bh, o: 0, origin: '0 50%' });
      mk(`${id}_val${i}`, { parent: id, x: x + (o.labelW || 250) + bw + 18, y: ry + 8 + (bh - (o.vfs || 32) * 1.25) / 2, o: 0, html: `<div class="mono" style="font-weight:600;font-size:${o.vfs || 32}px;color:${r.hl ? 'var(--green2)' : 'var(--sub)'};white-space:nowrap">${r.val}</div>` });
      const t = o.t0 + i * (o.stagger || 0.09);
      K(`${id}_lab${i}`, 'o', [[t - 0.001, 0, 'linear'], [t + 0.12, 1, 'linear']]);
      K(`${id}_bar${i}`, 'o', [[t - 0.001, 0, 'linear'], [t, 1, 'linear']]);
      K(`${id}_bar${i}`, 'sx', [[t, 0, 'linear'], [t + 0.45, 1, 'outExpo']]);
      K(`${id}_val${i}`, 'o', [[t + 0.2, 0, 'linear'], [t + 0.35, 1, 'linear']]);
      if (o.tick !== false) cue(t, 'tick');
    });
  };

  // quiz options
  window.optBoxes = function (id, opts, o = {}) {
    const x = o.x || 90, y = o.y || 800, gap = o.gap || 160;
    mk(id, { parent: o.parent, x: 0, y: 0, w: 1080, h: 1920, o: 1 });
    opts.forEach((t, i) => {
      mk(`${id}_${i}`, { parent: id, x, y: y + i * gap, o: o.o === undefined ? 1 : o.o, origin: '50% 50%',
        html: `<div class="opt" style="position:relative"><span class="l">${'ABCDEF'[i]}</span><span>${t}</span></div>` });
    });
  };
  window.optReveal = function (id, n, correct, t) {
    for (let i = 0; i < n; i++) {
      const el = $(`${id}_${i}`).firstChild;
      hook(tt => { el.className = 'opt' + (tt >= t ? (i === correct ? ' right' : ' wrong') : ''); });
      if (i !== correct) K(`${id}_${i}`, 'o', [[t, 1, 'linear'], [t + 0.3, 0.45, 'linear']]);
      else K(`${id}_${i}`, 's', [[t, 1, 'linear'], [t + 0.12, 1.06, 'outQuad'], [t + 0.4, 1, 'outBack']]);
    }
    cue(t, 'chime', { notes: [84, 91] });
  };
  // grid of dots (e.g. holdings)
  window.dotGrid = function (id, o) {
    const n = o.n, cols = o.cols, sz = o.size || 26, gap = o.gap || 10;
    let html = '';
    for (let i = 0; i < n; i++) {
      const r = Math.floor(i / cols), c = i % cols;
      html += `<div id="${id}_d${i}" style="position:absolute;left:${c * (sz + gap)}px;top:${r * (sz + gap)}px;width:${sz}px;height:${sz}px;border-radius:${o.radius || 6}px;background:${o.color || '#1f3b33'}"></div>`;
    }
    mk(id, { parent: o.parent, x: o.x || 72, y: o.y || 700, o: o.o === undefined ? 1 : o.o, html, origin: o.origin || '50% 50%' });
  };
  // simple horizontal timeline: points [{label, sub, x}] drawn left→right
  window.timelineH = function (id, pts, o) {
    const y = o.y || 900, x0 = o.x0 || 110, x1 = o.x1 || 970;
    mk(id, { parent: o.parent, x: 0, y: 0, w: 1080, h: 1920, o: 1 });
    mk(`${id}_line`, { parent: id, x: x0, y: y, w: x1 - x0, h: 6, o: 0, origin: '0 50%', style: { background: 'linear-gradient(90deg,#13a47d,#22d3a0)', borderRadius: '6px', boxShadow: '0 0 18px rgba(34,211,160,0.6)' } });
    K(`${id}_line`, 'o', [[o.t0 - 0.001, 0, 'linear'], [o.t0, 1, 'linear']]);
    K(`${id}_line`, 'sx', [[o.t0, 0, 'linear'], [o.t0 + (o.draw || 1.2), 1, 'inOutCubic']]);
    pts.forEach((p, i) => {
      const px = x0 + (x1 - x0) * p.x;
      const tp = o.t0 + (o.draw || 1.2) * p.x;
      mk(`${id}_dot${i}`, { parent: id, x: px - 18, y: y - 15, w: 36, h: 36, o: 0, origin: '50% 50%', style: { borderRadius: '50%', background: p.color || '#22d3a0', boxShadow: `0 0 24px ${p.color || '#22d3a0'}` } });
      K(`${id}_dot${i}`, 'o', [[tp - 0.001, 0, 'linear'], [tp, 1, 'linear']]);
      K(`${id}_dot${i}`, 's', [[tp, 0.2, 'linear'], [tp + 0.35, 1, 'outBack']]);
      const above = p.above !== undefined ? p.above : (i % 2 === 0);
      const lw = o.labW || 280;
      mk(`${id}_lab${i}`, { parent: id, x: Math.max(24, Math.min(1056 - lw, px - lw / 2)), y: above ? y - (o.aboveH || 170) : y + 50, w: lw, o: 0,
        html: `<div style="text-align:center"><div class="mono" style="font-size:${o.labFs || 26}px;letter-spacing:.14em;color:${p.color || 'var(--green2)'}">${p.label}</div><div style="font-weight:700;font-size:${o.subFs || 38}px;line-height:1.1;margin-top:8px">${p.sub}</div></div>` });
      appear(`${id}_lab${i}`, tp + 0.05, { dy: above ? 20 : -20 });
      cue(tp, 'tick');
    });
  };
  // RGB-split glitch jitter on an element for a time window
  window.glitchOn = function (id, t0, d, amp = 10) {
    const el = $(id);
    hook(t => {
      if (t < t0 || t > t0 + d) { if (el.dataset.g) { el.style.filter = el.dataset.g === 'x' ? '' : el.style.filter; } return; }
      const n = Math.floor(t * 60);
      const a = amp * (0.4 + 0.6 * Math.abs(Math.sin(n * 7.13)));
      el.style.filter = `drop-shadow(${a.toFixed(1)}px 0 0 rgba(255,60,80,0.75)) drop-shadow(${(-a).toFixed(1)}px 0 0 rgba(60,220,255,0.7))`;
      el.dataset.g = 'x';
    });
    cue(t0, 'glitch', { dur: Math.min(0.5, d) });
  };
  window.hookSettle = function (id, from = 1.05) { K(id, 's', [[0, from, 'linear'], [0.55, 1, 'outExpo']]); };

  // pane: a clipped window showing one region of a real screen at a given scale (split screens)
  window.paneCrop = function (id, asset, region, x, y, w, h, o = {}) {
    const meta = CAT[asset] || { w: 900, h: 600 };
    const s = o.scale || Math.min(w / region[2], h / region[3]) * (o.fill || 0.9);
    const iw = meta.w * s, ih = meta.h * s;
    const ix = w / 2 - (region[0] + region[2] / 2) * s, iy = h / 2 - (region[1] + region[3] / 2) * s;
    return mk(id, { parent: o.parent, x, y, o: o.o === undefined ? 1 : o.o, origin: '50% 50%',
      html: `<div style="position:relative;width:${w}px;height:${h}px;border-radius:28px;overflow:hidden;background:#0b1311;box-shadow:0 40px 120px rgba(0,0,0,0.6),0 0 0 2px ${o.border || 'rgba(23,181,138,0.3)'}">
        <img src="screens/${asset}@2x.png" style="position:absolute;left:${ix}px;top:${iy}px;width:${iw}px;height:${ih}px"></div>` });
  };

  // ---------------------------------------------------------------- VO helpers
  window.VT = i => (window.VO && VO.lines[i]) ? VO.lines[i].t0 : 0;
  window.VE = i => (window.VO && VO.lines[i]) ? VO.lines[i].t1 : 0;
  /* karaoke: words of an element pop in as they are spoken (timing ∝ word length within [t0,t1]) */
  window.karaoke = function (id, t0, t1, o = {}) {
    const ws = R.els[id].words || (R.els[id].words = splitWords(id));
    const lens = ws.map(w => Math.max(2, $(w).textContent.replace(/[^A-Za-z0-9$%]/g, '').length + 1.5));
    const tot = lens.reduce((a, b) => a + b, 0);
    const span = Math.max(0.2, (t1 - t0) * (o.fill || 0.92));
    let acc = 0;
    ws.forEach((w, i) => {
      const ti = t0 - (o.lead || 0.04) + span * acc / tot;
      acc += lens[i];
      if (o.dimStart) {
        // already laid out at rest (scale 1, no offset) so spacing is exact; light up + tiny pop when spoken
        K(w, 'o', [[ti - 0.001, 0.4, 'linear'], [ti, 0.4, 'linear'], [ti + 0.07, 1, 'linear']]);
        K(w, 's', [[ti - 0.001, 1, 'linear'], [ti, 1.06, 'linear'], [ti + 0.18, 1, 'outCubic']]);
      } else {
        K(w, 'o', [[ti - 0.001, 0, 'linear'], [ti, 0, 'linear'], [ti + 0.07, 1, 'linear']]);
        K(w, 'y', [[ti, o.dy === undefined ? 22 : o.dy, 'linear'], [ti + 0.22, 0, 'outExpo']]);
        K(w, 's', [[ti, 1.14, 'linear'], [ti + 0.2, 1, 'outCubic']]);
      }
    });
  };
  // subtitle bar synced to VO (bottom, above IG UI); lines given with display HTML
  window.subtitles = function (items, o = {}) {
    items.forEach((it, i) => {
      const id = `sub_${i}`;
      mk(id, { parent: 'fx', x: 120, y: o.y || 1330, w: 840, o: 1, html: `<div style="text-align:center"><span style="display:inline-block;background:rgba(6,11,10,0.86);border-radius:18px;padding:14px 26px;font-weight:750;font-size:${o.fs || 50}px;line-height:1.18;letter-spacing:-0.01em;color:#eef4f1;box-decoration-break:clone;-webkit-box-decoration-break:clone">${it.html}</span></div>` });
      K(id, 'o', [[0, 0, 'linear'], [it.t0 - 0.06, 0, 'linear'], [it.t0, 1, 'linear'], [it.t1 + 0.12, 1, 'linear'], [it.t1 + 0.2, 0, 'linear']]);
      K(id, 's', [[it.t0 - 0.06, 0.96, 'linear'], [it.t0 + 0.15, 1, 'outCubic']]);
    });
  };

  /* Cover: separate static composition (never touched by R.render) */
  window.coverDesign = function (o) {
    const root = $('root');
    const L = document.createElement('div');
    L.id = 'coverLayer';
    let vis = '';
    if (o.asset) {
      const meta = CAT[o.asset] || { w: 900, h: 600 };
      const w = o.visW || 860;
      const crop = o.crop; // [x,y,w,h] asset px, optional
      if (crop) {
        const s = w / crop[2];
        const h = crop[3] * s;
        vis = `<div style="position:absolute;left:${(1080 - w) / 2}px;top:${o.visY || 980}px;width:${w}px;height:${h}px;border-radius:28px;overflow:hidden;box-shadow:0 50px 140px rgba(0,0,0,0.7),0 0 0 2px rgba(23,181,138,0.35),0 0 90px rgba(23,181,138,0.18)">
          <img src="screens/${o.asset}@2x.png" style="position:absolute;left:${-crop[0] * s}px;top:${-crop[1] * s}px;width:${meta.w * s}px;height:${meta.h * s}px"></div>`;
      } else {
        const h = meta.h * w / meta.w;
        vis = `<div style="position:absolute;left:${(1080 - w) / 2}px;top:${o.visY || 980}px;width:${w}px;height:${h}px;border-radius:28px;overflow:hidden;box-shadow:0 50px 140px rgba(0,0,0,0.7),0 0 0 2px rgba(23,181,138,0.35),0 0 90px rgba(23,181,138,0.18)">
          <img src="screens/${o.asset}@2x.png" style="width:${w}px;height:${h}px;display:block"></div>`;
      }
    }
    L.innerHTML = `<div style="position:absolute;inset:0;background:radial-gradient(900px 900px at 50% 62%, rgba(23,181,138,0.16), rgba(23,181,138,0) 70%),radial-gradient(1400px 1100px at 50% 45%, #0c1614 0%, #080e0d 70%)"></div>
      <div style="position:absolute;inset:-200px;opacity:0.5;background-image:linear-gradient(rgba(23,181,138,0.07) 1px, transparent 1px),linear-gradient(90deg, rgba(23,181,138,0.07) 1px, transparent 1px);background-size:72px 72px;-webkit-mask-image:radial-gradient(900px 1200px at 50% 48%, #000 0%, transparent 75%)"></div>
      <div style="position:absolute;left:72px;top:${o.brandY || 262}px">${BRAND}</div>
      ${o.eyebrow ? `<div class="eyebrow" style="position:absolute;left:74px;top:${(o.brandY || 262) + 100}px">${o.eyebrow}</div>` : ''}
      <div class="${o.cls || 'h1'}" style="position:absolute;left:72px;top:${o.hY || 430}px;width:940px;${o.hCss || ''};text-shadow:0 10px 40px rgba(0,0,0,0.6)">${o.lines.join('<br>')}</div>
      ${vis}
      ${o.extra || ''}
      ${o.asset ? `<div class="capline" style="position:absolute;left:74px;top:${o.capY || 1628}px"><b>●</b> ${capText(o.asset)}</div>` : ''}
      <div class="vignette"></div>`;
    root.appendChild(L);
  };
})();
