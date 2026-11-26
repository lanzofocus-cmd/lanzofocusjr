from kit import build, follow_sub

TITLE = ("THE WORLD IS BIGGER THAN", "YOUR CURRENT PROBLEM")
OUTPUT = "30_The_World_Is_Bigger_Than_Your_Current_Problem_16x9.mp4"
SPEC = [
    ("Right now…", "pulse", dict()),
    ("Your problem may feel like the entire world.", "big", dict(text="THE PROBLEM", sub="FEELS LIKE EVERYTHING", acc="ENTIRE WORLD.")),
    ("The disappointment.", "chart", dict(kind="down", lbl="DISAPPOINTMENT", acc="DISAPPOINTMENT.")),
    ("The embarrassment.", "stage", dict(lbl="EMBARRASSED", performing=False, acc="EMBARRASSMENT.")),
    ("The uncertainty.", "fog", dict(lbl="UNCERTAIN", acc="UNCERTAINTY.")),
    ("The thing that didn't go according to plan.", "doc", dict(title="THE PLAN", empty=False, stamp="DIDN'T WORK", acc="DIDN'T PLAN.")),
    ("But there is a world beyond this moment.", "sunrise", dict(acc="WORLD BEYOND")),
    ("People you haven't met.", "crowd", dict(n=9, acc="PEOPLE MET.")),
    ("Places you haven't seen.", "map", dict(a_lbl="HERE", b_lbl="SOMEWHERE NEW", acc="PLACES SEEN.")),
    ("Skills you haven't learned.", "list", dict(items=["NEW SKILL", "NEW SKILL", "NEW SKILL"], mode="empty", acc="SKILLS LEARNED.")),
    ("Experiences you haven't had.", "door", dict(open_=True, lbl="NOT YET LIVED", acc="EXPERIENCES HAD.")),
    ("Your current situation is real.", "big", dict(text="REAL", acc="REAL.")),
    ("But it isn't the entire story.", "book", dict(chapter="ONE CHAPTER", acc="ISN'T ENTIRE STORY.")),
    ("Don't let one difficult chapter convince you…", "book", dict(chapter="A HARD CHAPTER", acc="DIFFICULT CHAPTER")),
    ("That the whole book is finished.", "book", dict(chapter="TO BE CONTINUED", text="NOT FINISHED", acc="WHOLE FINISHED.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
