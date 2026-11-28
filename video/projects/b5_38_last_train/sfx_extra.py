"""A train roaring past, station echo and announcements murmur, a ticking station clock, split-flap clatter,
trains arriving and leaving with brake hiss, the last-call bell, running footsteps, a leap, and the rhythm of
wheels into the dawn."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end = w[3][1]
    m.bed(X.murmur(end, 0.06), 0.0)
    st, en = w[0]
    m.add(X.faded(X.lp(X.noise(en - st), 6), 0.4, 0.8, 0.5), st)
    m.add(X.whoosh(1.5, 0.5), st + (en - st) * 0.3)
    st, en = w[1]
    k = st
    while k < en:
        m.add(X.tick(0.15, 1.0), k)
        k += 0.25
    for j in range(5):
        m.add(X.faded(X.hp(X.noise(0.4), 2), 0.01, 0.2, 0.15), st + j * (en - st) / 5)       # flaps
        m.add(X.faded(X.hp(X.noise(0.8), 5), 0.05, 0.6, 0.12), st + j * (en - st) / 5 + 0.6)  # brake hiss
    st, en = w[2]
    m.add(X.chime(0.3, 880, 1.5, (1, 1.26)), st + 0.2)
    m.add(X.chime(0.3, 880, 1.5, (1, 1.26)), st + 0.7)
    m.steps(st + (en - st) * 0.15, st + (en - st) * 0.55, 5.5, 0.6, 1.1)
    m.add(X.thud(0.6, 1.2, 0.3), st + (en - st) * 0.55)
    k = st + (en - st) * 0.2
    gap = 0.6
    while k < end:
        m.add(X.clank(0.2, 0.6, 0.2), k)
        m.add(X.clank(0.15, 0.6, 0.2), k + 0.12)
        k += gap
        gap = max(0.22, gap * 0.95)
    m.add(X.swell(en - st, 0.25, bright=True), st + (en - st) * 0.5)
    m.add(X.chime(0.35, 392.0, 4.5), w[3][0] + 0.2)
