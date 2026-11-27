from kit import build, follow_sub

TITLE = ("YOU'RE MORE INFLUENCED", "THAN YOU THINK")
OUTPUT = "83_Youre_More_Influenced_Than_You_Think_16x9.mp4"
SPEC = [
    ("You think your opinions are entirely your own.", "brain", dict(says="MY OPINION.", acc="ENTIRELY OWN.")),
    ("But consider where they came from.", "question", dict(acc="CAME")),
    ("The videos you watched.", "ring", dict(tags=["VIDEOS"], acc="VIDEOS")),
    ("The people you grew up around.", "ring", dict(tags=["VIDEOS", "FAMILY"], acc="GREW")),
    ("The conversations you heard.", "ring", dict(tags=["VIDEOS", "FAMILY", "CONVERSATIONS"], acc="CONVERSATIONS")),
    ("The communities you joined.", "ring", dict(tags=["VIDEOS", "FAMILY", "CONVERSATIONS", "COMMUNITIES"], acc="COMMUNITIES")),
    ("The things everyone around you considered normal.", "ring", dict(tags=["VIDEOS", "FAMILY", "CONVERSATIONS", "COMMUNITIES", "NORMAL", "NORMAL"], acc="NORMAL.")),
    ("Your beliefs didn't appear out of nowhere.", "dots", dict(connect=True, acc="DIDN'T NOWHERE.")),
    ("They were influenced.", "big", dict(text="INFLUENCED", acc="INFLUENCED.")),
    ("And that's not necessarily bad.", "scale", dict(left="GOOD", right="BAD", tip=0, acc="NOT BAD.")),
    ("But it means you should occasionally examine them.", "doc", dict(title="BELIEFS", empty=False, stamp="EXAMINED?", acc="EXAMINE")),
    ("Ask:", "pulse", dict(acc="ASK:")),
    ("\"Do I believe this because I've thought about it…", "quote", dict(text="DID I THINK THIS THROUGH?", acc="THOUGHT")),
    ("Or because I've heard it so many times that it feels true?\"", "bubbles", dict(texts=["IT'S TRUE.", "IT'S TRUE.", "IT'S TRUE.", "IT'S TRUE."], acc="HEARD MANY TRUE?\"")),
    ("Familiarity can feel like truth.", "scale", dict(left="FAMILIAR", right="TRUE", tip=0, acc="FAMILIARITY TRUTH.")),
    ("Don't let repetition replace thinking.", "brain", dict(says="THINK.", acc="REPETITION THINKING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
