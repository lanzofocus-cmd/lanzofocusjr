from kit import build, follow_sub

TITLE = ("YOU MAY BE MAKING YOUR LIFE", "HARDER THAN IT NEEDS TO BE")
OUTPUT = "124_Making_Life_Harder_Than_It_Needs_To_Be_16x9.mp4"
SPEC = [
    ("You overcomplicate the plan.", "tangle", dict(lbl="THE PLAN", acc="OVERCOMPLICATE")),
    ("You create too many steps.", "list", dict(items=["STEP 1", "STEP 2", "STEP 3", "STEP 4", "STEP 5"], mode="empty", acc="TOO MANY STEPS.")),
    ("You wait for the perfect system.", "doc", dict(title="SYSTEM V12", empty=False, acc="PERFECT SYSTEM.")),
    ("You try to optimize everything.", "gauge", dict(lbl="OPTIMIZING", start=0.3, end=0.98, acc="OPTIMIZE")),
    ("And suddenly…", "pulse", dict()),
    ("The simple action you needed to take…", "list", dict(items=["THE SIMPLE ACTION"], mode="empty", acc="SIMPLE ACTION")),
    ("Has become buried beneath preparation.", "iceberg", dict(top="PREPARATION", bottom="THE ACTION", acc="BURIED PREPARATION.")),
    ("Sometimes…", "pulse", dict()),
    ("The solution is simpler than your plan.", "scale", dict(left="SIMPLE", right="COMPLEX", tip=-1, acc="SIMPLER")),
    ("Start with the basics.", "bricks", dict(rows=1, lbl="THE BASICS", uneven=False, acc="BASICS.")),
    ("Do the obvious thing.", "list", dict(items=["THE OBVIOUS THING"], mode="check", acc="OBVIOUS")),
    ("Take the first step.", "stairs", dict(n=6, climb=1, acc="FIRST STEP.")),
    ("Then adjust.", "compass", dict(lbl="ADJUST", acc="ADJUST.")),
    ("Complexity can feel intelligent.", "brain", dict(says="SO SMART.", acc="COMPLEXITY INTELLIGENT.")),
    ("But simplicity is often what gets things done.", "list", dict(items=["DONE"], mode="check", acc="SIMPLICITY DONE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
