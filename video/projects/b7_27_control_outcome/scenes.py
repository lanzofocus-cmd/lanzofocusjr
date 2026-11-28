from kit import build, follow_sub, hook

TITLE = ("TRYING TO CONTROL", "THE OUTCOME")
OUTPUT = "227_The_Problem_With_Trying_To_Control_The_Outcome_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You can prepare carefully.", "list", dict(items=["PREPARE"], mode="check", acc="PREPARE")),
    ("Practice.", "list", dict(items=["PREPARE", "PRACTICE"], mode="check", acc="PRACTICE")),
    ("Research.", "list", dict(items=["PREPARE", "PRACTICE", "RESEARCH"], mode="check", acc="RESEARCH")),
    ("Make a plan.", "list", dict(items=["PREPARE", "PRACTICE", "RESEARCH", "PLAN"], mode="check", acc="PLAN")),
    ("And still not get the result you wanted.", "chart", dict(kind="down", lbl="THE RESULT", acc="RESULT")),
    ("This can feel unfair.", "scale", dict(left="EFFORT", right="RESULT", tip=-1, acc="UNFAIR")),
    ("Because we often assume effort should produce a predictable outcome.", "map", dict(a_lbl="EFFORT", b_lbl="OUTCOME", acc="EFFORT PREDICTABLE")),
    ("But effort doesn't control everything.", "list", dict(items=["EFFORT CONTROLS ALL"], mode="strike", acc="CONTROL EVERYTHING")),
    ("Other people make decisions.", "crowd", dict(n=7, acc="OTHER PEOPLE")),
    ("Circumstances change.", "chart", dict(kind="wave", lbl="CIRCUMSTANCES", acc="CIRCUMSTANCES")),
    ("Unexpected problems appear.", "tangle", dict(lbl="UNEXPECTED", acc="UNEXPECTED")),
    ("Sometimes the result simply doesn't match what you hoped.", "scale", dict(left="HOPED", right="GOT", tip=-1, acc="MATCH HOPED")),
    ("That doesn't make preparation useless.", "list", dict(items=["PREPARATION IS USELESS"], mode="strike", acc="PREPARATION USELESS")),
    ("It means preparation improves your chances…", "hud", dict(lbl="YOUR CHANCES", start=30, end=78, icons=None, crowd=0, acc="IMPROVES CHANCES")),
    ("Without guaranteeing the result.", "hud", dict(lbl="YOUR CHANCES", start=78, end=78, icons=None, crowd=0, tag="NOT 100%", acc="GUARANTEEING")),
    ("Focus on the things you can influence.", "compass", dict(lbl="INFLUENCE", acc="FOCUS INFLUENCE")),
    ("Your preparation.", "list", dict(items=["PREPARATION"], mode="check", acc="PREPARATION")),
    ("Your decisions.", "list", dict(items=["PREPARATION", "DECISIONS"], mode="check", acc="DECISIONS")),
    ("Your response.", "list", dict(items=["PREPARATION", "DECISIONS", "RESPONSE"], mode="check", acc="RESPONSE")),
    ("Your willingness to learn.", "list", dict(items=["PREPARATION", "DECISIONS", "RESPONSE", "WILLINGNESS TO LEARN"], mode="check", acc="LEARN")),
    ("You can't always control the outcome.", "fog", dict(lbl="THE OUTCOME", acc="CONTROL OUTCOME")),
    ("But you can control whether the experience teaches you something useful.", "key", dict(lbl="THE LESSON", drop=True, acc="EXPERIENCE TEACHES USEFUL")),
    ("What is one thing you've learned to focus on instead of worrying about outcomes you can't control?", "cta", dict(kind="comment", lbl="WHAT YOU FOCUS ON", acc="FOCUS WORRYING CONTROL")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EFFORT", start=20, end=100, lbl2="CONTROL OVER RESULT", start2=30, end2=31, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
