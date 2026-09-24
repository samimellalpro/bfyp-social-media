"""BFYP Vault V2 — original music generator driven by the edit timeline.

A track is described by style, bpm, key, progression and a list of sections
(start beat, type). Everything is synthesized; nothing is sampled.
"""
import numpy as np
import instruments as I
from dsp import (SR, ns, db, Bus, stereo, pan_mono, butter, filt, filt_sweep, exp_curve, reverb, delay,
                 chorus, compress, duck_curve, saturate, midi_to_hz)

NOTE = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7,
        "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
SCALES = {
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "major": [0, 2, 4, 5, 7, 9, 11],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "harm": [0, 2, 3, 5, 7, 8, 11],
}
ROMAN = {"i": 0, "ii": 1, "iii": 2, "iv": 3, "v": 4, "vi": 5, "vii": 6}


def parse_chord(sym, key_root, mode):
    """Roman numeral with optional suffix: 'i', 'VI', 'iv7', 'VII', 'i9', 'V' (major V in minor)."""
    base = ""
    for ch in sym:
        if ch.lower() in "iv":
            base += ch
        else:
            break
    suffix = sym[len(base):]
    deg = ROMAN[base.lower()]
    scale = SCALES[mode]
    root = key_root + scale[deg]
    # triad quality from scale unless numeral case forces it
    third = scale[(deg + 2) % 7] - scale[deg]
    fifth = scale[(deg + 4) % 7] - scale[deg]
    third %= 12
    fifth %= 12
    if base.isupper():
        third = 4
        if fifth != 7:
            fifth = 7
    elif base.islower():
        third = 3 if third in (3,) else (3 if base.islower() else third)
    ints = [0, third, fifth]
    if "7" in suffix:
        seventh = scale[(deg + 6) % 7] - scale[deg]
        ints.append(seventh % 12 if seventh % 12 else 10)
    if "9" in suffix:
        seventh = (scale[(deg + 6) % 7] - scale[deg]) % 12
        ints += [seventh, 14]
    if "sus2" in suffix:
        ints[1] = 2
    if "sus4" in suffix:
        ints[1] = 5
    if "add9" in suffix:
        ints.append(14)
    return root % 12, sorted(set(ints))


def voice_chord(root_pc, ints, prev=None, lo=55, hi=75, n_notes=4):
    pcs = [(root_pc + i) % 12 for i in ints]
    cands = []
    # build candidate voicings: choose notes of pcs in range, pick sets of n_notes closest spread
    pool = [m for m in range(lo, hi + 1) if m % 12 in pcs]
    import itertools
    best = None
    for combo in itertools.combinations(pool, min(n_notes, len(pool))):
        got = set(m % 12 for m in combo)
        if not set(pcs[:3]).issubset(got):
            continue
        span = combo[-1] - combo[0]
        if span > 16:
            continue
        if prev is None:
            cost = abs(np.mean(combo) - (lo + hi) / 2) + span * 0.1
        else:
            cost = sum(min(abs(c - p) for p in prev) for c in combo) + 0.2 * span
        if best is None or cost < best[0]:
            best = (cost, combo)
    return list(best[1]) if best else [root_pc + 60 + i for i in ints[:n_notes]]


