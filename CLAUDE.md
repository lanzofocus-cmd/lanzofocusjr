# LanzoFocus video projects

## Voiceover
- Always use the **male voice "Marcus"** for voiceovers — not a female voice.
  - Higgsfield `generate_audio`, model `text2speech_v2`, variant `elevenlabs`,
    `voice_type: preset`, `voice_id: 6f98d3dd-324f-4845-8c28-c1d1647a06cd` (~2.4 credits per script).
  - `seed_audio` with this voice was falsely rejected by its content filter once; ElevenLabs worked.

## Style and format
- 16:9, 1920x1080, 30 fps. Black background with a soft centre glow, glowing white line icons and figures,
  bold uppercase captions revealed word by word, `@lanzofocusjr` watermark at bottom right. No TikTok logo.
- Background music sits under the voice, ducked, fading in and out.

## Pipeline (`video/`)
1. Save the voiceover as `video/assets/voiceover.mp3` and the music as `video/assets/music.wav`.
2. `python3 make_timings.py assets/voiceover.mp3 3.0` writes `timings.json` from the pauses in the voiceover.
3. `./build.sh` writes `output/The_Version_Youre_Becoming_16x9.mp4`.
For a new script, update `LINES` in `make_timings.py` and the scenes in `render.py`.
