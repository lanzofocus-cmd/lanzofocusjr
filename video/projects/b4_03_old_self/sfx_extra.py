"""Sound design: floodlights slamming on, crowd-less stadium air, running feet, rain on the track, a phone
hitting the ground, a heartbeat as the old self decides, and a rising run to the finish."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.4
SFX_VOLUME = 0.3


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[8][1], 0.08), 0.0)
    st, en = w[0]
    for k in range(6):  # the floodlights, tower by tower
        m.add(X.clank(0.5, 0.35, 0.8), st + 0.2 + k * 0.23, pan=-0.6 + k * 0.24)
    m.add(X.low_hit(0.6), st + 0.2)
    st, en = w[2]
    m.steps(st + 0.05, st + (en - st) * 0.25, 5.5, 0.6, 1.1, pan=-0.2)
    m.steps(st + 0.05, en, 5.0, 0.35, 1.2, pan=0.4)
    m.add(X.tick(0.3, 0.7), st + (en - st) * 0.27)            # phone unlock
    st, en = w[3]
    m.steps(st, en, 5.0, 0.6, 1.15)
    m.bed(X.rain(w[5][1] - st - (en - st) * 0.2, 0.12), st + (en - st) * 0.2)
    m.add(X.thunder(0.5), st + (en - st) * 0.5)
    st, en = w[6]
    m.add(X.heartbeat(0.6), st + 0.2)
    m.add(X.thud(0.4, 2.5, 0.2), st + (en - st) * 0.45 + 0.35)  # phone hits the track
    m.add(X.heartbeat(0.6), st + 1.2)
    st, en = w[7]
    k = st
    while k < en:  # footsteps speeding up
        m.add(X.step(0.7, 1.1), k)
        u = (k - st) / (en - st)
        k += 1 / (3 + 4 * u)
    m.add(X.swell(en - st + 1.0, 0.3), st)
    st, en = w[8]
    m.steps(st, st + (en - st) * 0.42, 6.5, 0.6, 1.1)
    m.add(X.low_hit(0.8), st + (en - st) * 0.42)
    m.add(X.chime(0.3, 440.0, 4.0), st + (en - st) * 0.42)
