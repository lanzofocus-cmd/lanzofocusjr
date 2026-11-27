from kit import build, follow_sub

TITLE = ("YOUR ENVIRONMENT IS QUIETLY", "MAKING DECISIONS FOR YOU")
OUTPUT = "116_Your_Environment_Is_Quietly_Making_Decisions_16x9.mp4"
SPEC = [
    ("You think you're making every decision consciously.", "brain", dict(says="I CHOSE THIS.", acc="EVERY CONSCIOUSLY.")),
    ("But look at your environment.", "ring", dict(acc="ENVIRONMENT.")),
    ("What's easy to access?", "phone", dict(content="highlight", acc="EASY ACCESS?")),
    ("What distractions are always nearby?", "notifs", dict(items=["PING", "NEW VIDEO", "SNACKS?"], acc="DISTRACTIONS NEARBY?")),
    ("What habits are encouraged?", "path", dict(kind="straight", acc="HABITS ENCOURAGED?")),
    ("What do people around you consider normal?", "ring", dict(tags=["NORMAL", "NORMAL", "NORMAL"], acc="NORMAL?")),
    ("Your environment influences your behavior…", "arrows", dict(items=["BEHAVIOR"], acc="ENVIRONMENT BEHAVIOR…")),
    ("Before you even think about it.", "brain", dict(says="...", acc="BEFORE THINK")),
    ("Sometimes the easiest way to make a better decision…", "path", dict(kind="fork", labels=("HARD", "EASY"), acc="EASIEST BETTER")),
    ("Is to make it easier to make.", "stairs", dict(n=3, climb=1, acc="EASIER")),
    ("Remove the distraction.", "list", dict(items=["THE DISTRACTION"], mode="strike", acc="REMOVE")),
    ("Prepare what you need.", "list", dict(items=["WHAT YOU NEED"], mode="check", acc="PREPARE")),
    ("Change the surroundings.", "door", dict(open_=True, lbl="NEW SURROUNDINGS", acc="SURROUNDINGS.")),
    ("Don't rely entirely on willpower.", "gauge", dict(lbl="WILLPOWER", start=0.8, end=0.2, acc="WILLPOWER.")),
    ("Design your environment to support the person you're trying to become.", "bricks", dict(rows=4, lbl="DESIGNED FOR YOU", uneven=False, acc="DESIGN SUPPORT BECOME.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
