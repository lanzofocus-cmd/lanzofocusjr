from kit import build, follow_sub, hook

TITLE = ("WHY THE TRUTH CAN", "FEEL LIKE AN INSULT")
OUTPUT = "213_Why_The_Truth_Can_Feel_Like_An_Insult_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes the truth hurts…", "gauge", dict(lbl="IT STINGS", start=0.1, end=0.75, acc="TRUTH HURTS")),
    ("Not because it's cruel.", "list", dict(items=["CRUEL"], mode="strike", acc="CRUEL")),
    ("But because it challenges something we were comfortable believing.", "lock", dict(lbl="COMFORTABLE BELIEF", opening=True, acc="CHALLENGES COMFORTABLE")),
    ("Maybe you thought you were good at something.", "hud", dict(lbl="HOW GOOD I THINK I AM", start=50, end=90, icons=None, crowd=0, acc="GOOD")),
    ("Then someone gave honest feedback.", "bubbles", dict(texts=["HONESTLY? IT NEEDS WORK."], acc="HONEST FEEDBACK")),
    ("Maybe you believed you were being reasonable.", "scale", dict(left="ME", right="REASONABLE", tip=0, acc="REASONABLE")),
    ("Then someone explained how your behavior affected them.", "bubbles", dict(texts=["THAT REALLY HURT ME."], acc="BEHAVIOR AFFECTED")),
    ("Maybe you thought you understood a situation.", "puzzle", dict(missing=False, lbl="UNDERSTOOD", acc="UNDERSTOOD")),
    ("Then you discovered information that changed everything.", "puzzle", dict(missing=True, lbl="NEW PIECE", acc="DISCOVERED CHANGED")),
    ("Your first reaction may be defensive.", "shield", dict(front="DEFENSIVE", back="EGO", acc="DEFENSIVE")),
    ("You want to explain.", "bubbles", dict(texts=["BUT LET ME EXPLAIN..."], acc="EXPLAIN")),
    ("You want to argue.", "bubbles", dict(texts=["BUT LET ME EXPLAIN...", "THAT'S NOT FAIR!"], acc="ARGUE")),
    ("You want to prove that the feedback is wrong.", "doc", dict(title="FEEDBACK", empty=False, stamp="WRONG!", acc="PROVE WRONG")),
    ("But before reacting…", "hourglass", dict(acc="BEFORE REACTING")),
    ("Consider whether there's something useful inside the discomfort.", "key", dict(lbl="INSIDE THE DISCOMFORT", drop=True, acc="USEFUL INSIDE DISCOMFORT")),
    ("You don't have to accept every criticism.", "list", dict(items=["ACCEPT EVERY CRITICISM"], mode="strike", acc="ACCEPT EVERY")),
    ("Some criticism is unfair.", "list", dict(items=["SOME IS UNFAIR"], mode="check", acc="UNFAIR")),
    ("Some people are wrong.", "list", dict(items=["SOME IS UNFAIR", "SOME PEOPLE ARE WRONG"], mode="check", acc="WRONG")),
    ("But automatically rejecting every uncomfortable truth prevents you from learning.", "door", dict(closing=True, lbl="LEARNING", acc="REJECTING PREVENTS LEARNING")),
    ("The goal isn't to agree with everyone.", "list", dict(items=["AGREE WITH EVERYONE"], mode="strike", acc="AGREE EVERYONE")),
    ("The goal is to become someone who can examine information without immediately protecting their ego.", "hud", dict(lbl="CURIOSITY", start=20, end=90, lbl2="EGO", start2=90, end2=20, icons=None, crowd=0, acc="EXAMINE PROTECTING EGO")),
    ("What's the difference between criticism that helps you grow and criticism that simply tears you down?", "scale", dict(left="HELPS YOU GROW", right="TEARS YOU DOWN", tip=0, acc="GROW TEARS")),
    ("Share your perspective.", "cta", dict(kind="comment", lbl="YOUR PERSPECTIVE", acc="PERSPECTIVE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EGO", start=40, end=100, lbl2="OPEN TO TRUTH", start2=60, end2=5, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
