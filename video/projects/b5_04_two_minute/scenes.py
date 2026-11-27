from kit import build, follow_sub

TITLE = ("THE TWO-MINUTE", "DECISION")
OUTPUT = "144_The_Two_Minute_Decision_16x9.mp4"
SPEC = [
    ("Your life doesn't always change through huge decisions.", "path", dict(kind="fork", labels=("HUGE", "SMALL"), acc="HUGE DECISIONS")),
    ("Sometimes it changes through two minutes.", "big", dict(text="2:00", sub="MINUTES", acc="TWO MINUTES")),
    ("Two minutes of starting.", "list", dict(items=["START"], mode="check", acc="STARTING")),
    ("Two minutes of opening the book.", "book", dict(chapter="PAGE 1", acc="BOOK")),
    ("Two minutes of putting your phone away.", "phone", dict(lbl="PUT IT AWAY", acc="PHONE AWAY")),
    ("Two minutes of finally doing the thing.", "list", dict(items=["START", "OPEN THE BOOK", "PHONE AWAY", "DO THE THING"], mode="check", acc="FINALLY THING")),
    ("The hardest part isn't always the work.", "bricks", dict(rows=3, lbl="THE WORK", uneven=False, acc="HARDEST WORK")),
    ("Sometimes it's crossing the distance between thinking and beginning.", "map", dict(a_lbl="THINKING", b_lbl="BEGINNING", acc="DISTANCE THINKING BEGINNING")),
    ("Don't tell me your huge goal.", "list", dict(items=["HUGE GOAL"], mode="strike", acc="HUGE GOAL")),
    ("Tell me the two-minute action you can start today.", "cta", dict(kind="comment", lbl="YOUR 2-MINUTE ACTION", acc="TWO-MINUTE TODAY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
