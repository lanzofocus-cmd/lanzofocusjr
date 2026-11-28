from kit import build, follow_sub, hook

TITLE = ("YOUR PROBLEM", "IS TOO VAGUE")
OUTPUT = "272_The_Moment_You_Realize_Your_Problem_Is_Too_Vague_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("\"I need to improve my life.\"", "quote", dict(text="I NEED TO IMPROVE MY LIFE.", acc="IMPROVE")),
    ("\"I need to become better.\"", "quote", dict(text="I NEED TO BECOME BETTER.", acc="BETTER")),
    ("\"I need to be more productive.\"", "quote", dict(text="I NEED TO BE MORE PRODUCTIVE.", acc="PRODUCTIVE")),
    ("These statements sound meaningful.", "list", dict(items=["SOUNDS MEANINGFUL"], mode="check", acc="MEANINGFUL")),
    ("But they're difficult to act on.", "fog", dict(lbl="WHERE DO I START?", acc="DIFFICULT ACT")),
    ("What does \"improve my life\" actually mean?", "question", dict(a_lbl="IMPROVE", b_lbl="HOW?", acc="IMPROVE MEAN")),
    ("What does \"become better\" look like?", "question", dict(a_lbl="BETTER", b_lbl="AT WHAT?", acc="BETTER LOOK")),
    ("What does \"productive\" mean for you?", "question", dict(a_lbl="PRODUCTIVE", b_lbl="DOING WHAT?", acc="PRODUCTIVE")),
    ("A vague problem creates vague solutions.", "fog", dict(lbl="VAGUE", acc="VAGUE SOLUTIONS")),
    ("You feel like you need to do something…", "gauge", dict(lbl="URGE TO ACT", start=0.3, end=0.85, acc="SOMETHING")),
    ("But you don't know where to begin.", "map", dict(a_lbl="YOU", b_lbl="???", acc="BEGIN")),
    ("Try making the problem specific.", "key", dict(lbl="SPECIFIC", drop=True, acc="SPECIFIC")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I need to improve.\"", "list", dict(items=["I NEED TO IMPROVE."], mode="strike", acc="IMPROVE")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What is one area that's currently causing difficulty?\"", "puzzle", dict(missing=True, lbl="ONE AREA", acc="ONE AREA DIFFICULTY")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I need to be productive.\"", "list", dict(items=["I NEED TO BE PRODUCTIVE."], mode="strike", acc="PRODUCTIVE")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What task needs to be completed today?\"", "list", dict(items=["TODAY: FINISH THE REPORT"], mode="check", acc="TASK TODAY")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I need to change.\"", "list", dict(items=["I NEED TO CHANGE."], mode="strike", acc="CHANGE")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What behavior am I trying to change, and what would the first step look like?\"", "stairs", dict(n=6, climb=1, acc="BEHAVIOR FIRST STEP")),
    ("Clarity doesn't solve every problem.", "list", dict(items=["SOLVES EVERYTHING"], mode="strike", acc="CLARITY")),
    ("But it gives you somewhere to begin.", "startline", dict(behind=False, acc="SOMEWHERE BEGIN")),
    ("What's a vague goal you've been trying to turn into a specific action?", "cta", dict(kind="comment", lbl="VAGUE → SPECIFIC", acc="VAGUE SPECIFIC ACTION")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="MOTIVATION", start=30, end=95, lbl2="CLARITY", start2=5, end2=5, icons="q", tag="\"IMPROVE MY LIFE\"", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
