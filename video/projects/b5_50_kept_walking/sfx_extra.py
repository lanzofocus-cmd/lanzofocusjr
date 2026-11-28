"""A murmuring crowd at the start line and a shimmer when the star appears, the shuffle of hundreds of feet,
birdsong to desert wind, steps dropping away one by one, a howling blizzard with a single pair of footsteps,
night wind on the mountain, then a sunrise swell and a final bell for KEEP GOING."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.22
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    a, b = w[0]
    m.add(X.faded(X.murmur(b - a + (w[1][1] - w[1][0]), 1.0), 0.5, 1.0, 0.16), a)
    m.add(X.chime(0.2, 784.0, 3.0), a + (b - a) * 0.5)
    a, b = w[1]
    for j in range(int((b - a) / 0.12)):
        m.add(X.step(0.08, rng.uniform(0.8, 1.3), soft=True), a + j * 0.12 + rng.uniform(0, 0.06), pan=rng.uniform(-0.9, 0.9))
    a, b = w[2]
    for j in range(int((b - a) / 0.15)):
        u = j * 0.15 / (b - a)
        if rng.random() < 1.0 - 0.8 * u:
            m.add(X.step(0.1, rng.uniform(0.8, 1.3), soft=True), a + j * 0.15, pan=rng.uniform(-0.8, 0.8))
    m.add(X.faded(X.wind(b - a, 1.0), 1.5, 0.5, 0.08), a + (b - a) * 0.4)
    a, b = w[3]
    m.bed(X.wind(b - a + 0.5, 0.2), a)
    tt = a + 0.2
    while tt < b:
        m.add(X.step(0.35, 0.9, soft=True), tt)
        tt += 0.55
    a, b = w[4]
    m.bed(X.wind(b - a, 0.08), a)
    tt = a + 0.2
    while tt < b:
        m.add(X.step(0.3, 0.85), tt)
        tt += 0.6
    a, b = w[5]
    m.add(X.swell(b - a, 0.3, bright=True), a)
    for j in range(8):
        m.add(X.chime(0.04, 2000 + 250 * (j % 3), 0.25, (1, 1.2)), a + 0.5 + j * 0.6, pan=rng.uniform(-0.8, 0.8))
    m.add(X.chime(0.3, 523.25, 4.0), a + (b - a) * 0.45)
    m.add(X.low_hit(0.4, 3.0), w[6][0] + 0.1)
    m.add(X.chime(0.4, 392.0, 5.0), w[6][0] + 0.2)
