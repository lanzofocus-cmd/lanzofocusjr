from kit import build, follow_sub

TITLE = ("THE VALUE OF A", "BAD FIRST ATTEMPT")
OUTPUT = "187_The_Value_Of_A_Bad_First_Attempt_16x9.mp4"
SPEC = [
    ("Your first attempt isn't supposed to prove that you're talented.", "doc", dict(title="ATTEMPT #1", empty=False, acc="FIRST PROVE TALENTED")),
    ("It's supposed to give you information.", "chart", dict(kind="wave", lbl="DATA", acc="INFORMATION")),
    ("What worked?", "list", dict(items=["WHAT WORKED"], mode="check", acc="WORKED")),
    ("What didn't?", "list", dict(items=["WHAT WORKED", "WHAT DIDN'T"], mode="check", acc="DIDN'T")),
    ("What surprised you?", "list", dict(items=["WHAT WORKED", "WHAT DIDN'T", "WHAT SURPRISED YOU"], mode="check", acc="SURPRISED")),
    ("What needs to change?", "list", dict(items=["WHAT WORKED", "WHAT DIDN'T", "WHAT SURPRISED YOU", "WHAT TO CHANGE"], mode="check", acc="CHANGE")),
    ("A bad first attempt can be more useful than a perfect plan that never gets tested.", "scale", dict(left="BAD ATTEMPT", right="PERFECT PLAN", tip=-1, acc="BAD USEFUL NEVER TESTED")),
    ("You don't need to impress yourself immediately.", "mirror", dict(reflect="solid", lbl="NOT YET", acc="IMPRESS IMMEDIATELY")),
    ("You need something real to improve.", "stairs", dict(n=6, climb=2, acc="REAL IMPROVE")),
    ("Tell us what you're currently trying for the first time.", "cta", dict(kind="comment", lbl="YOUR FIRST ATTEMPT", acc="FIRST TIME")),
    ("Beginners deserve to be seen too.", "crowd", dict(n=5, highlight=2, highlight_label="BEGINNER", acc="BEGINNERS SEEN")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
