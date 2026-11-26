from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO KNOW YOU BEST", "MAY KNOW YOU LEAST")
OUTPUT = "36_The_People_Who_Know_You_Best_May_Know_You_Least_16x9.mp4"
SPEC = [
    ("Sometimes the people closest to you…", "ring", dict(acc="CLOSEST")),
    ("Only know the version of you that you've always shown them.", "frame", dict(who="THE VERSION THEY KNOW", acc="VERSION SHOWN")),
    ("They know your habits.", "list", dict(items=["YOUR HABITS"], mode="check", acc="HABITS.")),
    ("Your jokes.", "list", dict(items=["YOUR HABITS", "YOUR JOKES"], mode="check", acc="JOKES.")),
    ("Your routines.", "list", dict(items=["YOUR HABITS", "YOUR JOKES", "YOUR ROUTINES"], mode="check", acc="ROUTINES.")),
    ("Your old decisions.", "list", dict(items=["YOUR HABITS", "YOUR JOKES", "YOUR ROUTINES", "OLD DECISIONS"], mode="check", acc="OLD DECISIONS.")),
    ("But they may not know what you're thinking about becoming.", "iceberg", dict(top="WHAT THEY SEE", bottom="WHO YOU'RE BECOMING", acc="NOT BECOMING.")),
    ("And that's okay.", "big", dict(text="OKAY", acc="OKAY.")),
    ("You don't need everyone to understand every part of your growth.", "plant", dict(height=0.5, lbl="ROOTS THEY CAN'T SEE", acc="UNDERSTAND GROWTH.")),
    ("Some changes happen quietly…", "pulse", dict(acc="QUIETLY…")),
    ("Before the world has a chance to notice.", "chairs", dict(lbl="NOT NOTICED YET", acc="NOTICE.")),
    ("You can be growing into someone new…", "shed", dict(old="BEFORE", new="BECOMING", acc="GROWING NEW…")),
    ("Even while others still see the person you used to be.", "frame", dict(who="WHAT THEY SEE", new="WHO YOU ARE", acc="USED")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
