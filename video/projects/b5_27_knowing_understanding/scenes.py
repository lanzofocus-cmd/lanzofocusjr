from kit import build, follow_sub

TITLE = ("KNOWING VS", "UNDERSTANDING")
OUTPUT = "167_The_Difference_Between_Knowing_And_Understanding_16x9.mp4"
SPEC = [
    ("You can know something…", "book", dict(chapter="ADVICE", acc="KNOW")),
    ("Without understanding it.", "fog", dict(lbl="UNDERSTANDING", acc="UNDERSTANDING")),
    ("You can hear advice.", "bubbles", dict(texts=["HERE'S A TIP."], acc="ADVICE")),
    ("Read a quote.", "quote", dict(text="JUST START.", acc="QUOTE")),
    ("Watch a video.", "phone", dict(lbl="WATCHED", acc="VIDEO")),
    ("And still never apply the lesson.", "list", dict(items=["APPLY THE LESSON"], mode="empty", acc="NEVER APPLY")),
    ("Understanding begins when the idea changes the way you behave.", "shed", dict(old="KNEW IT", new="LIVED IT", acc="UNDERSTANDING BEHAVE")),
    ("Knowledge that never reaches your decisions remains information.", "map", dict(a_lbl="KNOWLEDGE", b_lbl="DECISIONS", acc="KNOWLEDGE DECISIONS INFORMATION")),
    ("Share this with someone who collects advice but needs to start applying it.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE APPLYING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
