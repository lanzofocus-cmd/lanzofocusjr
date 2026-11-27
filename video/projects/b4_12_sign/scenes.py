from kit import build, follow_sub

TITLE = ("YOU KEEP WAITING", "FOR A SIGN")
OUTPUT = "102_You_Keep_Waiting_For_A_Sign_16x9.mp4"
SPEC = [
    ("You want a sign.", "big", dict(text="A SIGN", acc="SIGN.")),
    ("Something obvious.", "sunrise", dict(acc="OBVIOUS.")),
    ("Something that tells you the decision is right.", "doc", dict(title="DECISION", empty=False, stamp="RIGHT?", acc="RIGHT.")),
    ("Something that guarantees you won't regret it.", "doc", dict(title="GUARANTEE", empty=True, acc="GUARANTEES REGRET")),
    ("But sometimes…", "pulse", dict()),
    ("There isn't a sign.", "chairs", dict(lbl="NO SIGN", acc="ISN'T SIGN.")),
    ("There is simply a choice.", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="CHOICE.")),
    ("And the uncertainty that comes with it.", "fog", dict(lbl="UNCERTAIN", acc="UNCERTAINTY")),
    ("You research.", "list", dict(items=["RESEARCH"], mode="check", acc="RESEARCH.")),
    ("You ask.", "list", dict(items=["RESEARCH", "ASK"], mode="check", acc="ASK.")),
    ("You think.", "list", dict(items=["RESEARCH", "ASK", "THINK"], mode="check", acc="THINK.")),
    ("You wait.", "list", dict(items=["RESEARCH", "ASK", "THINK", "WAIT"], mode="check", acc="WAIT.")),
    ("But eventually…", "pulse", dict()),
    ("You reach a point where more information won't eliminate every doubt.", "progress", dict(lbl="CERTAINTY", value=0.8, acc="INFORMATION WON'T DOUBT.")),
    ("You have to decide with what you know.", "compass", dict(lbl="WHAT YOU KNOW", acc="DECIDE KNOW.")),
    ("Not every decision comes with certainty.", "lock", dict(lbl="CERTAINTY", acc="NOT CERTAINTY.")),
    ("Sometimes your decision is the beginning of your certainty.", "path", dict(kind="dashed", walker=True, acc="DECISION BEGINNING CERTAINTY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
