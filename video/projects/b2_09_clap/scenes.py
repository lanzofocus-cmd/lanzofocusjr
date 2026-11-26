from kit import build, follow_sub

TITLE = ("NOT EVERYONE WILL", "CLAP FOR YOU")
OUTPUT = "19_Not_Everyone_Will_Clap_For_You_16x9.mp4"
SPEC = [
    ("Some people will support you.", "bubbles", dict(texts=["PROUD OF YOU!", "GO FOR IT!"], inverted=True, acc="SUPPORT")),
    ("Some people won't understand you.", "bubbles", dict(texts=["BUT WHY?", "I DON'T GET IT."], acc="WON'T UNDERSTAND")),
    ("And some people will only become interested after you've succeeded.", "chart", dict(kind="up", lbl="INTEREST IN YOU", lbl2="AFTER SUCCESS", acc="ONLY AFTER SUCCEEDED.")),
    ("Don't let the absence of applause convince you that what you're doing has no value.", "chairs", dict(lbl="NO APPLAUSE", acc="ABSENCE APPLAUSE VALUE.")),
    ("Not every worthwhile journey has an audience.", "path", dict(kind="winding", acc="AUDIENCE.")),
    ("Not every important step gets recognition.", "stairs", dict(n=6, climb=2, acc="RECOGNITION.")),
    ("And not every person needs to know what you're building.", "bricks", dict(rows=4, lbl="QUIETLY BUILDING", uneven=False, acc="BUILDING.")),
    ("Your progress doesn't become real when someone notices it.", "progress", dict(lbl="YOUR PROGRESS", value=0.6, acc="REAL NOTICES")),
    ("It was real before they looked.", "plant", dict(height=0.7, lbl="ALREADY GROWING", acc="REAL BEFORE")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
