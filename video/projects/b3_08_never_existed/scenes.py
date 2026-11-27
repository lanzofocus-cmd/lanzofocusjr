from kit import build, follow_sub

TITLE = ("THE VERSION OF YOU", "THAT NEVER EXISTED")
OUTPUT = "48_The_Version_Of_You_That_Never_Existed_16x9.mp4"
SPEC = [
    ("You've probably imagined a version of yourself…", "mirror", dict(reflect="dashed", lbl="IMAGINED YOU", acc="IMAGINED VERSION")),
    ("Who never made those mistakes.", "list", dict(items=["NO MISTAKES"], mode="check", acc="NEVER MISTAKES.")),
    ("Who started earlier.", "startline", dict(behind=True, acc="EARLIER.")),
    ("Who was more confident.", "gauge", dict(lbl="CONFIDENCE", start=0.9, end=0.95, acc="CONFIDENT.")),
    ("Who made better decisions.", "path", dict(kind="fork", labels=("WHAT YOU DID", "THE PERFECT CHOICE"), acc="BETTER DECISIONS.")),
    ("Who never wasted time.", "hourglass", dict(acc="NEVER WASTED")),
    ("And sometimes…", "pulse", dict()),
    ("You spend so much energy comparing yourself to that imaginary person…", "scale", dict(left="YOU", right="IMAGINARY YOU", tip=1, acc="COMPARING IMAGINARY")),
    ("That you forget to work with the real person standing here.", "alone", dict(tag="THE REAL YOU", acc="REAL HERE.")),
    ("The imaginary version had perfect information.", "doc", dict(title="ALL ANSWERS", empty=False, acc="IMAGINARY PERFECT")),
    ("The real you had to learn.", "book", dict(chapter="LEARNING", acc="REAL LEARN.")),
    ("The imaginary version knew the consequences.", "map", dict(a_lbl="CHOICE", b_lbl="KNOWN OUTCOME", acc="KNEW CONSEQUENCES.")),
    ("The real you discovered them.", "fog", dict(lbl="DISCOVERING", acc="DISCOVERED")),
    ("You cannot compete with a person who exists only in your imagination.", "frame", dict(who="NOT REAL", dashed_fig=True, acc="CANNOT IMAGINATION.")),
    ("Your job isn't to become the person you would have been without mistakes.", "list", dict(items=["NO MISTAKES"], mode="strike", acc="ISN'T WITHOUT")),
    ("It's to become the person who learned from them.", "shed", dict(old="MISTAKES", new="LEARNED", acc="LEARNED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
