from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO NEVER", "ADMIT THEY DON'T KNOW")
OUTPUT = "268_The_People_Who_Never_Admit_They_Dont_Know_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("There's a strange pressure to always appear knowledgeable.", "gauge", dict(lbl="PRESSURE", start=0.2, end=0.8, acc="PRESSURE KNOWLEDGEABLE")),
    ("People pretend to understand.", "mirror", dict(reflect="dashed", lbl="PRETENDING", acc="PRETEND")),
    ("They avoid asking questions.", "list", dict(items=["ASK QUESTIONS"], mode="strike", acc="AVOID QUESTIONS")),
    ("They nod along.", "crowd", dict(n=7, acc="NOD")),
    ("They use complicated words.", "bubbles", dict(texts=["SYNERGISTIC PARADIGMS..."], acc="COMPLICATED")),
    ("They hide confusion.", "iceberg", dict(top="NODDING", bottom="CONFUSION", acc="HIDE CONFUSION")),
    ("But pretending to understand something doesn't make you understand it.", "scale", dict(left="PRETENDING", right="UNDERSTANDING", tip=1, acc="PRETENDING UNDERSTAND")),
    ("It simply makes learning more difficult.", "lock", dict(lbl="LEARNING", acc="LEARNING DIFFICULT")),
    ("Imagine being in a room where everyone is pretending to understand…", "chairs", dict(n=7, lbl="EVERYONE NODDING", acc="ROOM EVERYONE PRETENDING")),
    ("And nobody asks the question that would help everyone.", "question", dict(a_lbl="THE ONE", b_lbl="QUESTION", acc="NOBODY HELP")),
    ("The conversation continues.", "bubbles", dict(texts=["...AND SO ON."], acc="CONTINUES")),
    ("The confusion remains.", "fog", dict(lbl="CONFUSION", acc="REMAINS")),
    ("And the opportunity to learn disappears.", "door", dict(closing=True, lbl="LEARNING", acc="LEARN DISAPPEARS")),
    ("There's nothing embarrassing about saying:", "pulse", dict(acc="EMBARRASSING")),
    ("\"I don't understand.\"", "quote", dict(text="I DON'T UNDERSTAND.", acc="UNDERSTAND")),
    ("\"Can you explain that?\"", "quote", dict(text="CAN YOU EXPLAIN THAT?", acc="EXPLAIN")),
    ("\"How does that work?\"", "quote", dict(text="HOW DOES THAT WORK?", acc="WORK")),
    ("\"Why is that the case?\"", "quote", dict(text="WHY IS THAT THE CASE?", acc="WHY")),
    ("Curiosity is not weakness.", "sticker", dict(tags=["WEAK"], strike=True, acc="CURIOSITY WEAKNESS")),
    ("Admitting what you don't know is often the beginning of genuinely knowing something.", "door", dict(open_=True, lbl="REAL KNOWLEDGE", drop=True, acc="ADMITTING BEGINNING KNOWING")),
    ("What question do you think people are afraid to ask because they don't want to look uninformed?", "cta", dict(kind="comment", lbl="THE QUESTION NOBODY ASKS", acc="QUESTION AFRAID UNINFORMED")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PEOPLE NODDING", start=10, end=100, lbl2="PEOPLE WHO UNDERSTAND", start2=10, end2=12, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
