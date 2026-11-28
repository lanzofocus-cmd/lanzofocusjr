from kit import build, follow_sub, hook

TITLE = ("YOUR ENVIRONMENT CAN", "CHANGE YOUR BEHAVIOR")
OUTPUT = "202_Why_Your_Environment_Can_Change_Your_Behavior_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine trying to concentrate in a room filled with distractions.", "tangle", dict(lbl="DISTRACTIONS", acc="CONCENTRATE DISTRACTIONS")),
    ("Your phone is beside you.", "notifs", dict(items=["NEW MESSAGE"], acc="PHONE")),
    ("Your favorite apps are open.", "notifs", dict(items=["NEW MESSAGE", "3 NEW VIDEOS", "TRENDING NOW"], acc="APPS")),
    ("Your desk is cluttered.", "bricks", dict(rows=3, lbl="CLUTTER", uneven=True, acc="CLUTTERED")),
    ("People are constantly interrupting you.", "bubbles", dict(texts=["HEY, GOT A SEC?", "QUICK QUESTION!"], acc="INTERRUPTING")),
    ("Then imagine blaming yourself because you can't focus.", "mirror", dict(reflect="solid", lbl="IT'S MY FAULT?", acc="BLAMING FOCUS")),
    ("We often treat behavior as if it's only about willpower.", "battery", dict(lbl="WILLPOWER", start=0.9, end=0.4, drains=4, acc="BEHAVIOR WILLPOWER")),
    ("But your environment quietly influences the decisions you make.", "ring", dict(tags=["PHONE", "DESK", "PEOPLE", "APPS"], acc="ENVIRONMENT INFLUENCES")),
    ("A phone within reach makes checking it easier.", "phone", dict(lbl="WITHIN REACH", acc="PHONE EASIER")),
    ("A clean workspace makes beginning easier.", "doc", dict(title="CLEAN DESK", empty=True, acc="CLEAN BEGINNING")),
    ("Having everything you need prepared removes unnecessary friction.", "list", dict(items=["BOOK OUT", "PEN READY", "PHONE AWAY"], mode="check", acc="PREPARED FRICTION")),
    ("Being around people who take something seriously can make it feel normal to take it seriously yourself.", "crowd", dict(n=5, highlight=2, highlight_label="YOU", acc="SERIOUSLY NORMAL")),
    ("This doesn't mean your environment controls you.", "list", dict(items=["IT CONTROLS YOU"], mode="strike", acc="CONTROLS")),
    ("It means you should stop making difficult decisions harder than necessary.", "stairs", dict(n=4, climb=2, acc="DIFFICULT HARDER")),
    ("If you want to read more, put the book somewhere visible.", "book", dict(chapter="IN SIGHT", acc="READ VISIBLE")),
    ("If you want to practice something, make the equipment easy to access.", "key", dict(lbl="EASY ACCESS", acc="PRACTICE EASY")),
    ("If you want fewer distractions, don't place your biggest distraction directly in front of you.", "door", dict(closing=True, lbl="PHONE IN ANOTHER ROOM", acc="FEWER DISTRACTION")),
    ("Sometimes improving your behavior doesn't require becoming a completely different person.", "list", dict(items=["A DIFFERENT PERSON"], mode="strike", acc="IMPROVING DIFFERENT")),
    ("It requires changing the conditions surrounding the person you already are.", "ring", dict(tags=["BOOK", "CLEAN DESK", "GOOD PEOPLE", "NO PHONE"], drop=True, acc="CHANGING CONDITIONS ALREADY")),
    ("What is one thing in your environment you could change to make your life easier?", "hud", dict(lbl="FRICTION", start=80, end=15, icons=None, crowd=0, acc="ENVIRONMENT EASIER")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="ONE THING TO CHANGE", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="FOCUS", start=90, end=12, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
