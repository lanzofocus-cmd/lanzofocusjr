"""A slow clock tick that speeds into a whirring blur, a time-lapse city hum with day/night pulses and wind,
a quiet winter, then one heartbeat as the person stands, running steps and the city slowing to real time."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.25
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    tt, gap = st + 0.1, 0.5
    while tt < en:
        m.add(X.tick(0.35, 1.2), tt)
        tt += gap
        gap = max(0.05, gap * 0.82)
    st2 = w[1][0]
    en2 = w[2][1]
    m.add(X.faded(X.machine(en2 - st2, 1.0, 9.0), 0.6, 0.8, 0.08), st2)
    m.add(X.faded(X.murmur(en2 - st2, 1.0), 0.6, 0.8, 0.12), st2)
    for j in range(int((en2 - st2) / 0.55)):
        m.add(X.whoosh(0.4, 0.06), st2 + j * 0.55, pan=rng.uniform(-0.8, 0.8))
    st, en = w[2]
    m.bed(X.wind(en - st, 0.08), st + (en - st) * 0.5)
    st, en = w[3]
    m.add(X.heartbeat(0.7), st + (en - st) * 0.05)
    tt = st + (en - st) * 0.18
    gap = 0.3
    while tt < en:
        m.add(X.step(0.35, 1.1), tt, pan=0.1)
        tt += gap
        gap = min(0.45, gap * 1.02)
    m.add(X.faded(X.murmur(en - st, 1.0), 0.5, 0.8, 0.1), st + (en - st) * 0.3)
    m.add(X.swell(en - st, 0.24, bright=True), st + (en - st) * 0.3)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
