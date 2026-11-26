from kit import build, follow_sub

TITLE = ("YOU KEEP UNDERESTIMATING", "YOURSELF")
OUTPUT = "25_You_Keep_Underestimating_Yourself_16x9.mp4"
SPEC = [
    ("You've survived things you once thought would overwhelm you.", "list", dict(items=["THE BREAKUP", "THE LOSS", "THE HARD YEAR"], mode="check", acc="SURVIVED OVERWHELM")),
    ("You've learned things you didn't know before.", "chart", dict(kind="up", lbl="WHAT YOU KNOW", acc="LEARNED")),
    ("You've adapted to situations you never expected.", "path", dict(kind="winding", acc="ADAPTED")),
    ("Yet somehow…", "pulse", dict()),
    ("You still assume the next challenge is impossible.", "stairs", dict(n=6, climb=0, highlight=0, acc="IMPOSSIBLE.")),
    ("Why?", "big", dict(text="WHY?", acc="WHY?")),
    ("Because you're judging your future ability…", "shed", dict(old="TODAY'S YOU", new="FUTURE YOU", acc="FUTURE ABILITY…")),
    ("Using your current experience.", "progress", dict(lbl="CURRENT EXPERIENCE", value=0.35, acc="CURRENT")),
    ("You haven't learned the skill yet.", "list", dict(items=["THE SKILL"], mode="tag", tag="NOT YET", acc="SKILL YET.")),
    ("You haven't developed the confidence yet.", "list", dict(items=["THE SKILL", "THE CONFIDENCE"], mode="tag", tag="NOT YET", acc="CONFIDENCE YET.")),
    ("You haven't discovered what you're capable of yet.", "list", dict(items=["THE SKILL", "THE CONFIDENCE", "YOUR LIMITS"], mode="tag", tag="NOT YET", acc="CAPABLE YET.")),
    ("But \"not yet\" is very different from \"never.\"", "scale", dict(left="NOT YET", right="NEVER", tip=0, acc="\"NOT YET\" \"NEVER.\"")),
    ("Stop treating your current limitations like permanent predictions.", "doc", dict(title="PREDICTION", empty=True, stamp="NOT PERMANENT", acc="LIMITATIONS PERMANENT")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
