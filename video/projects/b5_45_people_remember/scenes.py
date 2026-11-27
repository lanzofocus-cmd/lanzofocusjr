from kit import build, follow_sub

TITLE = ("THE PEOPLE", "WHO REMEMBER")
OUTPUT = "185_The_People_Who_Remember_16x9.mp4"
SPEC = [
    ("People remember how you made them feel…", "pulse", dict(acc="REMEMBER FEEL")),
    ("But not always for the reasons you expect.", "question", dict(a_lbl="WHY", b_lbl="THEY REMEMBER", acc="REASONS EXPECT")),
    ("Sometimes it's the person who listened.", "bubbles", dict(texts=["I'M LISTENING."], acc="LISTENED")),
    ("The person who noticed.", "crowd", dict(n=7, highlight=5, highlight_label="NOTICED", acc="NOTICED")),
    ("The person who made them feel included.", "ring", dict(acc="INCLUDED")),
    ("The person who didn't make everything about themselves.", "stage", dict(lbl="NOT THE STAR", empty=True, acc="EVERYTHING THEMSELVES")),
    ("You don't need to be extraordinary to leave a meaningful impression.", "frame", dict(who="SOMEONE KIND", acc="EXTRAORDINARY MEANINGFUL")),
    ("Sometimes you just need to be genuinely present.", "alone", dict(tag="PRESENT", others=2, acc="GENUINELY PRESENT")),
    ("Share this with someone who made you feel seen when you needed it.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE SEEN")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
