from kit import build, follow_sub

TITLE = ("YOU DON'T KNOW", "WHAT YOU DON'T KNOW")
OUTPUT = "76_You_Dont_Know_What_You_Dont_Know_16x9.mp4"
SPEC = [
    ("One of the most dangerous things about being inexperienced…", "big", dict(text="DANGER", acc="DANGEROUS INEXPERIENCED…")),
    ("Is not knowing which questions to ask.", "question", dict(acc="QUESTIONS")),
    ("You can feel confident.", "gauge", dict(lbl="CONFIDENCE", start=0.6, end=0.9, acc="CONFIDENT.")),
    ("You can think you understand something.", "brain", dict(says="I GET IT.", acc="UNDERSTAND")),
    ("You can make decisions based on information you believe is complete.", "doc", dict(title="ALL THE INFO?", empty=False, acc="COMPLETE.")),
    ("And then…", "pulse", dict()),
    ("You discover an entire layer you never knew existed.", "iceberg", dict(top="WHAT YOU KNEW", bottom="AN ENTIRE LAYER", acc="ENTIRE LAYER")),
    ("That's why humility matters.", "book", dict(chapter="STILL LEARNING", acc="HUMILITY")),
    ("Not because you should doubt everything.", "bubbles", dict(texts=["NOT DOUBT"], acc="NOT DOUBT")),
    ("But because your current understanding is probably incomplete.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="INCOMPLETE.")),
    ("The world is larger than your experience.", "map", dict(a_lbl="YOUR EXPERIENCE", b_lbl="THE WORLD", acc="LARGER")),
    ("And that's not a reason to feel small.", "alone", dict(acc="NOT SMALL.")),
    ("It's a reason to stay curious.", "compass", dict(lbl="CURIOSITY", acc="CURIOUS.")),
    ("The moment you stop believing there's more to learn…", "book", dict(chapter="THE END?", acc="STOP MORE LEARN…")),
    ("Is the moment you stop giving yourself room to grow.", "plant", dict(height=0.3, lbl="ROOM TO GROW", acc="ROOM GROW.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
