from kit import build, follow_sub

TITLE = ("YOU'RE NOT STUCK WHERE", "YOU THINK YOU ARE")
OUTPUT = "09_Youre_Not_Stuck_Where_You_Think_You_Are_16x9.mp4"
NODES = ["FUTURE", "CAREER", "MONEY", "GOALS", "PROBLEMS"]
SPEC = [
    ("Sometimes you feel stuck…", "alone", dict(tag="STUCK", acc="STUCK…")),
    ("Because you're trying to solve your entire life at once.", "tangle", dict(lbl="YOUR ENTIRE LIFE", acc="ENTIRE ONCE.")),
    ("Your future.", "network", dict(nodes=NODES[:1], tangled=False, acc="FUTURE.")),
    ("Your career.", "network", dict(nodes=NODES[:2], tangled=False, acc="CAREER.")),
    ("Your finances.", "network", dict(nodes=NODES[:3], tangled=False, acc="FINANCES.")),
    ("Your goals.", "network", dict(nodes=NODES[:4], tangled=False, acc="GOALS.")),
    ("Your problems.", "network", dict(nodes=NODES, tangled=False, acc="PROBLEMS.")),
    ("Everything feels connected.", "network", dict(nodes=NODES, tangled=True, acc="CONNECTED.")),
    ("Everything feels urgent.", "network", dict(nodes=["URGENT", "URGENT", "URGENT", "URGENT", "URGENT"], tangled=True, acc="URGENT.")),
    ("And suddenly…", "pulse", dict()),
    ("Doing nothing feels easier than doing anything.", "scale", dict(left="NOTHING", right="ANYTHING", tip=-1, acc="NOTHING EASIER")),
    ("But you don't need to solve your entire life today.", "tangle", dict(lbl="NOT TODAY", acc="DON'T TODAY.")),
    ("You need to solve the next problem.", "network", dict(nodes=NODES, focus=4, tangled=True, acc="NEXT")),
    ("Take the next step.", "stairs", dict(n=6, climb=1, highlight=0, acc="NEXT STEP.")),
    ("Make the next decision.", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="NEXT DECISION.")),
    ("Then the next.", "stairs", dict(n=6, climb=2, acc="NEXT.")),
    ("A complicated future becomes manageable…", "stairs", dict(n=6, climb=4, acc="MANAGEABLE…")),
    ("When you stop trying to reach it all at once.", "stairs", dict(n=6, climb=5, acc="ONCE.")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
