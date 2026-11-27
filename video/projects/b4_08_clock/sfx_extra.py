"""Sound design: one enormous tick-tock that never stops (it is the heartbeat of the film), things dissolving,
heavy footsteps of Time, a phone's scroll clicks, years rushing past, a desk lamp click, and the final chime."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.34
TICK = 0.5


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    end = w[8][1]
    k, n = 0.0, 0
    while k < end:  # the clock, all the way through (low "tock" on alternate beats)
        m.add(X.tick(0.45 if n % 2 == 0 else 0.3, 1.0 if n % 2 == 0 else 0.6), k)
        k += TICK
        n += 1
    m.bed(X.wind(end, 0.08), 0.0)
    m.add(X.low_hit(0.8), w[0][0] + 0.2)
    st, en = w[0]
    for j in range(5):  # props dissolving
        m.add(X.whoosh(0.5, 0.25), st + (en - st) * 0.45 + (j + 1) * TICK, pan=rng.uniform(-0.6, 0.6))
    st, en = w[1]
    for j in range(6):
        m.add(X.tick(0.15, 2.2), st + 0.3 + j * 0.35, pan=0.2)          # scrolling
    m.add(X.swell(2.5, 0.3, bright=True), st + (en - st) * 0.35)       # years rush by
    for j in range(8):
        m.add(X.page_flip(0.3), st + (en - st) * (0.4 + 0.06 * j))
    for i in (2, 3, 5):  # Time's heavy steps
        st, en = w[i]
        k = st
        while k < en:
            m.add(X.thud(0.6, 0.6, 0.6), k, pan=rng.uniform(-0.3, 0.3))
            k += 0.9
    st, en = w[4]
    m.add(X.clank(0.25, 2.5, 0.15), st + 0.1)                          # lamp click
    k = st + 0.4
    while k < en:  # pen, keys, brush
        m.add(X.tick(0.12, rng.uniform(1.5, 3.0)), k)
        k += rng.uniform(0.12, 0.3)
    st, en = w[5]
    for j in range(6):
        m.add(X.chime(0.08, 600 + 120 * j, 1.2, (1, 1.5)), st + 0.3 + j * 0.25)
    m.add(X.low_hit(0.6), w[6][0])
    m.add(X.chime(0.3, 440.0, 4.0), w[8][0] + 0.2)
