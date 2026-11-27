from kit import build, follow_sub

TITLE = ("THE UNFINISHED", "SENTENCE")
OUTPUT = "156_The_Unfinished_Sentence_16x9.mp4"
SPEC = [
    ("Some of the biggest decisions in your life begin with an unfinished sentence.", "doc", dict(title="SOMEDAY", empty=True, acc="BIGGEST UNFINISHED SENTENCE")),
    ("\"I wish I could…\"", "quote", dict(text="I WISH I COULD...", acc="WISH")),
    ("\"I've always wanted to…\"", "quote", dict(text="I'VE ALWAYS WANTED TO...", acc="ALWAYS WANTED")),
    ("\"Maybe someday…\"", "quote", dict(text="MAYBE SOMEDAY...", acc="SOMEDAY")),
    ("The sentence stays unfinished because finishing it would require you to admit what you actually want.", "lock", dict(lbl="WHAT YOU WANT", acc="ADMIT WANT")),
    ("And admitting what you want can be uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.75, acc="UNCOMFORTABLE")),
    ("But you can't move toward a destination you refuse to name.", "map", dict(a_lbl="YOU", b_lbl="?", acc="DESTINATION NAME")),
    ("Finish the sentence in the comments: \"I've always wanted to…\"", "cta", dict(kind="comment", lbl="I'VE ALWAYS WANTED TO...", acc="FINISH SENTENCE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
