from kit import build, follow_sub, hook

TITLE = ("BEING BUSY VS", "BEING NEEDED")
OUTPUT = "274_The_Difference_Between_Being_Busy_And_Being_Needed_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Some people feel important because everyone needs them.", "ring", dict(tags=["NEED YOU", "NEED YOU", "NEED YOU", "NEED YOU"], acc="IMPORTANT NEEDS")),
    ("They answer every message.", "notifs", dict(items=["REPLIED", "REPLIED", "REPLIED"], acc="MESSAGE")),
    ("Solve every problem.", "list", dict(items=["SOLVE EVERY PROBLEM"], mode="check", acc="SOLVE")),
    ("Help everyone.", "list", dict(items=["SOLVE EVERY PROBLEM", "HELP EVERYONE"], mode="check", acc="HELP")),
    ("Handle everything.", "list", dict(items=["SOLVE EVERY PROBLEM", "HELP EVERYONE", "HANDLE EVERYTHING"], mode="check", acc="EVERYTHING")),
    ("And when they finally have time for themselves…", "hourglass", dict(acc="TIME THEMSELVES")),
    ("They feel guilty.", "gauge", dict(lbl="GUILT", start=0.1, end=0.8, acc="GUILTY")),
    ("Because being needed has become part of their identity.", "sticker", dict(tags=["THE HELPER", "ALWAYS AVAILABLE"], acc="NEEDED IDENTITY")),
    ("But being needed isn't the same as being valuable.", "scale", dict(left="NEEDED", right="VALUABLE", tip=0, drop=True, acc="NEEDED VALUABLE")),
    ("You can matter without constantly solving problems.", "hud", dict(lbl="YOUR WORTH", start=100, end=100, icons=None, crowd=0, tag="NO TASK REQUIRED", acc="MATTER SOLVING")),
    ("You can be a good friend without being available every second.", "list", dict(items=["AVAILABLE EVERY SECOND"], mode="strike", acc="FRIEND AVAILABLE")),
    ("You can contribute without carrying everything.", "bricks", dict(rows=2, lbl="YOUR SHARE", uneven=False, acc="CONTRIBUTE CARRYING")),
    ("And sometimes…", "pulse", dict(acc="")),
    ("People become so busy being useful to everyone else…", "battery", dict(lbl="YOU", start=0.9, end=0.05, drains=5, acc="BUSY USEFUL")),
    ("That they forget to build a life of their own.", "house", dict(progress=0.1, watchers=False, lbl="YOUR OWN LIFE", acc="BUILD LIFE OWN")),
    ("You deserve time that isn't defined by what someone else needs from you.", "hourglass", dict(acc="DESERVE TIME DEFINED")),
    ("What do you think people need to learn about being helpful without becoming overwhelmed?", "cta", dict(kind="comment", lbl="HELPFUL, NOT DRAINED", acc="HELPFUL OVERWHELMED")),
    ("", "follow"),
]
_HOOK = ("battery", dict(lbl="NEEDED BY EVERYONE", start=1.0, end=0.03, drains=5))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
