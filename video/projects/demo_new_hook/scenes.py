from kit import build, follow_sub, hook

TITLE = ("THE PRICE OF", "AN OPINION")
OUTPUT = "151_The_Price_Of_An_Opinion_NEW_HOOK_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Every time you change your decision to avoid someone's opinion…", "path", dict(kind="fork", labels=("YOUR WAY", "THEIR WAY"), acc="CHANGE AVOID OPINION")),
    ("You pay for it with a piece of your own direction.", "hud", dict(lbl="THEIR APPROVAL", start=40, end=92, lbl2="YOUR DIRECTION", start2=80, end2=35, icons="thumb", acc="PAY DIRECTION")),
    ("Not every opinion deserves equal weight.", "scale", dict(left="THEIR OPINION", right="YOUR DIRECTION", tip=1, acc="EQUAL WEIGHT")),
    ("Some people know your potential.", "crowd", dict(n=5, highlight=1, highlight_label="POTENTIAL", acc="POTENTIAL")),
    ("Some people only know your past.", "frame", dict(who="YOUR PAST", acc="PAST")),
    ("And some people simply prefer you exactly where they understand you.", "cage", dict(words=["STAY HERE", "STAY THE SAME"], acc="PREFER UNDERSTAND")),
    ("Listen carefully.", "bubbles", dict(texts=["HERE'S WHAT I THINK."], acc="LISTEN")),
    ("But decide for yourself.", "beam", dict(lbl="YOUR DIRECTION", tags=("STAY HERE", "WHY CHANGE?", "BE REALISTIC"), acc="DECIDE YOURSELF")),
    ("Share this with someone who needs permission to stop living according to everybody else's expectations.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE PERMISSION EXPECTATIONS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, "hud", dict(lbl="THEIR APPROVAL", start=15, end=100, lbl2="YOUR DIRECTION", start2=100, end2=8, icons="thumb", count=2.3))
