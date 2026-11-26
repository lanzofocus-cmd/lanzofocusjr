from kit import build, follow_sub

TITLE = ("READ THIS BEFORE", "YOU GIVE UP")
OUTPUT = "05_Read_This_Before_You_Give_Up_16x9.mp4"
SPEC = [
    ("The hardest part isn't always starting.", "startline", dict(behind=False, acc="HARDEST")),
    ("Sometimes…", "pulse", dict()),
    ("It's continuing after nobody cares.", "chairs", dict(lbl="NOBODY'S CLAPPING", acc="CONTINUING NOBODY")),
    ("When the results are invisible.", "progress", dict(lbl="RESULTS", value=0.05, invisible=True, acc="INVISIBLE.")),
    ("When your progress feels embarrassingly slow.", "timeline", dict(n=10, progress=0.12, tag="STILL HERE", acc="SLOW.")),
    ("When you've worked for something…", "list", dict(items=["SHOWED UP", "PUT IN THE HOURS", "KEPT GOING"], mode="check", acc="WORKED")),
    ("And it still hasn't happened.", "doc", dict(title="RESULTS", empty=True, stamp="NOT YET", acc="STILL")),
    ("That's when most people begin questioning everything.", "crowd", dict(n=9, highlight=4, highlight_label="WHY BOTHER?", acc="QUESTIONING")),
    ("But slow progress isn't proof that you're failing.", "plant", dict(height=0.15, acc="ISN'T PROOF")),
    ("Sometimes you're simply in the part of the story…", "book", dict(chapter="CHAPTER 2", acc="STORY…")),
    ("Where nothing looks impressive yet.", "plant", dict(height=0.25, lbl="ROOTS GROWING", acc="YET.")),
    ("Don't mistake a quiet chapter…", "book", dict(chapter="A QUIET CHAPTER", acc="QUIET")),
    ("For the end of your story.", "book", dict(chapter="NOT THE END", text="KEEP WRITING", acc="END")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
