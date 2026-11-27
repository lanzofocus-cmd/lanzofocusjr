from kit import build, follow_sub

TITLE = ("THE NEXT CHAPTER", "DOESN'T NEED PERMISSION")
OUTPUT = "186_The_Next_Chapter_Doesnt_Need_Permission_16x9.mp4"
SPEC = [
    ("You don't need everyone to understand your next chapter.", "book", dict(chapter="NEXT CHAPTER", acc="EVERYONE NEXT CHAPTER")),
    ("Some people only know the previous one.", "frame", dict(who="THE OLD YOU", acc="PREVIOUS")),
    ("They may be confused.", "question", dict(a_lbl="WAIT,", b_lbl="WHAT?", acc="CONFUSED")),
    ("They may disagree.", "bubbles", dict(texts=["I DON'T THINK SO."], acc="DISAGREE")),
    ("They may question the change.", "bubbles", dict(texts=["I DON'T THINK SO.", "WHY CHANGE?"], acc="QUESTION CHANGE")),
    ("But growth isn't always recognizable to people who haven't seen what you've been thinking about.", "iceberg", dict(top="THE CHANGE", bottom="WHAT YOU'VE BEEN THINKING", acc="GROWTH RECOGNIZABLE THINKING")),
    ("You can move forward without waiting for unanimous approval.", "path", dict(kind="straight", acc="FORWARD UNANIMOUS APPROVAL")),
    ("Save this if you're making a change that not everyone understands.", "cta", dict(kind="save", lbl="KEEP GOING", acc="SAVE CHANGE UNDERSTANDS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
