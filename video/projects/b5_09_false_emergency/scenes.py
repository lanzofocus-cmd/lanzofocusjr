from kit import build, follow_sub

TITLE = ("THE FALSE", "EMERGENCY")
OUTPUT = "149_The_False_Emergency_16x9.mp4"
SPEC = [
    ("Not everything that feels urgent deserves your attention.", "gauge", dict(lbl="URGENCY", start=0.2, end=0.95, acc="URGENT ATTENTION")),
    ("A notification.", "notifs", dict(items=["NEW NOTIFICATION"], acc="NOTIFICATION")),
    ("A random opinion.", "bubbles", dict(texts=["WELL, ACTUALLY..."], acc="OPINION")),
    ("A message.", "notifs", dict(items=["NEW NOTIFICATION", "NEW MESSAGE"], acc="MESSAGE")),
    ("A problem that can wait.", "list", dict(items=["THAT PROBLEM"], mode="tag", tag="CAN WAIT", acc="WAIT")),
    ("Your mind can turn small things into emergencies simply because they're demanding attention.", "brain", dict(says="URGENT!", says2="RIGHT NOW!", acc="EMERGENCIES DEMANDING")),
    ("But urgency and importance are not the same thing.", "scale", dict(left="URGENT", right="IMPORTANT", tip=1, acc="URGENCY IMPORTANCE")),
    ("Don't let the loudest thing decide your priorities.", "list", dict(items=["WHAT MATTERS", "WHAT'S LOUD"], mode="check", acc="LOUDEST PRIORITIES")),
    ("Comment \"PRIORITIES\" if you're learning to stop reacting to everything.", "cta", dict(kind="comment", lbl="COMMENT \"PRIORITIES\"", acc="PRIORITIES REACTING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
