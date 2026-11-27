"""Sound design: a spotlight clunk in an empty hall, ghostly laughter and murmurs, seats folding as people leave,
lights switching off bank by bank, guitar practice under a work light, real applause, then silence."""
import numpy as np
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def pluck(f, gain=0.3, length=1.4):
    """Karplus-Strong plucked string."""
    n = int(length * X.SR)
    p = int(X.SR / f)
    buf = np.random.default_rng(int(f)).uniform(-1, 1, p).astype(np.float32)
    out = np.zeros(n, dtype=np.float32)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = 0.996 * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return out * gain


def strum(chord, gain=0.25):
    s = np.zeros(int(1.6 * X.SR), dtype=np.float32)
    for j, f in enumerate(chord):
        p = pluck(f, gain)
        a = int(j * 0.012 * X.SR)
        s[a:a + len(p)] += p[:len(s) - a]
    return s


CHORDS = [(110.0, 164.8, 220.0, 277.2, 329.6), (98.0, 146.8, 196.0, 246.9, 293.7), (130.8, 196.0, 261.6, 329.6, 392.0), (146.8, 220.0, 293.7, 370.0, 440.0)]


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[10][1], 0.03, 60), 0.0)                       # room tone
    m.add(X.clank(0.6, 0.35, 1.0), w[0][0] + 0.15)
    m.add(X.low_hit(0.5), w[0][0] + 0.15)
    st, en = w[1]
    for j in range(10):  # ghostly "ha" bursts
        b = X.lp(X.noise(0.18), 10) * X.env_ad(int(0.18 * SR), 0.01, 12)
        m.add(b * 0.2, st + j * (en - st) / 10, pan=rng.uniform(-0.7, 0.7))
    m.bed(X.murmur(w[3][1] - w[1][0], 0.08), w[1][0])
    st, en = w[3]
    for j in range(8):  # seats flipping up as people leave
        m.add(X.thud(0.25, 2.0, 0.2), st + (en - st) * rng.uniform(0.1, 0.9), pan=rng.uniform(-0.8, 0.8))
    st, en = w[5]
    for j in range(5):
        m.add(X.clank(0.4, 0.5, 0.6), st + 0.2 + j * (en - st) * 0.12, pan=-0.6 + j * 0.3)
    st, en = w[7]
    k, c = st + 0.1, 0
    while k < en - 0.3:  # practice
        m.add(strum(CHORDS[c % 4], 0.22), k, pan=0.1)
        k += 0.75
        c += 1
    st, en = w[8]
    m.bed(X.applause(en - st + 1.5, 0.45), st)
    k, c = st, 0
    while k < w[10][1] - 0.5:  # the performer keeps playing through the applause and the silence
        m.add(strum(CHORDS[c % 4], 0.2), k, pan=0.1)
        k += 0.75
        c += 1
    m.add(X.chime(0.25, 329.6, 4.0), w[10][0] + 0.2)
