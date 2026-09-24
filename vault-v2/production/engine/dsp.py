"""BFYP Vault V2 — DSP core (original synthesis, no samples).

Everything here is deterministic given seeds. 48 kHz, float64 internally.
"""
import numpy as np
from scipy import signal
from scipy.ndimage import maximum_filter1d

SR = 48000


# ----------------------------------------------------------------- utilities
def db(x):
    return 10.0 ** (x / 20.0)


def to_db(x):
    return 20.0 * np.log10(np.maximum(np.abs(x), 1e-12))


def secs(n):
    return n / SR


def ns(t):
    return int(round(t * SR))


def midi_to_hz(m):
    return 440.0 * 2.0 ** ((np.asarray(m, dtype=float) - 69.0) / 12.0)


def fade(x, fin=0.002, fout=0.004):
    """Short raised-cosine fades to kill clicks (works on mono or stereo)."""
    x = np.array(x, dtype=float, copy=True)
    n = x.shape[-1]
    a = min(ns(fin), n // 2)
    b = min(ns(fout), n // 2)
    if a > 0:
        w = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, a))
        x[..., :a] *= w
    if b > 0:
        w = 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, b))
        x[..., -b:] *= w
    return x


def pan_mono(x, pan=0.0):
    """Equal-power pan: pan in [-1, 1]. Returns (2, n)."""
    ang = (pan + 1.0) * np.pi / 4.0
    return np.vstack([x * np.cos(ang), x * np.sin(ang)])


def stereo(x):
    x = np.asarray(x, dtype=float)
    if x.ndim == 1:
        return np.vstack([x, x])
    return x


class Bus:
    """A stereo timeline buffer you can drop sounds into."""

    def __init__(self, dur, pad=4.0):
        self.dur = dur
        self.x = np.zeros((2, ns(dur + pad)))

    def add(self, sig, t, gain=1.0, pan=None):
        sig = np.asarray(sig, dtype=float)
        if sig.ndim == 1:
            sig = pan_mono(sig, 0.0 if pan is None else pan) if pan is not None else np.vstack([sig, sig]) * 0.7071
        i0 = ns(t)
        if i0 < 0:
            sig = sig[:, -i0:]
            i0 = 0
        n = min(sig.shape[1], self.x.shape[1] - i0)
        if n <= 0:
            return
        self.x[:, i0:i0 + n] += sig[:, :n] * gain

    def trim(self, dur=None):
        d = self.dur if dur is None else dur
        return self.x[:, :ns(d)]


# ---------------------------------------------------------------- oscillators
def _phase(freq, n, ph0=0.0):
    f = np.full(n, float(freq)) if np.ndim(freq) == 0 else np.asarray(freq, dtype=float)[:n]
    dt = f / SR
    ph = (ph0 + np.concatenate([[0.0], np.cumsum(dt)[:-1]])) % 1.0
    return ph, dt


def _polyblep(t, dt):
    y = np.zeros_like(t)
    m = t < dt
    x = t[m] / dt[m]
    y[m] = x + x - x * x - 1.0
    m2 = t > 1.0 - dt
    x = (t[m2] - 1.0) / dt[m2]
    y[m2] = x * x + x + x + 1.0
    return y


def osc_saw(freq, n, ph0=0.0):
    ph, dt = _phase(freq, n, ph0)
    return 2.0 * ph - 1.0 - _polyblep(ph, dt)


def osc_square(freq, n, ph0=0.0, pw=0.5):
    ph, dt = _phase(freq, n, ph0)
    ph2 = (ph + pw) % 1.0
    s1 = 2.0 * ph - 1.0 - _polyblep(ph, dt)
    s2 = 2.0 * ph2 - 1.0 - _polyblep(ph2, dt)
    return 0.5 * (s1 - s2)


def osc_sine(freq, n, ph0=0.0):
    ph, _ = _phase(freq, n, ph0)
    return np.sin(2 * np.pi * ph)


def osc_tri(freq, n, ph0=0.0):
    ph, _ = _phase(freq, n, ph0)
    return 2.0 * np.abs(2.0 * ph - 1.0) - 1.0


