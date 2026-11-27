from kit import build, follow_sub

TITLE = ("WHAT IF YOU'RE WRONG", "ABOUT YOURSELF?")
OUTPUT = "59_What_If_Youre_Wrong_About_Yourself_16x9.mp4"
SPEC = [
    ("You've probably decided you're not good at something.", "sticker", dict(tags=["NOT GOOD AT IT"], acc="DECIDED NOT")),
    ("Maybe you're bad at speaking.", "list", dict(items=["SPEAKING"], mode="tag", tag="BAD AT", acc="SPEAKING.")),
    ("Bad at sports.", "list", dict(items=["SPEAKING", "SPORTS"], mode="tag", tag="BAD AT", acc="SPORTS.")),
    ("Bad at learning.", "list", dict(items=["SPEAKING", "SPORTS", "LEARNING"], mode="tag", tag="BAD AT", acc="LEARNING.")),
    ("Bad at making friends.", "list", dict(items=["SPEAKING", "SPORTS", "LEARNING", "FRIENDS"], mode="tag", tag="BAD AT", acc="FRIENDS.")),
    ("But when did you decide?", "question", dict(acc="WHEN DECIDE?")),
    ("After one attempt?", "timeline", dict(n=10, progress=0.1, tag="ATTEMPT 1", acc="ONE ATTEMPT?")),
    ("A few embarrassing moments?", "stage", dict(lbl="EMBARRASSED", performing=False, acc="EMBARRASSING")),
    ("Someone else's opinion?", "bubbles", dict(texts=["YOU'RE BAD AT THIS."], acc="OPINION?")),
    ("Or after genuinely giving yourself the time to improve?", "stairs", dict(n=6, climb=4, acc="GENUINELY IMPROVE?")),
    ("Sometimes…", "pulse", dict()),
    ("The labels we place on ourselves are based on very little evidence.", "doc", dict(title="EVIDENCE", empty=True, acc="LABELS LITTLE EVIDENCE.")),
    ("We turn a temporary struggle…", "chart", dict(kind="invest", lbl="A STRUGGLE", acc="TEMPORARY STRUGGLE…")),
    ("Into a permanent identity.", "sticker", dict(tags=["BAD AT THIS"], acc="PERMANENT IDENTITY.")),
    ("\"I struggled with this.\"", "quote", dict(text="I STRUGGLED WITH THIS.", acc="STRUGGLED")),
    ("Becomes…", "pulse", dict(acc="BECOMES…")),
    ("\"I'm bad at this.\"", "quote", dict(text="I'M BAD AT THIS.", acc="BAD")),
    ("And that tiny change can influence everything that happens afterward.", "path", dict(kind="fork", labels=("I STRUGGLED", "I'M BAD"), acc="TINY EVERYTHING")),
    ("Before accepting a label…", "sticker", dict(tags=["LABEL?"], acc="LABEL…")),
    ("Make sure you've given yourself enough evidence to deserve it.", "doc", dict(title="EVIDENCE", empty=True, stamp="NOT ENOUGH", acc="ENOUGH EVIDENCE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
