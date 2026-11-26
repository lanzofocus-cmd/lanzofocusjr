from kit import build, follow_sub

TITLE = ("THE MOST EXPENSIVE", "WORD IS “LATER”")
OUTPUT = "26_The_Most_Expensive_Word_Is_Later_16x9.mp4"
SPEC = [
    ("Later.", "big", dict(text="LATER", acc="LATER.")),
    ("It's a tiny word.", "big", dict(text="later", sub="5 LETTERS", acc="TINY")),
    ("But it can quietly become the reason entire years disappear.", "timeline", dict(n=10, progress=0.9, tag="YEARS GONE", acc="YEARS DISAPPEAR.")),
    ("Later, I'll learn.", "list", dict(items=["LEARN"], mode="tag", tag="LATER", acc="LEARN.")),
    ("Later, I'll apologize.", "list", dict(items=["LEARN", "APOLOGIZE"], mode="tag", tag="LATER", acc="APOLOGIZE.")),
    ("Later, I'll start.", "list", dict(items=["LEARN", "APOLOGIZE", "START"], mode="tag", tag="LATER", acc="START.")),
    ("Later, I'll take care of it.", "list", dict(items=["LEARN", "APOLOGIZE", "START", "TAKE CARE OF IT"], mode="tag", tag="LATER", acc="CARE")),
    ("And because later feels close…", "map", dict(a_lbl="NOW", b_lbl="LATER", acc="CLOSE…")),
    ("You don't notice how far away it keeps moving.", "timeline", dict(n=8, progress=0.3, tag="LATER →", acc="FAR MOVING.")),
    ("You don't need to do everything immediately.", "list", dict(items=["NOT EVERYTHING", "NOT ALL AT ONCE"], mode="empty", acc="EVERYTHING IMMEDIATELY.")),
    ("But some things deserve more than another postponement.", "price", dict(text="POSTPONED", sub="AGAIN?", acc="DESERVE POSTPONEMENT.")),
    ("If it matters to you…", "key", dict(lbl="IT MATTERS", acc="MATTERS")),
    ("Give it a place in your life today.", "list", dict(items=["TODAY"], mode="check", acc="TODAY.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
