from kit import build, follow_sub

TITLE = ("THE MOMENT YOU STOP", "NEEDING TO EXPLAIN")
OUTPUT = "72_The_Moment_You_Stop_Needing_To_Explain_16x9.mp4"
SPEC = [
    ("You don't owe everyone a detailed explanation of your life.", "doc", dict(title="EXPLANATION", empty=True, stamp="NOT OWED", acc="DON'T OWE")),
    ("Why you changed.", "bubbles", dict(texts=["WHY'D YOU CHANGE?"], acc="CHANGED.")),
    ("Why you left.", "bubbles", dict(texts=["WHY'D YOU CHANGE?", "WHY'D YOU LEAVE?"], acc="LEFT.")),
    ("Why you chose differently.", "bubbles", dict(texts=["WHY'D YOU CHANGE?", "WHY'D YOU LEAVE?", "WHY THAT?"], acc="DIFFERENTLY.")),
    ("Why you don't want something anymore.", "bubbles", dict(texts=["WHY'D YOU CHANGE?", "WHY'D YOU LEAVE?", "WHY THAT?", "WHY NOT?"], acc="ANYMORE.")),
    ("Why you're pursuing something new.", "door", dict(open_=True, lbl="SOMETHING NEW", acc="NEW.")),
    ("Some people ask because they genuinely want to understand.", "bubbles", dict(texts=["HELP ME UNDERSTAND."], inverted=True, acc="GENUINELY UNDERSTAND.")),
    ("Others ask because they expect you to justify yourself.", "bubbles", dict(texts=["JUSTIFY THAT."], acc="JUSTIFY")),
    ("Learn the difference.", "scale", dict(left="CURIOUS", right="DEMANDING", tip=0, acc="DIFFERENCE.")),
    ("You can communicate honestly…", "quote", dict(text="HERE'S WHAT I DECIDED.", acc="HONESTLY…")),
    ("Without turning every personal decision into a debate.", "list", dict(items=["DEBATE EVERYTHING"], mode="strike", acc="DEBATE.")),
    ("An explanation can provide clarity.", "doc", dict(title="CLARITY", empty=False, acc="CLARITY.")),
    ("But you don't need permission to make every decision.", "doc", dict(title="PERMISSION", empty=True, stamp="NOT NEEDED", acc="DON'T PERMISSION")),
    ("Save this reminder for when you feel pressured to justify yourself.", "cta", dict(kind="save", acc="SAVE PRESSURED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
