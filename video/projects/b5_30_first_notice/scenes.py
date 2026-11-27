from kit import build, follow_sub

TITLE = ("THE FIRST THING", "YOU NOTICE")
OUTPUT = "170_The_First_Thing_You_Notice_16x9.mp4"
SPEC = [
    ("What you notice first says something about what your mind is searching for.", "brain", dict(says="SEARCHING...", acc="NOTICE SEARCHING")),
    ("Problems.", "list", dict(items=["PROBLEMS"], mode="check", acc="PROBLEMS")),
    ("Opportunities.", "list", dict(items=["PROBLEMS", "OPPORTUNITIES"], mode="check", acc="OPPORTUNITIES")),
    ("Threats.", "list", dict(items=["PROBLEMS", "OPPORTUNITIES", "THREATS"], mode="check", acc="THREATS")),
    ("Possibilities.", "list", dict(items=["PROBLEMS", "OPPORTUNITIES", "THREATS", "POSSIBILITIES"], mode="check", acc="POSSIBILITIES")),
    ("Beauty.", "sunrise", dict(acc="BEAUTY")),
    ("Your attention is constantly filtering the world.", "dots", dict(connect=True, acc="ATTENTION FILTERING")),
    ("You may not control everything you see…", "fog", dict(lbl="EVERYTHING", acc="CONTROL SEE")),
    ("But you can train yourself to notice more than just what's wrong.", "compass", dict(lbl="WHAT'S RIGHT", acc="TRAIN NOTICE WRONG")),
    ("What's something good you noticed today that you normally would've overlooked?", "cta", dict(kind="comment", lbl="SOMETHING GOOD TODAY", acc="GOOD NOTICED OVERLOOKED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
