from kit import build, follow_sub

TITLE = ("THE MOMENT YOU", "ACTUALLY LEARN")
OUTPUT = "175_The_Moment_You_Actually_Learn_16x9.mp4"
SPEC = [
    ("You don't learn the most when everything goes according to plan.", "chart", dict(kind="up", lbl="THE PLAN", acc="LEARN PLAN")),
    ("You learn when the plan stops working.", "chart", dict(kind="down", lbl="THE PLAN", acc="STOPS WORKING")),
    ("When you have to adjust.", "path", dict(kind="fork", labels=("PLAN A", "PLAN B"), acc="ADJUST")),
    ("When your assumptions are challenged.", "brain", dict(says="WAIT... WHAT?", acc="ASSUMPTIONS CHALLENGED")),
    ("When you discover that being confident doesn't mean being correct.", "scale", dict(left="CONFIDENT", right="CORRECT", tip=0, acc="CONFIDENT CORRECT")),
    ("The goal isn't to avoid every mistake.", "list", dict(items=["AVOID EVERY MISTAKE"], mode="strike", acc="AVOID MISTAKE")),
    ("It's to become someone who can learn from reality instead of arguing with it.", "compass", dict(lbl="REALITY", acc="LEARN REALITY ARGUING")),
    ("Share one mistake that taught you something valuable.", "cta", dict(kind="comment", lbl="YOUR MOST USEFUL MISTAKE", acc="MISTAKE VALUABLE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
