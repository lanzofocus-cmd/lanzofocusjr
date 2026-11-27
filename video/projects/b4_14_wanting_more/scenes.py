from kit import build, follow_sub

TITLE = ("THE TRAP OF ALWAYS", "WANTING MORE")
OUTPUT = "104_The_Trap_Of_Always_Wanting_More_16x9.mp4"
SPEC = [
    ("You achieve something.", "list", dict(items=["ACHIEVED"], mode="check", acc="ACHIEVE")),
    ("And immediately…", "pulse", dict()),
    ("You want the next thing.", "stairs", dict(n=6, climb=1, highlight=2, acc="NEXT")),
    ("The next goal.", "stairs", dict(n=6, climb=2, highlight=3, acc="GOAL.")),
    ("The next achievement.", "stairs", dict(n=6, climb=3, highlight=4, acc="ACHIEVEMENT.")),
    ("The next level.", "stairs", dict(n=6, climb=4, highlight=5, acc="LEVEL.")),
    ("And there's nothing wrong with ambition.", "sunrise", dict(acc="NOTHING WRONG AMBITION.")),
    ("But if you never stop to recognize what you've accomplished…", "list", dict(items=["DONE", "DONE", "DONE"], mode="check", acc="NEVER RECOGNIZE")),
    ("Your life becomes a permanent chase.", "timeline", dict(n=10, progress=0.9, tag="STILL CHASING", acc="PERMANENT CHASE.")),
    ("Every destination turns into another starting line.", "startline", dict(behind=False, acc="DESTINATION STARTING LINE.")),
    ("You never feel like you've arrived.", "map", dict(a_lbl="HERE", b_lbl="ALWAYS THERE", acc="NEVER ARRIVED.")),
    ("You never allow yourself to appreciate the journey.", "path", dict(kind="winding", acc="NEVER APPRECIATE JOURNEY.")),
    ("Ambition should give your life direction.", "compass", dict(lbl="DIRECTION", acc="AMBITION DIRECTION.")),
    ("It shouldn't make you incapable of appreciating your life.", "lock", dict(lbl="APPRECIATION", opening=True, acc="SHOULDN'T APPRECIATING")),
    ("Take a moment to recognize how far you've come.", "map", dict(a_lbl="WHERE YOU STARTED", b_lbl="HERE", acc="RECOGNIZE FAR")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
