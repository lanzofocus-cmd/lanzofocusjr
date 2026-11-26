from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH", "WANTING EVERYTHING")
OUTPUT = "28_The_Problem_With_Wanting_Everything_16x9.mp4"
WANTS = ["SUCCESS", "PEACE", "CONFIDENCE", "MONEY", "FREEDOM", "RESPECT"]
SPEC = [
    ("You want success.", "network", dict(nodes=WANTS[:1], tangled=False, acc="SUCCESS.")),
    ("Peace.", "network", dict(nodes=WANTS[:2], tangled=False, acc="PEACE.")),
    ("Confidence.", "network", dict(nodes=WANTS[:3], tangled=False, acc="CONFIDENCE.")),
    ("Money.", "network", dict(nodes=WANTS[:4], tangled=False, acc="MONEY.")),
    ("Freedom.", "network", dict(nodes=WANTS[:5], tangled=False, acc="FREEDOM.")),
    ("Respect.", "network", dict(nodes=WANTS, tangled=False, acc="RESPECT.")),
    ("But wanting everything at once…", "network", dict(nodes=WANTS, tangled=True, acc="EVERYTHING ONCE…")),
    ("Can make you feel like you're accomplishing nothing.", "progress", dict(lbl="ACCOMPLISHED", value=0.04, acc="NOTHING.")),
    ("Because your attention is divided between a hundred different destinations.", "tangle", dict(lbl="100 DESTINATIONS", acc="DIVIDED HUNDRED")),
    ("You don't need to abandon your dreams.", "list", dict(items=["SUCCESS", "PEACE", "FREEDOM"], mode="empty", acc="ABANDON")),
    ("You need to give them direction.", "compass", dict(lbl="DIRECTION", acc="DIRECTION.")),
    ("Choose what matters most right now.", "network", dict(nodes=WANTS, focus=0, tangled=False, acc="CHOOSE MOST")),
    ("Focus your energy.", "gauge", dict(lbl="FOCUS", start=0.2, end=0.9, acc="FOCUS")),
    ("Make progress.", "progress", dict(lbl="PROGRESS", value=0.6, acc="PROGRESS.")),
    ("Then expand.", "network", dict(nodes=WANTS, focus=None, tangled=False, acc="EXPAND.")),
    ("A thousand scattered steps won't always take you forward.", "dots", dict(connect=False, n=12, acc="SCATTERED WON'T")),
    ("Sometimes…", "pulse", dict()),
    ("One focused step will.", "stairs", dict(n=6, climb=1, acc="ONE FOCUSED")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
