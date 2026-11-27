"""Sound design: desert wind at dawn, a crowd of footsteps setting off, the sprinter's fast feet and panting,
gear being fiddled with, hesitant steps turning back, then one steady set of footsteps through rain, snow
and night, and the city of light swelling at the end."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.3
SFX_VOLUME = 0.32


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    m.bed(X.wind(w[10][1], 0.14), 0.0)
    st, en = w[0]
    for j in range(7):  # everyone sets off
        m.steps(st + (en - st) * 0.55 + j * 0.04, en, 2.6, 0.25, rng.uniform(0.9, 1.2), pan=-0.6 + j * 0.2)
    st, en = w[1]
    k = st
    while k < st + (en - st) * 0.6:  # sprinter
        m.add(X.step(0.6, 1.3), k, pan=-0.3)
        k += 0.13
    for j in range(4):  # panting
        b = X.lp(X.noise(0.35), 10) * X.fade_env(int(0.35 * SR), 0.05, 0.2) * 0.3
        m.add(b, st + (en - st) * 0.62 + j * 0.45, pan=-0.3)
    st, en = w[2]
    for j in range(8):
        m.add(X.tick(0.2, rng.uniform(0.8, 1.6)), st + 0.2 + j * (en - st) / 9)
    st, en = w[3]
    m.steps(st, st + (en - st) * 0.45, 2.0, 0.5, 1.0)
    m.steps(st + (en - st) * 0.6, en, 1.8, 0.5, 0.95)
    for i in (4, 5, 6, 7, 8, 9):  # the consistent one, never stopping
        a, b = w[i]
        m.steps(a, b, 2.2, 0.55, 1.0, soft=(i == 5))
    st, en = w[5]
    n = 5
    seg = (en - st) / n
    m.bed(X.rain(seg, 0.14), st)
    m.bed(X.wind(seg, 0.18), st + seg)
    m.add(X.chime(0.06, 1200, 2.0, (1, 1.5)), st + seg * 2.3)
    m.add(X.swell(w[9][1] - w[6][0], 0.25, bright=True), w[6][0])
    m.add(X.low_hit(0.8), w[9][0])
    m.add(X.chime(0.35, 392.0, 4.5), w[9][0] + 0.3)
