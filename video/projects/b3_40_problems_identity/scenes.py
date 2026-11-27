from kit import build, follow_sub

TITLE = ("YOUR PROBLEMS ARE NOT", "YOUR ENTIRE IDENTITY")
OUTPUT = "80_Your_Problems_Are_Not_Your_Entire_Identity_16x9.mp4"
SPEC = [
    ("When something difficult happens…", "chart", dict(kind="down", lbl="SOMETHING HARD", acc="DIFFICULT")),
    ("It can take over your thoughts.", "bubbles", dict(texts=["THE PROBLEM", "THE PROBLEM", "THE PROBLEM"], center="brain", acc="TAKE OVER")),
    ("You begin thinking about it constantly.", "brain", dict(says="THE PROBLEM...", acc="CONSTANTLY.")),
    ("Talking about it.", "quote", dict(text="SO, THE PROBLEM...", acc="TALKING")),
    ("Planning around it.", "network", dict(nodes=["PROBLEM", "PROBLEM", "PROBLEM", "PROBLEM"], tangled=True, acc="PLANNING")),
    ("And eventually…", "pulse", dict()),
    ("It becomes the lens through which you see everything.", "compass", dict(lbl="THE PROBLEM", settle=False, acc="LENS EVERYTHING.")),
    ("But you are more than the problem you're currently solving.", "iceberg", dict(top="THE PROBLEM", bottom="ALL OF YOU", acc="MORE PROBLEM")),
    ("You still have interests.", "list", dict(items=["INTERESTS"], mode="check", acc="INTERESTS.")),
    ("Relationships.", "list", dict(items=["INTERESTS", "RELATIONSHIPS"], mode="check", acc="RELATIONSHIPS.")),
    ("Curiosity.", "list", dict(items=["INTERESTS", "RELATIONSHIPS", "CURIOSITY"], mode="check", acc="CURIOSITY.")),
    ("Potential.", "list", dict(items=["INTERESTS", "RELATIONSHIPS", "CURIOSITY", "POTENTIAL"], mode="check", acc="POTENTIAL.")),
    ("Experiences waiting for you.", "door", dict(open_=True, lbl="WAITING FOR YOU", acc="EXPERIENCES WAITING")),
    ("Your problem deserves attention.", "key", dict(lbl="ATTENTION", acc="DESERVES ATTENTION.")),
    ("But it doesn't deserve your entire identity.", "sticker", dict(tags=["THE PROBLEM"], strike=True, acc="DOESN'T ENTIRE IDENTITY.")),
    ("Don't let one difficult part of your life convince you that it is your entire life.", "puzzle", dict(missing=False, lbl="ONE PIECE, NOT THE WHOLE", acc="ONE PART ENTIRE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
