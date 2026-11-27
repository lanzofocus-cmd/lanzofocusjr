from kit import build, follow_sub

TITLE = ("YOU CAN MISS SOMETHING", "AND STILL BE OKAY")
OUTPUT = "63_You_Can_Miss_Something_And_Still_Be_Okay_16x9.mp4"
SPEC = [
    ("Not every opportunity will be yours.", "door", dict(closing=True, lbl="NOT THIS ONE", acc="NOT YOURS.")),
    ("Not every friendship will last.", "crowd", dict(n=3, highlight=1, acc="FRIENDSHIP LAST.")),
    ("Not every event will include you.", "stage", dict(acc="INCLUDE")),
    ("Not every door will open.", "door", dict(lbl="CLOSED", acc="DOOR OPEN.")),
    ("And sometimes…", "pulse", dict()),
    ("You'll feel like you missed something important.", "timeline", dict(n=8, progress=0.4, tag="MISSED IT", acc="MISSED IMPORTANT.")),
    ("But missing one opportunity doesn't mean missing your entire future.", "map", dict(a_lbl="ONE MISS", b_lbl="YOUR FUTURE", acc="ONE DOESN'T ENTIRE FUTURE.")),
    ("There are other people.", "crowd", dict(n=9, acc="OTHER PEOPLE.")),
    ("Other experiences.", "list", dict(items=["EXPERIENCE", "EXPERIENCE", "EXPERIENCE"], mode="empty", acc="EXPERIENCES.")),
    ("Other possibilities.", "network", dict(nodes=["PATH A", "PATH B", "PATH C", "PATH D", "PATH E"], tangled=False, acc="POSSIBILITIES.")),
    ("Your life isn't a single doorway…", "door", dict(lbl="ONE DOOR?", acc="ISN'T SINGLE")),
    ("Where everything depends on getting through it.", "alone", dict(tag="EVERYTHING?", acc="EVERYTHING DEPENDS")),
    ("Sometimes a door closes.", "door", dict(closing=True, lbl="CLOSED", acc="CLOSES.")),
    ("And your story continues somewhere else.", "path", dict(kind="fork", labels=("CLOSED", "SOMEWHERE ELSE"), acc="CONTINUES SOMEWHERE")),
    ("Don't let one missed opportunity convince you that opportunity itself is gone.", "sunrise", dict(acc="ONE MISSED GONE.")),
    ("Share this with someone who's struggling to move on from something they missed.", "cta", dict(kind="share", acc="SHARE MOVE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
