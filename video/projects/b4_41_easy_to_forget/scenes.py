from kit import build, follow_sub

TITLE = ("THE THINGS THAT ARE", "EASY TO FORGET")
OUTPUT = "131_The_Things_That_Are_Easy_To_Forget_16x9.mp4"
SPEC = [
    ("You forget how much you've learned.", "chart", dict(kind="up", lbl="WHAT YOU'VE LEARNED", acc="FORGET LEARNED.")),
    ("How much you've changed.", "shed", dict(old="BEFORE", new="NOW", acc="CHANGED.")),
    ("How many problems you've already solved.", "list", dict(items=["SOLVED", "SOLVED", "SOLVED", "SOLVED"], mode="check", acc="ALREADY SOLVED.")),
    ("Because you're focused on the next challenge.", "stairs", dict(n=6, climb=3, highlight=4, acc="NEXT CHALLENGE.")),
    ("But your mind naturally notices what's missing.", "puzzle", dict(missing=True, lbl="WHAT'S MISSING", acc="NOTICES MISSING.")),
    ("The unfinished goal.", "list", dict(items=["UNFINISHED GOAL"], mode="empty", acc="UNFINISHED")),
    ("The remaining work.", "progress", dict(lbl="REMAINING", value=0.6, acc="REMAINING")),
    ("The next obstacle.", "bricks", dict(rows=2, lbl="NEXT OBSTACLE", uneven=True, acc="OBSTACLE.")),
    ("So occasionally…", "pulse", dict()),
    ("Look backward.", "timeline", dict(n=10, progress=0.7, tag="LOOK BACK", acc="BACKWARD.")),
    ("Not to live in the past.", "frame", dict(who="THE PAST", acc="NOT PAST.")),
    ("But to recognize the progress you might otherwise overlook.", "map", dict(a_lbl="WHERE YOU STARTED", b_lbl="HERE", acc="RECOGNIZE PROGRESS OVERLOOK.")),
    ("You don't need to be finished to appreciate how far you've come.", "progress", dict(lbl="NOT FINISHED, STILL FAR", value=0.65, acc="FINISHED APPRECIATE FAR")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
