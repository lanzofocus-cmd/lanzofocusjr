"""Clanking, dragging chain over rock, straining breath, links unlocking and clicking into place with bright
tones, the chain swinging out with a whoosh and locking into a bridge, then calm footsteps over metal."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.12), 0.0)
    m.add(X.clank(0.8, 0.8, 1.2), w[0][0] + 0.6)
    a, b = w[0][0], w[1][1]
    k = a + 0.8
    while k < b:
        m.add(X.chain_rattle(0.3, 0.6), k)
        k += 0.9
    st, en = w[2]
    for j in range(14):
        m.add(X.chime(0.08, 523.25 * (1 + 0.04 * j), 0.6, (1, 1.5)), st + (en - st) * (0.1 + 0.05 * j))
        m.add(X.tick(0.2, 1.3), st + (en - st) * (0.1 + 0.05 * j))
    st, en = w[3]
    m.add(X.whoosh(1.4, 0.4), st + 0.2)
    m.add(X.clank(0.7, 0.6, 1.5), st + (en - st) * 0.4)
    k = st + (en - st) * 0.45
    while k < en:
        m.add(X.clank(0.15, 2.0, 0.2), k)
        k += 0.45
    m.add(X.swell(en - st, 0.22, bright=True), st)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
