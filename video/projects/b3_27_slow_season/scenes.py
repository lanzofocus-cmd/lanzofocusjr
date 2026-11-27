from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED TO", "HAVE A SLOW SEASON")
OUTPUT = "67_Youre_Allowed_To_Have_A_Slow_Season_16x9.mp4"
SPEC = [
    ("Not every period of your life will be explosive growth.", "chart", dict(kind="up", lbl="EXPLOSIVE GROWTH?", acc="NOT EXPLOSIVE")),
    ("Some seasons will be quieter.", "chart", dict(kind="flat", lbl="A QUIET SEASON", acc="QUIETER.")),
    ("You might be learning.", "book", dict(chapter="LEARNING", acc="LEARNING.")),
    ("Recovering from setbacks.", "chart", dict(kind="invest", lbl="RECOVERING", acc="RECOVERING")),
    ("Figuring things out.", "puzzle", dict(missing=True, lbl="FIGURING IT OUT", acc="FIGURING")),
    ("Building foundations nobody can see yet.", "plant", dict(height=0.15, lbl="FOUNDATIONS", acc="FOUNDATIONS NOBODY")),
    ("And because the progress isn't obvious…", "progress", dict(lbl="PROGRESS", value=0.4, invisible=True, acc="ISN'T OBVIOUS…")),
    ("You may feel like you're wasting time.", "hourglass", dict(acc="WASTING")),
    ("But not every season needs to produce a visible achievement.", "list", dict(items=["VISIBLE ACHIEVEMENT"], mode="empty", acc="NOT VISIBLE")),
    ("Sometimes…", "pulse", dict()),
    ("The most important thing happening is that you're becoming more stable.", "bricks", dict(rows=3, lbl="STABLE", uneven=False, acc="STABLE.")),
    ("More knowledgeable.", "book", dict(chapter="MORE KNOWLEDGE", acc="KNOWLEDGEABLE.")),
    ("More thoughtful.", "brain", dict(says="HMM.", acc="THOUGHTFUL.")),
    ("More prepared.", "list", dict(items=["PREPARED"], mode="check", acc="PREPARED.")),
    ("A slow season isn't automatically a wasted season.", "plant", dict(height=0.4, lbl="ROOTS GROWING", acc="SLOW ISN'T WASTED")),
    ("Don't judge the entire process by how quickly the results appear.", "timeline", dict(n=10, progress=0.3, tag="STILL GROWING", acc="DON'T QUICKLY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
