from kit import build, follow_sub

TITLE = ("YOU HAVE MORE TIME THAN", "YOUR PANIC TELLS YOU")
OUTPUT = "98_You_Have_More_Time_Than_Your_Panic_Tells_You_16x9.mp4"
SPEC = [
    ("Your mind makes everything feel urgent.", "notifs", dict(items=["URGENT", "URGENT", "URGENT", "URGENT"], acc="URGENT.")),
    ("You need to succeed now.", "list", dict(items=["SUCCEED"], mode="tag", tag="NOW!", acc="NOW.")),
    ("Learn now.", "list", dict(items=["SUCCEED", "LEARN"], mode="tag", tag="NOW!", acc="NOW.")),
    ("Figure everything out now.", "list", dict(items=["SUCCEED", "LEARN", "FIGURE IT OUT"], mode="tag", tag="NOW!", acc="NOW.")),
    ("And suddenly…", "pulse", dict()),
    ("Every unfinished goal feels like a crisis.", "gauge", dict(lbl="PANIC", start=0.3, end=0.95, acc="UNFINISHED CRISIS.")),
    ("But not everything needs to happen immediately.", "hourglass", dict(acc="NOT IMMEDIATELY.")),
    ("You can develop skills over years.", "chart", dict(kind="up", lbl="SKILLS", lbl2="YEARS", acc="YEARS.")),
    ("Build relationships over time.", "ring", dict(acc="TIME.")),
    ("Discover what you want gradually.", "path", dict(kind="winding", acc="GRADUALLY.")),
    ("Make mistakes.", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKES.")),
    ("Change directions.", "compass", dict(lbl="NEW DIRECTION", acc="DIRECTIONS.")),
    ("Your life isn't a race against everyone else's clock.", "timeline", dict(compare=True, acc="ISN'T RACE CLOCK.")),
    ("Urgency can help you act.", "gauge", dict(lbl="URGENCY", start=0.3, end=0.6, acc="URGENCY ACT.")),
    ("But panic can make you forget that you have time to learn.", "hourglass", dict(acc="PANIC FORGET TIME LEARN.")),
    ("Take the next step.", "stairs", dict(n=6, climb=1, acc="NEXT STEP.")),
    ("Not every step at once.", "stairs", dict(n=6, climb=1, highlight=1, acc="NOT ONCE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
