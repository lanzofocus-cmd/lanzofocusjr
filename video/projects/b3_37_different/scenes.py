from kit import build, follow_sub

TITLE = ("THE THINGS THAT", "MAKE YOU DIFFERENT")
OUTPUT = "77_The_Things_That_Make_You_Different_16x9.mp4"
SPEC = [
    ("You've probably spent time trying to hide something about yourself.", "shield", dict(front="HIDING", back="", acc="HIDE")),
    ("An interest.", "list", dict(items=["AN INTEREST"], mode="empty", acc="INTEREST.")),
    ("A personality trait.", "list", dict(items=["AN INTEREST", "A TRAIT"], mode="empty", acc="PERSONALITY")),
    ("A way of thinking.", "list", dict(items=["AN INTEREST", "A TRAIT", "A WAY OF THINKING"], mode="empty", acc="THINKING.")),
    ("Something you thought made you stand out too much.", "crowd", dict(n=7, highlight=3, highlight_label="DIFFERENT", acc="STAND OUT")),
    ("But imagine spending your entire life…", "timeline", dict(n=10, progress=0.8, acc="ENTIRE LIFE…")),
    ("Trying to become less noticeable…", "frame", dict(who="LESS NOTICEABLE", fade=True, acc="LESS NOTICEABLE…")),
    ("Only to realize you were hiding the very things that made you interesting.", "iceberg", dict(top="WHAT YOU SHOWED", bottom="WHAT MADE YOU INTERESTING", acc="HIDING INTERESTING.")),
    ("You don't have to turn every difference into your identity.", "sticker", dict(tags=["DIFFERENT"], acc="EVERY IDENTITY.")),
    ("You don't have to be unusual for attention.", "stage", dict(lbl="FOR ATTENTION?", acc="UNUSUAL ATTENTION.")),
    ("But you also don't have to erase yourself to fit every environment.", "frame", dict(who="ERASED?", dashed_fig=True, acc="ERASE FIT")),
    ("Belonging shouldn't require you to disappear.", "ring", dict(center_tag="STILL YOU", acc="BELONGING DISAPPEAR.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
