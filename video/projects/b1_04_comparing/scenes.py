from kit import build, follow_sub

TITLE = ("YOU'RE COMPARING", "THE WRONG THINGS")
OUTPUT = "04_Youre_Comparing_The_Wrong_Things_16x9.mp4"
SPEC = [
    ("You're comparing your entire life…", "timeline", dict(n=9, progress=0.4, tag="YOUR LIFE", acc="ENTIRE")),
    ("To someone else's highlight reel.", "phone", dict(content="highlight", lbl="YOU", acc="HIGHLIGHT REEL.")),
    ("You see their achievements.", "phone", dict(content="highlight", acc="ACHIEVEMENTS.")),
    ("Their confidence.", "gauge", dict(lbl="THEIR CONFIDENCE", start=0.8, end=0.9, acc="CONFIDENCE.")),
    ("Their success.", "big", dict(text="SUCCESS", acc="SUCCESS.")),
    ("But you don't see the years behind it.", "iceberg", dict(top="WHAT YOU SEE", bottom="THE YEARS BEHIND IT", acc="YEARS")),
    ("The failures.", "list", dict(items=["FAILED", "FAILED", "FAILED"], mode="strike", acc="FAILURES.")),
    ("The doubts.", "bubbles", dict(texts=["WHAT IF I'M WRONG?", "SHOULD I QUIT?"], acc="DOUBTS.")),
    ("The sacrifices.", "receipt", dict(items=[("WEEKENDS", "GONE"), ("SLEEP", "LESS"), ("COMFORT", "GONE")], acc="SACRIFICES.")),
    ("And even if you did…", "pulse", dict()),
    ("Their journey still wouldn't be yours.", "path", dict(kind="fork", labels=("THEIR PATH", "YOUR PATH"), acc="YOURS.")),
    ("You were never supposed to have the same timeline.", "timeline", dict(compare=True, acc="SAME TIMELINE.")),
    ("The same opportunities.", "door", dict(lbl="DIFFERENT DOORS", acc="OPPORTUNITIES.")),
    ("The same story.", "book", dict(chapter="YOUR STORY", acc="STORY.")),
    ("Comparison doesn't show you where you should be.", "map", dict(a_lbl="WHERE YOU ARE", b_lbl="WHERE THEY ARE", acc="COMPARISON")),
    ("It distracts you from where you are.", "alone", dict(tag="YOU ARE HERE", acc="DISTRACTS")),
    ("And you can't build your own life…", "bricks", dict(rows=3, lbl="YOUR LIFE", uneven=False, acc="BUILD")),
    ("While constantly measuring it against someone else's.", "timeline", dict(compare=True, acc="MEASURING")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
