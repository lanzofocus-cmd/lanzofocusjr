from kit import build, follow_sub

TITLE = ("THE WRONG", "MEASUREMENT")
OUTPUT = "142_The_Wrong_Measurement_16x9.mp4"
SPEC = [
    ("Imagine measuring your life using someone else's ruler.", "progress", dict(lbl="THEIR RULER", value=0.2, acc="MEASURING RULER")),
    ("Their achievements.", "list", dict(items=["THEIR ACHIEVEMENTS"], mode="tag", tag="NOT YOURS", acc="ACHIEVEMENTS")),
    ("Their timeline.", "list", dict(items=["THEIR ACHIEVEMENTS", "THEIR TIMELINE"], mode="tag", tag="NOT YOURS", acc="TIMELINE")),
    ("Their opportunities.", "list", dict(items=["THEIR ACHIEVEMENTS", "THEIR TIMELINE", "THEIR OPPORTUNITIES"], mode="tag", tag="NOT YOURS", acc="OPPORTUNITIES")),
    ("Their circumstances.", "list", dict(items=["THEIR ACHIEVEMENTS", "THEIR TIMELINE", "THEIR OPPORTUNITIES", "THEIR CIRCUMSTANCES"], mode="tag", tag="NOT YOURS", acc="CIRCUMSTANCES")),
    ("Then wondering why you always feel behind.", "startline", dict(behind=True, acc="BEHIND")),
    ("You might be making progress and still feel unsuccessful because you're measuring something that was never yours to measure.", "chart", dict(kind="up", lbl="YOUR PROGRESS", acc="PROGRESS NEVER YOURS")),
    ("Stop comparing different journeys using the same scoreboard.", "timeline", dict(compare=True, acc="DIFFERENT SAME SCOREBOARD")),
    ("Save this for the next time comparison makes your own progress look smaller than it really is.", "cta", dict(kind="save", lbl="FOR NEXT TIME", acc="SAVE SMALLER")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
