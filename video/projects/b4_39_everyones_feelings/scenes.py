from kit import build, follow_sub

TITLE = ("YOU'RE NOT RESPONSIBLE FOR", "EVERYONE'S FEELINGS")
OUTPUT = "129_Youre_Not_Responsible_For_Everyones_Feelings_16x9.mp4"
SPEC = [
    ("You care about people.", "ring", dict(center_tag="CARING", acc="CARE")),
    ("You want them to be happy.", "bubbles", dict(texts=["ARE YOU OKAY?", "CAN I HELP?"], inverted=True, acc="HAPPY.")),
    ("You don't want to disappoint anyone.", "crowd", dict(n=7, acc="DISAPPOINT")),
    ("But eventually…", "pulse", dict()),
    ("You may begin believing that every negative emotion someone experiences…", "ring", dict(tags=["SAD", "UPSET", "ANNOYED", "HURT"], acc="EVERY NEGATIVE")),
    ("Is your responsibility to fix.", "sticker", dict(tags=["FIX IT ALL"], acc="RESPONSIBILITY FIX.")),
    ("You feel guilty for saying no.", "quote", dict(text="NO... SORRY.", acc="GUILTY NO.")),
    ("Guilty for choosing differently.", "path", dict(kind="fork", labels=("THEIRS", "YOURS"), acc="GUILTY DIFFERENTLY.")),
    ("Guilty for having boundaries.", "shield", dict(front="BOUNDARY", back="GUILT?", acc="GUILTY BOUNDARIES.")),
    ("But you can care about someone's feelings…", "key", dict(lbl="CARE", acc="CARE FEELINGS…")),
    ("Without being responsible for controlling them.", "lock", dict(lbl="NOT YOURS TO CONTROL", acc="WITHOUT CONTROLLING")),
    ("Kindness doesn't require you to abandon your own needs.", "scale", dict(left="KINDNESS", right="YOUR NEEDS", tip=0, acc="KINDNESS DOESN'T ABANDON NEEDS.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