class Track:
    def __init__(self, style, bpm, key="A", mode="minor", prog=("i", "VI", "III", "VII"), dur=20.0,
                 sections=None, events=None, seed=1, chords_per_bar=1, swing=0.0, gain=None):
        self.style = style
        self.bpm = bpm
        self.beat = 60.0 / bpm
        self.bar = 4 * self.beat
        self.step = self.beat / 4
        self.key = NOTE[key] if isinstance(key, str) else key
        self.mode = mode
        self.prog = list(prog)
        self.dur = dur
        self.sections = sections or [{"beat": 0, "type": "drop"}]
        self.events = events or []
        self.seed = seed
        self.rng = np.random.RandomState(seed)
        self.cpb = chords_per_bar
        self.swing = swing
        self.gain = gain or {}
        self.kick_times = []
        n_bars = int(np.ceil(dur / self.bar)) + 1
        self.n_bars = n_bars
        # chords
        self.chords = []
        prev = None
        for b in range(n_bars * self.cpb):
            sym = self.prog[b % len(self.prog)]
            rpc, ints = parse_chord(sym, self.key, mode)
            v = voice_chord(rpc, ints, prev)
            prev = v
            bass_root = 28 + ((rpc - 4) % 12)  # E1..D#2 range
            self.chords.append({"root": rpc, "ints": ints, "voicing": v, "bass": bass_root, "sym": sym})
        # buses
        self.drums = Bus(dur)
        self.bass = Bus(dur)
        self.harm = Bus(dur)
        self.lead = Bus(dur)
        self.fx = Bus(dur)

    # ---------------------------------------------------------------- helpers
    def t_of(self, bar, step):
        sw = 0.0
        if self.swing and step % 2 == 1:
            sw = self.swing * self.step
        return bar * self.bar + step * self.step + sw

    def section_at(self, t):
        cur = self.sections[0]
        for s in self.sections:
            if s["beat"] * self.beat <= t + 1e-6:
                cur = s
        return cur["type"]

    def chord_at(self, bar, step=0):
        idx = bar * self.cpb + int(step // (16 / self.cpb))
        return self.chords[min(idx, len(self.chords) - 1)]

    def active(self, t):
        return t < self.dur + 0.05

    def g(self, name, default=1.0):
        return self.gain.get(name, default)

    # ---------------------------------------------------------------- render
    def render(self):
        style = STYLES[self.style]
        for bar in range(self.n_bars):
            for step in range(16):
                t = self.t_of(bar, step)
                if t >= self.dur:
                    continue
                sec = self.section_at(t)
                style(self, bar, step, t, sec)
        return self.mix()

    # instrument placement shortcuts
    def K(self, t, v=1.0, kind="house", tune=1.0):
        self.drums.add(I.kick(kind, tune, seed=int(t * 1000) % 97), t, 0.95 * v * self.g("kick"))
        self.kick_times.append(t)

    def S(self, t, v=1.0, clap=False):
        x = I.clap(seed=int(t * 100) % 13) if clap else I.snare(seed=int(t * 100) % 13)
        st = reverb(x, t60=1.1, wet=0.22, seed=3)
        self.drums.add(st, t, 0.62 * v * self.g("snare"))

    def H(self, t, v=1.0, open_=False, pan=0.15):
        x = I.hat(open_, seed=int(t * 1000) % 31)
        self.drums.add(pan_mono(x, pan), t, (0.42 if not open_ else 0.34) * v * self.g("hat"))

    def SH(self, t, v=1.0, pan=-0.25):
        self.drums.add(pan_mono(I.shaker(seed=int(t * 1000) % 29), pan), t, 0.3 * v * self.g("shaker"))

    def P(self, t, v=1.0, kind="rim", f=1700.0, pan=0.3):
        x = I.rim(f=f, seed=int(t * 1000) % 17) if kind == "rim" else I.tom(f, seed=int(t * 1000) % 17)
        self.drums.add(pan_mono(x, pan), t, 0.28 * v * self.g("perc"))

    def B(self, t, midi, dur, v=1.0, kind="sub", glide_from=None):
        f = midi_to_hz(midi)
        if kind == "sub":
            x = I.sub_note(f, dur, glide_from=midi_to_hz(glide_from) if glide_from else None)
            gain = 0.62
        elif kind == "808":
            x = I.bass_808(f, dur, glide_from=midi_to_hz(glide_from) if glide_from else None)
            gain = 0.6
        elif kind == "pluck":
            x = I.bass_pluck(f, dur)
            gain = 0.5
        elif kind == "reese":
            x = I.reese(f, dur)
            gain = 0.5
        elif kind == "log":
            x = I.log_drum(f, dur)
            gain = 0.55
        self.bass.add(x, t, gain * v * self.g("bass"))

    def PAD(self, t, midis, dur, v=1.0, cutoff=2600.0, sweep=None, attack=0.25):
        x = I.pad(midi_to_hz(np.array(midis)), dur, cutoff=cutoff, bright_sweep=sweep, attack=attack, seed=int(t * 10) % 50)
        self.harm.add(x, t, 0.2 * v * self.g("pad"))

    def STAB(self, t, midis, dur=0.25, v=1.0, cutoff=3500.0, organ=False):
        if organ:
            x = stereo(I.organ_stab(midi_to_hz(np.array(midis)), dur))
        else:
            x = I.stab(midi_to_hz(np.array(midis)), dur, cutoff=cutoff, seed=int(t * 10) % 50)
        self.harm.add(x, t, 0.34 * v * self.g("stab"))

    def EP(self, t, midis, dur=0.9, v=1.0):
        for i, m in enumerate(midis):
            x = I.epiano(midi_to_hz(m), dur)
            self.harm.add(pan_mono(x, (i - len(midis) / 2) * 0.15), t + i * 0.008, 0.16 * v * self.g("ep"))

    def PL(self, t, midi, dur=0.3, v=1.0, cutoff=5000.0, pan=0.0):
        x = I.pluck(midi_to_hz(midi), dur, cutoff=cutoff, seed=int(t * 100) % 40)
        self.lead.add(x, t, 0.2 * v * self.g("pluck"))

    def BL(self, t, midi, dur=0.8, v=1.0, pan=0.0):
        x = I.bell(midi_to_hz(midi), dur, ratio=3.5, index=1.8, decay=0.3)
        self.lead.add(pan_mono(x, pan), t, 0.16 * v * self.g("bell"))

    # ---------------------------------------------------------------- mixing
    def apply_events(self, mix):
        n = mix.shape[1]
        for e in self.events:
            kind = e["type"]
            t0 = e.get("beat", 0) * self.beat if "beat" in e else e.get("t", 0)
            if kind == "stop":
                t1 = t0 + e.get("beats", 1) * self.beat
                i0, i1 = ns(t0), ns(t1)
                f = ns(0.01)
                w = np.ones(n)
                w[i0:i1] = 0
                w[max(0, i0 - f):i0] = np.linspace(1, 0, min(f, i0))
                w[i1:i1 + f] = np.linspace(0, 1, len(w[i1:i1 + f]))
                mix = mix * w
            elif kind == "tapestop":
                d = e.get("beats", 1) * self.beat
                i0 = ns(t0)
                seg = mix[:, i0:i0 + ns(d) * 2]
                ts = I.tape_stop(seg, d)
                mix[:, i0:i0 + ts.shape[1]] = ts
                mix[:, i0 + ts.shape[1]: i0 + ns(d)] = 0
            elif kind == "lpf":
                t1 = t0 + e.get("beats", 4) * self.beat
                i0, i1 = ns(t0), min(n, ns(t1))
                f0 = e.get("f0", 600.0)
                f1 = e.get("f1", 18000.0)
                seg = mix[:, i0:i1]
                if seg.shape[1] > 256:
                    mix[:, i0:i1] = filt_sweep(seg, "lp", exp_curve(f0, f1, seg.shape[1], e.get("shape", 1.5)), q=0.8, block=128)
            elif kind == "end":
                i0 = ns(t0)
                # let a short tail ring then silence music
                tail = ns(e.get("tail", 0.35))
                if i0 < n:
                    w = np.ones(n)
                    w[i0:i0 + tail] = np.linspace(1, 0, len(w[i0:i0 + tail])) ** 2
                    w[i0 + tail:] = 0
                    mix = mix * w
        return mix

    def mix(self):
        n = self.drums.x.shape[1]
        duck = duck_curve(n, self.kick_times, depth=0.55, release=0.9 * self.beat / 2)
        duck_h = duck_curve(n, self.kick_times, depth=0.35, release=0.9 * self.beat / 2)
        drums = compress(self.drums.x, thresh_db=-14, ratio=2.5, attack=0.004, release=0.09, makeup_db=1.0)
        drums = saturate(drums * 1.0, 1.15)
        bass = self.bass.x * duck
        bass = butter(bass, "lp", 5000, 2)
        # keep bass mono below 150 Hz
        bm = bass.mean(axis=0)
        low = butter(bm, "lp", 150, 2)
        bass = stereo(low) + (bass - stereo(butter(bass.mean(axis=0), "lp", 150, 2)))
        harm = filt(chorus(self.harm.x, depth_ms=4, rate=0.25, mix=0.25), "highshelf", 7000, 0.7, 3.0)
        harm = reverb(harm, t60=2.2, wet=0.28, seed=11, dark=3000) * duck_h
        lead = filt(delay(self.lead.x, time=self.beat * 0.75, fb=0.32, mix=0.22), "highshelf", 6000, 0.7, 2.5)
        lead = reverb(lead, t60=1.8, wet=0.22, seed=12) * duck_h
        fx = self.fx.x
        # loudness-based stem balance (K-weighted), keeps every style consistent
        tgt = dict(BALANCE)
        tgt.update(STYLE_BALANCE.get(self.style, {}))
        stems = {"drums": drums, "bass": bass, "harm": harm, "lead": lead}
        for k, s in stems.items():
            L = _stem_lufs(s[:, : ns(self.dur)])
            if L is not None:
                stems[k] = s * db(tgt[k] - L)
        drums, bass, harm, lead = stems["drums"], stems["bass"], stems["harm"], stems["lead"]
        mix = drums * self.g("drums_bus", 1.0) + bass + harm + lead + fx
        mix = self.apply_events(mix)
        return mix[:, : ns(self.dur + 2.5)]


BALANCE = {"drums": -17.0, "bass": -21.5, "harm": -20.0, "lead": -22.0}
STYLE_BALANCE = {
    "cinematic": {"drums": -19.0, "harm": -19.0, "bass": -21.0},
    "amapiano": {"bass": -19.0, "harm": -20.0},
    "minimal": {"lead": -21.5},
    "futurebass": {"harm": -19.0},
}


def _stem_lufs(x):
    import pyloudnorm as pyln
    if np.max(np.abs(x)) < 1e-5:
        return None
    try:
        L = pyln.Meter(SR).integrated_loudness(stereo(x).T)
    except Exception:
        return None
    return L if np.isfinite(L) else None


# ======================================================================= STYLES
def _intensity(sec):
    return {"hook": 2, "tension": 1, "build": 1, "drop": 3, "break": 1, "cta": 3, "calm": 1}.get(sec, 2)


def st_techhouse(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if step % 4 == 0 and (I_ >= 2 or (sec == "build")):
        T.K(t, 1.0)
    if sec == "tension" and step in (0, 8):
        T.K(t, 0.7, "soft")
    if step in (4, 12) and I_ >= 2:
        T.S(t, 0.9, clap=True)
    if step % 4 == 2:
        T.H(t, 0.9 if I_ >= 2 else 0.5, open_=(I_ >= 3))
    if step % 2 == 1 and I_ >= 2:
        T.SH(t, 0.6 + 0.3 * (step % 4 == 3))
    if sec == "build" and bar % 2 == 1 and step >= 8:
        T.S(t, 0.3 + 0.05 * (step - 8), clap=False)
    # rolling bass: offbeat 16ths
    if I_ >= 2 and step % 4 in (2, 3):
        T.B(t, ch["bass"] + (12 if step % 4 == 3 else 0), T.step * 0.9, 0.9, "pluck")
    if sec == "tension" and step % 4 == 2:
        T.B(t, ch["bass"], T.step * 1.8, 0.7, "sub")
    # stabs
    if I_ >= 2 and step in (3, 6, 11):
        T.STAB(t, v, T.step * 1.6, 0.8 if I_ == 3 else 0.55, cutoff=6500 if I_ == 3 else 2400)
    if I_ >= 3 and step == 0:
        T.PAD(t, v, T.bar * 0.98, 0.8, cutoff=5200)
    if sec in ("tension", "break") and step == 0:
        T.PAD(t, v, T.bar * 0.98, 0.9, cutoff=1100)
    if I_ >= 3 and step % 2 == 0:
        arp = sorted(v)
        T.PL(t, arp[(step // 2) % len(arp)] + 12, T.step * 1.8, 0.6, cutoff=6500)


def st_garage(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if I_ >= 2 and step in (0, 7, 10) or (sec == "tension" and step == 0):
        T.K(t, 1.0 if step == 0 else 0.8)
    if I_ >= 2 and step in (4, 12):
        T.S(t, 0.95, clap=(bar % 2 == 0))
    if step % 2 == 1 or (I_ >= 3 and step % 2 == 0 and step % 4 != 0):
        T.H(t, 0.7 if step % 2 == 1 else 0.4)
    if I_ >= 3 and step in (2, 14):
        T.H(t, 0.6, open_=True)
    if step in (0, 6, 10) and I_ >= 2:
        T.B(t, ch["bass"] + 12 if step == 10 else ch["bass"], T.step * (5 if step == 0 else 3), 1.0, "sub")
    if sec == "tension" and step == 0:
        T.B(t, ch["bass"], T.bar * 0.9, 0.8, "sub")
    if I_ >= 2 and step in (2, 5, 13):
        T.STAB(t, v, T.step * 1.2, 0.6 if I_ == 2 else 0.8, organ=True)
    if I_ >= 3 and step == 0:
        T.PAD(t, v, T.bar, 0.6, cutoff=4200)
    if sec in ("tension", "break") and step == 0:
        T.PAD(t, v, T.bar, 0.8, cutoff=900)
    if I_ >= 3 and step in (8, 9, 11):
        T.BL(t, sorted(v)[[0, 2, 1][[8, 9, 11].index(step)] % len(v)] + 12, 0.5, 0.5, pan=0.3)


def st_trap(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    # half-time: bar has snare on step 8
    if I_ >= 2 and step in ((0, 7, 11) if bar % 2 == 0 else (0, 3, 10)):
        T.K(t, 1.0, "house", 0.9)
    if I_ >= 2 and step == 8:
        T.S(t, 1.0, clap=True)
        T.S(t, 0.5, clap=False)
    # hats: 8ths with rolls
    if I_ >= 1 and step % 2 == 0:
        T.H(t, 0.7)
    if I_ >= 2 and bar % 2 == 1 and step >= 12:
        for k in range(3):
            T.H(t + k * T.step / 3, 0.35 + 0.1 * k)
    # 808
    if I_ >= 2 and step in ((0, 7, 11) if bar % 2 == 0 else (0, 10)):
        glide = ch["bass"] + 12 if (step == 10) else None
        T.B(t, ch["bass"] + (12 if step == 11 else 0), T.step * (6 if step == 0 else 3), 0.95, "808", glide_from=glide)
    if sec == "tension" and step == 0:
        T.B(t, ch["bass"], T.bar * 0.8, 0.7, "808")
    if step == 0:
        T.PAD(t, v, T.bar, 0.7 if I_ >= 2 else 0.9, cutoff=2000 if I_ < 3 else 4200)
    # bell melody
    if I_ >= 2 and step in (0, 3, 6, 10, 12):
        mel = sorted(v)
        seqs = [mel[0] + 12, mel[2] + 12, mel[1] + 12, mel[-1] + 12, mel[2] + 12]
        T.BL(t, seqs[[0, 3, 6, 10, 12].index(step)], 0.6, 0.55, pan=-0.2)


def st_futurebass(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if I_ >= 2 and step in (0, 10):
        T.K(t, 1.0)
    if I_ >= 2 and step == 8:
        T.S(t, 1.0, clap=True)
    if step % 2 == 0 and I_ >= 2:
        T.H(t, 0.55)
    if I_ >= 3 and step in (0, 3, 6, 8, 11, 14):
        T.STAB(t, v + [v[0] + 12], T.step * 2.4, 0.9, cutoff=6000)
    elif I_ == 2 and step in (0, 6, 12):
        T.STAB(t, v, T.step * 2.0, 0.6, cutoff=2500)
    if sec in ("tension", "break") and step == 0:
        T.PAD(t, v, T.bar, 0.9, cutoff=1400)
    if step in (0, 8) and I_ >= 2:
        T.B(t, ch["bass"] + 12, T.step * 7, 0.9, "sub")
    if I_ >= 3 and step % 2 == 1:
        T.PL(t, sorted(v)[(step // 2) % len(v)] + 24, T.step * 1.5, 0.35, cutoff=7000)


def st_synthwave(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if I_ >= 2 and step in (0, 8):
        T.K(t, 1.0, "house", 0.95)
    if I_ >= 2 and step in (4, 12):
        T.S(t, 1.0, clap=False)
    if I_ >= 1 and step % 2 == 0:
        T.H(t, 0.45)
    # 16th arpeggiated octave bass
    if I_ >= 2 or sec == "build":
        T.B(t, ch["bass"] + (12 if step % 2 else 0) + 12, T.step * 0.9, 0.75, "pluck")
    elif sec == "tension" and step % 4 == 0:
        T.B(t, ch["bass"] + 12, T.step * 3.5, 0.7, "pluck")
    if step == 0:
        T.PAD(t, v, T.bar, 0.8, cutoff=3800 if I_ >= 2 else 1500)
    if I_ >= 3 and step % 2 == 0:
        arp = sorted(v) + [sorted(v)[0] + 12]
        T.PL(t, arp[(step // 2) % len(arp)] + 12, T.step * 1.8, 0.55, cutoff=7000)


def st_minimal(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if step % 4 == 0 and I_ >= 2:
        T.K(t, 0.9, "house", 1.05)
    if sec == "tension" and step == 0:
        T.K(t, 0.6, "soft")
    if step in (4, 12) and I_ >= 3:
        T.S(t, 0.55, clap=True)
    if step % 4 == 2:
        T.H(t, 0.6 if I_ >= 2 else 0.35)
    if step in (3, 7, 14) and I_ >= 1:
        T.P(t, 0.7, "rim", f=1500 + 300 * (step % 3), pan=0.35 if step == 7 else -0.3)
    if step % 2 == 0 and I_ >= 2:
        T.B(t, ch["bass"] + (12 if step % 8 == 6 else 0), T.step * 1.6, 0.75, "sub")
    if sec == "tension" and step in (0, 6, 10):
        T.B(t, ch["bass"], T.step * 2, 0.6, "sub")
    if step in (0, 3, 6, 9, 12) and I_ >= 2:
        mel = sorted(v)
        T.BL(t, mel[(step // 3) % len(mel)] + 12, 0.45, 0.5, pan=0.25 if step % 2 else -0.25)
    if step == 0:
        T.PAD(t, v, T.bar, 0.55, cutoff=1800 if I_ < 3 else 4000)


def st_amapiano(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if step in (0, 8) and I_ >= 2:
        T.K(t, 0.9, "soft", 1.0)
    if step in (4, 12) and I_ >= 2:
        T.S(t, 0.6, clap=True)
    if step % 1 == 0 and I_ >= 1:
        T.SH(t, 0.5 + 0.35 * (step % 4 == 2), pan=-0.3)
    if step in (6, 14) and I_ >= 2:
        T.P(t, 0.6, "rim", 1900, pan=0.35)
    # log drum pattern
    pat = (0, 3, 6, 10, 11, 14) if bar % 2 == 0 else (0, 3, 7, 10, 13)
    if step in pat and I_ >= 2:
        T.B(t, ch["bass"] + 12 + (0 if step % 3 else 0), T.step * 2.2, 0.85, "log")
    if sec in ("tension",) and step in (0, 6, 10):
        T.B(t, ch["bass"] + 12, T.step * 2, 0.7, "log")
    if step in (0, 6, 12) and I_ >= 1:
        T.EP(t, v, T.step * 5, 0.8 if I_ >= 2 else 0.6)
    if I_ >= 3 and step == 0:
        T.PAD(t, v, T.bar, 0.45, cutoff=3800)


def st_dnb(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    if I_ >= 2 and step in (0, 10):
        T.K(t, 1.0)
    if I_ >= 2 and step in (4, 12):
        T.S(t, 1.0, clap=False)
    if I_ >= 2 and step % 2 == 0:
        T.H(t, 0.5)
    if I_ >= 3 and step % 4 == 2:
        T.SH(t, 0.5)
    if step == 0 and I_ >= 2:
        T.B(t, ch["bass"] + 12, T.bar * 0.5, 0.8, "reese")
    if step == 8 and I_ >= 2:
        T.B(t, ch["bass"] + 12, T.bar * 0.45, 0.7, "reese")
    if sec in ("tension", "break") and step == 0:
        T.B(t, ch["bass"] + 12, T.bar * 0.9, 0.6, "sub")
    if step == 0:
        T.PAD(t, v, T.bar, 0.7, cutoff=2200 if I_ < 3 else 4600)
    if I_ >= 3 and step % 4 == 0:
        T.PL(t, sorted(v)[(step // 4) % len(v)] + 12, T.step * 3, 0.45, cutoff=4500)


def st_cinematic(T, bar, step, t, sec):
    I_ = _intensity(sec)
    ch = T.chord_at(bar, step)
    v = ch["voicing"]
    # ticking suspense
    if step % 2 == 0:
        T.P(t, 0.55 if I_ < 3 else 0.35, "rim", 2600, pan=0.2 if step % 4 else -0.2)
    if I_ <= 1 and step in (0, 8):
        T.P(t, 0.9, "tom", 70, pan=0.0)
    if step == 0 and I_ <= 2:
        T.B(t, ch["bass"] + 12, T.bar * 0.95, 0.75, "sub")
    if step == 0:
        T.PAD(t, v, T.bar, 0.9, sweep=(700, 4800) if I_ >= 2 else (500, 1800))
    if I_ >= 3:
        if step in (0, 7, 10):
            T.K(t, 1.0, "house", 0.9)
            T.B(t, ch["bass"] + 12, T.step * 3, 0.9, "808")
        if step == 8:
            T.S(t, 1.0, clap=True)
        if step % 2 == 0:
            T.H(t, 0.5)


STYLES = {
    "techhouse": st_techhouse,
    "garage": st_garage,
    "trap": st_trap,
    "futurebass": st_futurebass,
    "synthwave": st_synthwave,
    "minimal": st_minimal,
    "amapiano": st_amapiano,
    "dnb": st_dnb,
    "cinematic": st_cinematic,
}
