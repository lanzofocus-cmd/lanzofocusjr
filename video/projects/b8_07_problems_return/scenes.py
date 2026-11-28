from kit import build, follow_sub, hook

TITLE = ("WHY SOME PROBLEMS", "KEEP RETURNING")
OUTPUT = "257_Why_Some_Problems_Keep_Returning_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever solved a problem…", "list", dict(items=["PROBLEM"], mode="check", acc="SOLVED")),
    ("Only for it to return a few weeks later?", "loop", dict(items=["PROBLEM", "FIX", "WEEKS PASS", "PROBLEM"], acc="RETURN WEEKS")),
    ("Maybe you keep running out of time.", "hourglass", dict(acc="TIME")),
    ("Maybe you repeatedly forget important things.", "brain", dict(says="WAIT, WHAT WAS IT?", acc="FORGET")),
    ("Maybe you constantly lose motivation.", "battery", dict(lbl="MOTIVATION", start=0.9, end=0.1, drains=0, acc="MOTIVATION")),
    ("Maybe the same argument keeps happening.", "bubbles", dict(texts=["YOU ALWAYS...", "NO, YOU ALWAYS..."], acc="SAME ARGUMENT")),
    ("You solve the immediate situation.", "list", dict(items=["SOLVED (FOR NOW)"], mode="check", acc="IMMEDIATE")),
    ("But somehow, the problem returns.", "loop", dict(items=["PROBLEM", "FIX", "CALM", "PROBLEM"], acc="RETURNS")),
    ("That's because sometimes you're treating the symptom…", "iceberg", dict(top="THE SYMPTOM", bottom="THE CAUSE", acc="SYMPTOM")),
    ("Instead of the cause.", "iceberg", dict(top="THE SYMPTOM", bottom="THE CAUSE", acc="CAUSE")),
    ("Imagine repeatedly cleaning water from the floor.", "pipe", dict(lbl="CLEANING, AGAIN", acc="CLEANING WATER")),
    ("But never fixing the leaking pipe.", "pipe", dict(mop=False, lbl="THE REAL PROBLEM", acc="FIXING LEAKING PIPE")),
    ("You can clean the floor every day.", "loop", dict(items=["MOP", "DRY", "DRIP", "MOP"], acc="CLEAN EVERY")),
    ("But the problem will continue.", "pipe", dict(acc="CONTINUE")),
    ("The same principle applies to life.", "map", dict(a_lbl="THE PIPE", b_lbl="YOUR LIFE", acc="PRINCIPLE LIFE")),
    ("If you constantly run out of time…", "hourglass", dict(acc="TIME")),
    ("Maybe the problem isn't simply that you need to work faster.", "list", dict(items=["WORK FASTER"], mode="strike", acc="FASTER")),
    ("Maybe you need to organize your priorities.", "list", dict(items=["1. MOST IMPORTANT", "2. NEXT", "3. CAN WAIT"], mode="check", acc="PRIORITIES")),
    ("If you repeatedly forget something…", "fog", dict(lbl="FORGOTTEN", acc="FORGET")),
    ("Maybe you need a system instead of relying entirely on memory.", "doc", dict(title="SYSTEM", empty=False, stamp="WRITTEN DOWN", acc="SYSTEM MEMORY")),
    ("If the same conflict keeps happening…", "loop", dict(items=["TENSION", "ARGUMENT", "MAKE UP", "TENSION"], acc="CONFLICT")),
    ("Maybe the problem isn't the individual argument.", "list", dict(items=["THIS ARGUMENT"], mode="strike", acc="INDIVIDUAL ARGUMENT")),
    ("Maybe it's the communication pattern underneath it.", "iceberg", dict(top="THE ARGUMENT", bottom="THE PATTERN", acc="COMMUNICATION PATTERN")),
    ("When a problem repeats, don't only ask how to fix it again.", "loop", dict(items=["FIX", "AGAIN", "FIX", "AGAIN"], acc="REPEATS FIX AGAIN")),
    ("Ask why it keeps happening.", "key", dict(lbl="WHY?", drop=True, acc="WHY")),
    ("What's a recurring problem you've realized needs a better system, not just another temporary solution?", "cta", dict(kind="comment", lbl="NEEDS A SYSTEM", acc="RECURRING SYSTEM TEMPORARY")),
    ("", "follow"),
]
_HOOK = ("loop", dict(items=["PROBLEM", "QUICK FIX", "CALM", "PROBLEM"], lbl="AGAIN?"))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
