"""Desert wind, slow sinking footsteps in sand with creaking straps, a strained low groan when the orb won't move,
a hush, then crate after crate thudding into the sand, and a light airy swell as the dream lifts them."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[5][1], 0.1), 0.0)
    st, en = w[1][1], 0
    tt = 0.3
    while tt < w[2][0]:
        m.add(X.step(0.4, 0.7, soft=True), tt)
        m.add(X.faded(X.lp(X.noise(0.35), 10), 0.1, 0.2, 0.06), tt + 0.1, pan=-0.3)
        tt += 0.85
    st, en = w[2]
    m.add(X.faded(X.hum(en - st, 1.0, 50), 0.4, 0.6, 0.12), st + (en - st) * 0.2)
    m.add(X.thud(0.6, 0.7), st + (en - st) * 0.6)
    st, en = w[4]
    for j in range(8):
        tt = st + (en - st) * (0.05 + 0.45 * (j + 1) / 8)
        m.add(X.thud(0.55, 0.9 + rng.uniform(-0.1, 0.2), 0.35), tt, pan=-0.3)
        m.add(X.faded(X.lp(X.noise(0.4), 6), 0.02, 0.3, 0.08), tt, pan=-0.3)
    m.add(X.power_up(1.6, 0.2), st + (en - st) * 0.5)
    m.add(X.swell(en - st, 0.26, bright=True), st + (en - st) * 0.45)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
