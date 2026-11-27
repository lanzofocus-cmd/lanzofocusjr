from kit import build, follow_sub

TITLE = ("YOUR LIFE CAN CHANGE", "WITHOUT A BIG MOMENT")
OUTPUT = "95_Your_Life_Can_Change_Without_A_Big_Moment_16x9.mp4"
SPEC = [
    ("You keep expecting change to feel dramatic.", "big", dict(text="DRAMATIC?", acc="DRAMATIC.")),
    ("A decision.", "list", dict(items=["A DECISION"], mode="empty", acc="DECISION.")),
    ("A breakthrough.", "list", dict(items=["A DECISION", "A BREAKTHROUGH"], mode="empty", acc="BREAKTHROUGH.")),
    ("A new beginning.", "list", dict(items=["A DECISION", "A BREAKTHROUGH", "A NEW BEGINNING"], mode="empty", acc="BEGINNING.")),
    ("A moment where everything suddenly makes sense.", "puzzle", dict(missing=False, lbl="IT ALL CLICKS?", acc="SUDDENLY SENSE.")),
    ("But most changes don't arrive like that.", "doc", dict(title="BIG MOMENT", empty=True, stamp="RARE", acc="DON'T ARRIVE")),
    ("They begin with a small decision…", "path", dict(kind="fork", labels=("SAME", "SLIGHTLY DIFFERENT"), acc="SMALL DECISION…")),
    ("Repeated.", "timeline", dict(n=10, progress=0.5, tag="AGAIN", acc="REPEATED.")),
    ("A different response.", "arrows", dict(items=["RESPONSE"], acc="DIFFERENT RESPONSE.")),
    ("A new habit.", "list", dict(items=["NEW HABIT"], mode="check", acc="HABIT.")),
    ("A conversation.", "bubbles", dict(texts=["CAN WE TALK?"], acc="CONVERSATION.")),
    ("A choice you make when nobody notices.", "chairs", dict(lbl="NOBODY NOTICED", acc="NOBODY NOTICES.")),
    ("Then another.", "stairs", dict(n=6, climb=1, acc="ANOTHER.")),
    ("Then another.", "stairs", dict(n=6, climb=3, acc="ANOTHER.")),
    ("And one day…", "sunrise", dict(acc="ONE DAY…")),
    ("You look back and realize your life is different.", "shed", dict(old="THEN", new="NOW", acc="LOOK DIFFERENT.")),
    ("You didn't notice the transformation because you were busy living through it.", "plant", dict(height=0.8, lbl="GREW QUIETLY", acc="TRANSFORMATION LIVING")),
    ("Don't underestimate the small beginnings that don't look important yet.", "plant", dict(height=0.1, lbl="SMALL BEGINNINGS", acc="UNDERESTIMATE SMALL BEGINNINGS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
