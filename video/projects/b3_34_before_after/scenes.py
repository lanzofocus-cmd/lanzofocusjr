from kit import build, follow_sub

TITLE = ("YOUR LIFE ISN'T A", "BEFORE-AND-AFTER PICTURE")
OUTPUT = "74_Your_Life_Isnt_A_Before_And_After_Picture_16x9.mp4"
SPEC = [
    ("You want the transformation.", "frame", dict(who="BEFORE", new="AFTER", acc="TRANSFORMATION.")),
    ("The moment everything looks different.", "sunrise", dict(acc="DIFFERENT.")),
    ("The moment people notice.", "stage", dict(lbl="NOTICED", acc="NOTICE.")),
    ("The moment you finally become the person you've been trying to become.", "shed", dict(old="BEFORE", new="AFTER", acc="FINALLY BECOME")),
    ("But real life isn't a before-and-after picture.", "frame", dict(who="BEFORE / AFTER", dashed_fig=True, fade=True, acc="ISN'T BEFORE-AND-AFTER")),
    ("It's a process.", "path", dict(kind="winding", acc="PROCESS.")),
    ("Sometimes you improve.", "chart", dict(kind="up", lbl="IMPROVING", acc="IMPROVE.")),
    ("Sometimes you struggle.", "chart", dict(kind="flat", lbl="STRUGGLING", acc="STRUGGLE.")),
    ("Sometimes you go backward.", "chart", dict(kind="down", lbl="BACKWARD", acc="BACKWARD.")),
    ("Sometimes you discover that the goal you wanted…", "compass", dict(lbl="THE GOAL", acc="DISCOVER GOAL")),
    ("Needs to change.", "arrows", dict(items=["THE GOAL"], acc="CHANGE.")),
    ("There isn't always a clean dividing line between your old self and your new self.", "shed", dict(old="OLD SELF", new="NEW SELF", acc="ISN'T CLEAN")),
    ("You're becoming.", "plant", dict(height=0.6, lbl="BECOMING", acc="BECOMING.")),
    ("And becoming is messy.", "tangle", dict(lbl="MESSY", acc="MESSY.")),
    ("Don't wait for a dramatic transformation to recognize that change is already happening.", "progress", dict(lbl="ALREADY CHANGING", value=0.45, acc="DON'T DRAMATIC ALREADY HAPPENING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
