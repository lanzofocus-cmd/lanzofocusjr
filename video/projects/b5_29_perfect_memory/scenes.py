from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH", "PERFECT MEMORY")
OUTPUT = "169_The_Problem_With_Perfect_Memory_16x9.mp4"
SPEC = [
    ("Your memory isn't a perfect recording.", "frame", dict(who="THE MEMORY", acc="MEMORY PERFECT")),
    ("It changes.", "frame", dict(who="THE MEMORY", dashed_fig=True, acc="CHANGES")),
    ("It emphasizes certain details.", "puzzle", dict(missing=False, lbl="SOME DETAILS", acc="EMPHASIZES")),
    ("It forgets others.", "puzzle", dict(missing=True, lbl="MISSING PIECES", acc="FORGETS")),
    ("Sometimes you remember how something made you feel…", "pulse", dict(acc="REMEMBER FEEL")),
    ("And confuse that feeling with the entire event.", "iceberg", dict(top="THE FEELING", bottom="THE WHOLE EVENT", acc="CONFUSE ENTIRE")),
    ("That's why it's important to question your own version of the story.", "book", dict(chapter="YOUR VERSION", text="?", acc="QUESTION VERSION")),
    ("Not everything you remember is everything that happened.", "frame", dict(who="WHAT YOU REMEMBER", fade=True, acc="REMEMBER HAPPENED")),
    ("Comment \"PERSPECTIVE\" if you've ever realized your memory of a situation was incomplete.", "cta", dict(kind="comment", lbl="COMMENT \"PERSPECTIVE\"", acc="PERSPECTIVE INCOMPLETE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
