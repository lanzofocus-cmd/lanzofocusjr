from kit import build, follow_sub

TITLE = ("THE PRICE OF", "AN OPINION")
OUTPUT = "151_The_Price_Of_An_Opinion_16x9.mp4"
SPEC = [
    ("Every time you change your decision to avoid someone's opinion…", "path", dict(kind="fork", labels=("YOUR WAY", "THEIR WAY"), acc="CHANGE AVOID OPINION")),
    ("You pay for it with a piece of your own direction.", "price", dict(text="YOUR DIRECTION", sub="THE REAL PRICE", acc="PAY DIRECTION")),
    ("Not every opinion deserves equal weight.", "scale", dict(left="THEIR OPINION", right="YOUR DIRECTION", tip=1, acc="EQUAL WEIGHT")),
    ("Some people know your potential.", "crowd", dict(n=5, highlight=1, highlight_label="POTENTIAL", acc="POTENTIAL")),
    ("Some people only know your past.", "frame", dict(who="YOUR PAST", acc="PAST")),
    ("And some people simply prefer you exactly where they understand you.", "cage", dict(words=["STAY HERE", "STAY THE SAME"], acc="PREFER UNDERSTAND")),
    ("Listen carefully.", "bubbles", dict(texts=["HERE'S WHAT I THINK."], acc="LISTEN")),
    ("But decide for yourself.", "compass", dict(lbl="YOUR DECISION", acc="DECIDE YOURSELF")),
    ("Share this with someone who needs permission to stop living according to everybody else's expectations.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE PERMISSION EXPECTATIONS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
