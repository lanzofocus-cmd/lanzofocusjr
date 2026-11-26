from kit import build, follow_sub

TITLE = ("STOP CONFUSING", "BUSY WITH PROGRESS")
OUTPUT = "31_Stop_Confusing_Busy_With_Progress_16x9.mp4"
SPEC = [
    ("You can be busy all day…", "notifs", dict(items=["9:00 MEETING", "10 NEW EMAILS", "REPLY TO MAX", "UPDATE FILE"], acc="BUSY")),
    ("And still move nowhere.", "path", dict(kind="winding", acc="NOWHERE.")),
    ("You can answer messages.", "list", dict(items=["ANSWER MESSAGES"], mode="check", acc="MESSAGES.")),
    ("Organize files.", "list", dict(items=["ANSWER MESSAGES", "ORGANIZE FILES"], mode="check", acc="ORGANIZE")),
    ("Make plans.", "list", dict(items=["ANSWER MESSAGES", "ORGANIZE FILES", "MAKE PLANS"], mode="check", acc="PLANS.")),
    ("Watch videos about improving.", "list", dict(items=["ANSWER MESSAGES", "ORGANIZE FILES", "MAKE PLANS", "WATCH VIDEOS"], mode="check", acc="IMPROVING.")),
    ("And feel exhausted…", "progress", dict(lbl="ENERGY", value=0.05, acc="EXHAUSTED…")),
    ("Without doing the thing that actually matters.", "list", dict(items=["THE THING THAT MATTERS"], mode="empty", acc="ACTUALLY MATTERS.")),
    ("Busyness creates movement.", "tangle", dict(lbl="MOVEMENT", acc="BUSYNESS MOVEMENT.")),
    ("But movement isn't always progress.", "scale", dict(left="MOVEMENT", right="PROGRESS", tip=0, acc="ISN'T PROGRESS.")),
    ("Before you fill your day…", "timeline", dict(n=8, progress=0.0, acc="FILL")),
    ("Ask yourself one question.", "question", dict(acc="ONE QUESTION.")),
    ("What is the one thing that would actually move me forward?", "network", dict(nodes=["EMAILS", "MEETINGS", "THE ONE THING", "ERRANDS", "SCROLLING"], focus=2, tangled=True, acc="ONE THING FORWARD?")),
    ("Then do that.", "list", dict(items=["THE ONE THING"], mode="check", acc="DO")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
