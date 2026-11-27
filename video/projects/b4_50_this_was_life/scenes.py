from kit import build, follow_sub

TITLE = ("ONE DAY, YOU'LL REALIZE", "THIS WAS YOUR LIFE")
OUTPUT = "140_One_Day_Youll_Realize_This_Was_Your_Life_16x9.mp4"
SPEC = [
    ("You keep waiting for the big moment.", "hourglass", dict(acc="BIG MOMENT.")),
    ("The achievement.", "list", dict(items=["THE ACHIEVEMENT"], mode="empty", acc="ACHIEVEMENT.")),
    ("The breakthrough.", "list", dict(items=["THE ACHIEVEMENT", "THE BREAKTHROUGH"], mode="empty", acc="BREAKTHROUGH.")),
    ("The day everything finally feels complete.", "puzzle", dict(missing=False, lbl="COMPLETE?", acc="COMPLETE.")),
    ("But look around.", "ring", dict(acc="LOOK AROUND.")),
    ("This is your life.", "big", dict(text="THIS", sub="IS YOUR LIFE", acc="YOUR LIFE.")),
    ("The ordinary day.", "big", dict(text="TUESDAY", sub="JUST ANOTHER DAY", acc="ORDINARY DAY.")),
    ("The conversations.", "bubbles", dict(texts=["HOW WAS YOUR DAY?", "PRETTY GOOD."], acc="CONVERSATIONS.")),
    ("The responsibilities.", "list", dict(items=["RESPONSIBILITIES"], mode="check", acc="RESPONSIBILITIES.")),
    ("The small decisions.", "path", dict(kind="fork", labels=("LEFT", "RIGHT"), acc="SMALL DECISIONS.")),
    ("The people currently beside you.", "crowd", dict(n=4, acc="BESIDE")),
    ("The things you're learning.", "book", dict(chapter="LEARNING", acc="LEARNING.")),
    ("The experiences you're having.", "dots", dict(connect=False, acc="EXPERIENCES")),
    ("You may be waiting for life to begin…", "startline", dict(behind=False, acc="WAITING BEGIN…")),
    ("While life is already happening.", "pulse", dict(acc="ALREADY HAPPENING.")),
    ("And one day…", "sunrise", dict(acc="ONE DAY…")),
    ("You'll look back at this exact period.", "timeline", dict(n=10, progress=0.5, tag="THIS PERIOD", acc="EXACT PERIOD.")),
    ("You'll remember things you currently overlook.", "frame", dict(who="OVERLOOKED", acc="REMEMBER OVERLOOK.")),
    ("You'll miss moments you thought were ordinary.", "frame", dict(who="AN ORDINARY MOMENT", new="YOU, LATER", acc="MISS ORDINARY.")),
    ("You'll wish you could return…", "map", dict(a_lbl="THEN", b_lbl="NOW", acc="RETURN…")),
    ("Not to change everything.", "list", dict(items=["CHANGE EVERYTHING"], mode="strike", acc="NOT CHANGE")),
    ("But simply to experience it again.", "pulse", dict(acc="EXPERIENCE AGAIN.")),
    ("So don't spend your entire life waiting for a better chapter.", "book", dict(chapter="A BETTER CHAPTER?", acc="WAITING BETTER CHAPTER.")),
    ("Pay attention to the one you're living.", "book", dict(chapter="THIS CHAPTER", text="YOU ARE HERE", acc="ATTENTION LIVING.")),
    ("If this made you think of someone, share it with them.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE")),
    ("And save this video for a day when you need the reminder.", "cta", dict(kind="save", acc="SAVE REMINDER.")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
