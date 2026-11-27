"""Great doors groaning open, a cavernous hall, lazy whispers, the kingdom cracking, a chandelier crash,
footsteps on stone steps, the throne taken, and a choir-like swell as the light returns."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[4][1], 0.08), 0.0)
    st, en = w[0]
    m.add(X.lp(X.noise(1.6), 4) * X.fade_env(int(1.6 * SR), 0.2, 0.8) * 0.3, st + 0.2)   # door groan
    m.add(X.low_hit(0.6), st + 0.3)
    m.bed(X.murmur(w[1][1] - w[1][0], 0.06), w[1][0])
    st, en = w[2]
    for k in (0.5, 1.5, 2.4):
        m.add(X.thud(0.9, 0.6), st + k)
        m.add(X.lp(X.noise(0.8), 3) * X.env_ad(int(0.8 * SR), 0.01, 4) * 0.3, st + k)
    m.add(X.clank(0.8, 1.4, 1.5), st + 1.65)
    m.add(X.chain_rattle(0.4), st + 1.7)
    st, en = w[3]
    m.steps(st + (en - st) * 0.15, st + (en - st) * 0.55, 2.0, 0.5, 0.85)
    m.add(X.low_hit(0.7), st + (en - st) * 0.55)
    m.add(X.chime(0.3, 261.6, 5.0, (1, 1.26, 1.5, 2.0)), st + (en - st) * 0.55)
    m.add(X.swell(en - st, 0.25, bright=True), st)
    m.add(X.chime(0.3, 392.0, 4.5), w[4][0] + 0.2)
