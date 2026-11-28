from kit import build, follow_sub, hook

TITLE = ("YOU HAVE BEEN", "WASTING ENERGY")
OUTPUT = "260_The_Moment_You_Realize_You_Have_Been_Wasting_Energy_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine spending an entire day worrying about something…", "brain", dict(says="WHAT IF...", says2="AND THEN...", acc="ENTIRE WORRYING")),
    ("That never actually happens.", "frame", dict(who="NEVER HAPPENED", dashed_fig=True, acc="NEVER HAPPENS")),
    ("You replay conversations.", "loop", dict(items=["REPLAY", "REWIND", "REPLAY", "REWIND"], acc="REPLAY")),
    ("Imagine arguments.", "bubbles", dict(texts=["AND THEN I'D SAY..."], acc="ARGUMENTS")),
    ("Predict problems.", "doc", dict(title="WORST CASE", empty=False, acc="PREDICT")),
    ("Prepare for situations that may never exist.", "shield", dict(front="READY", back="FOR NOTHING", acc="PREPARE NEVER EXIST")),
    ("And by the time the day ends…", "hourglass", dict(acc="ENDS")),
    ("Nothing happened.", "big", dict(text="NOTHING.", acc="NOTHING")),
    ("But you still feel exhausted.", "battery", dict(lbl="YOUR ENERGY", start=0.9, end=0.05, drains=0, acc="EXHAUSTED")),
    ("This is one of the strange ways the mind consumes energy.", "battery", dict(lbl="YOUR ENERGY", start=0.9, end=0.15, drains=4, acc="MIND CONSUMES ENERGY")),
    ("It can make you experience an imagined problem as if it were already happening.", "iceberg", dict(top="REAL", bottom="IMAGINED", acc="IMAGINED ALREADY")),
    ("Planning is useful.", "list", dict(items=["PLANNING"], mode="check", acc="PLANNING")),
    ("Preparing is useful.", "list", dict(items=["PLANNING", "PREPARING"], mode="check", acc="PREPARING")),
    ("Thinking carefully is useful.", "list", dict(items=["PLANNING", "PREPARING", "THINKING CAREFULLY"], mode="check", acc="THINKING")),
    ("But repeatedly imagining the same problem without taking action…", "loop", dict(items=["IMAGINE", "WORRY", "IMAGINE", "WORRY"], acc="REPEATEDLY ACTION")),
    ("Can become a loop.", "loop", dict(items=["IMAGINE", "WORRY", "IMAGINE", "WORRY"], lbl="THE LOOP", acc="LOOP")),
    ("If something is within your control, identify the next reasonable step.", "stairs", dict(n=6, climb=1, acc="CONTROL NEXT STEP")),
    ("If something isn't within your control, recognize that repeatedly thinking about it doesn't automatically change it.", "fog", dict(lbl="OUT OF YOUR CONTROL", acc="CONTROL THINKING CHANGE")),
    ("Your attention is valuable.", "price", dict(text="YOUR ATTENTION", sub="VALUABLE", acc="ATTENTION VALUABLE")),
    ("Don't spend all of it living through problems that haven't happened.", "hud", dict(lbl="IMAGINED PROBLEMS", start=90, end=10, lbl2="REAL LIFE", start2=10, end2=90, icons=None, crowd=0, drop=True, acc="LIVING HAVEN'T HAPPENED")),
    ("Save this for the next time you catch yourself mentally preparing for something that may never happen.", "cta", dict(kind="save", lbl="IT MAY NEVER HAPPEN", acc="SAVE PREPARING NEVER")),
    ("", "follow"),
]
_HOOK = ("battery", dict(lbl="ENERGY ON \"WHAT IF\"", start=1.0, end=0.04, drains=5))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
