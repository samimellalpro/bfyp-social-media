"""BFYP Vault V2 — synthesized instruments and sound effects (original, sample-free)."""
import numpy as np
from dsp import (SR, ns, db, fade, osc_saw, osc_square, osc_sine, osc_tri, noise, filt, butter, band,
                 filt_sweep, exp_curve, env_adsr, env_exp, saturate, reverb, pan_mono, stereo, midi_to_hz)


# ============================================================== DRUMS
def kick(style="house", tune=1.0, seed=0, decay=None):
    if style == "808":
        dur = decay or 0.9
        n = ns(dur)
        t = np.arange(n) / SR
        f = 48 * tune + (160 * tune - 48 * tune) * np.exp(-t / 0.035)
        body = osc_sine(f, n) * env_exp(n, dur / 3.2, attack=0.0015)
        body = saturate(body * 1.3, 1.4)
        click = butter(noise(ns(0.006), seed), "hp", 2500) * np.linspace(1, 0, ns(0.006))
        out = body
        out[: len(click)] += click * 0.25
        return fade(out, 0.0005, 0.02)
    if style == "soft":
        dur = decay or 0.35
        n = ns(dur)
        t = np.arange(n) / SR
        f = 52 * tune + (120 * tune) * np.exp(-t / 0.025)
        body = osc_sine(f, n) * env_exp(n, 0.11, attack=0.002)
        return fade(saturate(body, 1.1), 0.001, 0.01)
    # punchy house/techno kick (phone-speaker friendly: knock + click, controlled sub)
    dur = decay or 0.38
    n = ns(dur)
    t = np.arange(n) / SR
    f = 52 * tune + (240 * tune - 52 * tune) * np.exp(-t / 0.02)
    body = osc_sine(f, n) * (0.75 * env_exp(n, 0.12, attack=0.0008) + 0.25 * env_exp(n, 0.03))
    knock = osc_sine(160 * tune * (1 + 0.4 * np.exp(-t / 0.01)), n) * env_exp(n, 0.035, attack=0.0005)
    body = saturate(body * 1.05 + knock * 0.5, 1.8)
    cl = ns(0.005)
    click = band(noise(cl, seed + 11), 2000, 9000, 2) * np.linspace(1, 0, cl) ** 1.5
    body[:cl] += click * 0.55
    body = butter(body, "hp", 32, 2)
    return fade(body, 0.0003, 0.02)


def snare(tone=190.0, seed=1, decay=0.17, snap=1.0):
    n = ns(decay + 0.1)
    t = np.arange(n) / SR
    body = osc_sine(tone * (1 + 0.6 * np.exp(-t / 0.012)), n) * env_exp(n, 0.045, attack=0.0008)
    nz = band(noise(n, seed), 1400, 9000, 2) * env_exp(n, decay * 0.55, attack=0.0008)
    crack = butter(noise(ns(0.01), seed + 3), "hp", 4000) * np.linspace(1, 0, ns(0.01))
    out = body * 0.55 + nz * 1.1 * snap
    out[: len(crack)] += crack * 0.3
    return fade(saturate(out, 1.3), 0.0003, 0.02)


def clap(seed=2, decay=0.22, spread=0.009):
    n = ns(decay + 0.08)
    out = np.zeros(n)
    base = band(noise(n, seed), 900, 3200, 2)
    for k in range(4):
        i0 = ns(k * spread)
        e = np.zeros(n)
        L = ns(0.012) if k < 3 else n - i0
        seg = env_exp(L, 0.005 if k < 3 else decay * 0.45, attack=0.0005)
        e[i0:i0 + L] = seg[: n - i0]
        out += base * e * (0.8 if k < 3 else 1.0)
    out = filt(out, "peak", 1200, 1.2, 3)
    return fade(out, 0.0003, 0.02)


_HAT_FREQS = np.array([205.3, 304.4, 369.6, 522.7, 540.0, 800.0])


def hat(open_=False, seed=3, decay=None, bright=1.0):
    d = decay or (0.32 if open_ else 0.045)
    n = ns(d + 0.03)
    metal = np.zeros(n)
    for f in _HAT_FREQS * 1.63 * bright:
        metal += osc_square(f, n, ph0=np.random.RandomState(seed + int(f)).rand())
    metal /= len(_HAT_FREQS)
    nz = noise(n, seed)
    x = 0.55 * metal + 0.7 * nz
    x = band(x, 6500, 16000, 2)
    x = butter(x, "hp", 7000, 2)
    x *= env_exp(n, d * (0.42 if open_ else 0.33), attack=0.0005)
    return fade(x, 0.0002, 0.01)


