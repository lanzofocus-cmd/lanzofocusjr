from kit import build, follow_sub

TITLE = ("THE WRONG QUESTION", "ABOUT SUCCESS")
OUTPUT = "174_The_Wrong_Question_About_Success_16x9.mp4"
SPEC = [
    ("Instead of asking, \"Am I successful?\"", "quote", dict(text="AM I SUCCESSFUL?", acc="SUCCESSFUL")),
    ("Ask:", "arrows", dict(items=["THE QUESTION"], acc="")),
    ("\"Am I becoming someone I respect?\"", "mirror", dict(reflect="solid", lbl="RESPECT?", acc="BECOMING RESPECT")),
    ("Because success can look impressive from the outside…", "stage", dict(lbl="IMPRESSIVE", acc="IMPRESSIVE OUTSIDE")),
    ("And feel completely wrong on the inside.", "iceberg", dict(top="LOOKS RIGHT", bottom="FEELS WRONG", acc="WRONG INSIDE")),
    ("Your achievements matter.", "crown", dict(lbl="ACHIEVEMENTS", acc="ACHIEVEMENTS MATTER")),
    ("But so does the person you become while chasing them.", "shed", dict(old="WHO YOU WERE", new="WHO YOU BECOME", acc="PERSON BECOME")),
    ("Don't build a life you only enjoy showing people.", "phone", dict(lbl="FOR SHOW", acc="ONLY SHOWING")),
    ("What matters more to you than looking successful?", "scale", dict(left="LOOKING SUCCESSFUL", right="?", tip=1, acc="MATTERS MORE")),
    ("Tell us below.", "cta", dict(kind="comment", lbl="WHAT MATTERS MORE", acc="BELOW")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
