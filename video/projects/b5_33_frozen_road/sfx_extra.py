"""A howling blizzard, a boot tapping on hard ice, the sharp crack of the first step with a warm hum beneath,
crunching footsteps with small cracks, dripping thaw, and birdsong as spring arrives."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end3 = w[3][1]
    m.bed(X.wind(end3, 0.28), 0.0)
    st, en = w[1]
    for k in (0.35, 0.6):
        m.add(X.tick(0.4, 0.7), st + (en - st) * k)
    st, en = w[2]
    m.add(X.snap(0.8), st + (en - st) * 0.35)
    m.add(X.hum(en - st, 0.06, 110), st + (en - st) * 0.35)
    st, en = w[3]
    k = st
    while k < st + (en - st) * 0.9:
        m.add(X.step(0.5, 0.9, soft=True), k)
        m.add(X.hp(X.noise(0.15), 2) * X.env_ad(int(0.15 * SR), 0.002, 20) * 0.15, k + 0.02)
        k += 0.5
    for j in range(10):
        m.add(X.tick(0.1, 1.6), st + (en - st) * 0.3 + j * 0.35, pan=rng.uniform(-0.6, 0.6))
        m.add(X.chime(0.04, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + (en - st) * 0.5 + j * 0.3, pan=rng.uniform(-0.7, 0.7))
    m.add(X.swell(en - st, 0.22, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
