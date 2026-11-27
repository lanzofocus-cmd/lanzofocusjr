from kit import build, follow_sub

TITLE = ("THE QUESTION THAT", "CHANGES EVERYTHING")
OUTPUT = "148_The_Question_That_Changes_Everything_16x9.mp4"
SPEC = [
    ("Instead of asking, \"Why is this happening to me?\"", "quote", dict(text="WHY IS THIS HAPPENING TO ME?", acc="WHY ME")),
    ("Try asking:", "arrows", dict(items=["THE QUESTION"], acc="TRY")),
    ("\"What can this situation teach me about what I do next?\"", "book", dict(chapter="WHAT NEXT?", text="LESSON", acc="TEACH NEXT")),
    ("You can't always control what happens.", "fog", dict(lbl="WHAT HAPPENS", acc="CAN'T CONTROL")),
    ("But you can change the question you're asking yourself.", "key", dict(lbl="A NEW QUESTION", acc="CHANGE QUESTION")),
    ("And sometimes a better question creates a better direction.", "compass", dict(lbl="BETTER DIRECTION", acc="BETTER QUESTION DIRECTION")),
    ("Save this.", "cta", dict(kind="save", acc="SAVE")),
    ("The question you ask during difficult moments can change the decision you make next.", "path", dict(kind="fork", labels=("WHY ME?", "WHAT NEXT?"), acc="DIFFICULT DECISION NEXT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
