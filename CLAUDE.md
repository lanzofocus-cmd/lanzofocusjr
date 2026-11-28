# LanzoFocus video projects

## Voiceover
- Use the **free local Kokoro voice `af_heart`** (female, American) for every video. No Higgsfield credits.
  - `python3 tts/speak.py projects/<name> af_heart 0.92` writes `voiceover.mp3` and exact `timings.json`.
  - First time in a fresh container: `pip install kokoro-onnx soundfile` and download the two model files
    listed at the top of `tts/speak.py` (from GitHub releases, ~350 MB, not committed).
- Older videos used Higgsfield's paid male voice "Marcus" (`text2speech_v2`, variant `elevenlabs`,
  voice_id `6f98d3dd-324f-4845-8c28-c1d1647a06cd`). Only use it if the user asks again.

## Music
- Two tracks: "VYZEE – Slowed" (`video/assets/music.m4a`) and "two faced" by purc (`video/assets/music_twofaced.m4a`,
  added from batch 6 on as the user's new choice). New videos set `MUSIC = "twofaced"` (or `"vyzee"`) in `scenes.py`.
- Always start on the song's best part: `MUSIC` picks a pre-built bed `assets/bed_<name>.m4a` that begins on the
  drop and loops only the strong section (`tools_music.py <src> <start> <end> <out>`; two faced = 23.98–59.8 s,
  VYZEE = 4.0–60 s). Without `MUSIC` the old behaviour (music.m4a from 0 s, 1.5 s fade-in) is used.
- If the user sends a new audio file, find its best part (energy/bass analysis), build a bed, and use it.

## Style and format
- 16:9, 1920x1080, 30 fps. Black background with a soft centre glow, glowing white line icons and figures,
  bold uppercase captions revealed word by word, `@lanzofocusjr` watermark at bottom right. No TikTok logo.
- Background music sits under the voice, ducked, fading in and out.

## Hook (first 3 s)
- Never open on a text-only title card. New videos set
  `HOOK = hook(TITLE, "<motif>", dict(...))`: a moving visual from frame 0 (counters, crowd, figure) with the title
  slammed in word by word as a glowing boxed headline, over the song's drop.
- Second style reference (user's TikTok, clipzy.editss style): HUD stat panels with counting percentages
  ("PUBLIC APPROVAL 93%"), grey crowds with a glowing white hero, energy batteries, a wall of light between the
  crowd and "YOUR FUTURE". Kit motifs: `hud` (lbl/start/end, lbl2/start2/end2, icons thumb|thumbdown|heart|q,
  tag, cross, count), `battery`, `beam` (lbl, tags). Use them in hooks and in body scenes.
- Sample: `projects/demo_new_hook` (video 151 re-cut with the new hook + two faced).

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
