from kit import build, follow_sub

TITLE = ("THE THINGS YOU", "KEEP TOLERATING")
OUTPUT = "146_The_Things_You_Keep_Tolerating_16x9.mp4"
SPEC = [
    ("Your standards aren't only shown by what you demand.", "doc", dict(title="STANDARDS", empty=False, acc="STANDARDS DEMAND")),
    ("They're shown by what you repeatedly tolerate.", "list", dict(items=["TOLERATED", "TOLERATED", "TOLERATED"], mode="check", acc="REPEATEDLY TOLERATE")),
    ("The disrespect you excuse.", "quote", dict(text="IT'S FINE.", acc="DISRESPECT EXCUSE")),
    ("The habits you ignore.", "list", dict(items=["THAT HABIT"], mode="tag", tag="IGNORED", acc="HABITS IGNORE")),
    ("The situations you keep returning to.", "door", dict(open_=True, lbl="AGAIN", acc="RETURNING")),
    ("Every repeated tolerance teaches you what you're willing to live with.", "book", dict(chapter="LESSON", text="THIS IS NORMAL", acc="TEACHES WILLING")),
    ("Eventually, what you tolerate becomes familiar.", "plant", dict(height=0.6, roots=True, lbl="FAMILIAR", acc="FAMILIAR")),
    ("And familiar doesn't always mean healthy.", "scale", dict(left="FAMILIAR", right="HEALTHY", tip=1, acc="FAMILIAR HEALTHY")),
    ("What's one thing people should stop normalizing?", "list", dict(items=["NORMAL?"], mode="strike", acc="STOP NORMALIZING")),
    ("Give your answer in the comments.", "cta", dict(kind="comment", lbl="STOP NORMALIZING...", acc="COMMENTS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