def noise(n, seed=0, color="white"):
    rng = np.random.RandomState(seed)
    w = rng.randn(n)
    if color == "white":
        return w / 3.0
    if color == "pink":
        # Paul Kellet-ish via filtering white noise
        b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
        a = [1, -2.494956002, 2.017265875, -0.522189400]
        p = signal.lfilter(b, a, w)
        return p / (np.std(p) * 3.0 + 1e-9)
    if color == "brown":
        br = np.cumsum(w)
        br = signal.lfilter([1, -1], [1, -0.995], br)
        return br / (np.std(br) * 3.0 + 1e-9)
    return w


# --------------------------------------------------------------------- filters
def _biquad(kind, f0, q=0.7071, gain_db=0.0):
    f0 = float(np.clip(f0, 10.0, SR * 0.49))
    A = 10 ** (gain_db / 40.0)
    w0 = 2 * np.pi * f0 / SR
    cw, sw = np.cos(w0), np.sin(w0)
    alpha = sw / (2 * q)
    if kind == "lp":
        b = [(1 - cw) / 2, 1 - cw, (1 - cw) / 2]
        a = [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "hp":
        b = [(1 + cw) / 2, -(1 + cw), (1 + cw) / 2]
        a = [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "bp":
        b = [alpha, 0, -alpha]
        a = [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "notch":
        b = [1, -2 * cw, 1]
        a = [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "peak":
        b = [1 + alpha * A, -2 * cw, 1 - alpha * A]
        a = [1 + alpha / A, -2 * cw, 1 - alpha / A]
    elif kind == "lowshelf":
        sa = 2 * np.sqrt(A) * alpha
        b = [A * ((A + 1) - (A - 1) * cw + sa), 2 * A * ((A - 1) - (A + 1) * cw), A * ((A + 1) - (A - 1) * cw - sa)]
        a = [(A + 1) + (A - 1) * cw + sa, -2 * ((A - 1) + (A + 1) * cw), (A + 1) + (A - 1) * cw - sa]
    elif kind == "highshelf":
        sa = 2 * np.sqrt(A) * alpha
        b = [A * ((A + 1) + (A - 1) * cw + sa), -2 * A * ((A - 1) + (A + 1) * cw), A * ((A + 1) + (A - 1) * cw - sa)]
        a = [(A + 1) - (A - 1) * cw + sa, 2 * ((A - 1) - (A + 1) * cw), (A + 1) - (A - 1) * cw - sa]
    else:
        raise ValueError(kind)
    b = np.array(b) / a[0]
    a = np.array(a) / a[0]
    return b, a


def filt(x, kind, f0, q=0.7071, gain_db=0.0):
    b, a = _biquad(kind, f0, q, gain_db)
    return signal.lfilter(b, a, x, axis=-1)


def butter(x, kind, f0, order=4):
    btype = {"lp": "lowpass", "hp": "highpass"}[kind]
    sos = signal.butter(order, float(np.clip(f0, 10, SR * 0.49)), btype=btype, fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def band(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, min(hi, SR * 0.49)], btype="bandpass", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=-1)


def filt_sweep(x, kind, f_curve, q=0.7071, block=64):
    """Time-varying biquad. f_curve: array of cutoff per sample (len == x.shape[-1])
    or a callable of normalized time. Works on mono or stereo."""
    x = np.asarray(x, dtype=float)
    n = x.shape[-1]
    if callable(f_curve):
        f_curve = f_curve(np.linspace(0, 1, n))
    f_curve = np.asarray(f_curve, dtype=float)
    out = np.zeros_like(x)
    zi = None
    for i0 in range(0, n, block):
        i1 = min(n, i0 + block)
        b, a = _biquad(kind, f_curve[(i0 + i1) // 2], q)
        seg = x[..., i0:i1]
        if zi is None:
            zi = np.zeros(x.shape[:-1] + (2,))
        y, zi = signal.lfilter(b, a, seg, axis=-1, zi=zi)
        out[..., i0:i1] = y
    return out


def exp_curve(f0, f1, n, shape=1.0):
    u = np.linspace(0, 1, n) ** shape
    return f0 * (f1 / f0) ** u


# -------------------------------------------------------------------- envelopes
def env_adsr(n, a=0.005, d=0.1, s=0.7, r=0.1, hold=None):
    """ADSR where the note lasts n samples total (release included at the end)."""
    A, D, R = ns(a), ns(d), ns(r)
    e = np.zeros(n)
    rel_start = max(0, n - R)
    idx = np.arange(n)
    # attack
    m = idx < A
    e[m] = idx[m] / max(A, 1)
    # decay
    m = (idx >= A) & (idx < A + D)
    e[m] = 1.0 - (1.0 - s) * (idx[m] - A) / max(D, 1)
    m = idx >= A + D
    e[m] = s
    # release
    if R > 0:
        lvl = e[rel_start] if rel_start < n else s
        m = idx >= rel_start
        e[m] = lvl * (1.0 - (idx[m] - rel_start) / max(R, 1))
    return np.clip(e, 0, 1)


def env_exp(n, tau, attack=0.001):
    t = np.arange(n) / SR
    e = np.exp(-t / max(tau, 1e-4))
    A = ns(attack)
    if A > 0:
        e[:A] *= np.linspace(0, 1, A)
    return e


# ---------------------------------------------------------------------- effects
def saturate(x, drive=1.5):
    return np.tanh(x * drive) / np.tanh(drive)


def make_ir(t60=1.6, dur=None, predelay=0.012, bright=9000.0, dark=2500.0, seed=7, width=1.0, er_gain=0.35):
    dur = dur or min(4.0, t60 * 1.25)
    n = ns(dur)
    t = np.arange(n) / SR
    rng = np.random.RandomState(seed)
    tail = rng.randn(2, n)
    env = 10 ** (-3.0 * t / t60)
    fade_in = np.clip(t / 0.03, 0, 1)
    tail *= env * fade_in
    tail = filt_sweep(tail, "lp", exp_curve(bright, dark, n, 0.6), q=0.5, block=256)
    # early reflections
    er = np.zeros((2, n))
    for k in range(12):
        d = rng.uniform(0.004, 0.07)
        g = er_gain * (1.0 - d / 0.08) * rng.uniform(0.5, 1.0)
        ch = k % 2
        i = ns(d)
        if i < n:
            er[ch, i] += g * (1 if rng.rand() > 0.3 else -1)
    ir = tail / (np.sqrt(np.sum(tail ** 2) / 2) + 1e-9) + er
    # width: mid/side
    mid = (ir[0] + ir[1]) / 2
    side = (ir[0] - ir[1]) / 2 * width
    ir = np.vstack([mid + side, mid - side])
    pd = ns(predelay)
    ir = np.pad(ir, ((0, 0), (pd, 0)))
    return ir / (np.max(np.abs(ir)) + 1e-9)


_IR_CACHE = {}


def reverb(x, t60=1.6, wet=0.2, seed=7, bright=9000.0, dark=2500.0, predelay=0.012, width=1.0, hp=180.0):
    key = (round(t60, 3), seed, bright, dark, predelay, width)
    if key not in _IR_CACHE:
        _IR_CACHE[key] = make_ir(t60=t60, seed=seed, bright=bright, dark=dark, predelay=predelay, width=width)
    ir = _IR_CACHE[key]
    xs = stereo(x)
    src = butter(xs, "hp", hp, 2)
    wetL = signal.fftconvolve(src[0], ir[0])[: xs.shape[1]]
    wetR = signal.fftconvolve(src[1], ir[1])[: xs.shape[1]]
    w = np.vstack([wetL, wetR])
    # normalise wet energy relative to dry
    gain = np.sqrt(np.mean(src ** 2) + 1e-12) / (np.sqrt(np.mean(w ** 2)) + 1e-12)
    return xs + w * gain * wet


def delay(x, time, fb=0.35, mix=0.25, lp=5000.0, pingpong=True, taps=6):
    xs = stereo(x)
    out = np.zeros_like(xs)
    d = ns(time)
    src = butter(xs, "lp", lp, 2)
    cur = src
    g = 1.0
    for k in range(1, taps + 1):
        g *= fb
        shifted = np.zeros_like(xs)
        if d * k < xs.shape[1]:
            if pingpong:
                ch = (k % 2)
                shifted[ch, d * k:] = (cur[0, :-d * k] + cur[1, :-d * k]) * 0.5
            else:
                shifted[:, d * k:] = cur[:, :-d * k]
        out += shifted * g
    return xs + out * mix


def chorus(x, depth_ms=6.0, rate=0.35, mix=0.35, base_ms=12.0):
    xs = stereo(x)
    n = xs.shape[1]
    t = np.arange(n) / SR
    out = np.copy(xs)
    for ch, ph in ((0, 0.0), (1, np.pi / 2)):
        dly = (base_ms + depth_ms * 0.5 * (1 + np.sin(2 * np.pi * rate * t + ph))) * SR / 1000.0
        idx = np.arange(n) - dly
        i0 = np.floor(idx).astype(int)
        frac = idx - i0
        i0c = np.clip(i0, 0, n - 1)
        i1c = np.clip(i0 + 1, 0, n - 1)
        wet = xs[ch, i0c] * (1 - frac) + xs[ch, i1c] * frac
        wet[i0 < 0] = 0
        out[ch] = xs[ch] * (1 - mix * 0.5) + wet * mix
    return out


def env_follow(x, attack=0.003, release=0.12):
    """Peak-ish envelope: max filter (attack) then one-pole release smoothing."""
    a = np.max(np.abs(stereo(x)), axis=0)
    a = maximum_filter1d(a, size=max(1, ns(attack)), mode="nearest")
    k = np.exp(-1.0 / (release * SR))
    # forward-backward smoothing keeps peaks without lag distortion
    sm = signal.lfilter([1 - k], [1, -k], a)
    return np.maximum(sm, 1e-9)


def compress(x, thresh_db=-18.0, ratio=3.0, attack=0.005, release=0.12, makeup_db=0.0, knee_db=6.0):
    xs = stereo(x)
    env = to_db(env_follow(xs, attack, release))
    over = env - thresh_db
    # soft knee
    gr = np.where(over <= -knee_db / 2, 0.0,
                  np.where(over >= knee_db / 2, over * (1 - 1 / ratio),
                           (1 - 1 / ratio) * (over + knee_db / 2) ** 2 / (2 * knee_db)))
    g = db(-gr + makeup_db)
    return xs * g


def limiter(x, ceiling_db=-1.0, lookahead=0.003, release=0.06):
    xs = stereo(x)
    ceil = db(ceiling_db)
    peak = np.max(np.abs(xs), axis=0)
    la = max(1, ns(lookahead))
    # required gain per sample
    need = np.minimum(1.0, ceil / np.maximum(peak, 1e-9))
    # look-ahead: min over window ahead
    need_la = -maximum_filter1d(-need, size=2 * la + 1, mode="nearest")
    k = np.exp(-1.0 / (release * SR))
    # smooth: release smoothing on gain (allow instant attack)
    g = np.empty_like(need_la)
    # vectorised approx: smooth then take min with requirement
    sm = signal.lfilter([1 - k], [1, -k], need_la - 1.0) + 1.0
    g = np.minimum(sm, need_la)
    # attack smoothing to avoid clicks: short moving average of gain
    w = np.hanning(2 * la + 1)
    w /= w.sum()
    g = np.minimum(np.convolve(g, w, mode="same"), need_la * 1.0 + 1e-6)
    y = xs * g
    return np.clip(y, -ceil, ceil)


def true_peak_db(x):
    xs = stereo(x)
    up = signal.resample_poly(xs, 4, 1, axis=-1)
    return to_db(np.max(np.abs(up)))


def lufs(x):
    import pyloudnorm as pyln
    meter = pyln.Meter(SR)
    return meter.integrated_loudness(stereo(x).T)


def duck_curve(n, times, depth=0.6, attack=0.004, release=0.16, shape=1.6):
    """Sidechain-like gain curve dipping at each trigger time."""
    g = np.ones(n)
    A = max(1, ns(attack))
    R = ns(release)
    rel = 1.0 - depth * (1.0 - np.linspace(0, 1, R) ** (1 / shape))  # depth -> 1
    atk = 1.0 - depth * np.linspace(0, 1, A)
    seg = np.concatenate([atk, rel])
    for t in times:
        i0 = ns(t) - A
        if i0 >= n:
            continue
        j0 = max(0, i0)
        s = seg[j0 - i0:]
        j1 = min(n, j0 + len(s))
        g[j0:j1] = np.minimum(g[j0:j1], s[: j1 - j0])
    return g


TARGET_CURVE = {  # 1/3-octave density target (dB), modern electronic mix, phone-friendly
    31.5: -4, 40: -1.5, 50: 0, 63: 0, 80: 0, 100: -1, 125: -2.2, 160: -3.5, 200: -5, 250: -6.3,
    315: -7.5, 400: -8.7, 500: -9.8, 630: -10.8, 800: -11.8, 1000: -12.8, 1250: -13.7, 1600: -14.6,
    2000: -15.5, 2500: -16.4, 3150: -17.3, 4000: -18.3, 5000: -19.5, 6300: -21, 8000: -22.8,
    10000: -25, 12500: -28, 16000: -33, 20000: -40,
}


def band_profile(x):
    xs = stereo(x)
    mono = xs.mean(axis=0)
    f, P = signal.welch(mono, SR, nperseg=8192)
    Pdb = 10 * np.log10(np.maximum(P, 1e-18))
    fc = np.array(sorted(TARGET_CURVE))
    out = []
    for c in fc:
        m = (f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))
        out.append(np.mean(Pdb[m]) if np.any(m) else np.nan)
    return fc, np.array(out)


def spectral_tilt_match(x, max_boost=7.0, max_cut=12.0, lo=35.0, hi=16000.0):
    """Gentle auto-EQ toward TARGET_CURVE (linear-phase FIR)."""
    xs = stereo(x)
    fc, band_db = band_profile(xs)
    target = np.array([TARGET_CURVE[c] for c in fc])
    valid = (fc >= lo) & (fc <= hi) & ~np.isnan(band_db)
    diff = target - band_db
    off = np.median(diff[valid])
    corr = np.clip(diff - off, -max_cut, max_boost)
    corr[~valid] = 0.0
    k = np.array([0.25, 0.5, 0.25])
    corr = np.convolve(np.pad(corr, 1, mode="edge"), k, mode="valid")
    freqs = np.concatenate([[0], fc, [SR / 2]])
    gains = np.concatenate([[corr[0]], corr, [corr[-1]]])
    fir = signal.firwin2(16385, np.clip(freqs / (SR / 2), 0, 1), db(gains))
    fir = signal.minimum_phase(fir, method="homomorphic", half=False)
    y = np.vstack([signal.fftconvolve(ch, fir)[: xs.shape[1]] for ch in xs])
    return y, dict(zip([int(v) for v in fc], np.round(corr, 1)))


def master(x, target_lufs=-13.0, ceiling=-1.0, auto_eq=True):
    xs = stereo(x)
    xs = butter(xs, "hp", 30.0, 2)
    xs = filt(xs, "lowshelf", 55.0, 0.7, -2.5)
    info = {}
    if auto_eq:
        xs, info["eq"] = spectral_tilt_match(xs)
    xs = compress(xs, thresh_db=-16.0, ratio=1.8, attack=0.02, release=0.25, knee_db=8)
    # loudness normalise then limit, iterate to hit target within ceiling
    lim = ceiling - 0.6
    for _ in range(6):
        L = lufs(xs)
        if not np.isfinite(L):
            break
        xs = xs * db(target_lufs - L)
        xs = limiter(xs, ceiling_db=lim, lookahead=0.004, release=0.08)
        tp = true_peak_db(xs)
        if tp > ceiling:
            xs = xs * db(ceiling - tp - 0.05)
            lim -= min(1.5, tp - ceiling + 0.05)  # inter-sample overs the sample-peak limiter cannot see: clamp lower next pass
        if abs(lufs(xs) - target_lufs) < 0.3:
            break
    info["lufs"] = lufs(xs)
    info["tp"] = true_peak_db(xs)
    return xs, info
