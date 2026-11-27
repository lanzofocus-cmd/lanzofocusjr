from kit import build, follow_sub

TITLE = ("THE PERSON YOU ARE WHEN", "NOBODY NEEDS ANYTHING")
OUTPUT = "66_The_Person_You_Are_When_Nobody_Needs_Anything_16x9.mp4"
SPEC = [
    ("Pay attention to who you are…", "mirror", dict(reflect="solid", acc="WHO")),
    ("When nobody is asking you to perform.", "stage", dict(empty=True, performing=False, acc="NOBODY PERFORM.")),
    ("When nobody needs your help.", "crowd", dict(n=5, dim=True, acc="NOBODY HELP.")),
    ("When nobody is watching.", "chairs", dict(lbl="NOBODY WATCHING", acc="NOBODY WATCHING.")),
    ("When there's no reward.", "receipt", dict(items=[("REWARD", "$0")], acc="NO REWARD.")),
    ("No audience.", "chairs", dict(lbl="EMPTY", acc="NO AUDIENCE.")),
    ("No pressure.", "gauge", dict(lbl="PRESSURE", start=0.6, end=0.02, acc="NO PRESSURE.")),
    ("What do you choose to do?", "path", dict(kind="fork", labels=("?", "?"), acc="CHOOSE")),
    ("What interests you?", "question", dict(acc="INTERESTS")),
    ("What do you think about?", "brain", dict(says="...", acc="THINK")),
    ("What do you care about?", "key", dict(lbl="WHAT MATTERS", acc="CARE")),
    ("Because sometimes…", "pulse", dict()),
    ("We're so busy responding to the expectations around us…", "ring", dict(tags=["BE THIS", "DO THAT", "HELP ME", "BE MORE"], acc="EXPECTATIONS")),
    ("That we forget to discover what exists underneath them.", "iceberg", dict(top="THE ROLES", bottom="WHO YOU ARE", acc="DISCOVER UNDERNEATH")),
    ("You should know yourself outside of your roles.", "sticker", dict(tags=["EMPLOYEE", "FRIEND", "CHILD"], strike=True, acc="OUTSIDE ROLES.")),
    ("Not just who you are to other people…", "ring", dict(acc="OTHER PEOPLE…")),
    ("But who you are when you're simply yourself.", "alone", dict(tag="SIMPLY YOU", acc="SIMPLY YOURSELF.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
