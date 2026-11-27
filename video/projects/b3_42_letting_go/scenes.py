from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN", "GIVING UP AND LETTING GO")
OUTPUT = "82_Giving_Up_Vs_Letting_Go_16x9.mp4"
SPEC = [
    ("Sometimes people tell you to never give up.", "bubbles", dict(texts=["NEVER GIVE UP!", "KEEP PUSHING!"], acc="NEVER GIVE UP.")),
    ("But that's not always wise.", "big", dict(text="ALWAYS?", acc="NOT WISE.")),
    ("Sometimes the goal is wrong.", "compass", dict(lbl="WRONG GOAL", settle=False, acc="WRONG.")),
    ("Sometimes the method isn't working.", "path", dict(kind="winding", acc="METHOD ISN'T")),
    ("Sometimes continuing costs more than it gives.", "receipt", dict(items=[("TIME", "-$$$"), ("ENERGY", "-$$$"), ("RETURN", "$0")], acc="COSTS GIVES.")),
    ("Sometimes…", "pulse", dict()),
    ("The strongest decision is to let go.", "key", dict(lbl="LET GO", acc="STRONGEST LET GO.")),
    ("But there's a difference between abandoning something because it became difficult…", "list", dict(items=["IT GOT HARD"], mode="strike", acc="ABANDONING DIFFICULT…")),
    ("And leaving something because you've genuinely learned it's no longer right for you.", "door", dict(open_=True, lbl="NO LONGER RIGHT", acc="GENUINELY LEARNED")),
    ("One is avoidance.", "shield", dict(front="AVOIDANCE", back="", acc="AVOIDANCE.")),
    ("The other is judgment.", "scale", dict(left="KEEP", right="LET GO", tip=0, acc="JUDGMENT.")),
    ("The important thing is knowing which one you're doing.", "question", dict(a_lbl="AVOIDING?", b_lbl="JUDGING?", acc="KNOWING WHICH")),
    ("Don't worship persistence.", "sticker", dict(tags=["NEVER QUIT"], strike=True, acc="DON'T WORSHIP PERSISTENCE.")),
    ("Use wisdom to decide what deserves your persistence.", "network", dict(nodes=["GOAL A", "GOAL B", "WHAT MATTERS", "GOAL D", "GOAL E"], focus=2, tangled=False, acc="WISDOM DESERVES PERSISTENCE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
