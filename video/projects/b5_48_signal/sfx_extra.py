"""Oscilloscope beeps, radio static and crackle across the noise valley, a sonar-like ping for every pulse,
a rising carrier tone as the pulses fuse into a beam, then a lock-on chime and a warm swell."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def ping(gain=0.25, f=1320.0):
    return X.chime(gain, f, 1.2, (1, 2.0))


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    for j in range(3):
        m.add(ping(0.2, 880.0), st + 1.0 + j * 1.0)
    st, en = w[1][0], w[3][0] + (w[3][1] - w[3][0]) * 0.4
    m.add(X.faded(X.hp(X.noise(en - st), 1) * 0.5, 0.6, 1.0, 0.1), st)
    for j in range(int((en - st) / 0.23)):
        if rng.random() < 0.5:
            m.add(X.spark(0.08), st + j * 0.23, pan=rng.uniform(-0.6, 0.6))
    a, b = w[1]
    for t0 in (0.15, 0.55):
        m.add(ping(0.25), a + (b - a) * t0)
    a, b = w[2]
    for k in range(10):
        m.add(ping(0.22, 1100 + k * 40), a + (b - a) * k * 0.09)
        m.add(X.thud(0.25, 1.4, 0.2), a + (b - a) * k * 0.09)
    a, b = w[3]
    m.add(X.power_up(2.0, 0.35), a)
    m.add(X.faded(X.hum(b - a, 1.0, 220), 0.5, 1.0, 0.05), a + 0.5)
    m.add(X.chime(0.3, 523.25, 3.0), a + (b - a) * 0.38)
    m.add(X.swell(b - a, 0.26, bright=True), a + (b - a) * 0.3)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
