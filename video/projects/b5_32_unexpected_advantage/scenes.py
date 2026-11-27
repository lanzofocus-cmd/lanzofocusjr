from kit import build, follow_sub

TITLE = ("THE UNEXPECTED", "ADVANTAGE")
OUTPUT = "172_The_Unexpected_Advantage_16x9.mp4"
SPEC = [
    ("Being inexperienced can be an advantage.", "startline", dict(behind=False, acc="INEXPERIENCED ADVANTAGE")),
    ("You don't know what you're supposed to be afraid of yet.", "fog", dict(lbl="UNKNOWN", acc="AFRAID YET")),
    ("You haven't learned every reason something supposedly can't work.", "list", dict(items=["WON'T WORK", "TOO HARD", "BEEN TRIED"], mode="strike", acc="REASON CAN'T")),
    ("You ask questions others stopped asking.", "question", dict(a_lbl="WHY NOT?", acc="QUESTIONS STOPPED")),
    ("You try things others stopped considering.", "door", dict(open_=True, lbl="TRY IT", acc="TRY CONSIDERING")),
    ("Experience is valuable.", "book", dict(chapter="EXPERIENCE", acc="EXPERIENCE VALUABLE")),
    ("But don't let someone else's experience convince you that curiosity is foolish.", "key", dict(lbl="CURIOSITY", acc="CONVINCE CURIOSITY FOOLISH")),
    ("Share this with someone who's afraid to start because they're a beginner.", "cta", dict(kind="share", lbl="FOR A BEGINNER", acc="SHARE BEGINNER")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
