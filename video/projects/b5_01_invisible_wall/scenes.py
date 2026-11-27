from kit import build, follow_sub

TITLE = ("THE INVISIBLE", "WALL")
OUTPUT = "141_The_Invisible_Wall_16x9.mp4"
SPEC = [
    ("Sometimes the thing stopping you isn't a lack of opportunity.", "door", dict(open_=True, lbl="OPPORTUNITY", acc="STOPPING OPPORTUNITY")),
    ("It's a wall you've built so long ago that you forgot it was even there.", "bricks", dict(rows=5, lbl="BUILT LONG AGO", uneven=False, acc="WALL FORGOT")),
    ("\"I can't.\"", "quote", dict(text="I CAN'T.", acc="CAN'T")),
    ("\"I'm not that type of person.\"", "quote", dict(text="I'M NOT THAT TYPE OF PERSON.", acc="NOT TYPE")),
    ("\"People like me don't do that.\"", "quote", dict(text="PEOPLE LIKE ME DON'T DO THAT.", acc="DON'T")),
    ("But those aren't facts.", "doc", dict(title="FACTS", empty=True, stamp="NOT FACTS", acc="AREN'T FACTS")),
    ("They're conclusions you made before you had enough evidence.", "scale", dict(left="CONCLUSION", right="EVIDENCE", tip=-1, acc="CONCLUSIONS EVIDENCE")),
    ("And the dangerous thing about a belief is that it can become a prison without ever looking like one.", "cage", dict(words=["I CAN'T", "NOT ME", "PEOPLE LIKE ME"], acc="BELIEF PRISON")),
    ("Question the walls you've never tried to climb.", "stairs", dict(n=6, climb=4, acc="QUESTION CLIMB")),
    ("What's one belief about yourself you're starting to question?", "cta", dict(kind="comment", lbl="ONE BELIEF YOU'RE QUESTIONING", acc="BELIEF QUESTION")),
    ("Write it down. Someone else might need to see that they're not alone.", "crowd", dict(n=7, highlight=3, highlight_label="NOT ALONE", acc="WRITE ALONE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