def shaker(seed=4, dur=0.09):
    n = ns(dur)
    x = band(noise(n, seed), 5000, 12000, 2)
    e = env_adsr(n, a=0.012, d=0.04, s=0.2, r=0.03)
    return fade(x * e, 0.0005, 0.005)


def rim(seed=5, f=1700.0):
    n = ns(0.06)
    x = filt(noise(n, seed), "bp", f, 8.0) * 4 + osc_sine(f * 0.5, n) * 0.3
    return fade(x * env_exp(n, 0.012), 0.0002, 0.005)


def tom(f=110.0, decay=0.35, seed=6):
    n = ns(decay + 0.05)
    t = np.arange(n) / SR
    x = osc_sine(f * (1 + 0.5 * np.exp(-t / 0.02)), n) * env_exp(n, decay / 3.2, attack=0.001)
    x += band(noise(n, seed), 300, 3000, 1) * env_exp(n, 0.02) * 0.2
    return fade(saturate(x, 1.2), 0.0005, 0.01)


def log_drum(freq=55.0, dur=0.42, seed=7, drive=1.8):
    """Amapiano-style 'log drum' bass: pitch-dropping tone with body."""
    n = ns(dur)
    t = np.arange(n) / SR
    f = freq * (1 + 1.2 * np.exp(-t / 0.018))
    x = osc_tri(f, n) * 0.6 + osc_sine(f, n) * 0.7 + osc_sine(f * 2, n) * 0.12 * np.exp(-t / 0.05)
    x *= env_adsr(n, a=0.002, d=0.12, s=0.55, r=0.08)
    x = saturate(x, drive)
    x = butter(x, "lp", 1800, 2)
    return fade(x, 0.0005, 0.02)


def crash(seed=8, decay=1.8, bright=1.0):
    n = ns(decay + 0.2)
    metal = np.zeros(n)
    rng = np.random.RandomState(seed)
    for k in range(10):
        metal += osc_square(rng.uniform(300, 1200) * bright, n, ph0=rng.rand())
    x = 0.4 * metal / 10 + noise(n, seed)
    x = butter(x, "hp", 3500, 2)
    x = filt(x, "highshelf", 9000, 0.7, -3)
    x *= env_exp(n, decay / 4.0, attack=0.001)
    return fade(x, 0.0005, 0.05)


def reverse_crash(seed=9, dur=1.2):
    c = crash(seed, decay=dur * 1.3)[: ns(dur)]
    return fade(c[::-1] * np.linspace(0.2, 1, ns(dur)) ** 2, 0.02, 0.002)


# ============================================================== TONAL
def sub_note(freq, dur, drive=1.15, glide_from=None, glide_t=0.06):
    n = ns(dur)
    if glide_from:
        t = np.arange(n) / SR
        f = freq + (glide_from - freq) * np.exp(-t / glide_t)
    else:
        f = freq
    x = osc_sine(f, n) + 0.12 * osc_sine(np.asarray(f) * 2, n)
    # upper-harmonic layer so the bass line reads on phone speakers
    mid = butter(osc_saw(np.asarray(f) * 2, n) * 0.5 + osc_square(f, n) * 0.3, "lp", 700, 2)
    x = x * 0.85 + mid * 0.35
    x *= env_adsr(n, a=0.004, d=0.05, s=0.92, r=min(0.05, dur * 0.3))
    return fade(saturate(x, drive + 0.35), 0.001, 0.01)


def bass_808(freq, dur, glide_from=None, seed=0):
    n = ns(dur)
    t = np.arange(n) / SR
    f = np.full(n, freq)
    if glide_from:
        f = freq + (glide_from - freq) * np.exp(-t / 0.07)
    x = osc_sine(f, n) * env_adsr(n, a=0.002, d=0.25, s=0.75, r=min(0.08, dur * 0.3))
    x += 0.06 * osc_sine(f * 2, n) * np.exp(-t / 0.2)
    kickish = osc_sine(f * (1 + 2.0 * np.exp(-t / 0.012)), n) * np.exp(-t / 0.03) * 0.5
    x = saturate(x + kickish, 1.6)
    return fade(x, 0.0005, 0.015)


