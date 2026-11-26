#!/usr/bin/env python3
"""Build timings.json from a voiceover by detecting its pauses.

Usage: python3 make_timings.py projects/<name> [intro_seconds]
Reads LINES from <project>/scenes.py and <project>/voiceover.mp3. Picks the pauses between script lines that best match where each
line should fall by character count, then writes <project>/timings.json.
"""
import json, re, subprocess, sys

import importlib.util, os
proj = sys.argv[1]
spec = importlib.util.spec_from_file_location("scenes", os.path.join(proj, "scenes.py"))
mod = importlib.util.module_from_spec(spec)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec.loader.exec_module(mod)
LINES = mod.LINES
vo = os.path.join(proj, "voiceover.mp3")
intro = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vo]))
log = subprocess.run(["ffmpeg", "-hide_banner", "-i", vo, "-af", "silencedetect=n=-38dB:d=0.15", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
pauses = [(s, e) for s, e in zip(starts, ends) if s > 0.05 and e < dur - 0.05]
if len(ends) and starts and starts[0] <= 0.05:
    speech0 = ends[0]
else:
    speech0 = 0.0
trail = [s for s in starts if s > dur - 1.5]
speech_end = trail[-1] if trail else dur

# expected boundary times by cumulative characters
chars = [len(l) for l in LINES]
total = sum(chars)
expected, acc = [], 0
for c in chars[:-1]:
    acc += c
    expected.append(speech0 + (speech_end - speech0) * acc / total)

# DP: assign 16 boundaries to pauses in order, minimising squared error (prefer longer pauses)
n, m = len(expected), len(pauses)
assert m >= n, f"only {m} pauses found for {n} boundaries"
INF = float("inf")
cost = [[INF] * (m + 1) for _ in range(n + 1)]
back = [[None] * (m + 1) for _ in range(n + 1)]
for j in range(m + 1):
    cost[0][j] = 0
for i in range(1, n + 1):
    for j in range(i, m + 1):
        mid = (pauses[j - 1][0] + pauses[j - 1][1]) / 2
        c = (mid - expected[i - 1]) ** 2 - 4 * (pauses[j - 1][1] - pauses[j - 1][0])
        best = min(range(i - 1, j), key=lambda k: cost[i - 1][k])
        cost[i][j] = cost[i - 1][best] + c
        back[i][j] = best
j = min(range(n, m + 1), key=lambda k: cost[n][k])
chosen = []
for i in range(n, 0, -1):
    chosen.append(pauses[j - 1]); j = back[i][j]
chosen.reverse()

segs, s = [], speech0
for ps, pe in chosen:
    segs.append([round(s + intro, 3), round(ps + intro, 3)]); s = pe
segs.append([round(s + intro, 3), round(speech_end + intro, 3)])
out = {"intro": intro, "segments": segs, "end": round(intro + dur + 2.8, 2)}
json.dump(out, open(os.path.join(proj, "timings.json"), "w"), indent=1)
for l, sg in zip(LINES, segs):
    print(f"{sg[0]:6.2f}-{sg[1]:6.2f}  {l}")
