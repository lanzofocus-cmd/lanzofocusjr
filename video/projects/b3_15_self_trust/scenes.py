from kit import build, follow_sub

TITLE = ("YOU MAY BE THE REASON", "YOU DON'T TRUST YOURSELF")
OUTPUT = "55_You_May_Be_The_Reason_You_Dont_Trust_Yourself_16x9.mp4"
SPEC = [
    ("You keep making promises to yourself.", "doc", dict(title="PROMISE", empty=False, acc="PROMISES YOURSELF.")),
    ("Tomorrow.", "list", dict(items=["TOMORROW"], mode="empty", acc="TOMORROW.")),
    ("Next week.", "list", dict(items=["TOMORROW", "NEXT WEEK"], mode="empty", acc="WEEK.")),
    ("After this.", "list", dict(items=["TOMORROW", "NEXT WEEK", "AFTER THIS"], mode="empty", acc="AFTER")),
    ("Once things settle down.", "list", dict(items=["TOMORROW", "NEXT WEEK", "AFTER THIS", "WHEN IT SETTLES"], mode="empty", acc="SETTLE")),
    ("And then…", "pulse", dict()),
    ("You break those promises.", "list", dict(items=["TOMORROW", "NEXT WEEK", "AFTER THIS", "WHEN IT SETTLES"], mode="strike", acc="BREAK")),
    ("Again.", "big", dict(text="AGAIN", acc="AGAIN.")),
    ("Eventually, something changes.", "gauge", dict(lbl="SELF-TRUST", start=0.7, end=0.2, acc="CHANGES.")),
    ("You stop believing your own words.", "quote", dict(text="I'LL START TOMORROW.", acc="STOP BELIEVING")),
    ("Not because you're incapable.", "sticker", dict(tags=["INCAPABLE"], strike=True, acc="NOT INCAPABLE.")),
    ("But because you've repeatedly taught yourself that your promises don't mean much.", "doc", dict(title="PROMISE", empty=False, stamp="BROKEN", acc="TAUGHT DON'T")),
    ("The solution isn't making bigger promises.", "big", dict(text="BIGGER?", acc="ISN'T BIGGER")),
    ("It's making smaller ones…", "list", dict(items=["ONE SMALL PROMISE"], mode="empty", acc="SMALLER")),
    ("And keeping them.", "list", dict(items=["ONE SMALL PROMISE"], mode="check", acc="KEEPING")),
    ("Don't promise yourself you'll transform your entire life tomorrow.", "list", dict(items=["TRANSFORM EVERYTHING"], mode="strike", acc="TRANSFORM ENTIRE")),
    ("Promise yourself you'll do one meaningful thing today.", "list", dict(items=["ONE MEANINGFUL THING"], mode="empty", acc="ONE MEANINGFUL TODAY.")),
    ("Then do it.", "list", dict(items=["ONE MEANINGFUL THING"], mode="check", acc="DO")),
    ("Self-trust isn't built by what you say you'll do.", "bubbles", dict(texts=["I WILL.", "I PROMISE."], acc="SELF-TRUST SAY")),
    ("It's built by what you actually do.", "bricks", dict(rows=4, lbl="SELF-TRUST", uneven=False, acc="ACTUALLY DO.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
