from kit import build, follow_sub

TITLE = ("YOUR OPINION OF YOURSELF", "ISN'T OBJECTIVE")
OUTPUT = "109_Your_Opinion_Of_Yourself_Isnt_Objective_16x9.mp4"
SPEC = [
    ("You think you know yourself.", "mirror", dict(reflect="solid", lbl="ME", acc="KNOW YOURSELF.")),
    ("But your self-image is influenced by experiences.", "ring", dict(tags=["EXPERIENCES"], acc="SELF-IMAGE EXPERIENCES.")),
    ("Mistakes.", "ring", dict(tags=["EXPERIENCES", "MISTAKES"], acc="MISTAKES.")),
    ("Feedback.", "ring", dict(tags=["EXPERIENCES", "MISTAKES", "FEEDBACK"], acc="FEEDBACK.")),
    ("Comparisons.", "ring", dict(tags=["EXPERIENCES", "MISTAKES", "FEEDBACK", "COMPARISONS"], acc="COMPARISONS.")),
    ("Emotions.", "ring", dict(tags=["EXPERIENCES", "MISTAKES", "FEEDBACK", "COMPARISONS", "EMOTIONS"], acc="EMOTIONS.")),
    ("And sometimes…", "pulse", dict()),
    ("You judge yourself more harshly than you judge anyone else.", "scale", dict(left="YOU", right="EVERYONE ELSE", tip=-1, acc="HARSHLY")),
    ("You remember your failures.", "list", dict(items=["FAILURES"], mode="check", acc="FAILURES.")),
    ("You overlook your progress.", "list", dict(items=["PROGRESS"], mode="strike", acc="OVERLOOK PROGRESS.")),
    ("You notice your weaknesses.", "sticker", dict(tags=["WEAK"], acc="WEAKNESSES.")),
    ("You dismiss your strengths.", "sticker", dict(tags=["WEAK", "STRONG"], acc="DISMISS STRENGTHS.")),
    ("Try looking at yourself the way you might look at a friend.", "crowd", dict(n=2, acc="FRIEND.")),
    ("With honesty…", "mirror", dict(reflect="solid", lbl="HONEST", acc="HONESTY…")),
    ("But also with fairness.", "scale", dict(left="HONESTY", right="FAIRNESS", tip=0, acc="FAIRNESS.")),
    ("Self-awareness isn't the same as self-criticism.", "scale", dict(left="AWARENESS", right="CRITICISM", tip=0, acc="SELF-AWARENESS SELF-CRITICISM.")),
    ("You can recognize what needs improvement without treating yourself like an enemy.", "shield", dict(front="NOT AN ENEMY", back="", acc="IMPROVEMENT ENEMY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
