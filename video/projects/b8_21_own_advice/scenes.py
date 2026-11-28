from kit import build, follow_sub, hook

TITLE = ("WHY YOU SHOULD TAKE", "YOUR OWN ADVICE")
OUTPUT = "271_Why_You_Should_Take_Your_Own_Advice_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Think about the advice you give other people.", "bubbles", dict(texts=["HERE'S WHAT I'D DO."], acc="ADVICE OTHER")),
    ("When a friend is struggling…", "crowd", dict(n=3, highlight=1, highlight_label="STRUGGLING", acc="STRUGGLING")),
    ("You tell them to be patient.", "bubbles", dict(texts=["BE PATIENT."], acc="PATIENT")),
    ("When someone makes a mistake…", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKE")),
    ("You tell them they can learn.", "bubbles", dict(texts=["YOU'LL LEARN FROM IT."], acc="LEARN")),
    ("When someone is overwhelmed…", "tangle", dict(lbl="OVERWHELMED", acc="OVERWHELMED")),
    ("You remind them to take things one step at a time.", "stairs", dict(n=6, climb=1, acc="ONE STEP")),
    ("When someone is worried…", "fog", dict(lbl="WORRY", acc="WORRIED")),
    ("You help them see another perspective.", "network", dict(nodes=["ANOTHER VIEW", "YOUR VIEW", "A BETTER VIEW"], tangled=False, acc="ANOTHER PERSPECTIVE")),
    ("But when the same situation happens to you…", "mirror", dict(reflect="solid", lbl="NOW IT'S YOU", acc="SAME YOU")),
    ("You suddenly forget everything.", "frame", dict(who="YOUR OWN ADVICE", fade=True, acc="FORGET EVERYTHING")),
    ("You criticize yourself.", "quote", dict(text="WHAT'S WRONG WITH ME?", acc="CRITICIZE")),
    ("You panic.", "gauge", dict(lbl="PANIC", start=0.3, end=0.95, acc="PANIC")),
    ("You expect perfection.", "doc", dict(title="STANDARD", empty=False, stamp="PERFECT ONLY", acc="PERFECTION")),
    ("You refuse to give yourself the patience you would give someone else.", "scale", dict(left="PATIENCE FOR THEM", right="PATIENCE FOR YOU", tip=-1, acc="REFUSE PATIENCE")),
    ("This doesn't mean your advice is always correct.", "list", dict(items=["ALWAYS CORRECT"], mode="strike", acc="ALWAYS CORRECT")),
    ("But it may reveal something important.", "key", dict(lbl="SOMETHING IMPORTANT", acc="REVEAL IMPORTANT")),
    ("You already know some of the principles that could help you.", "book", dict(chapter="YOU ALREADY KNOW", acc="ALREADY PRINCIPLES")),
    ("The challenge is applying them when you're personally involved.", "hud", dict(lbl="KNOWING IT", start=60, end=95, lbl2="APPLYING IT", start2=10, end2=15, icons=None, crowd=0, acc="APPLYING PERSONALLY")),
    ("Sometimes you need to step back…", "pulse", dict(acc="STEP BACK")),
    ("And treat yourself like someone you're genuinely trying to help.", "mirror", dict(reflect="solid", lbl="BE YOUR OWN FRIEND", drop=True, acc="TREAT YOURSELF HELP")),
    ("What's advice you regularly give others that you need to start applying to yourself?", "cta", dict(kind="comment", lbl="ADVICE FOR YOURSELF", acc="ADVICE APPLYING YOURSELF")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PATIENCE FOR OTHERS", start=40, end=100, lbl2="PATIENCE FOR YOURSELF", start2=40, end2=6, icons="heart", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
