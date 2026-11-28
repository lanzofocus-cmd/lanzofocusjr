from kit import build, follow_sub, hook

TITLE = ("STOP WAITING FOR A", "DRAMATIC CHANGE")
OUTPUT = "277_Why_You_Should_Stop_Waiting_For_A_Dramatic_Change_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often imagine change as a dramatic moment.", "stage", dict(lbl="THE BIG MOMENT", acc="CHANGE DRAMATIC")),
    ("A sudden realization.", "brain", dict(says="EUREKA!", acc="SUDDEN")),
    ("A completely different mindset.", "shed", dict(old="OLD MIND", new="NEW MIND", acc="DIFFERENT MINDSET")),
    ("A huge decision.", "path", dict(kind="fork", labels=("EVERYTHING", "NOTHING"), acc="HUGE DECISION")),
    ("A new life beginning.", "sunrise", dict(acc="NEW BEGINNING")),
    ("But real change can be much less dramatic.", "list", dict(items=["DRAMATIC"], mode="strike", acc="REAL LESS DRAMATIC")),
    ("It might be noticing a pattern.", "dots", dict(connect=True, acc="NOTICING PATTERN")),
    ("Making a different decision.", "path", dict(kind="fork", labels=("USUAL", "DIFFERENT"), acc="DIFFERENT DECISION")),
    ("Learning a new skill.", "book", dict(chapter="NEW SKILL", acc="SKILL")),
    ("Changing how you respond to something.", "gauge", dict(lbl="REACTION", start=0.8, end=0.4, acc="RESPOND")),
    ("Doing one thing differently than you did yesterday.", "list", dict(items=["ONE THING DIFFERENT"], mode="check", acc="ONE DIFFERENTLY YESTERDAY")),
    ("Then repeating that process.", "loop", dict(items=["NOTICE", "ADJUST", "REPEAT", "NOTICE"], acc="REPEATING")),
    ("The problem with waiting for dramatic change…", "hourglass", dict(acc="WAITING DRAMATIC")),
    ("Is that ordinary change can feel insignificant.", "progress", dict(lbl="FEELS LIKE", value=0.05, acc="ORDINARY INSIGNIFICANT")),
    ("You might be improving without noticing it.", "progress", dict(lbl="REAL PROGRESS", value=0.6, invisible=True, acc="IMPROVING NOTICING")),
    ("You might be making better decisions without feeling transformed.", "list", dict(items=["BETTER CHOICE", "BETTER CHOICE", "BETTER CHOICE"], mode="check", acc="BETTER TRANSFORMED")),
    ("You might be learning slowly.", "stairs", dict(n=10, climb=3, acc="SLOWLY")),
    ("But slow improvement is still improvement.", "chart", dict(kind="up", lbl="SLOW = STILL UP", drop=True, acc="SLOW STILL IMPROVEMENT")),
    ("You don't need every step to feel like a movie scene.", "chairs", dict(n=7, lbl="NO AUDIENCE NEEDED", acc="STEP MOVIE")),
    ("Sometimes your life changes quietly.", "plant", dict(height=0.7, roots=True, lbl="QUIETLY", acc="CHANGES QUIETLY")),
    ("And you only recognize the difference when you look back.", "timeline", dict(n=10, progress=0.9, tag="LOOK HOW FAR", acc="RECOGNIZE BACK")),
    ("What's a small change you've made that eventually had a bigger impact than you expected?", "cta", dict(kind="comment", lbl="SMALL CHANGE, BIG IMPACT", acc="SMALL BIGGER IMPACT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="WAITING FOR A BIG MOMENT", start=10, end=95, lbl2="SMALL STEPS TAKEN", start2=0, end2=3, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
