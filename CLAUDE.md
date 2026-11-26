# LanzoFocus video projects

## Voiceover
- Always use the **male voice "Marcus"** for voiceovers — not a female voice.
  - Higgsfield `generate_audio`, model `text2speech_v2`, variant `elevenlabs`,
    `voice_type: preset`, `voice_id: 6f98d3dd-324f-4845-8c28-c1d1647a06cd` (~2.4 credits per script).
  - `seed_audio` with this voice was falsely rejected by its content filter once; ElevenLabs worked.

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
1. Generate the voiceover (see above) and save it as `video/projects/<name>/voiceover.mp3`.
   The Higgsfield CDN host `d8j0ntlcm91z4.cloudfront.net` must be allowed (the `lanzofocusjr` environment allows it).
2. `python3 make_timings.py projects/<name> 3.0` writes `timings.json` from the pauses in the voiceover.
3. `./build.sh projects/<name>` writes `output/<OUTPUT>` (16:9, voice + ducked music).
