from kit import build, follow_sub

TITLE = ("LONELY VS", "EMPTY")
OUTPUT = "162_The_Difference_Between_Lonely_And_Empty_16x9.mp4"
SPEC = [
    ("Being alone doesn't automatically mean something is missing.", "puzzle", dict(missing=False, lbl="NOTHING MISSING", acc="ALONE MISSING")),
    ("Sometimes being alone is where you finally hear your own thoughts.", "brain", dict(says="FINALLY, QUIET.", acc="HEAR THOUGHTS")),
    ("Where you discover what you actually enjoy.", "list", dict(items=["BOOKS", "WALKS", "MUSIC"], mode="check", acc="DISCOVER ENJOY")),
    ("Where you stop performing for an audience.", "stage", dict(lbl="NO AUDIENCE", empty=True, acc="PERFORMING AUDIENCE")),
    ("You don't need constant company to prove that your life is meaningful.", "alone", dict(tag="STILL MEANINGFUL", acc="CONSTANT MEANINGFUL")),
    ("Learn to enjoy your own presence.", "mirror", dict(reflect="solid", lbl="GOOD COMPANY", acc="ENJOY PRESENCE")),
    ("Save this for the days when being alone makes you question whether you're doing something wrong.", "cta", dict(kind="save", lbl="FOR QUIET DAYS", acc="SAVE ALONE WRONG")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
