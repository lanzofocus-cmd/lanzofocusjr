from kit import build, follow_sub

TITLE = ("YOU DON'T HAVE TO BE", "INTERESTING ALL THE TIME")
OUTPUT = "114_You_Dont_Have_To_Be_Interesting_All_The_Time_16x9.mp4"
SPEC = [
    ("You don't have to constantly entertain people.", "stage", dict(acc="CONSTANTLY ENTERTAIN")),
    ("You don't have to always have something funny to say.", "bubbles", dict(texts=["HAHA", "SO FUNNY"], acc="FUNNY")),
    ("You don't have to be the loudest person.", "gauge", dict(lbl="VOLUME", start=0.9, end=0.3, acc="LOUDEST")),
    ("The most exciting.", "list", dict(items=["MOST EXCITING"], mode="strike", acc="EXCITING.")),
    ("The most memorable.", "list", dict(items=["MOST EXCITING", "MOST MEMORABLE"], mode="strike", acc="MEMORABLE.")),
    ("Sometimes…", "pulse", dict()),
    ("You can simply exist.", "alone", dict(acc="SIMPLY EXIST.")),
    ("Listen.", "list", dict(items=["LISTEN"], mode="check", acc="LISTEN.")),
    ("Enjoy.", "list", dict(items=["LISTEN", "ENJOY"], mode="check", acc="ENJOY.")),
    ("Be quiet.", "list", dict(items=["LISTEN", "ENJOY", "BE QUIET"], mode="check", acc="QUIET.")),
    ("Not every interaction needs to be impressive.", "crowd", dict(n=3, acc="NOT IMPRESSIVE.")),
    ("Not every moment needs to become a story.", "book", dict(chapter="NOT A STORY", acc="NOT STORY.")),
    ("You don't have to perform a personality to deserve company.", "stage", dict(empty=True, performing=False, acc="PERFORM DESERVE COMPANY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
