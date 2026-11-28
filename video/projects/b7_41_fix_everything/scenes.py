from kit import build, follow_sub, hook

TITLE = ("TRYING TO FIX", "EVERYTHING AT ONCE")
OUTPUT = "241_The_Problem_With_Trying_To_Fix_Everything_At_Once_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine deciding to change your entire life tomorrow.", "sunrise", dict(acc="ENTIRE TOMORROW")),
    ("New routine.", "list", dict(items=["NEW ROUTINE"], mode="check", acc="ROUTINE")),
    ("New habits.", "list", dict(items=["NEW ROUTINE", "NEW HABITS"], mode="check", acc="HABITS")),
    ("New schedule.", "list", dict(items=["NEW ROUTINE", "NEW HABITS", "NEW SCHEDULE"], mode="check", acc="SCHEDULE")),
    ("New goals.", "list", dict(items=["NEW ROUTINE", "NEW HABITS", "NEW SCHEDULE", "NEW GOALS"], mode="check", acc="GOALS")),
    ("New personality.", "list", dict(items=["NEW ROUTINE", "NEW HABITS", "NEW SCHEDULE", "NEW GOALS", "NEW PERSONALITY"], mode="check", acc="PERSONALITY")),
    ("New everything.", "big", dict(text="NEW EVERYTHING", acc="EVERYTHING")),
    ("At first, the idea feels exciting.", "gauge", dict(lbl="EXCITEMENT", start=0.3, end=0.95, acc="EXCITING")),
    ("You create the perfect plan.", "doc", dict(title="THE PLAN", empty=False, stamp="PERFECT", acc="PERFECT PLAN")),
    ("But the plan requires you to change ten things simultaneously.", "tangle", dict(lbl="10 CHANGES AT ONCE", acc="TEN SIMULTANEOUSLY")),
    ("And suddenly…", "pulse", dict(acc="")),
    ("One difficult day makes the entire system collapse.", "bricks", dict(rows=6, lbl="COLLAPSE", uneven=True, acc="ONE DIFFICULT COLLAPSE")),
    ("This is why change can become overwhelming.", "battery", dict(lbl="CAPACITY", start=0.9, end=0.05, drains=5, acc="OVERWHELMING")),
    ("You try to improve everything before building the ability to maintain anything.", "scale", dict(left="IMPROVE ALL", right="MAINTAIN ONE", tip=1, acc="EVERYTHING MAINTAIN ANYTHING")),
    ("Sometimes the better approach is smaller.", "plant", dict(height=0.25, roots=True, lbl="SMALLER", acc="BETTER SMALLER")),
    ("Choose one area.", "list", dict(items=["ONE AREA"], mode="check", acc="ONE")),
    ("Make one adjustment.", "list", dict(items=["ONE AREA", "ONE ADJUSTMENT"], mode="check", acc="ADJUSTMENT")),
    ("Learn what works.", "list", dict(items=["ONE AREA", "ONE ADJUSTMENT", "LEARN WHAT WORKS"], mode="check", acc="WORKS")),
    ("Then build from there.", "stairs", dict(n=6, climb=3, acc="BUILD")),
    ("You don't need to transform your entire life in one week.", "timeline", dict(n=7, progress=1.0, tag="ONE WEEK?", acc="TRANSFORM WEEK")),
    ("You need a system that allows you to keep improving without constantly restarting.", "loop", dict(items=["ONE CHANGE", "KEEP IT", "ADD ONE", "KEEP IT"], lbl="KEEP IMPROVING", drop=True, acc="SYSTEM IMPROVING RESTARTING")),
    ("If you could improve just one area of your life first, what would you choose?", "cta", dict(kind="comment", lbl="YOUR ONE AREA", acc="ONE FIRST CHOOSE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="CHANGES AT ONCE", start=1, end=10, lbl2="CHANCE IT LASTS", start2=90, end2=4, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
