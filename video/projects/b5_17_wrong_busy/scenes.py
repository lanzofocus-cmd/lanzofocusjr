from kit import build, follow_sub

TITLE = ("THE WRONG", "KIND OF BUSY")
OUTPUT = "157_The_Wrong_Kind_Of_Busy_16x9.mp4"
SPEC = [
    ("Being busy can feel productive.", "gauge", dict(lbl="BUSY", start=0.3, end=0.9, acc="BUSY PRODUCTIVE")),
    ("Your day is full.", "list", dict(items=["9:00", "11:00", "1:00", "3:00", "5:00"], mode="check", acc="FULL")),
    ("Your notifications are constant.", "notifs", dict(acc="CONSTANT")),
    ("You're always doing something.", "tangle", dict(lbl="ALWAYS DOING", acc="ALWAYS SOMETHING")),
    ("But activity isn't automatically progress.", "scale", dict(left="ACTIVITY", right="PROGRESS", tip=1, acc="ACTIVITY PROGRESS")),
    ("You can spend an entire day moving…", "path", dict(kind="winding", acc="ENTIRE MOVING")),
    ("And still avoid the one thing that mattered most.", "list", dict(items=["THE ONE THING"], mode="empty", acc="AVOID MATTERED")),
    ("Before you ask how much you did…", "receipt", dict(items=[("EMAILS", "40"), ("MEETINGS", "6"), ("TABS", "23")], total="BUSY", acc="HOW MUCH")),
    ("Ask whether it moved you somewhere.", "compass", dict(lbl="SOMEWHERE", acc="MOVED SOMEWHERE")),
    ("What's the one task that actually matters most to you right now?", "cta", dict(kind="comment", lbl="YOUR ONE TASK", acc="ONE TASK MATTERS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
