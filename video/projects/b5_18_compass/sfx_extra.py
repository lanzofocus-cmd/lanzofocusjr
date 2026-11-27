"""A frantic ticking needle, wind across the plain, a rising babble of shouting voices and whistling arrows,
then silence, a heartbeat, the needle clicking still, and footsteps on a road that hums with light."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    k = st
    while k < st + (en - st) * 0.55:
        m.add(X.tick(0.25, 2.5), k)
        k += 0.07
    m.bed(X.wind(w[4][1], 0.18), st + (en - st) * 0.5)
    a, b = w[1][0], w[3][0] + (w[3][1] - w[3][0]) * 0.35
    m.bed(X.murmur(b - a, 0.16), a)
    for j in range(24):
        m.add(X.whoosh(0.35, 0.15), a + rng.uniform(0, b - a), pan=rng.uniform(-0.9, 0.9))
    st, en = w[3]
    m.add(X.heartbeat(0.5), st + (en - st) * 0.25)
    m.add(X.tick(0.6, 1.0), st + (en - st) * 0.45)
    m.add(X.chime(0.3, 523.25, 3.5), st + (en - st) * 0.47)
    m.steps(st + (en - st) * 0.6, en, 2.0, 0.5)
    m.add(X.swell(en - st, 0.22, bright=True), st + (en - st) * 0.4)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
