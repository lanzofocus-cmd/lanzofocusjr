from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED TO", "BE A BEGINNER")
OUTPUT = "20_Youre_Allowed_To_Be_A_Beginner_16x9.mp4"
SPEC = [
    ("You're embarrassed because you're not good at something yet.", "progress", dict(lbl="SKILL", value=0.06, acc="EMBARRASSED YET.")),
    ("But think about that.", "pulse", dict(acc="THINK")),
    ("You're judging yourself for being at the beginning…", "stairs", dict(n=6, climb=0, highlight=0, acc="JUDGING BEGINNING…")),
    ("Of something you've barely started.", "timeline", dict(n=9, progress=0.08, tag="DAY 1", acc="BARELY STARTED.")),
    ("Every expert was once confused.", "brain", dict(says="WAIT, WHAT?", acc="EXPERT CONFUSED.")),
    ("Every confident person once made mistakes.", "list", dict(items=["MISTAKE", "MISTAKE", "MISTAKE"], mode="strike", acc="CONFIDENT MISTAKES.")),
    ("Every skill you admire…", "phone", dict(content="highlight", acc="ADMIRE…")),
    ("Was built through a period when the person had no idea what they were doing.", "iceberg", dict(top="THE SKILL", bottom="THE CLUELESS YEARS", acc="NO IDEA")),
    ("Being bad at something isn't proof you should stop.", "doc", dict(title="PROOF", empty=True, stamp="NOT PROOF", acc="ISN'T STOP.")),
    ("It's evidence that you're learning.", "chart", dict(kind="up", lbl="LEARNING", acc="EVIDENCE LEARNING.")),
    ("Don't let the embarrassment of being a beginner…", "sticker", dict(tags=["BEGINNER"], acc="EMBARRASSMENT BEGINNER…")),
    ("Rob you of the satisfaction of becoming better.", "stairs", dict(n=6, climb=4, acc="SATISFACTION BETTER.")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
