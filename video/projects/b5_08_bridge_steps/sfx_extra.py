"""Canyon wind, falling pebbles, a run-up and skid at the edge, a whoosh for the dream leap, and a soft rising
chime for every stone that appears beneath a step."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.2), 0.0)
    for j in range(4):
        m.add(X.tick(0.2, 1.8), w[0][0] + 0.5 + j * 0.7, pan=-0.3)
    st, en = w[1]
    m.steps(st, st + (en - st) * 0.25, 2.0, 0.4)
    m.steps(st + (en - st) * 0.25, st + (en - st) * 0.55, 5.0, 0.6, 1.1)
    m.add(X.lp(X.noise(0.5), 4) * X.env_ad(int(0.5 * SR), 0.01, 6) * 0.4, st + (en - st) * 0.56)
    m.add(X.whoosh(1.4, 0.4), st + (en - st) * 0.45)
    st, en = w[2]
    m.add(X.chime(0.3, 659.25, 3.0), st + (en - st) * 0.5)
    st, en = w[3]
    for j in range(15):
        tt = st + (en - st) * 0.85 * (j / 15) ** 0.7 if False else st + (en - st) * 0.85 * j / 15
        m.add(X.chime(0.12, 523.25 * (1 + 0.06 * (j % 5)), 1.2, (1, 1.5)), tt)
        m.add(X.step(0.4, 1.0), tt + 0.1)
    m.add(X.swell(en - st, 0.22, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
