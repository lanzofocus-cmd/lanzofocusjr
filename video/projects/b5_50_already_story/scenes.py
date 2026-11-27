from kit import build, follow_sub

TITLE = ("YOU ARE ALREADY", "IN THE STORY")
OUTPUT = "190_You_Are_Already_In_The_Story_16x9.mp4"
SPEC = [
    ("You keep imagining the moment your real life begins.", "startline", dict(behind=False, acc="REAL LIFE BEGINS")),
    ("After the achievement.", "list", dict(items=["AFTER THE ACHIEVEMENT"], mode="empty", acc="ACHIEVEMENT")),
    ("After the transformation.", "list", dict(items=["AFTER THE ACHIEVEMENT", "AFTER THE TRANSFORMATION"], mode="empty", acc="TRANSFORMATION")),
    ("After the big opportunity.", "list", dict(items=["AFTER THE ACHIEVEMENT", "AFTER THE TRANSFORMATION", "AFTER THE OPPORTUNITY"], mode="empty", acc="OPPORTUNITY")),
    ("After everything finally makes sense.", "puzzle", dict(missing=True, lbl="MAKES SENSE?", acc="SENSE")),
    ("But this isn't a waiting room.", "chairs", dict(n=6, lbl="WAITING ROOM", acc="WAITING ROOM")),
    ("This is the story.", "book", dict(chapter="THIS", text="THE STORY", acc="STORY")),
    ("The awkward beginnings.", "frame", dict(who="AWKWARD BEGINNINGS", acc="AWKWARD BEGINNINGS")),
    ("The unexpected problems.", "chart", dict(kind="wave", lbl="THE PLOT", acc="UNEXPECTED PROBLEMS")),
    ("The ordinary days.", "big", dict(text="TUESDAY", sub="STILL PART OF IT", acc="ORDINARY")),
    ("The decisions nobody sees.", "iceberg", dict(top="WHAT THEY SEE", bottom="YOUR DECISIONS", acc="DECISIONS NOBODY")),
    ("You're not waiting to enter your life.", "door", dict(open_=True, lbl="ALREADY INSIDE", acc="WAITING ENTER")),
    ("You're already living it.", "pulse", dict(acc="ALREADY LIVING")),
    ("If this made you think differently about your life, share it with someone who keeps waiting for the \"real beginning.\"", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE REAL BEGINNING")),
    ("And follow LanzoFocus for perspectives that make you question, reflect, and see your life differently.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
