"""Pencil scratching out the plan, a rubber-stamp thump, confident footsteps, a paper storm (wind + fluttering),
thunder and snapping lines as the steps fall, then a new pencil line and a bright swell to the star."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def scratch(sec):
    return X.faded(X.hp(X.noise(sec), 2) * (0.6 + 0.4 * abs(X.np.sin(X.np.linspace(0, sec * 18, int(sec * 44100))))), 0.05, 0.1, 0.12)


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(scratch((en - st) * 0.8), st + 0.1, pan=0.2)
    m.add(X.thud(0.6, 1.2, 0.3), st + (en - st) * 0.87)
    st, en = w[1]
    tt = st
    while tt < en:
        m.add(X.step(0.3, 1.1), tt)
        tt += 0.42
    m.bed(X.wind(w[3][0] + (w[3][1] - w[3][0]) * 0.5 - (st + (en - st) * 0.4), 0.14), st + (en - st) * 0.4)
    for j in range(30):
        m.add(X.page_flip(0.15), st + (en - st) * 0.6 + j * 0.25, pan=rng.uniform(-0.9, 0.9))
    st, en = w[2]
    m.add(X.thunder(0.8), st + (en - st) * 0.14)
    for j in range(6):
        m.add(X.snap(0.35), st + (en - st) * (0.18 + j * 0.04), pan=rng.uniform(-0.4, 0.4))
    m.add(X.thud(0.5, 0.8), st + (en - st) * 0.52)
    st, en = w[3]
    m.add(scratch((en - st) * 0.3), st + (en - st) * 0.08, pan=-0.2)
    for j in range(8):
        m.add(X.step(0.25, 1.0), st + (en - st) * (0.47 + j * 0.05))
    m.add(X.swell(en - st, 0.26, bright=True), st + (en - st) * 0.35)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