def bass_pluck(freq, dur, cutoff=1400.0, seed=0):
    n = ns(dur)
    x = osc_saw(freq, n) * 0.6 + osc_square(freq * 0.5, n) * 0.25
    x = filt_sweep(x, "lp", exp_curve(cutoff, 160.0, n, 0.35), q=1.1)
    x *= env_adsr(n, a=0.003, d=0.12, s=0.5, r=min(0.05, dur * 0.3))
    x += osc_sine(freq, n) * 0.45 * env_adsr(n, a=0.003, d=0.1, s=0.9, r=0.04)
    return fade(x, 0.001, 0.01)


def reese(freq, dur, cutoff=700.0, seed=0):
    n = ns(dur)
    x = osc_saw(freq * 1.004, n) + osc_saw(freq * 0.996, n, 0.37) + 0.5 * osc_saw(freq * 0.5, n, 0.11)
    x = butter(x, "lp", cutoff, 4) * 0.4
    x += osc_sine(freq * 0.5, n) * 0.5
    x *= env_adsr(n, a=0.01, d=0.1, s=0.85, r=min(0.08, dur * 0.3))
    return fade(saturate(x, 1.3), 0.002, 0.01)


def supersaw(freq, n, voices=7, detune=0.18, seed=0):
    rng = np.random.RandomState(seed)
    L = np.zeros(n)
    R = np.zeros(n)
    for v in range(voices):
        off = (v - (voices - 1) / 2) / ((voices - 1) / 2 + 1e-9)
        f = freq * 2 ** (off * detune / 12.0)
        s = osc_saw(f, n, ph0=rng.rand())
        pan = off * 0.8
        ang = (pan + 1) * np.pi / 4
        L += s * np.cos(ang)
        R += s * np.sin(ang)
    return np.vstack([L, R]) / np.sqrt(voices)


def pad(freqs, dur, cutoff=2600.0, attack=0.25, release=0.5, seed=0, voices=5, bright_sweep=None):
    n = ns(dur + release)
    out = np.zeros((2, n))
    for i, f in enumerate(freqs):
        out += supersaw(f, n, voices=voices, detune=0.14, seed=seed + i * 17)
    out /= max(1, len(freqs)) ** 0.5
    if bright_sweep:
        out = filt_sweep(out, "lp", exp_curve(bright_sweep[0], bright_sweep[1], n, 0.7), q=0.8, block=128)
    else:
        out = butter(out, "lp", cutoff, 2)
    out = butter(out, "hp", 160, 2)
    e = env_adsr(n, a=attack, d=0.3, s=0.85, r=release)
    return fade(out * e, 0.005, 0.02)


def pluck(freq, dur=0.3, cutoff=5000.0, decay=0.22, seed=0, width=0.4):
    n = ns(dur)
    x = supersaw(freq, n, voices=3, detune=0.08, seed=seed) * 0.8
    x[0] += osc_square(freq, n, 0.1) * 0.25
    x[1] += osc_square(freq, n, 0.6) * 0.25
    x = filt_sweep(x, "lp", exp_curve(cutoff, 400.0, n, 0.45), q=1.0, block=64)
    x *= env_exp(n, decay, attack=0.002)
    mid = (x[0] + x[1]) / 2
    side = (x[0] - x[1]) / 2 * width
    return fade(np.vstack([mid + side, mid - side]), 0.001, 0.01)


def epiano(freq, dur=0.8, seed=0, bright=1.0):
    n = ns(dur)
    t = np.arange(n) / SR
    idx = (2.2 * bright) * np.exp(-t / 0.35) + 0.4
    mod = osc_sine(freq, n) * idx
    ph = np.cumsum(np.full(n, freq) / SR)
    car = np.sin(2 * np.pi * ph + mod)
    tine = osc_sine(freq * 14.0, n) * np.exp(-t / 0.02) * 0.08
    x = (car + tine) * env_adsr(n, a=0.003, d=0.9, s=0.35, r=min(0.2, dur * 0.3))
    return fade(x, 0.001, 0.01)


def bell(freq, dur=1.2, ratio=3.5, index=3.0, decay=0.5, seed=0):
    n = ns(dur)
    t = np.arange(n) / SR
    idx = index * np.exp(-t / (decay * 0.5))
    mod = osc_sine(freq * ratio, n) * idx
    ph = np.cumsum(np.full(n, freq) / SR)
    x = np.sin(2 * np.pi * ph + mod) * env_exp(n, decay, attack=0.0015)
    return fade(x, 0.0005, 0.02)


