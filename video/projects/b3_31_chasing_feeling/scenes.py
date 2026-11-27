from kit import build, follow_sub

TITLE = ("YOU'RE CHASING A FEELING,", "NOT A GOAL")
OUTPUT = "71_Youre_Chasing_A_Feeling_Not_A_Goal_16x9.mp4"
SPEC = [
    ("You keep saying you want to be successful.", "quote", dict(text="I WANT TO BE SUCCESSFUL.", acc="SUCCESSFUL.")),
    ("But what does success actually mean to you?", "question", dict(acc="SUCCESS ACTUALLY")),
    ("Maybe you imagine finally feeling respected.", "list", dict(items=["RESPECTED"], mode="empty", acc="RESPECTED.")),
    ("Finally feeling secure.", "list", dict(items=["RESPECTED", "SECURE"], mode="empty", acc="SECURE.")),
    ("Finally feeling proud.", "list", dict(items=["RESPECTED", "SECURE", "PROUD"], mode="empty", acc="PROUD.")),
    ("Finally feeling like you're enough.", "list", dict(items=["RESPECTED", "SECURE", "PROUD", "ENOUGH"], mode="empty", acc="ENOUGH.")),
    ("But here's the problem.", "big", dict(text="THE PROBLEM", acc="PROBLEM.")),
    ("You can achieve the goal…", "list", dict(items=["THE GOAL"], mode="check", acc="ACHIEVE")),
    ("And still not experience the feeling you expected.", "gauge", dict(lbl="THE FEELING", start=0.2, end=0.25, acc="STILL NOT FEELING")),
    ("Because achievements can't automatically fix every insecurity.", "trophy" if False else "iceberg", dict(top="THE ACHIEVEMENT", bottom="THE INSECURITY", acc="CAN'T INSECURITY.")),
    ("Money can't answer every question.", "coins", dict(lbl="NOT EVERY ANSWER", acc="MONEY CAN'T")),
    ("Recognition can't replace self-respect.", "scale", dict(left="RECOGNITION", right="SELF-RESPECT", tip=1, acc="RECOGNITION SELF-RESPECT.")),
    ("And success doesn't guarantee peace.", "doc", dict(title="SUCCESS", empty=False, stamp="NO GUARANTEE", acc="DOESN'T PEACE.")),
    ("So before you spend years chasing something…", "timeline", dict(n=10, progress=0.6, tag="CHASING", acc="YEARS CHASING")),
    ("Ask yourself what you're hoping it will make you feel.", "brain", dict(says="WHAT DO I WANT TO FEEL?", acc="HOPING FEEL.")),
    ("Sometimes understanding the desire is more important than chasing the destination.", "compass", dict(lbl="THE REAL DESIRE", acc="UNDERSTANDING DESIRE DESTINATION.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
