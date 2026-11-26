# LanzoFocus video projects

## Voiceover
- Use the **free local Kokoro voice `af_heart`** (female, American) for every video. No Higgsfield credits.
  - `python3 tts/speak.py projects/<name> af_heart 0.92` writes `voiceover.mp3` and exact `timings.json`.
  - First time in a fresh container: `pip install kokoro-onnx soundfile` and download the two model files
    listed at the top of `tts/speak.py` (from GitHub releases, ~350 MB, not committed).
- Older videos used Higgsfield's paid male voice "Marcus" (`text2speech_v2`, variant `elevenlabs`,
  voice_id `6f98d3dd-324f-4845-8c28-c1d1647a06cd`). Only use it if the user asks again.

## Music
- Always use the same background track (`video/assets/music.m4a`, "VYZEE – Slowed") for every video,
  unless the user sends a new audio file. If they do, replace `video/assets/music.m4a` with it.

## Style and format
- 16:9, 1920x1080, 30 fps. Black background with a soft centre glow, glowing white line icons and figures,
  bold uppercase captions revealed word by word, `@lanzofocusjr` watermark at bottom right. No TikTok logo.
- Background music sits under the voice, ducked, fading in and out.

## Pipeline (`video/`)
Each video lives in `video/projects/<name>/`: `scenes.py` (TITLE, OUTPUT, LINES = one entry per spoken
line, SCENES = one scene function per line, ending with `s_follow`), `voiceover.mp3`, `timings.json`.
Shared drawing helpers and the earlier scenes are in `render.py`.
Set `FOLLOW_SUB` in `scenes.py` when the script's closing line differs from the default.
1. `python3 tts/speak.py projects/<name> af_heart 0.92` (voiceover + timings).
   (For an externally made voiceover instead: save it as `voiceover.mp3`, then
   `python3 make_timings.py projects/<name> 3.0` finds the line timings from its pauses.)
2. `./build.sh projects/<name>` writes `output/<OUTPUT>` (16:9, voice + ducked music).
