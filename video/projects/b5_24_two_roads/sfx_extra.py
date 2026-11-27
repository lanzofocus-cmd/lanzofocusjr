"""Wind over the fork, a soft pastoral breeze with birds on the easy side and rain and wind on the hard side,
light strolling steps versus heavy climbing steps, a hollow knock on the dead-end wall, and a city swell."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[1][1], 0.15), 0.0)
    st, en = w[2][0], w[4][0]
    for j in range(10):
        m.add(X.chime(0.04, 2200 + 250 * (j % 3), 0.25, (1, 1.2)), st + j * 0.5, pan=-0.7)
    m.bed(X.rain(w[4][1] - st, 0.08), st)
    m.steps(st, en, 1.8, 0.35, 1.2, pan=-0.5, soft=True)
    m.steps(st, w[4][0] + 1.0, 1.5, 0.6, 0.85, pan=0.5)
    st3, en3 = w[3]
    m.add(X.thud(0.6, 1.0, 0.4), st3 + (en3 - st3) * 0.8, pan=-0.5)
    st, en = w[4]
    m.add(X.swell(en - st, 0.3, bright=True), st)
    m.add(X.low_hit(0.7), st + (en - st) * 0.3)
    m.add(X.chime(0.35, 392.0, 4.5), w[5][0] + 0.2)
