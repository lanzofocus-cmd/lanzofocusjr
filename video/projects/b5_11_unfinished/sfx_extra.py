"""Paper fluttering and piling up, a hollow airy drone around the plans, then hammering, sawing and the click of
lights coming on house by house, evening crickets, and wind lifting the paper away."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    for j in range(30):
        m.add(X.page_flip(0.25), st + j * (en - st) / 30, pan=rng.uniform(-0.6, 0.6))
    m.add(X.hum(w[1][1] - w[1][0], 0.05, 330), w[1][0])
    st, en = w[2]
    k = st + 0.2
    while k < en - 0.3:
        m.add(X.clank(0.25, 1.1, 0.25), k)
        k += 0.45
    m.add(X.tick(0.4, 1.0), en - 0.4)
    st, en = w[3]
    for j in range(30):
        m.add(X.clank(0.15, rng.uniform(0.9, 1.3), 0.2), st + (en - st) * 0.8 * j / 30, pan=rng.uniform(-0.5, 0.8))
    for j in range(8):
        m.add(X.tick(0.15, 1.0), st + (en - st) * (0.4 + 0.07 * j), pan=0.5)
    m.bed(X.wind(en - st, 0.15), st + (en - st) * 0.5)
    m.add(X.swell(en - st, 0.22), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
