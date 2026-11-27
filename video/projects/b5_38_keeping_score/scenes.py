from kit import build, follow_sub

TITLE = ("THE MOMENT YOU", "STOP KEEPING SCORE")
OUTPUT = "178_The_Moment_You_Stop_Keeping_Score_16x9.mp4"
SPEC = [
    ("Not every relationship should feel like a competition.", "scale", dict(left="YOU", right="THEM", tip=-1, acc="RELATIONSHIP COMPETITION")),
    ("Who texted first.", "receipt", dict(items=[("TEXTED FIRST", "ME")], acc="TEXTED FIRST")),
    ("Who gave more.", "receipt", dict(items=[("TEXTED FIRST", "ME"), ("GAVE MORE", "THEM")], acc="GAVE MORE")),
    ("Who apologized.", "receipt", dict(items=[("TEXTED FIRST", "ME"), ("GAVE MORE", "THEM"), ("APOLOGIZED", "ME")], acc="APOLOGIZED")),
    ("Who cared more.", "receipt", dict(items=[("TEXTED FIRST", "ME"), ("GAVE MORE", "THEM"), ("APOLOGIZED", "ME"), ("CARED MORE", "?")], total="2 - 1", acc="CARED MORE")),
    ("When everything becomes a scoreboard…", "big", dict(text="2 : 1", sub="THE SCOREBOARD", acc="SCOREBOARD")),
    ("You stop enjoying the relationship.", "gauge", dict(lbl="ENJOYMENT", start=0.8, end=0.15, acc="STOP ENJOYING")),
    ("Healthy connections aren't built by winning every invisible argument.", "list", dict(items=["WIN EVERY ARGUMENT"], mode="strike", acc="HEALTHY WINNING INVISIBLE")),
    ("They're built by understanding what actually matters.", "network", dict(nodes=["TRUST", "TIME", "CARE"], tangled=False, acc="UNDERSTANDING MATTERS")),
    ("Send this to someone who values genuine connection over keeping score.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND GENUINE CONNECTION")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
