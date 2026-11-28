from kit import build, follow_sub, hook

TITLE = ("WHY YOU SHOULD LEARN", "TO BE A BEGINNER")
OUTPUT = "206_Why_You_Should_Learn_To_Be_A_Beginner_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Being a beginner is uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.8, acc="BEGINNER UNCOMFORTABLE")),
    ("You don't know what you're doing.", "fog", dict(lbl="?", acc="KNOW")),
    ("You make mistakes that seem obvious to everyone else.", "crowd", dict(n=7, highlight=3, highlight_label="OOPS", acc="MISTAKES OBVIOUS")),
    ("You ask questions.", "question", dict(a_lbl="HOW DO", b_lbl="I DO THIS?", acc="QUESTIONS")),
    ("You need help.", "bubbles", dict(texts=["CAN YOU SHOW ME?"], acc="HELP")),
    ("You improve slowly.", "progress", dict(lbl="SKILL", value=0.1, acc="SLOWLY")),
    ("And sometimes, the worst part isn't the difficulty.", "list", dict(items=["THE DIFFICULTY"], mode="strike", acc="WORST DIFFICULTY")),
    ("It's watching someone else do the same thing effortlessly.", "stage", dict(lbl="EFFORTLESS", acc="EFFORTLESSLY")),
    ("But here's the problem.", "pulse", dict(acc="PROBLEM")),
    ("You are comparing their experience to your beginning.", "timeline", dict(compare=True, acc="EXPERIENCE BEGINNING")),
    ("You see the finished performance.", "stage", dict(lbl="THE PERFORMANCE", acc="FINISHED PERFORMANCE")),
    ("You don't see the hundreds of mistakes that helped create it.", "iceberg", dict(top="THE PERFORMANCE", bottom="HUNDREDS OF MISTAKES", acc="HUNDREDS MISTAKES")),
    ("Every expert was once unfamiliar with the basics.", "frame", dict(who="THE EXPERT, YEAR 1", acc="EXPERT BASICS")),
    ("Every skilled person once struggled with something that eventually became automatic.", "stairs", dict(n=7, climb=6, acc="STRUGGLED AUTOMATIC")),
    ("The only way to skip being a beginner…", "stairs", dict(n=7, climb=0, acc="SKIP BEGINNER")),
    ("Is to skip learning.", "list", dict(items=["LEARNING"], mode="strike", acc="LEARNING")),
    ("So if you're starting something new and feel awkward, don't immediately assume you're bad at it.", "sticker", dict(tags=["BAD AT IT"], strike=True, acc="AWKWARD BAD")),
    ("You might simply be experiencing the normal process of learning.", "chart", dict(kind="up", lbl="NORMAL LEARNING", acc="NORMAL LEARNING")),
    ("Allow yourself to be inexperienced.", "startline", dict(behind=False, acc="INEXPERIENCED")),
    ("Ask questions.", "list", dict(items=["ASK QUESTIONS"], mode="check", acc="QUESTIONS")),
    ("Make mistakes.", "list", dict(items=["ASK QUESTIONS", "MAKE MISTAKES"], mode="check", acc="MISTAKES")),
    ("Practice.", "list", dict(items=["ASK QUESTIONS", "MAKE MISTAKES", "PRACTICE"], mode="check", acc="PRACTICE")),
    ("The beginning isn't proof that you're incapable.", "doc", dict(title="PROOF", empty=True, stamp="NOT PROOF", acc="PROOF INCAPABLE")),
    ("It's proof that you're finally doing something you haven't done before.", "door", dict(open_=True, lbl="SOMETHING NEW", drop=True, acc="FINALLY BEFORE")),
    ("What skill are you currently a beginner at?", "hud", dict(lbl="SKILL", start=0, end=12, icons=None, crowd=0, tag="DAY 1", acc="SKILL BEGINNER")),
    ("Comment it. Let's normalize starting from zero.", "cta", dict(kind="comment", lbl="STARTING FROM ZERO", acc="NORMALIZE ZERO")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="SKILL LEVEL", start=0, end=3, icons="q", tag="BEGINNER", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
