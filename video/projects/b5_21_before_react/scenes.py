from kit import build, follow_sub

TITLE = ("THE MOMENT", "BEFORE YOU REACT")
OUTPUT = "161_The_Moment_Before_You_React_16x9.mp4"
SPEC = [
    ("There's a tiny moment between being triggered…", "pulse", dict(acc="TINY MOMENT TRIGGERED")),
    ("And reacting.", "gauge", dict(lbl="REACTION", start=0.3, end=0.95, acc="REACTING")),
    ("Most people never notice it.", "crowd", dict(n=7, dim=True, acc="NEVER NOTICE")),
    ("They respond immediately.", "arrows", dict(items=["INSTANT"], acc="IMMEDIATELY")),
    ("They say the thing.", "bubbles", dict(texts=["FINE. WHATEVER."], acc="SAY")),
    ("They send the message.", "phone", dict(lbl="SENT", acc="SEND MESSAGE")),
    ("They make the decision while their emotions are still in control.", "brain", dict(says="RIGHT NOW!", says2="NO THINKING", acc="EMOTIONS CONTROL")),
    ("But that tiny pause?", "hourglass", dict(acc="TINY PAUSE")),
    ("That's where you get your choice back.", "key", dict(lbl="YOUR CHOICE", acc="CHOICE BACK")),
    ("Comment \"PAUSE\" if you're practicing responding instead of reacting.", "cta", dict(kind="comment", lbl="COMMENT \"PAUSE\"", acc="PAUSE RESPONDING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
