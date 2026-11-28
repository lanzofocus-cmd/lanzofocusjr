from kit import build, follow_sub, hook

TITLE = ("YOUR SMALL DECISIONS DESERVE", "MORE ATTENTION")
OUTPUT = "240_Why_Your_Small_Decisions_Deserve_More_Attention_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often imagine their future being changed by one enormous decision.", "path", dict(kind="fork", labels=("ONE BIG CHOICE", "?"), acc="ENORMOUS DECISION")),
    ("A major opportunity.", "door", dict(open_=True, lbl="MAJOR", acc="OPPORTUNITY")),
    ("A life-changing event.", "big", dict(text="EVENT", sub="LIFE-CHANGING", acc="LIFE-CHANGING")),
    ("A dramatic moment.", "stage", dict(lbl="DRAMATIC", acc="DRAMATIC")),
    ("But much of your life is shaped by decisions that seem too small to matter.", "bricks", dict(rows=6, lbl="SMALL DECISIONS", uneven=False, acc="SHAPED SMALL")),
    ("What you repeatedly choose.", "loop", dict(items=["CHOOSE", "REPEAT", "CHOOSE", "REPEAT"], acc="REPEATEDLY CHOOSE")),
    ("What you repeatedly ignore.", "list", dict(items=["IGNORED", "IGNORED", "IGNORED"], mode="empty", acc="IGNORE")),
    ("How you spend ordinary afternoons.", "hourglass", dict(acc="ORDINARY AFTERNOONS")),
    ("How you respond to small problems.", "gauge", dict(lbl="RESPONSE", start=0.3, end=0.5, acc="RESPOND SMALL")),
    ("How you treat people when nothing important is happening.", "crowd", dict(n=5, highlight=2, highlight_label="ANY DAY", acc="TREAT NOTHING")),
    ("These decisions rarely feel dramatic.", "list", dict(items=["DRAMATIC"], mode="strike", acc="RARELY DRAMATIC")),
    ("But they create patterns.", "dots", dict(connect=True, acc="PATTERNS")),
    ("And patterns influence where you eventually end up.", "map", dict(a_lbl="SMALL CHOICES", b_lbl="WHERE YOU END UP", drop=True, acc="PATTERNS INFLUENCE EVENTUALLY")),
    ("You don't need to make every decision perfect.", "list", dict(items=["PERFECT DECISIONS"], mode="strike", acc="PERFECT")),
    ("But you should understand that small decisions are still decisions.", "doc", dict(title="SMALL CHOICE", empty=False, stamp="STILL COUNTS", acc="SMALL STILL")),
    ("Your future isn't only shaped by the moments you remember.", "frame", dict(who="BIG MOMENTS", acc="FUTURE REMEMBER")),
    ("It's also shaped by the moments you barely notice.", "progress", dict(lbl="QUIET PROGRESS", value=0.6, invisible=True, acc="BARELY NOTICE")),
    ("What's one small decision you think has a bigger impact than people realize?", "cta", dict(kind="comment", lbl="ONE SMALL DECISION", acc="SMALL BIGGER IMPACT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="ONE BIG DECISION", start=60, end=10, lbl2="1,000 SMALL ONES", start2=10, end2=98, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
