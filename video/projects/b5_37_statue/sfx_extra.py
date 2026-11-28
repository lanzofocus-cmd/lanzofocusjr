"""Night crickets in a stone courtyard, years of wind and settling dust, footsteps, then chisel strikes that
quicken into a carving rhythm, chips skittering, and a warm swell as the statue is revealed at dawn."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    for j in range(20):
        m.add(X.tick(0.06, 3.4), 0.3 + j * 0.45, pan=rng.uniform(-0.8, 0.8))
    m.bed(X.wind(w[1][1] - w[1][0], 0.2), w[1][0])
    st, en = w[2]
    m.steps(st, st + (en - st) * 0.55, 2.0, 0.5)
    m.add(X.clank(0.7, 1.6, 0.6), st + (en - st) * 0.7)
    st, en = w[3]
    k = st
    while k < st + (en - st) * 0.75:
        m.add(X.clank(0.35, rng.uniform(1.4, 1.9), 0.3), k)
        m.add(X.tick(0.15, 2.5), k + 0.05, pan=rng.uniform(-0.5, 0.5))
        k += 0.3
    m.add(X.swell(en - st, 0.25, bright=True), st + (en - st) * 0.4)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
