from kit import build, follow_sub

TITLE = ("THE MOMENT YOU REALIZE YOU'VE", "BEEN LIVING ON AUTOPILOT")
OUTPUT = "58_Living_On_Autopilot_16x9.mp4"
SPEC = [
    ("You wake up.", "sunrise", dict(acc="WAKE")),
    ("Do the same things.", "list", dict(items=["SAME THINGS"], mode="check", acc="SAME")),
    ("Think the same thoughts.", "brain", dict(says="SAME THOUGHTS", acc="SAME")),
    ("Follow the same routines.", "timeline", dict(n=8, progress=0.5, tag="SAME ROUTINE", acc="SAME")),
    ("React to the same problems.", "notifs", dict(items=["SAME PROBLEM", "SAME PROBLEM"], acc="SAME")),
    ("And another day passes.", "hourglass", dict(acc="ANOTHER")),
    ("Nothing terrible happened.", "list", dict(items=["NOTHING BAD"], mode="check", acc="NOTHING")),
    ("But nothing changed either.", "chart", dict(kind="flat", lbl="CHANGE", acc="NOTHING CHANGED")),
    ("Then weeks become months.", "timeline", dict(n=12, progress=0.7, acc="WEEKS MONTHS.")),
    ("And suddenly…", "pulse", dict()),
    ("You realize you've been living without consciously choosing much of your life.", "alone", dict(tag="WHO CHOSE THIS?", acc="CONSCIOUSLY CHOOSING")),
    ("You were simply reacting.", "big", dict(text="REACTING", acc="REACTING.")),
    ("To notifications.", "notifs", dict(items=["NOTIFICATION"], acc="NOTIFICATIONS.")),
    ("To expectations.", "ring", dict(tags=["DO THIS", "BE THAT"], acc="EXPECTATIONS.")),
    ("To habits.", "path", dict(kind="winding", acc="HABITS.")),
    ("To whatever happened next.", "dots", dict(connect=False, acc="WHATEVER NEXT.")),
    ("That's the danger of autopilot.", "big", dict(text="AUTOPILOT", acc="DANGER AUTOPILOT.")),
    ("It can take you somewhere…", "map", dict(a_lbl="HERE", b_lbl="SOMEWHERE?", acc="SOMEWHERE…")),
    ("Without you ever deciding where you wanted to go.", "compass", dict(lbl="UNCHOSEN", settle=False, acc="DECIDING WANTED")),
    ("Pause your routine occasionally.", "pulse", dict(acc="PAUSE")),
    ("Ask yourself whether you're actually choosing your life…", "path", dict(kind="fork", labels=("REPEAT", "CHOOSE"), acc="CHOOSING")),
    ("Or simply repeating it.", "timeline", dict(n=8, progress=0.5, tag="REPEAT", acc="REPEATING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
