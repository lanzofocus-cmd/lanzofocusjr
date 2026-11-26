from kit import build, follow_sub

TITLE = ("YOU'RE NOT ACTUALLY", "STARTING FROM ZERO")
OUTPUT = "17_Youre_Not_Actually_Starting_From_Zero_16x9.mp4"
SPEC = [
    ("You think you're starting from zero.", "big", dict(text="0", sub="YOU THINK", acc="ZERO.")),
    ("But you're starting with everything you've learned.", "bricks", dict(rows=4, lbl="EVERYTHING YOU'VE LEARNED", uneven=False, acc="EVERYTHING LEARNED.")),
    ("Every mistake.", "list", dict(items=["MISTAKE → LESSON"], mode="check", acc="MISTAKE.")),
    ("Every disappointment.", "list", dict(items=["MISTAKE → LESSON", "LETDOWN → LESSON"], mode="check", acc="DISAPPOINTMENT.")),
    ("Every time you tried something and discovered what didn't work.", "list", dict(items=["MISTAKE → LESSON", "LETDOWN → LESSON", "FAILED → LESSON"], mode="check", acc="DIDN'T WORK.")),
    ("Every experience has given you information.", "doc", dict(title="DATA", empty=False, acc="INFORMATION.")),
    ("Starting over doesn't erase your experience.", "book", dict(chapter="CHAPTER 2", text="CHAPTER 1 STILL COUNTS", acc="DOESN'T ERASE")),
    ("It changes what you do with it.", "arrows", dict(items=["EXPERIENCE"], acc="CHANGES")),
    ("So don't look at a new beginning like you've lost everything.", "startline", dict(behind=False, acc="LOST EVERYTHING.")),
    ("Look at it like you're finally building with knowledge you didn't have before.", "bricks", dict(rows=5, lbl="KNOWLEDGE", uneven=True, acc="BUILDING KNOWLEDGE")),
    ("You may be starting again…", "map", dict(a_lbl="START AGAIN", b_lbl="", acc="AGAIN…")),
    ("But you're not the same person who started the first time.", "shed", dict(old="FIRST TIME", new="NOW", acc="NOT SAME")),
    ("Follow LanzoFocus for ideas that help you see things differently.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
