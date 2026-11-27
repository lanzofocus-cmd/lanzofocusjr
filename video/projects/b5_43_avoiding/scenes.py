from kit import build, follow_sub

TITLE = ("THE THING", "YOU'RE AVOIDING")
OUTPUT = "183_The_Thing_Youre_Avoiding_16x9.mp4"
SPEC = [
    ("The thing you're avoiding may not be as difficult as you imagine.", "iceberg", dict(top="REALITY", bottom="WHAT YOU IMAGINE", acc="AVOIDING DIFFICULT IMAGINE")),
    ("But uncertainty makes it look bigger.", "fog", dict(lbl="UNCERTAINTY", acc="UNCERTAINTY BIGGER")),
    ("The message.", "list", dict(items=["THE MESSAGE"], mode="empty", acc="MESSAGE")),
    ("The conversation.", "list", dict(items=["THE MESSAGE", "THE CONVERSATION"], mode="empty", acc="CONVERSATION")),
    ("The application.", "list", dict(items=["THE MESSAGE", "THE CONVERSATION", "THE APPLICATION"], mode="empty", acc="APPLICATION")),
    ("The first attempt.", "list", dict(items=["THE MESSAGE", "THE CONVERSATION", "THE APPLICATION", "THE FIRST ATTEMPT"], mode="empty", acc="FIRST ATTEMPT")),
    ("Your mind creates an entire story about what might happen.", "brain", dict(says="WHAT IF THEY...", says2="AND THEN...", acc="ENTIRE STORY")),
    ("Then you live inside that story instead of finding out.", "cage", dict(words=["WHAT IF", "MAYBE"], acc="INSIDE STORY FINDING")),
    ("Sometimes clarity only comes after you stop avoiding the question.", "door", dict(open_=True, lbl="FIND OUT", acc="CLARITY AVOIDING")),
    ("Comment one thing you've been avoiding.", "cta", dict(kind="comment", lbl="NAME IT", acc="AVOIDING")),
    ("Naming it is the first step toward dealing with it.", "stairs", dict(n=6, climb=1, acc="NAMING FIRST STEP")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
