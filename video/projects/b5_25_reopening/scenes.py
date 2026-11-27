from kit import build, follow_sub

TITLE = ("THE DECISION YOU", "KEEP REOPENING")
OUTPUT = "165_The_Decision_You_Keep_Reopening_16x9.mp4"
SPEC = [
    ("Some decisions don't need to be reconsidered every day.", "doc", dict(title="DECIDED", empty=False, stamp="DONE", acc="RECONSIDERED EVERY")),
    ("You made the choice.", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="CHOICE")),
    ("You thought about it.", "brain", dict(says="I THOUGHT IT THROUGH.", acc="THOUGHT")),
    ("You had your reasons.", "list", dict(items=["REASON", "REASON", "REASON"], mode="check", acc="REASONS")),
    ("But then doubt returns…", "fog", dict(lbl="DOUBT", acc="DOUBT")),
    ("And you reopen the same question.", "door", dict(open_=True, lbl="THE SAME QUESTION", acc="REOPEN SAME")),
    ("Again.", "big", dict(text="AGAIN", acc="AGAIN")),
    ("And again.", "big", dict(text="AND AGAIN", acc="AGAIN")),
    ("Sometimes the problem isn't the decision.", "list", dict(items=["THE DECISION"], mode="strike", acc="PROBLEM DECISION")),
    ("It's your inability to let the decision remain decided.", "lock", dict(lbl="DECIDED", acc="REMAIN DECIDED")),
    ("What's one decision you've been overthinking for too long?", "cta", dict(kind="comment", lbl="THE ONE YOU OVERTHINK", acc="OVERTHINKING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
