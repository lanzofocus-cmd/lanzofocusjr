from kit import build, follow_sub

TITLE = ("THE FALSE", "FINISH LINE")
OUTPUT = "181_The_False_Finish_Line_16x9.mp4"
SPEC = [
    ("Sometimes you reach a goal…", "stairs", dict(n=6, climb=6, acc="REACH GOAL")),
    ("And immediately create another one.", "stairs", dict(n=9, climb=6, highlight=8, acc="IMMEDIATELY ANOTHER")),
    ("No celebration.", "stage", dict(lbl="NO CELEBRATION", empty=True, acc="CELEBRATION")),
    ("No reflection.", "mirror", dict(reflect="dashed", acc="REFLECTION")),
    ("Just the next target.", "arrows", dict(items=["NEXT", "NEXT", "NEXT"], acc="NEXT TARGET")),
    ("Ambition is useful.", "compass", dict(lbl="AMBITION", acc="AMBITION USEFUL")),
    ("But if every achievement becomes instantly meaningless…", "list", dict(items=["GOAL 1", "GOAL 2", "GOAL 3"], mode="strike", acc="ACHIEVEMENT MEANINGLESS")),
    ("You may never experience the satisfaction of actually arriving anywhere.", "map", dict(a_lbl="START", b_lbl="ARRIVED?", acc="SATISFACTION ARRIVING")),
    ("Learn to move forward without refusing to appreciate where you've already been.", "timeline", dict(n=8, progress=0.6, tag="LOOK HOW FAR", acc="FORWARD APPRECIATE BEEN")),
    ("Save this for your next achievement.", "cta", dict(kind="save", lbl="FOR YOUR NEXT WIN", acc="SAVE ACHIEVEMENT")),
    ("Take a moment to actually recognize it.", "crown", dict(lbl="YOU DID IT", acc="RECOGNIZE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
