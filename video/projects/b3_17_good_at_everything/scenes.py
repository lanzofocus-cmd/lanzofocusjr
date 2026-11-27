from kit import build, follow_sub

TITLE = ("YOU'RE NOT SUPPOSED TO BE", "GOOD AT EVERYTHING")
OUTPUT = "57_Youre_Not_Supposed_To_Be_Good_At_Everything_16x9.mp4"
SPEC = [
    ("Somewhere along the way…", "path", dict(kind="winding", acc="SOMEWHERE")),
    ("You started believing that being capable means being good at everything.", "list", dict(items=["GOOD AT THIS", "GOOD AT THAT", "GOOD AT EVERYTHING"], mode="check", acc="CAPABLE EVERYTHING.")),
    ("So when you struggle…", "chart", dict(kind="down", lbl="STRUGGLING", acc="STRUGGLE…")),
    ("You feel embarrassed.", "stage", dict(lbl="EMBARRASSED", performing=False, acc="EMBARRASSED.")),
    ("When someone knows more…", "crowd", dict(n=5, highlight=1, highlight_label="KNOWS MORE", acc="MORE…")),
    ("You feel inferior.", "scale", dict(left="YOU", right="THEM", tip=1, acc="INFERIOR.")),
    ("When you make a mistake…", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKE…")),
    ("You feel exposed.", "stage", dict(lbl="EXPOSED", acc="EXPOSED.")),
    ("But nobody is supposed to master everything.", "big", dict(text="NOBODY", sub="MASTERS EVERYTHING", acc="NOBODY EVERYTHING.")),
    ("You are allowed to have weaknesses.", "list", dict(items=["WEAKNESSES"], mode="check", acc="WEAKNESSES.")),
    ("You're allowed to ask questions.", "list", dict(items=["WEAKNESSES", "QUESTIONS"], mode="check", acc="QUESTIONS.")),
    ("You're allowed to need help.", "list", dict(items=["WEAKNESSES", "QUESTIONS", "HELP"], mode="check", acc="HELP.")),
    ("And you're allowed to be the least experienced person in the room.", "crowd", dict(n=7, highlight=3, highlight_label="NEWEST", acc="LEAST EXPERIENCED")),
    ("The goal isn't to never look inexperienced.", "mirror", dict(reflect="dashed", lbl="LOOKING GOOD", acc="ISN'T INEXPERIENCED.")),
    ("The goal is to keep learning.", "chart", dict(kind="up", lbl="LEARNING", acc="KEEP LEARNING.")),
    ("Your ego wants to look capable.", "mirror", dict(reflect="dashed", lbl="LOOK CAPABLE", acc="EGO LOOK")),
    ("Your growth requires you to become capable.", "stairs", dict(n=6, climb=4, acc="GROWTH BECOME")),
    ("Which one are you choosing?", "question", dict(a_lbl="LOOK", b_lbl="BECOME", acc="CHOOSING?")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
