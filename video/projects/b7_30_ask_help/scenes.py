from kit import build, follow_sub, hook

TITLE = ("LEARN TO ASK", "FOR HELP EARLIER")
OUTPUT = "230_Why_You_Should_Learn_To_Ask_For_Help_Earlier_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Some people wait until they're completely overwhelmed before asking for help.", "gauge", dict(lbl="OVERWHELM", start=0.3, end=0.98, acc="OVERWHELMED HELP")),
    ("They struggle alone.", "alone", dict(tag="STRUGGLING", acc="ALONE")),
    ("They hide the problem.", "iceberg", dict(top="I'M FINE", bottom="THE PROBLEM", acc="HIDE")),
    ("They keep trying to solve something they don't understand.", "loop", dict(items=["TRY", "FAIL", "TRY HARDER", "FAIL"], acc="SOLVE UNDERSTAND")),
    ("And eventually, the situation becomes much harder than it needed to be.", "bricks", dict(rows=6, lbl="HARDER", uneven=True, acc="HARDER")),
    ("Why?", "big", dict(text="WHY?", acc="WHY")),
    ("Because asking for help can feel like admitting weakness.", "sticker", dict(tags=["WEAK?"], acc="ADMITTING WEAKNESS")),
    ("But imagine learning something new.", "book", dict(chapter="NEW TOPIC", acc="LEARNING")),
    ("You spend hours confused.", "hourglass", dict(acc="HOURS CONFUSED")),
    ("Someone could explain it in five minutes.", "bubbles", dict(texts=["OH, IT'S LIKE THIS."], acc="FIVE MINUTES")),
    ("Would asking them make you less capable?", "question", dict(acc="LESS CAPABLE")),
    ("No.", "big", dict(text="NO.", acc="NO")),
    ("It would help you learn.", "chart", dict(kind="up", lbl="LEARNING", acc="LEARN")),
    ("There is a difference between becoming dependent on someone…", "scale", dict(left="DEPENDENT", right="RESOURCEFUL", tip=0, acc="DEPENDENT")),
    ("And using the knowledge available to you.", "network", dict(nodes=["TEACHER", "FRIEND", "COLLEAGUE", "MENTOR"], tangled=False, acc="KNOWLEDGE AVAILABLE")),
    ("You don't have to know everything.", "list", dict(items=["KNOW EVERYTHING"], mode="strike", acc="EVERYTHING")),
    ("You don't have to solve every problem alone.", "list", dict(items=["KNOW EVERYTHING", "SOLVE IT ALONE"], mode="strike", acc="ALONE")),
    ("Sometimes the fastest way forward is to admit what you don't understand.", "door", dict(open_=True, lbl="ASK", drop=True, acc="FASTEST ADMIT UNDERSTAND")),
    ("What is something you wish people felt more comfortable asking for help with?", "cta", dict(kind="comment", lbl="IT'S OKAY TO ASK ABOUT...", acc="COMFORTABLE HELP")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="STRUGGLING ALONE", start=5, end=95, lbl2="ASKED FOR HELP", start2=0, end2=0, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
