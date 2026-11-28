from kit import build, follow_sub, hook

TITLE = ("CONFIDENCE VS", "CERTAINTY")
OUTPUT = "225_The_Difference_Between_Confidence_And_Certainty_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Confidence doesn't mean knowing exactly what will happen.", "fog", dict(lbl="WHAT HAPPENS NEXT", acc="CONFIDENCE EXACTLY")),
    ("It doesn't mean believing you'll never fail.", "list", dict(items=["NEVER FAIL"], mode="strike", acc="NEVER FAIL")),
    ("It doesn't mean having every answer.", "list", dict(items=["NEVER FAIL", "EVERY ANSWER"], mode="strike", acc="EVERY ANSWER")),
    ("Sometimes confidence means knowing that you can handle being uncertain.", "shield", dict(front="I CAN HANDLE IT", back="YOU", acc="HANDLE UNCERTAIN")),
    ("You can enter a situation without knowing the outcome.", "door", dict(open_=True, lbl="UNKNOWN", acc="WITHOUT OUTCOME")),
    ("You can try something without guaranteeing success.", "startline", dict(behind=False, acc="TRY GUARANTEEING")),
    ("You can make a decision while understanding that you might need to adjust.", "path", dict(kind="fork", labels=("PLAN", "ADJUST"), acc="DECISION ADJUST")),
    ("Certainty says:", "lock", dict(lbl="CERTAINTY", acc="CERTAINTY")),
    ("\"I know this will work.\"", "quote", dict(text="I KNOW THIS WILL WORK.", acc="KNOW WORK")),
    ("Confidence says:", "key", dict(lbl="CONFIDENCE", acc="CONFIDENCE")),
    ("\"I can deal with what happens.\"", "quote", dict(text="I CAN DEAL WITH WHAT HAPPENS.", drop=True, acc="DEAL HAPPENS")),
    ("That difference matters.", "scale", dict(left="CERTAINTY", right="CONFIDENCE", tip=1, acc="DIFFERENCE")),
    ("Because life rarely gives you complete information before requiring a decision.", "puzzle", dict(missing=True, lbl="DECIDE ANYWAY", acc="COMPLETE DECISION")),
    ("You can't wait until every possibility is predictable.", "hourglass", dict(acc="WAIT PREDICTABLE")),
    ("Sometimes you have to make the best decision available…", "path", dict(kind="fork", labels=("BEST AVAILABLE", "WAIT"), acc="BEST AVAILABLE")),
    ("Then learn from the result.", "loop", dict(items=["DECIDE", "RESULT", "LEARN", "ADJUST"], acc="LEARN RESULT")),
    ("Save this if you want to remember that confidence doesn't require certainty.", "cta", dict(kind="save", lbl="NO CERTAINTY NEEDED", acc="SAVE CONFIDENCE CERTAINTY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="CERTAINTY", start=60, end=0, lbl2="CONFIDENCE", start2=10, end2=95, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
