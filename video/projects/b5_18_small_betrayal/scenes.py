from kit import build, follow_sub

TITLE = ("THE SMALL", "BETRAYAL")
OUTPUT = "158_The_Small_Betrayal_16x9.mp4"
SPEC = [
    ("Every time you repeatedly promise yourself something and ignore it…", "list", dict(items=["TOMORROW", "TOMORROW", "TOMORROW"], mode="strike", acc="PROMISE IGNORE")),
    ("You create a small distance between your words and your actions.", "map", dict(a_lbl="WORDS", b_lbl="ACTIONS", acc="DISTANCE WORDS ACTIONS")),
    ("Not because you failed once.", "list", dict(items=["FAILED ONCE"], mode="strike", acc="FAILED ONCE")),
    ("Because you stopped taking your own promises seriously.", "doc", dict(title="PROMISE", empty=True, stamp="IGNORED", acc="PROMISES SERIOUSLY")),
    ("You don't rebuild trust with yourself through huge declarations.", "quote", dict(text="THIS TIME, EVERYTHING CHANGES!", acc="REBUILD TRUST HUGE")),
    ("You rebuild it by making smaller promises…", "bricks", dict(rows=3, lbl="SMALL PROMISES", uneven=False, acc="SMALLER PROMISES")),
    ("And actually keeping them.", "list", dict(items=["KEPT", "KEPT", "KEPT"], mode="check", acc="KEEPING")),
    ("Choose one realistic promise for today.", "cta", dict(kind="comment", lbl="ONE PROMISE FOR TODAY", acc="ONE REALISTIC TODAY")),
    ("Make it small enough that you can genuinely keep it.", "key", dict(lbl="KEEP IT", acc="SMALL GENUINELY KEEP")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
