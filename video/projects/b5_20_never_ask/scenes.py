from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO", "NEVER ASK")
OUTPUT = "160_The_People_Who_Never_Ask_16x9.mp4"
SPEC = [
    ("Some people will judge your decisions without ever asking why you made them.", "crowd", dict(n=7, highlight=3, highlight_label="YOU", acc="JUDGE WITHOUT WHY")),
    ("They'll see the result.", "iceberg", dict(top="THE RESULT", bottom="THE SITUATION", acc="RESULT")),
    ("Not the situation.", "iceberg", dict(top="THE RESULT", bottom="THE SITUATION", acc="SITUATION")),
    ("The choice.", "iceberg", dict(top="THE CHOICE", bottom="THE OPTIONS YOU HAD", acc="CHOICE")),
    ("Not the options you had.", "iceberg", dict(top="THE CHOICE", bottom="THE OPTIONS YOU HAD", acc="OPTIONS")),
    ("The outcome.", "iceberg", dict(top="THE OUTCOME", bottom="THE FULL STORY", acc="OUTCOME")),
    ("Remember that criticism can be confident and still be incomplete.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="CONFIDENT INCOMPLETE")),
    ("You don't have to explain your entire life to someone who only sees one chapter.", "book", dict(chapter="ONE CHAPTER", acc="EXPLAIN ONE CHAPTER")),
    ("Share this with someone who's been judged by people who don't know the full story.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE FULL STORY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
