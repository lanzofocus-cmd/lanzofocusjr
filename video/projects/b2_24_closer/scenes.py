from kit import build, follow_sub

TITLE = ("YOU MAY BE CLOSER", "THAN YOU THINK")
OUTPUT = "34_You_May_Be_Closer_Than_You_Think_16x9.mp4"
SPEC = [
    ("You don't always recognize progress while it's happening.", "plant", dict(height=0.4, acc="RECOGNIZE PROGRESS")),
    ("Because you're looking at the distance remaining…", "timeline", dict(n=10, progress=0.6, tag="STILL SO FAR?", acc="DISTANCE REMAINING…")),
    ("Instead of the distance you've already traveled.", "timeline", dict(n=10, progress=0.6, tag="LOOK BACK", acc="ALREADY TRAVELED.")),
    ("You see the next goal.", "stairs", dict(n=6, climb=3, highlight=4, acc="NEXT GOAL.")),
    ("The next level.", "progress", dict(lbl="NEXT LEVEL", value=0.7, acc="LEVEL.")),
    ("The next thing you haven't achieved.", "list", dict(items=["NEXT GOAL", "NEXT LEVEL", "NEXT THING"], mode="empty", acc="HAVEN'T")),
    ("And forget that the person you are today…", "mirror", dict(reflect="solid", lbl="TODAY", acc="FORGET TODAY…")),
    ("Has already learned things the person you were yesterday didn't know.", "shed", dict(old="YESTERDAY", new="TODAY", acc="ALREADY LEARNED")),
    ("Keep your ambition.", "sunrise", dict(acc="AMBITION.")),
    ("But don't erase your progress.", "list", dict(items=["LEARNED THIS", "SURVIVED THAT", "BUILT THIS"], mode="check", acc="DON'T ERASE")),
    ("You can be proud of how far you've come…", "map", dict(a_lbl="WHERE YOU STARTED", b_lbl="HERE", acc="PROUD FAR")),
    ("And still excited about where you're going.", "path", dict(kind="straight", acc="EXCITED GOING.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
