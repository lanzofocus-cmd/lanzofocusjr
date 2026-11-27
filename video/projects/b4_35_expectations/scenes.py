from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN YOUR", "EXPECTATIONS AND REALITY")
OUTPUT = "125_Expectations_Vs_Reality_16x9.mp4"
SPEC = [
    ("You expected something to happen.", "frame", dict(who="THE EXPECTATION", acc="EXPECTED")),
    ("You imagined how it would feel.", "brain", dict(says="IT'LL BE AMAZING.", acc="IMAGINED FEEL.")),
    ("How people would respond.", "bubbles", dict(texts=["WOW!", "AMAZING!"], inverted=True, acc="RESPOND.")),
    ("What your life would look like afterward.", "sunrise", dict(acc="AFTERWARD.")),
    ("Then reality arrived…", "door", dict(open_=True, lbl="REALITY", acc="REALITY ARRIVED…")),
    ("And it was different.", "frame", dict(who="THE EXPECTATION", new="REALITY", acc="DIFFERENT.")),
    ("Maybe disappointing.", "chart", dict(kind="down", lbl="DISAPPOINTING", acc="DISAPPOINTING.")),
    ("Maybe more complicated.", "tangle", dict(lbl="COMPLICATED", acc="COMPLICATED.")),
    ("Maybe not as exciting as you expected.", "gauge", dict(lbl="EXCITEMENT", start=0.9, end=0.4, acc="NOT EXCITING")),
    ("But expectations can create a problem.", "big", dict(text="THE PROBLEM", acc="EXPECTATIONS PROBLEM.")),
    ("They make you compare reality…", "scale", dict(left="REALITY", right="IMAGINED", tip=1, acc="COMPARE REALITY…")),
    ("To something that never actually existed.", "frame", dict(who="NEVER EXISTED", dashed_fig=True, fade=True, acc="NEVER EXISTED.")),
    ("Your imagination isn't a promise.", "doc", dict(title="PROMISE", empty=True, stamp="NOT A PROMISE", acc="IMAGINATION ISN'T PROMISE.")),
    ("Learn to appreciate reality without constantly measuring it against the version you imagined.", "mirror", dict(reflect="solid", lbl="REAL LIFE", acc="APPRECIATE REALITY MEASURING IMAGINED.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
