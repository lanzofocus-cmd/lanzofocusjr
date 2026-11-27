from kit import build, follow_sub

TITLE = ("THE DAY", "YOU REALIZE")
OUTPUT = "180_The_Day_You_Realize_16x9.mp4"
SPEC = [
    ("One day, you may realize…", "sunrise", dict(acc="REALIZE")),
    ("The people you thought were paying attention weren't.", "chairs", dict(n=7, lbl="NOBODY WATCHING", acc="ATTENTION WEREN'T")),
    ("The things you thought mattered didn't.", "list", dict(items=["THEIR OPINION", "LOOKING PERFECT"], mode="strike", acc="MATTERED DIDN'T")),
    ("The worries that consumed you disappeared.", "fog", dict(lbl="OLD WORRIES", acc="WORRIES DISAPPEARED")),
    ("And the moments you barely noticed became the ones you remember.", "frame", dict(who="A SMALL MOMENT", new="YOU, LATER", acc="BARELY REMEMBER")),
    ("Don't wait until life is over to discover what deserved your attention.", "hourglass", dict(acc="DON'T WAIT ATTENTION")),
    ("What's something you wish you appreciated more while it was happening?", "cta", dict(kind="comment", lbl="WHAT YOU'D APPRECIATE MORE", acc="APPRECIATED HAPPENING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
