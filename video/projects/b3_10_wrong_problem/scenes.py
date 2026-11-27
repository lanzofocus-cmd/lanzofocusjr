from kit import build, follow_sub

TITLE = ("YOU'RE TRYING TO FIX", "THE WRONG PROBLEM")
OUTPUT = "50_Youre_Trying_To_Fix_The_Wrong_Problem_16x9.mp4"
SPEC = [
    ("You think you need more motivation.", "gauge", dict(lbl="MOTIVATION", start=0.2, end=0.25, acc="MOTIVATION.")),
    ("But maybe you need fewer distractions.", "notifs", dict(items=["PING", "PING", "PING"], acc="FEWER DISTRACTIONS.")),
    ("You think you need more confidence.", "gauge", dict(lbl="CONFIDENCE", start=0.2, end=0.25, acc="CONFIDENCE.")),
    ("But maybe you need more experience.", "stairs", dict(n=6, climb=2, acc="EXPERIENCE.")),
    ("You think you need more time.", "hourglass", dict(acc="TIME.")),
    ("But maybe you need clearer priorities.", "network", dict(nodes=["NOISE", "PRIORITY", "NOISE", "NOISE", "NOISE"], focus=1, tangled=False, acc="CLEARER PRIORITIES.")),
    ("You think you're lazy.", "sticker", dict(tags=["LAZY"], acc="LAZY.")),
    ("But maybe you're overwhelmed by a goal that has no defined next step.", "stairs", dict(n=6, climb=0, acc="OVERWHELMED NEXT STEP.")),
    ("Sometimes…", "pulse", dict()),
    ("The problem isn't the thing you've been trying to fix.", "puzzle", dict(missing=True, lbl="WRONG PIECE", acc="ISN'T FIX.")),
    ("It's the assumption that made you believe that was the problem.", "brain", dict(says="THIS IS THE PROBLEM.", acc="ASSUMPTION")),
    ("Before trying harder…", "gauge", dict(lbl="EFFORT", start=0.5, end=0.95, acc="HARDER…")),
    ("Take a step back.", "shed", dict(old="TOO CLOSE", new="STEP BACK", acc="STEP BACK.")),
    ("Ask:", "pulse", dict(acc="ASK:")),
    ("What if my diagnosis is wrong?", "doc", dict(title="DIAGNOSIS", empty=False, stamp="WRONG?", acc="DIAGNOSIS WRONG?")),
    ("Because working harder on the wrong problem…", "path", dict(kind="winding", acc="HARDER WRONG")),
    ("Can keep you stuck for a very long time.", "cage", dict(words=["WRONG FIX"], acc="STUCK LONG")),
    ("Comment: What problem have you recently realized wasn't actually the problem?", "cta", dict(kind="comment", lbl="WHAT WASN'T THE PROBLEM?", acc="COMMENT: WASN'T")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
