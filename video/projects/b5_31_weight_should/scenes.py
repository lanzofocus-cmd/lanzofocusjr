from kit import build, follow_sub

TITLE = ("THE WEIGHT", "OF \"SHOULD\"")
OUTPUT = "171_The_Weight_Of_Should_16x9.mp4"
SPEC = [
    ("Your life can become heavy when every decision begins with \"should.\"", "gauge", dict(lbl="WEIGHT", start=0.2, end=0.85, acc="HEAVY SHOULD")),
    ("I should be further ahead.", "sticker", dict(tags=["FURTHER AHEAD"], acc="SHOULD AHEAD")),
    ("I should be doing more.", "sticker", dict(tags=["FURTHER AHEAD", "DOING MORE"], acc="SHOULD MORE")),
    ("I should be like them.", "sticker", dict(tags=["FURTHER AHEAD", "DOING MORE", "LIKE THEM"], acc="SHOULD THEM")),
    ("I should already know.", "sticker", dict(tags=["FURTHER AHEAD", "DOING MORE", "LIKE THEM", "ALREADY KNOW"], acc="SHOULD KNOW")),
    ("But whose expectations are you carrying?", "question", dict(a_lbl="WHOSE", b_lbl="EXPECTATIONS?", acc="WHOSE CARRYING")),
    ("Some responsibilities are real.", "list", dict(items=["REAL"], mode="check", acc="REAL")),
    ("Some are expectations you've inherited without questioning.", "sticker", dict(tags=["FURTHER AHEAD", "DOING MORE", "LIKE THEM", "ALREADY KNOW"], strike=True, acc="INHERITED QUESTIONING")),
    ("Learn the difference.", "scale", dict(left="REAL", right="INHERITED", tip=0, acc="DIFFERENCE")),
    ("Comment one expectation you've decided to question.", "cta", dict(kind="comment", lbl="ONE \"SHOULD\" YOU'RE DROPPING", acc="EXPECTATION QUESTION")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
