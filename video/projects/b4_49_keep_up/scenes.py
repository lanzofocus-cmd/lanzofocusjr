from kit import build, follow_sub

TITLE = ("YOU DON'T HAVE TO KEEP", "UP WITH EVERYONE")
OUTPUT = "139_You_Dont_Have_To_Keep_Up_With_Everyone_16x9.mp4"
SPEC = [
    ("Someone is moving faster.", "timeline", dict(compare=True, acc="FASTER.")),
    ("Someone is achieving more.", "list", dict(items=["ACHIEVED", "ACHIEVED", "ACHIEVED"], mode="check", acc="MORE.")),
    ("Someone is getting attention.", "stage", dict(acc="ATTENTION.")),
    ("Someone is reaching a milestone.", "stairs", dict(n=6, climb=5, acc="MILESTONE.")),
    ("And you feel pressure to catch up.", "gauge", dict(lbl="PRESSURE", start=0.3, end=0.9, acc="PRESSURE CATCH")),
    ("But you don't know their circumstances.", "iceberg", dict(top="WHAT YOU SEE", bottom="THEIR CIRCUMSTANCES", acc="DON'T CIRCUMSTANCES.")),
    ("Their resources.", "iceberg", dict(top="WHAT YOU SEE", bottom="THEIR RESOURCES", acc="RESOURCES.")),
    ("Their responsibilities.", "iceberg", dict(top="WHAT YOU SEE", bottom="THEIR RESPONSIBILITIES", acc="RESPONSIBILITIES.")),
    ("Their opportunities.", "iceberg", dict(top="WHAT YOU SEE", bottom="THEIR OPPORTUNITIES", acc="OPPORTUNITIES.")),
    ("Their starting point.", "startline", dict(behind=True, acc="STARTING")),
    ("Comparing speed without understanding context…", "scale", dict(left="SPEED", right="CONTEXT", tip=1, acc="SPEED CONTEXT…")),
    ("Can make you feel behind for no reason.", "startline", dict(behind=True, acc="BEHIND NO REASON.")),
    ("Your progress doesn't need to match someone else's pace to be meaningful.", "progress", dict(lbl="YOUR PROGRESS", value=0.5, acc="DOESN'T PACE MEANINGFUL.")),
    ("Focus on your own direction.", "compass", dict(lbl="YOUR DIRECTION", acc="OWN DIRECTION.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
