from kit import build, follow_sub, hook

TITLE = ("WHY YOU SHOULD KEEP", "SOME THINGS SIMPLE")
OUTPUT = "275_Why_You_Should_Keep_Some_Things_Simple_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes people make simple problems unnecessarily complicated.", "tangle", dict(lbl="SIMPLE PROBLEM?", acc="SIMPLE COMPLICATED")),
    ("They create elaborate plans.", "doc", dict(title="PLAN V14", empty=False, acc="ELABORATE")),
    ("Research endlessly.", "book", dict(chapter="RESEARCH", text="PAGE 412", acc="ENDLESSLY")),
    ("Compare every option.", "network", dict(nodes=["OPTION A", "OPTION B", "OPTION C", "OPTION D", "OPTION E"], tangled=True, acc="COMPARE EVERY")),
    ("Build complicated systems.", "loop", dict(items=["APP", "SPREADSHEET", "CHECKLIST", "ANOTHER APP"], acc="COMPLICATED SYSTEMS")),
    ("And spend so much time preparing…", "hourglass", dict(acc="PREPARING")),
    ("That the actual task barely begins.", "progress", dict(lbl="THE ACTUAL TASK", value=0.03, acc="ACTUAL BARELY")),
    ("Complexity can feel impressive.", "stage", dict(lbl="IMPRESSIVE", acc="COMPLEXITY IMPRESSIVE")),
    ("But it isn't always useful.", "list", dict(items=["USEFUL"], mode="strike", acc="USEFUL")),
    ("Sometimes the best solution is the simplest one that genuinely works.", "key", dict(lbl="SIMPLE", drop=True, acc="BEST SIMPLEST WORKS")),
    ("A clear plan.", "list", dict(items=["CLEAR PLAN"], mode="check", acc="CLEAR")),
    ("A realistic schedule.", "list", dict(items=["CLEAR PLAN", "REALISTIC SCHEDULE"], mode="check", acc="REALISTIC")),
    ("A straightforward next step.", "list", dict(items=["CLEAR PLAN", "REALISTIC SCHEDULE", "NEXT STEP"], mode="check", acc="STRAIGHTFORWARD")),
    ("A system you can actually maintain.", "list", dict(items=["CLEAR PLAN", "REALISTIC SCHEDULE", "NEXT STEP", "MAINTAINABLE"], mode="check", acc="MAINTAIN")),
    ("You don't need to make every goal complicated to prove you're serious about it.", "scale", dict(left="COMPLICATED", right="SERIOUS", tip=0, acc="COMPLICATED SERIOUS")),
    ("You don't need a perfect system.", "list", dict(items=["PERFECT SYSTEM"], mode="strike", acc="PERFECT")),
    ("You need a system that helps you move.", "path", dict(kind="straight", acc="MOVE")),
    ("What's something you've overcomplicated that turned out to have a much simpler solution?", "cta", dict(kind="comment", lbl="THE SIMPLE FIX", acc="OVERCOMPLICATED SIMPLER")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PLANNING", start=10, end=100, lbl2="ACTUAL PROGRESS", start2=5, end2=3, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
