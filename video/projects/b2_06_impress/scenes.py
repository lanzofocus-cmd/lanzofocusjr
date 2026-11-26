from kit import build, follow_sub

TITLE = ("STOP TRYING TO", "IMPRESS EVERYONE")
OUTPUT = "16_Stop_Trying_To_Impress_Everyone_16x9.mp4"
SPEC = [
    ("The more people you try to impress…", "stage", dict(acc="IMPRESS…")),
    ("The more people get to control your decisions.", "ring", dict(tags=["DO THIS", "WEAR THAT", "SAY THIS", "BE THAT"], acc="CONTROL DECISIONS.")),
    ("You'll change your opinions.", "arrows", dict(items=["OPINIONS"], acc="OPINIONS.")),
    ("Hide your interests.", "list", dict(items=["WHAT YOU LOVE", "WHAT YOU ENJOY"], mode="strike", acc="HIDE")),
    ("Question your choices.", "question", dict(a_lbl="YOUR CHOICE", b_lbl="THEIR CHOICE", acc="QUESTION")),
    ("And slowly become someone designed for an audience.", "stage", dict(lbl="PERFORMING", acc="DESIGNED AUDIENCE.")),
    ("But the people who genuinely respect you…", "crowd", dict(n=5, highlight=2, highlight_label="RESPECT", acc="GENUINELY RESPECT")),
    ("Won't require you to constantly perform.", "stage", dict(empty=True, performing=False, acc="WON'T PERFORM.")),
    ("You don't need to win every room.", "trophy" if False else "chairs", dict(lbl="EVERY ROOM?", acc="WIN ROOM.")),
    ("You don't need to be everyone's favorite person.", "crowd", dict(n=9, dim=True, acc="FAVORITE")),
    ("And you don't need to explain every decision.", "doc", dict(title="EXPLANATION", empty=True, stamp="NOT REQUIRED", acc="EXPLAIN")),
    ("Sometimes the most freeing thing you can do…", "key", dict(lbl="FREEDOM", acc="FREEING")),
    ("Is stop auditioning for people who were never meant to be part of your story.", "book", dict(chapter="YOUR STORY", text="NO AUDITIONS", acc="AUDITIONING STORY.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
