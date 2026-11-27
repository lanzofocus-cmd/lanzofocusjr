"""A slow-motion hammer strike, an arena of buzzing pings, impacts, the shield clattering down, forge roar and
rhythmic hammering, each armor piece clanging on, and pings sparking harmlessly off steel."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.clank(1.0, 0.7, 2.0), st + 1.2)
    m.add(X.low_hit(0.7), st + 1.2)
    m.add(X.fire(en - st, 0.15), st)
    st, en = w[1]
    for j in range(16):
        m.add(X.tick(0.25, rng.uniform(2.5, 3.5)), st + rng.uniform(0, en - st), pan=rng.uniform(-0.8, 0.8))
    for k in (0.9, 1.7, 2.4):
        m.add(X.thud(0.7, 1.0, 0.4), st + k)
    m.add(X.clank(0.6, 1.0, 1.0), st + 2.2)
    st, en = w[2]
    m.add(X.fire(en - st, 0.2), st)
    k = st + 0.1
    while k < en:
        m.add(X.clank(0.5, 0.9, 0.6), k)
        k += 1.25
    st, en = w[3]
    for j in range(4):
        m.add(X.clank(0.8, 1.2 + 0.1 * j, 1.0), st + (en - st) * 0.45 * (0.1 + j * 0.2 + 0.18))
    m.steps(st + (en - st) * 0.45, en, 2.0, 0.6, 0.8)
    k = st + (en - st) * 0.45
    while k < en:
        m.add(X.clank(0.2, rng.uniform(1.8, 2.6), 0.3), k, pan=rng.uniform(-0.6, 0.6))
        k += 0.3
    m.add(X.swell(en - st, 0.22), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
