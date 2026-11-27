"""Room tone, a shimmer as the mirror wakes, soft footsteps, a heartbeat as the hand reaches, glass cracking,
a fading shimmer, then footsteps, pages, running feet and a warm resolving chime."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.hum(w[5][1], 0.04, 55), 0.0)
    st, en = w[0]
    for j in range(6):
        m.add(X.chime(0.07, 900 + 150 * j, 2.0, (1, 1.5)), st + 0.3 + j * 0.15)
    m.steps(st + 1.6, st + 2.8, 2.0, 0.4, 0.9, soft=True)
    st, en = w[2]
    m.add(X.heartbeat(0.6), st + 0.2)
    m.add(X.snap(0.8), st + 1.4)
    m.add(X.hp(X.noise(1.2), 2) * X.env_ad(int(1.2 * SR), 0.005, 3) * 0.3, st + 1.42)
    m.add(X.chime(0.15, 1200, 3.0, (1, 1.33, 1.5)), w[3][0] + 0.3)
    st, en = w[4]
    m.steps(st + 0.5, en, 2.6, 0.5, 1.0)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    m.add(X.chime(0.35, 440.0, 4.5), w[5][0] + 0.2)
