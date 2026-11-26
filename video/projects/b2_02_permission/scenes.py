from kit import build, follow_sub

TITLE = ("YOU'RE WAITING", "FOR PERMISSION")
OUTPUT = "12_Youre_Waiting_For_Permission_16x9.mp4"
SPEC = [
    ("What if nobody ever gives you permission?", "doc", dict(title="PERMISSION", empty=True, acc="NOBODY PERMISSION?")),
    ("Permission to start.", "list", dict(items=["TO START"], mode="empty", acc="START.")),
    ("Permission to change.", "list", dict(items=["TO START", "TO CHANGE"], mode="empty", acc="CHANGE.")),
    ("Permission to become something different.", "list", dict(items=["TO START", "TO CHANGE", "TO BECOME"], mode="empty", acc="DIFFERENT.")),
    ("You could spend your entire life waiting for someone to tell you you're ready.", "hourglass", dict(acc="ENTIRE WAITING READY.")),
    ("But some doors won't open until you stop waiting outside them.", "door", dict(open_=True, lbl="YOUR NEXT CHAPTER", acc="DOORS STOP WAITING")),
    ("You don't need everyone to understand your ambition.", "crowd", dict(n=7, highlight=3, highlight_label="AMBITION", acc="UNDERSTAND AMBITION.")),
    ("You don't need everyone to agree with your decisions.", "bubbles", dict(texts=["ARE YOU SURE?", "THAT'S RISKY.", "I WOULDN'T."], acc="AGREE DECISIONS.")),
    ("Sometimes, you simply have to make the decision…", "path", dict(kind="fork", labels=("WAIT", "GO"), acc="DECISION…")),
    ("And accept that not everyone will understand it.", "alone", dict(tag="DECIDED", others=4, acc="ACCEPT")),
    ("Your life isn't a group project.", "big", dict(text="SOLO PROJECT", sub="YOUR LIFE", acc="ISN'T GROUP PROJECT.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
