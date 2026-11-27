from kit import build, follow_sub

TITLE = ("YOUR LIFE IS MADE OF", "THINGS YOU DON'T NOTICE")
OUTPUT = "46_Your_Life_Is_Made_Of_Things_You_Dont_Notice_16x9.mp4"
SPEC = [
    ("You keep waiting for the important moments.", "hourglass", dict(acc="IMPORTANT")),
    ("The graduation.", "list", dict(items=["THE GRADUATION"], mode="empty", acc="GRADUATION.")),
    ("The achievement.", "list", dict(items=["THE GRADUATION", "THE ACHIEVEMENT"], mode="empty", acc="ACHIEVEMENT.")),
    ("The big opportunity.", "list", dict(items=["THE GRADUATION", "THE ACHIEVEMENT", "THE BIG BREAK"], mode="empty", acc="BIG OPPORTUNITY.")),
    ("The day everything changes.", "sunrise", dict(acc="EVERYTHING CHANGES.")),
    ("But your life is mostly made of moments that don't look important.", "dots", dict(connect=False, n=12, acc="MOSTLY DON'T")),
    ("A random conversation.", "bubbles", dict(texts=["HEY, HOW ARE YOU?"], acc="RANDOM CONVERSATION.")),
    ("A quiet afternoon.", "sunrise", dict(acc="QUIET AFTERNOON.")),
    ("A small decision.", "path", dict(kind="fork", labels=("LEFT", "RIGHT"), acc="SMALL DECISION.")),
    ("An ordinary Tuesday.", "big", dict(text="TUESDAY", sub="JUST ANOTHER DAY", acc="ORDINARY TUESDAY.")),
    ("You don't notice them because they don't announce themselves.", "chairs", dict(lbl="NO ANNOUNCEMENT", acc="DON'T ANNOUNCE")),
    ("But look back at your life…", "timeline", dict(n=10, progress=0.9, tag="LOOK BACK", acc="LOOK BACK")),
    ("And some of your most meaningful memories probably began as ordinary moments.", "dots", dict(connect=True, n=10, acc="MEANINGFUL ORDINARY")),
    ("That's the strange thing about life.", "big", dict(text="STRANGE", acc="STRANGE")),
    ("The moments that become important rarely tell you they're important while you're living them.", "frame", dict(who="JUST A MOMENT", acc="RARELY LIVING")),
    ("Pay attention.", "compass", dict(lbl="ATTENTION", acc="ATTENTION.")),
    ("You might already be living inside a memory you'll miss someday.", "frame", dict(who="SOMEDAY'S MEMORY", new="YOU, NOW", acc="ALREADY MEMORY MISS")),
    ("Share this with someone you want to appreciate a little more.", "cta", dict(kind="share", acc="SHARE APPRECIATE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
