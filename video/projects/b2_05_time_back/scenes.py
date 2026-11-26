from kit import build, follow_sub

TITLE = ("YOU CAN'T GET", "TIME BACK")
OUTPUT = "15_You_Cant_Get_Time_Back_16x9.mp4"
SPEC = [
    ("You can replace money.", "coins", dict(lbl="REPLACEABLE", acc="MONEY.")),
    ("You can replace possessions.", "receipt", dict(items=[("PHONE", "REPLACE"), ("CAR", "REPLACE")], acc="POSSESSIONS.")),
    ("You can recover from mistakes.", "chart", dict(kind="invest", lbl="RECOVERY", acc="RECOVER")),
    ("But you cannot return to a moment you already spent.", "hourglass", dict(acc="CANNOT SPENT.")),
    ("And the strange thing is…", "pulse", dict()),
    ("We often treat our time like it's unlimited.", "big", dict(text="∞", sub="WE THINK", acc="UNLIMITED.")),
    ("We postpone conversations.", "list", dict(items=["THAT CONVERSATION"], mode="tag", tag="LATER", acc="POSTPONE")),
    ("We delay goals.", "list", dict(items=["THAT CONVERSATION", "THAT GOAL"], mode="tag", tag="LATER", acc="DELAY")),
    ("We tell ourselves we'll appreciate people later.", "list", dict(items=["THAT CONVERSATION", "THAT GOAL", "THOSE PEOPLE"], mode="tag", tag="LATER", acc="APPRECIATE LATER.")),
    ("We'll start later.", "quote", dict(text="I'LL START LATER.", acc="LATER.")),
    ("We'll change later.", "quote", dict(text="I'LL CHANGE LATER.", acc="LATER.")),
    ("But later isn't guaranteed to look the way you imagined.", "path", dict(kind="dashed", fog=True, acc="ISN'T GUARANTEED")),
    ("Don't let your entire life become a collection of things you meant to do.", "list", dict(items=["MEANT TO CALL", "MEANT TO START", "MEANT TO GO"], mode="strike", acc="MEANT")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
