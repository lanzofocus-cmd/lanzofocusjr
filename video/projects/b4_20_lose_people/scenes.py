from kit import build, follow_sub

TITLE = ("THE PEOPLE YOU LOSE", "AREN'T ALWAYS LOSSES")
OUTPUT = "110_The_People_You_Lose_Arent_Always_Losses_16x9.mp4"
SPEC = [
    ("Sometimes a relationship ends…", "crowd", dict(n=2, acc="ENDS…")),
    ("And it feels like you've lost something important.", "puzzle", dict(missing=True, lbl="SOMETHING MISSING", acc="LOST IMPORTANT.")),
    ("But with time…", "hourglass", dict(acc="TIME…")),
    ("You may realize that the relationship was teaching you something.", "book", dict(chapter="WHAT IT TAUGHT", acc="TEACHING")),
    ("About boundaries.", "list", dict(items=["BOUNDARIES"], mode="check", acc="BOUNDARIES.")),
    ("Communication.", "list", dict(items=["BOUNDARIES", "COMMUNICATION"], mode="check", acc="COMMUNICATION.")),
    ("Your values.", "list", dict(items=["BOUNDARIES", "COMMUNICATION", "YOUR VALUES"], mode="check", acc="VALUES.")),
    ("What you need.", "list", dict(items=["BOUNDARIES", "COMMUNICATION", "YOUR VALUES", "WHAT YOU NEED"], mode="check", acc="NEED.")),
    ("What you won't accept.", "list", dict(items=["BOUNDARIES", "COMMUNICATION", "YOUR VALUES", "WHAT YOU NEED", "WON'T ACCEPT"], mode="check", acc="WON'T ACCEPT.")),
    ("Not every ending is good.", "list", dict(items=["GOOD ENDING?"], mode="empty", acc="NOT GOOD.")),
    ("Not every ending is necessary.", "list", dict(items=["NECESSARY?"], mode="empty", acc="NOT NECESSARY.")),
    ("But an ending doesn't automatically mean your life became worse.", "chart", dict(kind="invest", lbl="AFTER", acc="DOESN'T WORSE.")),
    ("Sometimes…", "pulse", dict()),
    ("It creates space for something different.", "door", dict(open_=True, lbl="SPACE", acc="SPACE DIFFERENT.")),
    ("You can miss someone…", "frame", dict(who="SOMEONE YOU MISS", acc="MISS")),
    ("And still recognize that moving forward was the right decision.", "path", dict(kind="straight", acc="FORWARD RIGHT DECISION.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
