from kit import build, follow_sub

TITLE = ("THE PERSON WHO NEVER", "QUITS LEARNING")
OUTPUT = "123_The_Person_Who_Never_Quits_Learning_16x9.mp4"
SPEC = [
    ("The world changes.", "arrows", dict(items=["THE WORLD"], acc="CHANGES.")),
    ("Technology changes.", "arrows", dict(items=["THE WORLD", "TECHNOLOGY"], acc="TECHNOLOGY")),
    ("People change.", "arrows", dict(items=["THE WORLD", "TECHNOLOGY", "PEOPLE"], acc="PEOPLE")),
    ("Ideas change.", "arrows", dict(items=["THE WORLD", "TECHNOLOGY", "PEOPLE", "IDEAS"], acc="IDEAS")),
    ("And the person who believes they already know everything…", "brain", dict(says="I KNOW IT ALL.", acc="ALREADY EVERYTHING…")),
    ("Eventually stops adapting.", "chart", dict(kind="flat", lbl="ADAPTING", acc="STOPS ADAPTING.")),
    ("Learning isn't only for school.", "book", dict(chapter="NOT JUST SCHOOL", acc="ISN'T SCHOOL.")),
    ("It's a lifelong process.", "timeline", dict(n=12, progress=0.7, tag="STILL LEARNING", acc="LIFELONG")),
    ("You can learn from books.", "list", dict(items=["BOOKS"], mode="check", acc="BOOKS.")),
    ("People.", "list", dict(items=["BOOKS", "PEOPLE"], mode="check", acc="PEOPLE.")),
    ("Mistakes.", "list", dict(items=["BOOKS", "PEOPLE", "MISTAKES"], mode="check", acc="MISTAKES.")),
    ("Experiences.", "list", dict(items=["BOOKS", "PEOPLE", "MISTAKES", "EXPERIENCES"], mode="check", acc="EXPERIENCES.")),
    ("Conversations.", "list", dict(items=["BOOKS", "PEOPLE", "MISTAKES", "EXPERIENCES", "CONVERSATIONS"], mode="check", acc="CONVERSATIONS.")),
    ("Questions.", "question", dict(acc="QUESTIONS.")),
    ("And sometimes…", "pulse", dict()),
    ("From someone you initially disagreed with.", "bubbles", dict(texts=["I DISAGREE.", "...OH, I SEE."], acc="DISAGREED")),
    ("Stay curious enough to keep discovering things that challenge what you already know.", "compass", dict(lbl="CURIOSITY", acc="CURIOUS CHALLENGE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
