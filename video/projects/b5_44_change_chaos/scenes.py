from kit import build, follow_sub

TITLE = ("CHANGE VS", "CHAOS")
OUTPUT = "184_The_Difference_Between_Change_And_Chaos_16x9.mp4"
SPEC = [
    ("Changing your life doesn't mean changing everything at once.", "tangle", dict(lbl="EVERYTHING AT ONCE", acc="EVERYTHING ONCE")),
    ("New goals.", "list", dict(items=["NEW GOALS"], mode="check", acc="GOALS")),
    ("New routines.", "list", dict(items=["NEW GOALS", "NEW ROUTINES"], mode="check", acc="ROUTINES")),
    ("New plans.", "list", dict(items=["NEW GOALS", "NEW ROUTINES", "NEW PLANS"], mode="check", acc="PLANS")),
    ("New expectations.", "list", dict(items=["NEW GOALS", "NEW ROUTINES", "NEW PLANS", "NEW EXPECTATIONS"], mode="check", acc="EXPECTATIONS")),
    ("Too much change at once can become another way to overwhelm yourself.", "gauge", dict(lbl="OVERWHELM", start=0.3, end=0.98, acc="OVERWHELM")),
    ("You don't need to destroy your entire routine to improve one part of your life.", "bricks", dict(rows=4, lbl="CHANGE ONE BRICK", uneven=False, acc="DESTROY ONE PART")),
    ("Make changes that you can actually live with.", "plant", dict(height=0.45, roots=True, lbl="SUSTAINABLE", acc="LIVE WITH")),
    ("What's one small change that would make your daily life noticeably better?", "cta", dict(kind="comment", lbl="ONE SMALL CHANGE", acc="SMALL CHANGE BETTER")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
