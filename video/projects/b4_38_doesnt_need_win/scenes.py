from kit import build, follow_sub

TITLE = ("THE PERSON WHO", "DOESN'T NEED TO WIN")
OUTPUT = "128_The_Person_Who_Doesnt_Need_To_Win_16x9.mp4"
SPEC = [
    ("Imagine entering every conversation…", "bubbles", dict(texts=["HI.", "HEY."], acc="IMAGINE CONVERSATION…")),
    ("Without needing to prove you're smarter.", "list", dict(items=["PROVE I'M SMARTER"], mode="strike", acc="WITHOUT SMARTER.")),
    ("Imagine hearing criticism…", "quote", dict(text="THAT COULD BE BETTER.", acc="CRITICISM…")),
    ("Without immediately defending yourself.", "shield", dict(front="NO DEFENSE NEEDED", back="", acc="WITHOUT DEFENDING")),
    ("Imagine someone succeeding…", "crowd", dict(n=5, highlight=2, highlight_label="SUCCEEDED", acc="SUCCEEDING…")),
    ("Without feeling threatened.", "gauge", dict(lbl="THREATENED", start=0.6, end=0.05, acc="WITHOUT THREATENED.")),
    ("Imagine admitting you're wrong…", "quote", dict(text="I WAS WRONG.", acc="ADMITTING WRONG…")),
    ("Without feeling smaller.", "alone", dict(tag="STILL WHOLE", acc="WITHOUT SMALLER.")),
    ("That's a different kind of confidence.", "gauge", dict(lbl="CONFIDENCE", start=0.4, end=0.9, acc="DIFFERENT CONFIDENCE.")),
    ("Not the confidence that comes from being superior.", "crown", dict(lbl="SUPERIOR?", acc="NOT SUPERIOR.")),
    ("The confidence that comes from not needing superiority.", "key", dict(lbl="SECURE", acc="NOT NEEDING SUPERIORITY.")),
    ("You don't have to win every comparison…", "scale", dict(left="YOU", right="THEM", tip=0, acc="WIN COMPARISON…")),
    ("To feel secure in who you are.", "mirror", dict(reflect="solid", lbl="SECURE", acc="SECURE WHO")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
