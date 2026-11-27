from kit import build, follow_sub

TITLE = ("THE THINGS THAT MAKE", "YOU FEEL ALIVE")
OUTPUT = "127_The_Things_That_Make_You_Feel_Alive_16x9.mp4"
SPEC = [
    ("When was the last time you did something…", "question", dict(acc="LAST")),
    ("Simply because it made you feel alive?", "sunrise", dict(acc="ALIVE?")),
    ("Not because it was productive.", "list", dict(items=["PRODUCTIVE"], mode="strike", acc="NOT PRODUCTIVE.")),
    ("Not because it earned recognition.", "list", dict(items=["PRODUCTIVE", "RECOGNITION"], mode="strike", acc="RECOGNITION.")),
    ("Not because it improved your future.", "list", dict(items=["PRODUCTIVE", "RECOGNITION", "YOUR FUTURE"], mode="strike", acc="FUTURE.")),
    ("But because you genuinely enjoyed it.", "gauge", dict(lbl="JOY", start=0.2, end=0.95, acc="GENUINELY ENJOYED")),
    ("Maybe it was playing a sport.", "list", dict(items=["A SPORT"], mode="check", acc="SPORT.")),
    ("Creating something.", "list", dict(items=["A SPORT", "CREATING"], mode="check", acc="CREATING")),
    ("Exploring.", "list", dict(items=["A SPORT", "CREATING", "EXPLORING"], mode="check", acc="EXPLORING.")),
    ("Learning.", "list", dict(items=["A SPORT", "CREATING", "EXPLORING", "LEARNING"], mode="check", acc="LEARNING.")),
    ("Talking with someone.", "bubbles", dict(texts=["TELL ME EVERYTHING."], inverted=True, acc="TALKING")),
    ("Laughing.", "bubbles", dict(texts=["HAHAHA", "HAHA"], inverted=True, acc="LAUGHING.")),
    ("Sometimes…", "pulse", dict()),
    ("You become so focused on building your future…", "bricks", dict(rows=4, lbl="THE FUTURE", uneven=False, acc="FOCUSED FUTURE…")),
    ("That you forget your present is worth experiencing.", "pulse", dict(acc="FORGET PRESENT WORTH")),
    ("Don't make your entire life preparation for a life you're not enjoying.", "doc", dict(title="PREPARATION", empty=False, stamp="ENJOY NOW", acc="ENTIRE PREPARATION ENJOYING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
