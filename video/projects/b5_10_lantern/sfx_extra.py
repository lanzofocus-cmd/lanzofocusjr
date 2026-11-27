"""Silence, a match strike and the lantern catching, a low forest wind, creaking branches, soft footsteps on leaves,
the lantern's faint creak with each step, owls, and morning birds as the forest opens."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.hp(X.noise(0.3), 2) * X.env_ad(int(0.3 * SR), 0.003, 9) * 0.5, st + 0.8)   # match
    m.add(X.fire(1.5, 0.2), st + 0.95)
    m.bed(X.wind(w[4][1] - st, 0.16), st + 0.6)
    m.add(X.hum(w[3][1], 0.04, 45), 0.0)
    for j in range(5):
        m.add(X.lp(X.noise(0.8), 3) * X.fade_env(int(0.8 * SR), 0.2, 0.4) * 0.12, 4 + j * 2.5, pan=rng.uniform(-0.8, 0.8))  # creaks
    for i in (2, 3, 4):
        a, b = w[i]
        m.steps(a, b, 1.8, 0.35, 0.9, soft=True)
    for j in range(2):
        m.add(X.chime(0.05, 380, 0.6, (1, 1.25)), w[3][0] + 0.8 + j * 0.7, pan=-0.7)  # owl
    st, en = w[4]
    m.add(X.swell(en - st, 0.22, bright=True), st)
    for j in range(10):
        m.add(X.chime(0.05, 2200 + 250 * (j % 4), 0.25, (1, 1.2)), st + 2.0 + j * 0.3, pan=rng.uniform(-0.8, 0.8))
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
