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
Each video lives in `video/projects/<name>/` with `scenes.py`, `voiceover.mp3` and `timings.json`.
Batch videos are named `projects/b<batch>_<nn>_<slug>/` and output `<nn>_<Title>_16x9.mp4`.

New videos use the scene kit (`kit.py`): `scenes.py` sets TITLE (two lines), OUTPUT and
`SPEC = [(spoken line, motif, dict(options, acc="WORDS TO HIGHLIGHT")), ..., (follow line, "follow")]`,
then `LINES, SCENES = build(SPEC)` and `FOLLOW_SUB = follow_sub(SPEC[-1][0])`. See `projects/b1_*` for examples.
Pick a motif that illustrates each line and vary them; motifs are the `m_*` functions in `kit.py`
(price, receipt, chart, coins, scale, door, brain, gauge, lock, doc, path, stairs, timeline, phone, iceberg,
network, tangle, plant, book, chairs, frame, shed, arrows, startline, bricks, map, dots, fog, mirror, cage,
shield, bubbles, quote, sticker, crowd, alone, list, progress, puzzle, compass, key, crown, sunrise,
hourglass, question, pulse, big). Add a new motif to `kit.py` when none fits.
Hand-written scenes (older videos) also work: SCENES is any list of `f(d, t, dur)` functions.
- Use the user's exact voiceover. If a script ends with a CTA instead of a "Follow LanzoFocus…" line, end the
  SPEC with `("", "follow")`: a silent follow card (default subtitle) after the spoken CTA.
- CTA lines use the `cta` motif: `dict(kind="comment" | "save" | "share", lbl="SHORT PROMPT")`.
- Every scene gets a slow camera push-in (`CAMERA_PUSH` in `render.py`) and `build.sh` mixes a soft whoosh at
  each scene change (`tools_sfx.py`). Renders take ~5 min each.
- Batch 3 (the 50-script "master instructions" set) lives in `projects/b3_*`, outputs numbered 41–90.

1. `python3 tts/speak.py projects/<name> af_heart 0.92` (voiceover + timings).
   (For an externally made voiceover instead: save it as `voiceover.mp3`, then
   `python3 make_timings.py projects/<name> 3.0` finds the line timings from its pauses.)
2. `python3 tools_preview.py projects/<name> /tmp/sheet.jpg` renders one frame per scene to check layout.
3. `./build.sh projects/<name>` writes `output/<OUTPUT>` (16:9, voice + ducked music), ~2 min each.
   Several at once: `ls -d projects/b1_* | xargs -P 3 -I{} ./build.sh {}` (4 CPUs).

## Story videos (batch 4, `projects/b4_*`, outputs 91–100)
Cinematic short-story videos with their own world, characters, palette and camera per video (not the scene kit).
- Shared toolkit: `story.py` (camera `Cam`/`cam_lerp`, soft light `glow`/`beam`/`darkness`, weather, the articulated
  `figure()` with modes and accessories, hooded `shade()` voices, `top_caption`/`low_caption`, `final_card`, `windows()`).
  Translucent shapes must use `tpoly()`/`overlay()`: plain ImageDraw overwrites the layer instead of blending.
- Story sound design: `projects/<name>/sfx_extra.py` defines `extra(out, tim, SR, rng)` (helpers in `story_sfx.py`);
  optional `SFX_VOLUME` (build.sh mix level) and `WHOOSH_LEVEL`. `tools_sfx.py` picks it up automatically.
- `scenes.py` may set `SPOKEN` (text sent to TTS, e.g. without leading "…") and `GAPS = {line index: pause}`.
- A scene function with `.seamless = True` continues the previous shot (no dip to black between them).

## Story animations (batch 5, `projects/b5_*`, outputs 101–150)
The 50 "cinematic motivational animations": same story toolkit as batch 4, one world per film.
- `scenes.py` may set `SILENT = {line index: seconds}` for animation-only scenes (empty LINES entries). Usual layout:
  silent hook → narrated scenes → silent final card (`stage_end`) → `s_follow`.
- Render queue: mark a finished project with `touch projects/<name>/.ready`; workers
  (`nohup ./tools_queue.sh 'b5_*' > logs/queue_N.log 2>&1 &`, up to 3) build every ready project that has no output yet.
  After a container restart, remove stale `projects/*/.lock` dirs and restart the workers.
- `story.py` extras: `light_hole`, `particles`, `stage_end`, `PCam`/`back_figure`; box shapes accept reversed corners.
