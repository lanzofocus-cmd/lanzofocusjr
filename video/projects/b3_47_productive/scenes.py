from kit import build, follow_sub

TITLE = ("STOP TRYING TO MAKE EVERY", "MOMENT PRODUCTIVE")
OUTPUT = "87_Stop_Trying_To_Make_Every_Moment_Productive_16x9.mp4"
SPEC = [
    ("You don't have to turn every moment into an opportunity.", "timeline", dict(n=10, progress=0.6, tag="OPTIMIZED?", acc="EVERY OPPORTUNITY.")),
    ("Every conversation into networking.", "list", dict(items=["CONVERSATION → NETWORKING"], mode="strike", acc="NETWORKING.")),
    ("Every hobby into a skill.", "list", dict(items=["CONVERSATION → NETWORKING", "HOBBY → SKILL"], mode="strike", acc="HOBBY SKILL.")),
    ("Every rest into recovery for more work.", "list", dict(items=["CONVERSATION → NETWORKING", "HOBBY → SKILL", "REST → RECOVERY"], mode="strike", acc="REST WORK.")),
    ("Every interest into something profitable.", "list", dict(items=["CONVERSATION → NETWORKING", "HOBBY → SKILL", "REST → RECOVERY", "INTEREST → PROFIT"], mode="strike", acc="PROFITABLE.")),
    ("Life isn't a machine where every minute must produce something.", "progress", dict(lbl="OUTPUT", value=1.0, acc="ISN'T MACHINE PRODUCE")),
    ("Sometimes…", "pulse", dict()),
    ("You should do something simply because you enjoy it.", "sunrise", dict(acc="SIMPLY ENJOY")),
    ("Read without needing to remember everything.", "book", dict(chapter="JUST READING", acc="READ WITHOUT")),
    ("Play without needing to improve.", "bubbles", dict(texts=["JUST FOR FUN"], inverted=True, acc="PLAY WITHOUT")),
    ("Spend time with someone without checking the clock.", "crowd", dict(n=2, acc="WITHOUT CLOCK.")),
    ("Rest without calculating what you could have accomplished.", "receipt", dict(items=[("REST", "PRICELESS")], acc="REST WITHOUT")),
    ("Your life has value beyond what it produces.", "key", dict(lbl="YOUR LIFE", acc="VALUE BEYOND PRODUCES.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
