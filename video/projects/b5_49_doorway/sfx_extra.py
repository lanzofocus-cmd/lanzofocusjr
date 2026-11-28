"""A low resonant tone as the door of light cracks open, crickets and a soft breeze in the dusk meadow, the door
creaking wider, a shimmer for each memory frame, and a bright bloom as the traveler steps through."""
import story_sfx as X
from story import windows

WHOOSH_LEVEL = 0.2
SFX_VOLUME = 0.3


def extra(out, tim, SR, rng):
    w = windows(tim, len(tim["segments"]))
    m = X.Mixer(out)
    st, en = w[0]
    m.add(X.faded(X.hum(en - st + 1, 1.0, 110), 1.0, 1.0, 0.1), st)
    m.add(X.power_up(en - st, 0.15), st)
    m.bed(X.wind(w[4][1] - w[1][0], 0.07), w[1][0])
    for j in range(int((w[4][0] - w[1][0]) / 0.45)):
        m.add(X.chime(0.02, 3800 + 300 * (j % 2), 0.12, (1,)), w[1][0] + j * 0.45 + rng.uniform(0, 0.1), pan=rng.uniform(-0.9, 0.9))
    a, b = w[2]
    m.add(X.faded(X.lp(X.noise(1.4), 20) * X.np.sin(X.np.linspace(0, 40, int(1.4 * 44100))), 0.1, 0.3, 0.12), a + 0.1)
    a, b = w[3]
    for i in range(4):
        m.add(X.chime(0.18, 660.0 + i * 110, 2.0), a + (b - a) * (0.04 + i * 0.12))
    m.add(X.swell(b - a, 0.28, bright=True), a + (b - a) * 0.4)
    m.add(X.chime(0.3, 523.25, 3.5), a + (b - a) * 0.85)
    m.add(X.chime(0.35, 392.0, 4.5), w[4][0] + 0.2)