def stab(freqs, dur=0.25, cutoff=3500.0, seed=0):
    n = ns(dur)
    out = np.zeros((2, n))
    for i, f in enumerate(freqs):
        out += supersaw(f, n, voices=3, detune=0.1, seed=seed + i)
    out = filt_sweep(out, "lp", exp_curve(cutoff, 500, n, 0.5), q=0.9)
    out *= env_exp(n, dur * 0.45, attack=0.002)
    return fade(butter(out, "hp", 180, 2) / max(1, len(freqs)) ** 0.5, 0.001, 0.01)


def organ_stab(freqs, dur=0.22, seed=0):
    n = ns(dur)
    x = np.zeros(n)
    for f in freqs:
        for h, g in ((1, 1.0), (2, 0.5), (3, 0.25), (4, 0.18)):
            x += osc_sine(f * h, n) * g
    x = butter(x, "hp", 200, 2)
    x *= env_adsr(n, a=0.003, d=0.08, s=0.6, r=0.05)
    return fade(x / len(freqs), 0.001, 0.01)


def braam(freq, dur=1.6, seed=0):
    n = ns(dur)
    x = supersaw(freq, n, voices=7, detune=0.25, seed=seed) + supersaw(freq * 0.5, n, voices=5, detune=0.2, seed=seed + 3)
    x = filt_sweep(x, "lp", exp_curve(300, 2200, n, 0.3) * np.r_[np.ones(n // 2), np.linspace(1, 0.5, n - n // 2)], q=1.2, block=128)
    x = saturate(x * 1.2, 1.8)
    x *= env_adsr(n, a=0.03, d=0.4, s=0.6, r=0.5)
    return fade(x, 0.005, 0.05)


# ============================================================== SFX
def impact(size=1.0, seed=20, tail=1.4):
    n = ns(tail + 0.3)
    t = np.arange(n) / SR
    f = 30 + 60 * np.exp(-t / 0.12)
    sub = osc_sine(f, n) * env_exp(n, 0.35 * size, attack=0.001)
    nz = butter(noise(n, seed, "pink"), "lp", 2200, 2) * env_exp(n, 0.12 * size, attack=0.0008)
    cl = ns(0.006)
    click = butter(noise(cl, seed + 1), "hp", 2500) * np.linspace(1, 0, cl)
    x = sub * 0.9 + nz * 0.8
    x[:cl] += click * 0.4
    x = saturate(x * 1.1, 1.3)
    st = reverb(x, t60=2.2, wet=0.35, seed=seed)
    return fade(st, 0.0003, 0.1)


def hit(seed=21, bright=1.0):
    """Short punchy text-slam hit."""
    k = kick("house", tune=1.0, seed=seed, decay=0.3)
    n = len(k)
    nz = band(noise(n, seed), 800, 7000 * bright, 2) * env_exp(n, 0.035, attack=0.0005)
    x = k * 0.8 + nz * 0.7
    return reverb(fade(x, 0.0003, 0.01), t60=0.9, wet=0.18, seed=seed)


def sub_drop(seed=22, dur=1.2):
    n = ns(dur)
    t = np.arange(n) / SR
    f = 28 + 62 * np.exp(-t / 0.25)
    x = osc_sine(f, n) * env_exp(n, dur / 2.5, attack=0.004)
    return fade(saturate(x, 1.2), 0.002, 0.05)


def whoosh(dur=0.55, seed=23, up=True, lo=250.0, hi=5000.0, pan_sweep=True):
    n = ns(dur)
    x = noise(n, seed, "pink") * 1.6
    fc = exp_curve(lo, hi, n, 0.9) if up else exp_curve(hi, lo, n, 0.9)
    x = filt_sweep(x, "bp", fc, q=1.4, block=64)
    u = np.linspace(0, 1, n)
    e = np.sin(np.pi * u ** (0.65 if up else 1.35)) ** 1.6
    x *= e
    if pan_sweep:
        pans = np.linspace(-0.7, 0.7, n) if up else np.linspace(0.7, -0.7, n)
        ang = (pans + 1) * np.pi / 4
        return fade(np.vstack([x * np.cos(ang), x * np.sin(ang)]), 0.003, 0.01)
    return fade(stereo(x), 0.003, 0.01)


def swish(seed=24, dur=0.22):
    return whoosh(dur=dur, seed=seed, up=True, lo=900, hi=9000)


def riser(dur=2.0, seed=25, pitch=True, end_cut=True):
    n = ns(dur)
    u = np.linspace(0, 1, n)
    nz = filt_sweep(noise(n, seed, "white") * 1.2, "hp", exp_curve(300, 9000, n, 1.3), q=0.9, block=64)
    nz = filt(nz, "lp", 14000, 0.7)
    x = nz * (u ** 2.2)
    if pitch:
        f = midi_to_hz(52 + 24 * u ** 1.6)
        tone = supersaw(1.0, n, voices=3, detune=0.2, seed=seed)  # placeholder replaced below
        s = osc_saw(f, n) * 0.5 + osc_saw(f * 1.006, n, 0.3) * 0.5
        s = butter(s, "lp", 6000, 2)
        x = x + s * 0.18 * (u ** 2.6)
    st = stereo(x)
    st = reverb(st, t60=1.4, wet=0.25, seed=seed)[:, :n]
    if end_cut:
        st[:, -ns(0.004):] *= np.linspace(1, 0, ns(0.004))
    return st


def downlifter(dur=1.5, seed=26):
    r = riser(dur, seed, pitch=True, end_cut=False)
    r = r[:, ::-1]
    return fade(r, 0.002, 0.2)


def click(seed=27, f=3200.0, gain=1.0):
    n = ns(0.03)
    x = filt(noise(n, seed), "bp", f, 3.0) * env_exp(n, 0.004, attack=0.0002) * 3.0
    x += osc_sine(f * 0.6, n) * env_exp(n, 0.003) * 0.3
    return fade(x * gain, 0.0001, 0.003)


def tick(seed=28, f=5200.0):
    return click(seed, f, 0.6)


def pop(seed=29, f0=900.0, f1=260.0):
    n = ns(0.07)
    t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t / 0.012)
    x = osc_sine(f, n) * env_exp(n, 0.02, attack=0.0008)
    return fade(x, 0.0003, 0.004)


def ding(note=88, seed=30, dur=1.4, ratio=3.5, index=2.4, decay=0.45):
    x = bell(midi_to_hz(note), dur=dur, ratio=ratio, index=index, decay=decay, seed=seed)
    x += 0.35 * bell(midi_to_hz(note + 12), dur=dur, ratio=2.0, index=1.0, decay=decay * 0.5)
    return reverb(x * 0.6, t60=1.6, wet=0.28, seed=seed)


def chime(notes=(84, 88), gap=0.09, seed=31):
    n = ns(1.6 + gap * len(notes))
    out = np.zeros((2, n))
    for i, m in enumerate(notes):
        d = ding(m, seed + i, dur=1.3, index=1.6, decay=0.4)
        i0 = ns(i * gap)
        L = min(d.shape[1], n - i0)
        out[:, i0:i0 + L] += d[:, :L] * (0.8 if i == 0 else 1.0)
    return out


def buzz_wrong(seed=32):
    n = ns(0.32)
    x = osc_square(138.0, n) * 0.5 + osc_saw(141.0, n) * 0.5
    x = band(x, 200, 2400, 2)
    e = np.zeros(n)
    for k in range(2):
        i0 = ns(k * 0.14)
        L = ns(0.12)
        e[i0:i0 + L] = env_adsr(L, a=0.002, d=0.05, s=0.7, r=0.02)
    return fade(x * e, 0.001, 0.01)


def shutter(seed=33):
    n = ns(0.2)
    x = np.zeros(n)
    for k, (t0, f, g) in enumerate(((0.0, 2500, 1.0), (0.055, 1800, 0.8))):
        i0 = ns(t0)
        L = ns(0.03)
        seg = filt(noise(L, seed + k), "bp", f, 2.0) * env_exp(L, 0.005, attack=0.0002) * 3
        x[i0:i0 + L] += seg * g
    x += filt(noise(n, seed + 5), "bp", 5200, 4.0) * env_exp(n, 0.02) * 0.3
    return fade(x, 0.0001, 0.01)


def typing(count=8, span=0.8, seed=34):
    rng = np.random.RandomState(seed)
    n = ns(span + 0.05)
    x = np.zeros(n)
    times = np.sort(rng.uniform(0, span, count))
    for i, t0 in enumerate(times):
        c = click(seed + i, f=rng.uniform(2200, 4200), gain=rng.uniform(0.5, 1.0))
        i0 = ns(t0)
        L = min(len(c), n - i0)
        x[i0:i0 + L] += c[:L]
    return x


def notif(seed=35, notes=(83, 90)):
    n = ns(0.9)
    out = np.zeros(n)
    for i, m in enumerate(notes):
        L = ns(0.5)
        f = midi_to_hz(m)
        s = (osc_sine(f, L) + 0.25 * osc_sine(f * 2, L)) * env_exp(L, 0.12, attack=0.004)
        i0 = ns(i * 0.13)
        out[i0:i0 + L] += s[: n - i0]
    return reverb(fade(out, 0.001, 0.02), t60=0.9, wet=0.18, seed=seed)


def glitch(dur=0.35, seed=36):
    rng = np.random.RandomState(seed)
    n = ns(dur)
    x = np.zeros(n)
    i = 0
    while i < n:
        L = ns(rng.uniform(0.008, 0.04))
        kind = rng.randint(3)
        if kind == 0:
            seg = osc_square(rng.uniform(300, 2500), L)
        elif kind == 1:
            seg = noise(L, rng.randint(1000))
        else:
            seg = np.zeros(L)
        seg = np.round(seg * 6) / 6  # crush
        x[i:i + L] += seg[: n - i] * rng.uniform(0.2, 0.6)
        i += L + ns(rng.uniform(0.0, 0.02))
    x = band(x, 300, 9000, 1)
    return fade(x, 0.001, 0.01)


def scan(dur=0.8, seed=37):
    n = ns(dur)
    t = np.arange(n) / SR
    x = noise(n, seed) * (0.5 + 0.5 * np.sin(2 * np.pi * 18 * t))
    x = filt_sweep(x, "bp", exp_curve(1200, 6000, n, 1.0), q=3.0)
    x *= np.sin(np.pi * np.linspace(0, 1, n)) ** 0.8
    return fade(x * 0.8, 0.005, 0.02)


def stamp(seed=38):
    n = ns(0.35)
    t = np.arange(n) / SR
    thump = osc_sine(70 + 60 * np.exp(-t / 0.02), n) * env_exp(n, 0.06, attack=0.0005)
    slap = butter(noise(n, seed), "lp", 3500, 2) * env_exp(n, 0.02, attack=0.0003)
    x = thump * 0.9 + slap * 0.9
    return reverb(fade(saturate(x, 1.3), 0.0002, 0.01), t60=0.6, wet=0.12, seed=seed)


def counter_ticks(times, seed=39, f=4200.0):
    """times relative to start; returns (mono array, duration)."""
    if len(times) == 0:
        return np.zeros(1)
    n = ns(max(times) + 0.05)
    x = np.zeros(n)
    for i, t0 in enumerate(times):
        c = tick(seed + i, f=f * (1 + 0.15 * (i / max(1, len(times) - 1))))
        i0 = ns(t0)
        L = min(len(c), n - i0)
        x[i0:i0 + L] += c[:L]
    return x


def heartbeat(seed=40):
    n = ns(0.8)
    x = np.zeros(n)
    for t0, g in ((0.0, 1.0), (0.22, 0.7)):
        k = kick("soft", tune=0.8, decay=0.25)
        i0 = ns(t0)
        x[i0:i0 + len(k)] += k[: n - i0] * g
    return butter(x, "lp", 400, 2)


def sparkle(seed=41, base=96):
    rng = np.random.RandomState(seed)
    n = ns(1.2)
    out = np.zeros((2, n))
    for i in range(5):
        m = base + [0, 4, 7, 12, 16][i]
        b = bell(midi_to_hz(m), dur=0.8, ratio=2.0, index=1.2, decay=0.25) * 0.25
        i0 = ns(i * 0.045)
        st = pan_mono(b, rng.uniform(-0.6, 0.6))
        L = min(st.shape[1], n - i0)
        out[:, i0:i0 + L] += st[:, :L]
    return reverb(out, t60=1.5, wet=0.3, seed=seed)


def bass_hit(freq=41.2, seed=42):
    return sub_note(freq, 0.9, drive=1.4)


def tape_stop(x, dur=0.5):
    """Apply a tape-stop (slow down to zero) to the start of stereo x over dur."""
    xs = stereo(x)
    n = ns(dur)
    n = min(n, xs.shape[1])
    u = np.linspace(0, 1, n)
    speed = (1 - u) ** 1.5
    pos = np.cumsum(speed)
    pos = np.clip(pos, 0, xs.shape[1] - 1)
    i0 = np.floor(pos).astype(int)
    fr = pos - i0
    i1 = np.clip(i0 + 1, 0, xs.shape[1] - 1)
    y = xs[:, i0] * (1 - fr) + xs[:, i1] * fr
    return y * np.linspace(1, 0, n) ** 0.5
