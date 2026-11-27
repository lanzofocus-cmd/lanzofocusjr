from kit import build, follow_sub

TITLE = ("WHAT YOU", "CALL LUCK")
OUTPUT = "73_What_You_Call_Luck_16x9.mp4"
SPEC = [
    ("You see someone succeed…", "crowd", dict(n=5, highlight=2, highlight_label="SUCCEEDED", acc="SUCCEED…")),
    ("And call it luck.", "quote", dict(text="THEY GOT LUCKY.", acc="LUCK.")),
    ("Sometimes it genuinely is.", "list", dict(items=["SOMETIMES, YES"], mode="check", acc="GENUINELY")),
    ("Timing matters.", "hourglass", dict(acc="TIMING")),
    ("Circumstances matter.", "chart", dict(kind="wave", lbl="CIRCUMSTANCES", acc="CIRCUMSTANCES")),
    ("Opportunities matter.", "door", dict(open_=True, lbl="OPPORTUNITY", acc="OPPORTUNITIES")),
    ("But sometimes…", "pulse", dict()),
    ("What looks like luck is the result of preparation meeting an opportunity nobody else noticed.", "iceberg", dict(top="LUCK", bottom="PREPARATION", acc="PREPARATION OPPORTUNITY NOTICED.")),
    ("Someone learned the skill before the opportunity appeared.", "timeline", dict(n=8, progress=0.5, tag="LEARNED EARLY", acc="BEFORE")),
    ("Someone kept practicing.", "stairs", dict(n=6, climb=4, acc="PRACTICING.")),
    ("Someone took a chance.", "path", dict(kind="dashed", fog=True, acc="CHANCE.")),
    ("Someone was ready when the moment arrived.", "door", dict(open_=True, lbl="READY", acc="READY")),
    ("You can't control every opportunity.", "dots", dict(connect=False, acc="CAN'T CONTROL")),
    ("But you can influence how prepared you are when one appears.", "progress", dict(lbl="PREPARED", value=0.8, acc="PREPARED")),
    ("You cannot guarantee luck.", "doc", dict(title="LUCK", empty=True, stamp="NO GUARANTEE", acc="CANNOT LUCK.")),
    ("But you can increase the number of moments where you're ready for it.", "coins", dict(lbl="READY MOMENTS", acc="INCREASE READY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
