#!/usr/bin/env python3
"""Free local voiceover with Kokoro (open source, runs offline, no credits).

Usage: python3 tts/speak.py projects/<name> [voice] [speed]
Voices each entry of LINES in <project>/scenes.py separately, joins them with pauses, and writes
<project>/voiceover.mp3 and <project>/timings.json (exact line timings, so make_timings.py is not needed).

Model files (download once, ~350 MB):
  curl -L -o tts/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
  curl -L -o tts/voices-v1.0.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
  pip install kokoro-onnx soundfile
"""
import importlib.util, json, os, subprocess, sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
proj = sys.argv[1]
voice = sys.argv[2] if len(sys.argv) > 2 else "af_heart"
speed = float(sys.argv[3]) if len(sys.argv) > 3 else 0.92
INTRO = 3.0

spec = importlib.util.spec_from_file_location("scenes", os.path.join(proj, "scenes.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
lines = getattr(mod, "SPOKEN", mod.LINES)
gaps = getattr(mod, "GAPS", {})  # optional {line index: pause after it, seconds}
silent = getattr(mod, "SILENT", {})  # optional {line index: length of a silent (animation-only) scene}

k = Kokoro(os.path.join(HERE, "kokoro-v1.0.onnx"), os.path.join(HERE, "voices-v1.0.bin"))
lang = "en-gb" if voice.startswith("b") else "en-us"
sr = 24000
audio, segs, t = [], [], 0.0
for i, line in enumerate(lines):
    line = line.replace("**", "")
    if not line.strip():  # silent scene (e.g. a closing card with no voiceover)
        s = np.zeros(int(silent.get(i, 3.2) * sr), dtype=np.float32)
        segs.append([round(INTRO + t, 3), round(INTRO + t + len(s) / sr, 3)])
        audio.append(s)
        t += len(s) / sr
        continue
    s, sr = k.create(line, voice=voice, speed=speed, lang=lang)
    # trim leading/trailing near-silence
    idx = np.where(np.abs(s) > 0.01)[0]
    if len(idx):
        s = s[max(0, idx[0] - int(0.03 * sr)): idx[-1] + int(0.08 * sr)]
    segs.append([round(INTRO + t, 3), round(INTRO + t + len(s) / sr, 3)])
    audio.append(s)
    t += len(s) / sr
    if i + 1 < len(lines):
        trailing = line.rstrip().endswith(("…", "..."))
        gap = gaps.get(i, 0.75 if trailing else 0.5)
        audio.append(np.zeros(int(gap * sr), dtype=s.dtype))
        t += gap
wav = os.path.join(proj, "voiceover.wav")
sf.write(wav, np.concatenate(audio), sr)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-b:a", "160k", os.path.join(proj, "voiceover.mp3")], check=True)
os.remove(wav)
json.dump({"intro": INTRO, "segments": segs, "end": round(INTRO + t + 2.8, 2)},
          open(os.path.join(proj, "timings.json"), "w"), indent=1)
for l, sg in zip(lines, segs):
    print(f"{sg[0]:6.2f}-{sg[1]:6.2f}  {l}")
