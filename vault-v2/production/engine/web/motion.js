/* BFYP Vault V2 — deterministic motion engine.
   Every visual state is a pure function of time t (seconds). The renderer
   seeks t frame by frame and captures; audio cues are exported to Python. */
(function () {
  const E = {
    linear: u => u,
    hold: u => (u >= 1 ? 1 : 0),
    inQuad: u => u * u,
    outQuad: u => 1 - (1 - u) * (1 - u),
    inOutQuad: u => (u < 0.5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2),
    inCubic: u => u * u * u,
    outCubic: u => 1 - Math.pow(1 - u, 3),
    inOutCubic: u => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2),
    outQuart: u => 1 - Math.pow(1 - u, 4),
    inQuart: u => u * u * u * u,
    inOutQuart: u => (u < 0.5 ? 8 * u * u * u * u : 1 - Math.pow(-2 * u + 2, 4) / 2),
    outQuint: u => 1 - Math.pow(1 - u, 5),
    inExpo: u => (u === 0 ? 0 : Math.pow(2, 10 * u - 10)),
    outExpo: u => (u === 1 ? 1 : 1 - Math.pow(2, -10 * u)),
    inOutExpo: u => (u === 0 ? 0 : u === 1 ? 1 : u < 0.5 ? Math.pow(2, 20 * u - 10) / 2 : (2 - Math.pow(2, -20 * u + 10)) / 2),
    outBack: u => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(u - 1, 3) + c1 * Math.pow(u - 1, 2); },
    outBackSoft: u => { const c1 = 1.0, c3 = c1 + 1; return 1 + c3 * Math.pow(u - 1, 3) + c1 * Math.pow(u - 1, 2); },
    inBack: u => { const c1 = 1.70158, c3 = c1 + 1; return c3 * u * u * u - c1 * u * u; },
    outElastic: u => { const c4 = (2 * Math.PI) / 3; return u === 0 ? 0 : u === 1 ? 1 : Math.pow(2, -10 * u) * Math.sin((u * 10 - 0.75) * c4) + 1; },
    spring: u => 1 - Math.exp(-6.5 * u) * Math.cos(9.5 * u),
  };

  const R = {
    W: 1080, H: 1920, fps: 30, dur: 20, bpm: 120,
    els: {}, order: [], hooks: [], cues: [], music: null, meta: {}, coverT: null,
    E,
  };
  window.R = R;
  window.E = E;

  R.setup = function (o) { Object.assign(R, o); };
  window.B = n => (n * 60) / R.bpm;

  function $(id) { return document.getElementById(id); }
  window.$ = $;

  // ---------------------------------------------------------------- elements
  window.mk = function (id, o = {}) {
    const d = document.createElement(o.tag || 'div');
    d.id = id;
    d.className = 'abs ' + (o.cls || '');
    if (o.html !== undefined) d.innerHTML = o.html;
    if (o.src) d.src = o.src;
    const st = o.style || {};
    for (const k in st) d.style[k] = st[k];
    if (o.w !== undefined) d.style.width = o.w + 'px';
    else if (!o.noMax) d.style.maxWidth = Math.max(200, 1008 - (o.x || 0)) + 'px';   // never run past the right safe edge
    if (o.h !== undefined) d.style.height = o.h + 'px';
    if (o.origin) d.style.transformOrigin = o.origin;
    const parent = o.parent ? $(o.parent) : $('cam');
    parent.appendChild(d);
    const base = { x: o.x || 0, y: o.y || 0, s: o.s === undefined ? 1 : o.s, sx: 1, sy: 1, r: 0, o: o.o === undefined ? 1 : o.o, blur: 0, bright: 1, sat: 1 };
    R.els[id] = { el: d, tr: {}, base, parent: o.parent || 'cam' };
    R.order.push(id);
    return d;
  };
  // register an existing DOM element (e.g. word spans)
  window.reg = function (id, base = {}) {
    const d = $(id);
    R.els[id] = { el: d, tr: {}, base: Object.assign({ x: 0, y: 0, s: 1, sx: 1, sy: 1, r: 0, o: 1, blur: 0, bright: 1, sat: 1 }, base), inline: true };
    R.order.push(id);
    return d;
  };

  window.K = function (id, prop, kfs) {
    const e = R.els[id];
    if (!e) throw new Error('K: unknown element ' + id);
    const arr = kfs.map(k => ({ t: k[0], v: k[1], e: k[2] || 'outCubic' }));
    arr.sort((a, b) => a.t - b.t);
    if (!e.tr[prop]) e.tr[prop] = arr;
    else { e.tr[prop] = e.tr[prop].concat(arr).sort((a, b) => a.t - b.t); }
  };

  function val(tr, t, base) {
    if (!tr || !tr.length) return base;
    if (t <= tr[0].t) return tr[0].v;
    for (let i = 1; i < tr.length; i++) {
      if (t <= tr[i].t) {
        const a = tr[i - 1], b = tr[i];
        const span = b.t - a.t;
        const u = span <= 1e-9 ? 1 : (t - a.t) / span;
        const w = (E[b.e] || E.outCubic)(Math.min(1, Math.max(0, u)));
        if (typeof a.v === 'number') return a.v + (b.v - a.v) * w;
        if (Array.isArray(a.v)) return a.v.map((x, j) => x + (b.v[j] - x) * w);
        return w < 1 ? a.v : b.v;
      }
    }
    return tr[tr.length - 1].v;
  }
  R.val = val;

  window.hook = fn => R.hooks.push(fn);
  window.cue = (t, type, p = {}) => R.cues.push(Object.assign({ t, type }, p));
  window.music = o => { R.music = o; };

  R.state = function (id, t) {
    const e = R.els[id], b = e.base, tr = e.tr;
    return {
      x: val(tr.x, t, b.x), y: val(tr.y, t, b.y), s: val(tr.s, t, b.s), sx: val(tr.sx, t, b.sx), sy: val(tr.sy, t, b.sy),
      r: val(tr.r, t, b.r), o: val(tr.o, t, b.o), blur: val(tr.blur, t, b.blur), bright: val(tr.bright, t, b.bright), sat: val(tr.sat, t, b.sat),
    };
  };

  R.render = function (t) {
    R.t = t;
    for (const id of R.order) {
      const e = R.els[id];
      const s = R.state(id, t);
      const st = e.el.style;
      const extra = e.jitter ? e.jitter(t) : null;
      const x = s.x + (extra ? extra.x : 0), y = s.y + (extra ? extra.y : 0);
      st.transform = `translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,0) rotate(${s.r.toFixed(3)}deg) scale(${(s.s * s.sx).toFixed(4)},${(s.s * s.sy).toFixed(4)})`;
      st.opacity = Math.max(0, Math.min(1, s.o)).toFixed(3);
      let f = '';
      if (s.blur > 0.05) f += `blur(${s.blur.toFixed(2)}px) `;
      if (Math.abs(s.bright - 1) > 0.002) f += `brightness(${s.bright.toFixed(3)}) `;
      if (Math.abs(s.sat - 1) > 0.002) f += `saturate(${s.sat.toFixed(3)}) `;
      st.filter = f || 'none';
      st.visibility = s.o < 0.003 ? 'hidden' : 'visible';
      if (e.tr.clip) {
        const c = val(e.tr.clip, t, [0, 0, 0, 0]);
        st.clipPath = `inset(${c[0].toFixed(2)}% ${c[1].toFixed(2)}% ${c[2].toFixed(2)}% ${c[3].toFixed(2)}% round ${e.clipRound || 0}px)`;
      }
      if (e.tr.w) st.width = val(e.tr.w, t, 0).toFixed(1) + 'px';
      if (e.tr.h) st.height = val(e.tr.h, t, 0).toFixed(1) + 'px';
      if (e.tr.p) st.setProperty('--p', val(e.tr.p, t, 0).toFixed(4));
    }
    for (const fn of R.hooks) fn(t);
  };

  // motion amount (px/frame) for adaptive motion blur in the renderer
  R.motion = function (t) {
    const dt = 1 / R.fps;
    let m = 0;
    for (const id of R.order) {
      const e = R.els[id];
      if (!e.tr.x && !e.tr.y && !e.tr.s && !e.tr.sx && !e.tr.sy) continue;
      const a = R.state(id, t), b = R.state(id, t + dt);
      if (a.o < 0.02 && b.o < 0.02) continue;
      const size = e.el.offsetWidth || 400;
      const d = Math.abs(b.x - a.x) + Math.abs(b.y - a.y) + Math.abs(b.s * b.sx - a.s * a.sx) * size * 0.5 + Math.abs(b.s * b.sy - a.s * a.sy) * (e.el.offsetHeight || 400) * 0.5;
      m = Math.max(m, d * Math.min(1, Math.max(a.o, b.o)) * (e.parent === 'cam' || e.inline ? 1 : 1));
    }
    return m;
  };

  // ---------------------------------------------------------------- helpers
  const clamp01 = u => Math.max(0, Math.min(1, u));
  window.clamp01 = clamp01;

  // appear: fade + rise + de-blur
  window.appear = function (id, t, o = {}) {
    const d = o.dur || 0.42, dy = o.dy === undefined ? 46 : o.dy, dx = o.dx || 0, e = o.ease || 'outExpo';
    const b = R.els[id].base;
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + d * 0.6, 1, 'outCubic']]);
    K(id, 'y', [[t, b.y + dy, 'linear'], [t + d, b.y, e]]);
    if (dx) K(id, 'x', [[t, b.x + dx, 'linear'], [t + d, b.x, e]]);
    if (o.blur !== 0) K(id, 'blur', [[t, o.blur || 14, 'linear'], [t + d * 0.7, 0, 'outCubic']]);
    if (o.s) K(id, 's', [[t, o.s, 'linear'], [t + d, b.s, e]]);
  };
  window.vanish = function (id, t, o = {}) {
    const d = o.dur || 0.25;
    const b = R.els[id].base;
    K(id, 'o', [[t, 1, 'linear'], [t + d, 0, o.ease || 'inQuad']]);
    if (o.dy) K(id, 'y', [[t, b.y, 'linear'], [t + d, b.y + o.dy, 'inCubic']]);
    if (o.dx) K(id, 'x', [[t, b.x, 'linear'], [t + d, b.x + o.dx, 'inCubic']]);
    if (o.blur) K(id, 'blur', [[t, 0, 'linear'], [t + d, o.blur, 'inQuad']]);
    if (o.s) K(id, 's', [[t, b.s, 'linear'], [t + d, o.s, 'inCubic']]);
  };
  // slam: big → normal, very fast, with blur (text slams on beats)
  window.slam = function (id, t, o = {}) {
    const d = o.dur || 0.22, from = o.from || 1.45;
    const b = R.els[id].base;
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0.0, 'linear'], [t + 0.05, 1, 'linear']]);
    K(id, 's', [[t, b.s * from, 'linear'], [t + d, b.s, o.ease || 'outQuart']]);
    K(id, 'blur', [[t, o.blur || 18, 'linear'], [t + d * 0.8, 0, 'outCubic']]);
  };
  window.popIn = function (id, t, o = {}) {
    const d = o.dur || 0.38;
    const b = R.els[id].base;
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + 0.08, 1, 'linear']]);
    K(id, 's', [[t, b.s * (o.from || 0.4), 'linear'], [t + d, b.s, o.ease || 'outBack']]);
  };
  // wipe reveal via clip-path (left→right by default)
  window.wipe = function (id, t, o = {}) {
    const d = o.dur || 0.45, dir = o.dir || 'l';
    const start = { l: [0, 100, 0, 0], r: [0, 0, 0, 100], t: [0, 0, 100, 0], b: [100, 0, 0, 0] }[dir];
    R.els[id].clipRound = o.round || 0;
    K(id, 'clip', [[t, start, 'linear'], [t + d, [0, 0, 0, 0], o.ease || 'outExpo']]);
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 1, 'linear']]);
  };
  window.unwipe = function (id, t, o = {}) {
    const d = o.dur || 0.35, dir = o.dir || 'r';
    const end = { l: [0, 100, 0, 0], r: [0, 0, 0, 100], t: [0, 0, 100, 0], b: [100, 0, 0, 0] }[dir];
    K(id, 'clip', [[t, [0, 0, 0, 0], 'linear'], [t + d, end, o.ease || 'inExpo']]);
  };

  // split an element's text into words (keeps inner <span class> markup per word group)
  window.splitWords = function (id) {
    const root = $(id);
    const out = [];
    let k = 0;
    function walk(node, cls) {
      const kids = Array.from(node.childNodes);
      for (const n of kids) {
        if (n.nodeType === 3) {
          const parts = n.textContent.split(/(\s+)/);
          const frag = document.createDocumentFragment();
          for (const p of parts) {
            if (!p) continue;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(' ')); continue; }
            const s = document.createElement('span');
            s.className = 'word ' + (cls || '');
            s.id = `${id}_w${k++}`;
            s.textContent = p;
            frag.appendChild(s);
            out.push(s.id);
          }
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') {
          if (n.classList.contains('word')) { n.id = `${id}_w${k++}`; out.push(n.id); continue; }
          walk(n, (cls || '') + ' ' + n.className);
          // unwrap container spans so words carry the class
          if (n.tagName === 'SPAN' && !n.classList.contains('keep')) {
            while (n.firstChild) node.insertBefore(n.firstChild, n);
            node.removeChild(n);
          }
        }
      }
    }
    walk(root, '');
    out.forEach(w => reg(w));
    return out;
  };
  // per-word staggered entrance
  window.wordsIn = function (id, t, o = {}) {
    const ws = R.els[id].words || (R.els[id].words = splitWords(id));
    const st = o.stagger === undefined ? 0.07 : o.stagger, d = o.dur || 0.4;
    ws.forEach((w, i) => {
      const ti = t + i * st;
      K(w, 'o', [[ti - 0.0001, 0, 'linear'], [ti, 0, 'linear'], [ti + d * 0.5, 1, 'outCubic']]);
      K(w, 'y', [[ti, o.dy === undefined ? 38 : o.dy, 'linear'], [ti + d, 0, o.ease || 'outExpo']]);
      if (o.blur !== 0) K(w, 'blur', [[ti, o.blur || 10, 'linear'], [ti + d * 0.7, 0, 'outCubic']]);
      if (o.s) K(w, 's', [[ti, o.s, 'linear'], [ti + d, 1, o.ease || 'outBack']]);
    });
    return ws.length ? t + (ws.length - 1) * st + d : t;
  };
  window.wordsOut = function (id, t, o = {}) {
    const ws = R.els[id].words || [];
    ws.forEach((w, i) => {
      const ti = t + i * (o.stagger || 0.02);
      K(w, 'o', [[ti, 1, 'linear'], [ti + (o.dur || 0.18), 0, 'inQuad']]);
    });
  };

  // counter: formats a number tween into an element's text
  window.counter = function (id, t0, t1, a, b, fmt, ease = 'outExpo') {
    const el = $(id);
    hook(t => {
      const u = clamp01((t - t0) / Math.max(1e-6, t1 - t0));
      const v = a + (b - a) * E[ease](u);
      el.textContent = fmt(v, u);
    });
  };
  // typewriter with caret
  window.typer = function (id, text, t0, cps = 22, o = {}) {
    const el = $(id);
    hook(t => {
      const n = Math.max(0, Math.min(text.length, Math.floor((t - t0) * cps)));
      const caretOn = (o.caret !== false) && (t >= t0 - 0.3) && (Math.floor(t * 2.2) % 2 === 0 || n < text.length) && (!o.caretOff || t < o.caretOff);
      el.innerHTML = escapeHtml(text.slice(0, n)) + (caretOn ? '<span style="color:var(--green2);font-weight:400">|</span>' : '');
    });
    // key clicks for audio
    const n = text.length;
    const every = Math.max(1, Math.round(cps / 12));
    for (let i = 0; i < n; i += every) cue(t0 + i / cps, 'key', { gain: 0.55 });
    return t0 + n / cps;
  };
  function escapeHtml(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  // camera helpers (operate on #cam)
  window.camPunch = function (t, amt = 0.045, d = 0.35) {
    K('cam', 's', [[t - 0.0001, 1, 'linear'], [t, 1 + amt, 'linear'], [t + d, 1, 'outCubic']]);
  };
  window.camShake = function (t, d = 0.35, amp = 16) {
    const e = R.els['cam'];
    const prev = e.jitter;
    e.jitter = tt => {
      let base = prev ? prev(tt) : { x: 0, y: 0 };
      if (tt < t || tt > t + d) return base;
      const u = (tt - t) / d, k = (1 - u) * (1 - u) * amp;
      const n = Math.floor(tt * 60);
      return { x: base.x + k * Math.sin(n * 12.9898) * 0.9, y: base.y + k * Math.cos(n * 78.233) * 0.9 };
    };
  };
  window.flash = function (t, o = {}) {
    const id = 'flash_' + Math.round(t * 1000) + '_' + Math.floor(Math.random() * 1e6);
    mk(id, { cls: 'flash', parent: 'fx', style: { background: o.color || '#ffffff', width: '1080px', height: '1920px' }, o: 0 });
    K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, o.peak || 0.55, 'linear'], [t + (o.dur || 0.22), 0, 'outQuad']]);
  };

  // image camera: frame a region (in image px) into a target rect on screen
  // container must be created with mk(id, {origin:'0 0'}) and hold an <img> at natural size * base scale bs.
  window.frameRegion = function (region, target, bs) {
    // region: [rx, ry, rw, rh] in image px; target: [cx, cy, tw] screen center + width
    const s = target[2] / (region[2] * bs);
    const cx = region[0] + region[2] / 2, cy = region[1] + region[3] / 2;
    return { s, x: target[0] - s * cx * bs, y: target[1] - s * cy * bs };
  };
  window.camImg = function (id, bs, keys) {
    // keys: [[t, region, target, ease], ...]
    const xs = [], ys = [], ss = [];
    for (const k of keys) {
      const f = frameRegion(k[1], k[2], bs);
      xs.push([k[0], f.x, k[3] || 'inOutCubic']);
      ys.push([k[0], f.y, k[3] || 'inOutCubic']);
      ss.push([k[0], f.s, k[3] || 'inOutCubic']);
    }
    K(id, 'x', xs); K(id, 'y', ys); K(id, 's', ss);
  };

  // transitions between shots
  window.shotIn = function (id, t, kind = 'rise', d = 0.45) {
    const b = R.els[id].base;
    if (kind === 'rise') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + d * 0.4, 1, 'linear']]); K(id, 'y', [[t, 140, 'linear'], [t + d, 0, 'outExpo']]); K(id, 'blur', [[t, 16, 'linear'], [t + d * 0.6, 0, 'outCubic']]); }
    if (kind === 'zoom') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + d * 0.35, 1, 'linear']]); K(id, 's', [[t, 0.72, 'linear'], [t + d, 1, 'outExpo']]); K(id, 'blur', [[t, 20, 'linear'], [t + d * 0.6, 0, 'outCubic']]); }
    if (kind === 'zoomIn') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 0, 'linear'], [t + d * 0.35, 1, 'linear']]); K(id, 's', [[t, 1.35, 'linear'], [t + d, 1, 'outExpo']]); K(id, 'blur', [[t, 24, 'linear'], [t + d * 0.6, 0, 'outCubic']]); }
    if (kind === 'left') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 1, 'linear']]); K(id, 'x', [[t, 1080, 'linear'], [t + d, 0, 'outExpo']]); }
    if (kind === 'right') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 1, 'linear']]); K(id, 'x', [[t, -1080, 'linear'], [t + d, 0, 'outExpo']]); }
    if (kind === 'up') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 1, 'linear']]); K(id, 'y', [[t, 1920, 'linear'], [t + d, 0, 'outExpo']]); }
    if (kind === 'cut') { K(id, 'o', [[t - 0.0001, 0, 'linear'], [t, 1, 'linear']]); }
  };
  window.shotOut = function (id, t, kind = 'fade', d = 0.3) {
    if (kind === 'fade') { K(id, 'o', [[t, 1, 'linear'], [t + d, 0, 'inQuad']]); K(id, 'blur', [[t, 0, 'linear'], [t + d, 10, 'inQuad']]); }
    if (kind === 'zoom') { K(id, 'o', [[t, 1, 'linear'], [t + d, 0, 'inQuad']]); K(id, 's', [[t, 1, 'linear'], [t + d, 1.6, 'inCubic']]); K(id, 'blur', [[t, 0, 'linear'], [t + d, 18, 'inQuad']]); }
    if (kind === 'shrink') { K(id, 'o', [[t, 1, 'linear'], [t + d, 0, 'inQuad']]); K(id, 's', [[t, 1, 'linear'], [t + d, 0.7, 'inCubic']]); K(id, 'blur', [[t, 0, 'linear'], [t + d, 14, 'inQuad']]); }
    if (kind === 'left') { K(id, 'x', [[t, 0, 'linear'], [t + d, -1080, 'inExpo']]); K(id, 'o', [[t + d - 0.0001, 1, 'linear'], [t + d, 0, 'linear']]); }
    if (kind === 'right') { K(id, 'x', [[t, 0, 'linear'], [t + d, 1080, 'inExpo']]); K(id, 'o', [[t + d - 0.0001, 1, 'linear'], [t + d, 0, 'linear']]); }
    if (kind === 'up') { K(id, 'y', [[t, 0, 'linear'], [t + d, -1920, 'inExpo']]); K(id, 'o', [[t + d - 0.0001, 1, 'linear'], [t + d, 0, 'linear']]); }
    if (kind === 'cut') { K(id, 'o', [[t - 0.0001, 1, 'linear'], [t, 0, 'linear']]); }
  };
  window.shot = function (id, o = {}) { return mk(id, Object.assign({ cls: 'shot', o: 0 }, o)); };

  // brand logo svg
  window.LOGO = `<svg class="logo" viewBox="0 0 100 100"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1dc193"/><stop offset="1" stop-color="#0e9673"/></linearGradient></defs><rect x="3" y="3" width="94" height="94" rx="23" fill="url(#lg)"/><path d="M31 66 L46 53.5 L52 51.5 L65.5 38.5" stroke="#f3fffa" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="65.5" cy="38.5" r="6" fill="#f3fffa"/></svg>`;
  window.BRAND = `<div class="brand">${LOGO}<div class="wm"><b>B</b>ETTERFORYOURPOCKET</div></div>`;
  window.CHECK = `<svg viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7" stroke="#22d3a0" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
})();
