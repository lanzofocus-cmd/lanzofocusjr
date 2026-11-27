from kit import build, follow_sub

TITLE = ("THE BORING", "MIDDLE")
OUTPUT = "152_The_Boring_Middle_16x9.mp4"
SPEC = [
    ("Everyone loves the beginning.", "startline", dict(behind=False, acc="BEGINNING")),
    ("The excitement.", "list", dict(items=["EXCITEMENT"], mode="check", acc="EXCITEMENT")),
    ("The new plan.", "list", dict(items=["EXCITEMENT", "NEW PLAN"], mode="check", acc="PLAN")),
    ("The fresh energy.", "list", dict(items=["EXCITEMENT", "NEW PLAN", "FRESH ENERGY"], mode="check", acc="ENERGY")),
    ("Everyone loves the ending.", "stairs", dict(n=6, climb=6, acc="ENDING")),
    ("The achievement.", "list", dict(items=["ACHIEVEMENT"], mode="check", acc="ACHIEVEMENT")),
    ("The result.", "list", dict(items=["ACHIEVEMENT", "RESULT"], mode="check", acc="RESULT")),
    ("The celebration.", "stage", dict(lbl="CELEBRATION", acc="CELEBRATION")),
    ("But most progress happens in the middle.", "timeline", dict(n=10, progress=0.5, tag="THE MIDDLE", acc="PROGRESS MIDDLE")),
    ("The part with no announcement.", "chairs", dict(n=5, lbl="NOBODY ANNOUNCES IT", acc="NO ANNOUNCEMENT")),
    ("No applause.", "stage", dict(lbl="NO APPLAUSE", empty=True, acc="APPLAUSE")),
    ("No dramatic transformation.", "mirror", dict(reflect="solid", lbl="SAME AS YESTERDAY", acc="DRAMATIC TRANSFORMATION")),
    ("Just ordinary days doing ordinary things.", "bricks", dict(rows=4, lbl="ONE DAY AT A TIME", uneven=False, acc="ORDINARY")),
    ("That's where the real story is written.", "book", dict(chapter="THE MIDDLE", text="THE REAL STORY", acc="REAL STORY WRITTEN")),
    ("Save this for the middle of whatever you're currently working toward.", "cta", dict(kind="save", lbl="FOR THE MIDDLE", acc="SAVE MIDDLE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
