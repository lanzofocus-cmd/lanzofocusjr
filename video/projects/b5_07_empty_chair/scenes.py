from kit import build, follow_sub

TITLE = ("THE EMPTY", "CHAIR")
OUTPUT = "147_The_Empty_Chair_16x9.mp4"
SPEC = [
    ("One day, there will be an empty chair where someone used to sit.", "chairs", dict(n=5, lbl="SOMEONE SAT HERE", acc="EMPTY CHAIR")),
    ("A conversation you can't repeat.", "bubbles", dict(texts=["REMEMBER WHEN...?"], acc="CAN'T REPEAT")),
    ("A voice you can't hear the same way.", "pulse", dict(acc="VOICE SAME")),
    ("A moment you didn't realize was important.", "frame", dict(who="JUST A MOMENT", fade=True, acc="MOMENT IMPORTANT")),
    ("We spend so much time waiting for special moments…", "hourglass", dict(acc="WAITING SPECIAL")),
    ("That we forget ordinary moments are the ones we eventually miss.", "frame", dict(who="AN ORDINARY DAY", new="YOU, LATER", acc="ORDINARY MISS")),
    ("Look around.", "ring", dict(acc="LOOK AROUND")),
    ("Someone is here now.", "crowd", dict(n=3, highlight=1, highlight_label="HERE NOW", acc="HERE NOW")),
    ("Send this to someone you don't want to take for granted.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND GRANTED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
