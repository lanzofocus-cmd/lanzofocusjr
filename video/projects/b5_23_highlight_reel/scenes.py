from kit import build, follow_sub

TITLE = ("WHAT DOESN'T MAKE", "THE HIGHLIGHT REEL")
OUTPUT = "163_The_Things_That_Dont_Make_The_Highlight_Reel_16x9.mp4"
SPEC = [
    ("Your life isn't only the moments worth posting.", "phone", dict(lbl="WORTH POSTING?", acc="POSTING")),
    ("It's the ordinary breakfast.", "list", dict(items=["BREAKFAST"], mode="check", acc="BREAKFAST")),
    ("The unfinished homework.", "list", dict(items=["BREAKFAST", "HOMEWORK"], mode="check", acc="HOMEWORK")),
    ("The random conversation.", "bubbles", dict(texts=["WAIT, REALLY?", "HAHA, YEAH."], acc="CONVERSATION")),
    ("The walk home.", "path", dict(kind="straight", acc="WALK HOME")),
    ("The days when absolutely nothing interesting happens.", "big", dict(text="NOTHING", sub="AND THAT'S OKAY", acc="NOTHING")),
    ("If you only value moments that look impressive…", "stage", dict(lbl="IMPRESSIVE", acc="IMPRESSIVE")),
    ("You may overlook most of your actual life.", "iceberg", dict(top="THE HIGHLIGHTS", bottom="YOUR ACTUAL LIFE", acc="OVERLOOK ACTUAL")),
    ("What's an ordinary moment you genuinely enjoy?", "frame", dict(who="AN ORDINARY MOMENT", acc="ORDINARY ENJOY")),
    ("Tell us in the comments.", "cta", dict(kind="comment", lbl="YOUR ORDINARY MOMENT", acc="COMMENTS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
