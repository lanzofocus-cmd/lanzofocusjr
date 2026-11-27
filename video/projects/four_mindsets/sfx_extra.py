"""Story sound design for FOUR MINDSETS: wind bed, footsteps, rain, distant thunder, a slip, the summit chime."""
import numpy as np

WHOOSH_LEVEL = 0.5


def extra(out, tim, SR, rng):
    segs, intro, end = tim["segments"], tim["intro"], tim["end"]
    n_sc = len(segs)
    win = []
    for i in range(n_sc):
        st = segs[i][0] - 0.15 if i else intro
        en = segs[i + 1][0] - 0.15 if i + 1 < n_sc else end
        win.append((st, en))
    L = len(out)

    def add(sig, t, gain=1.0, pan=0.0):
        a = int(t * SR)
        if a >= L or a < 0:
            return
        if sig.ndim == 1:
            sig = np.stack([sig * (1 - pan) * 0.7, sig * (1 + pan) * 0.7], axis=1)
        seg = out[a:a + len(sig)]
        seg += sig[:len(seg)] * gain

    def lowpass(x, k):
        return np.convolve(x, np.ones(k) / k, mode="same")

    def noise(sec):
        return rng.standard_normal(int(sec * SR)).astype(np.float32)

    def step(gain=1.0, pitch=1.0):
        n = int(0.09 * SR)
        tt = np.arange(n) / SR
        thump = np.sin(2 * np.pi * 85 * pitch * tt) * np.exp(-tt * 45)
        tick = lowpass(noise(0.09), 6) * np.exp(-tt * 90) * 0.5
        return (thump + tick) * gain

    # low wind bed through the staircase scenes
    wa, wb = 0.0, win[10][1]
    w = lowpass(lowpass(noise(wb - wa), 180), 60)
    env = np.minimum(1, np.minimum(np.arange(len(w)) / SR / 2.0, (len(w) - np.arange(len(w))) / SR / 1.5))
    w = w / (np.abs(w).max() + 1e-6) * env * 0.12
    add(np.stack([w, np.roll(w, 900)], axis=1), wa)

    def steps_linear(i, q0, q1, gain, pitch, pan=0.0, power=1.0):
        st, en = win[i]
        dur = en - st
        k0, k1 = int(np.floor(min(q0, q1))) + 1, int(np.floor(max(q0, q1)))
        for k in range(k0, k1 + 1):
            if q1 == q0:
                break
            p = ((k - q0) / (q1 - q0)) ** (1 / power)
            add(step(gain * rng.uniform(0.8, 1.1), pitch), st + p * dur + 0.05, pan=pan)

    # Motivation's fast hops (scene 2), Discipline's even steps (4, 5), Obsession's sprint (6)
    st, en = win[1]
    for j in range(7):
        add(step(0.9, 1.3), st + (en - st) * (1 - (1 - (j + 1) / 7) ** (1 / 1.6)) * 0.95, pan=0.2)
    steps_linear(3, 1.8, 6.5, 0.8, 0.9, -0.1)
    steps_linear(4, 6.5, 15.0, 0.8, 0.9, -0.1)
    steps_linear(5, 0.2, 21.0, 0.7, 1.15, 0.15, power=1.6)
    # Consistency's steps through the montage, quiet and regular
    steps_linear(7, 14.5, 24.0, 0.55, 1.0)
    steps_linear(8, 24.0, 33.0, 0.55, 1.0)
    steps_linear(10, 37.0, 40.0, 0.6, 1.0)

    # rain: scene 5 and the montage RAIN shot
    def rain(t0, t1, gain):
        r = noise(t1 - t0)
        r = r - lowpass(r, 4)
        env = np.minimum(1, np.minimum(np.arange(len(r)) / SR / 0.3, (len(r) - np.arange(len(r))) / SR / 0.3))
        add(np.stack([r, np.roll(r, 300)], axis=1) * env[:, None] * gain, t0)
    rain(win[4][0], win[4][1], 0.10)
    s8 = win[7]
    rain(s8[0] + (s8[1] - s8[0]) * 0.5, s8[0] + (s8[1] - s8[0]) * 0.75, 0.08)

    # distant thunder at the lightning flash
    st, en = win[4]
    th = lowpass(lowpass(noise(2.6), 400), 200)
    tt = np.arange(len(th)) / SR
    th = th / (np.abs(th).max() + 1e-6) * (np.minimum(1, tt / 0.05) * np.exp(-tt * 1.4)) * 0.9
    add(th, st + (en - st) * 0.32 + 0.15)

    # the slip: a scuff and a soft thud
    st, en = win[6]
    tslip = st + (en - st) * 0.24
    sc = lowpass(noise(0.35), 10) * np.linspace(1, 0, int(0.35 * SR)) * 0.35
    add(sc, tslip, pan=0.2)
    add(step(1.6, 0.6), tslip + 0.3)

    # rising swell into the summit, then a warm chime when Consistency arrives
    st, en = win[9]
    st2, en2 = win[10]
    arrive = st2 + (en2 - st2) * 0.45
    sw = lowpass(noise(arrive - st), 30)
    ramp = np.linspace(0, 1, len(sw)) ** 2
    add(sw / (np.abs(sw).max() + 1e-6) * ramp * 0.25, st)
    n = int(3.5 * SR)
    tt = np.arange(n) / SR
    chime = sum(np.sin(2 * np.pi * f * tt) * a for f, a in ((523.25, 1), (659.25, 0.6), (783.99, 0.5), (1046.5, 0.25)))
    chime *= np.exp(-tt * 1.2) * np.minimum(1, tt / 0.01) * 0.35
    add(chime, arrive)
    # soft single step on the final "show up again tomorrow" card
    st, en = win[15]
    add(step(0.9, 1.0), st + 0.6 + 1.4 * 0.5)
