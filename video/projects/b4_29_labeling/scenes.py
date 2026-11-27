from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH LABELING", "PEOPLE TOO QUICKLY")
OUTPUT = "119_The_Problem_With_Labeling_People_Too_Quickly_16x9.mp4"
SPEC = [
    ("You meet someone.", "crowd", dict(n=2, acc="MEET")),
    ("They make one mistake.", "list", dict(items=["ONE MISTAKE"], mode="strike", acc="ONE MISTAKE.")),
    ("They say something awkward.", "quote", dict(text="UM... SO... YEAH.", acc="AWKWARD.")),
    ("They disappoint you.", "chart", dict(kind="down", lbl="FIRST IMPRESSION", acc="DISAPPOINT")),
    ("And immediately…", "pulse", dict()),
    ("You decide who they are.", "sticker", dict(tags=["RUDE", "WEIRD"], acc="DECIDE WHO")),
    ("But people are more complicated than a single moment.", "iceberg", dict(top="ONE MOMENT", bottom="THE WHOLE PERSON", acc="COMPLICATED SINGLE")),
    ("A mistake can reveal something.", "dots", dict(connect=False, n=3, acc="REVEAL")),
    ("A pattern can reveal something more.", "dots", dict(connect=True, acc="PATTERN MORE.")),
    ("But one moment isn't always the complete picture.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="ISN'T COMPLETE PICTURE.")),
    ("Give people enough time to show you who they are.", "hourglass", dict(acc="TIME SHOW")),
    ("And pay attention to patterns rather than isolated performances.", "timeline", dict(n=10, progress=0.8, tag="THE PATTERN", acc="PATTERNS ISOLATED")),
    ("Don't judge someone entirely by their best moment.", "stage", dict(lbl="BEST MOMENT", acc="BEST")),
    ("Or entirely by their worst.", "chart", dict(kind="down", lbl="WORST MOMENT", acc="WORST.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
