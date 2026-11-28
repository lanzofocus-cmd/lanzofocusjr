from kit import build, follow_sub, hook

TITLE = ("DOING SOMETHING", "WITHOUT POSTING IT")
OUTPUT = "223_The_Value_Of_Doing_Something_Without_Posting_It_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine accomplishing something…", "crown", dict(lbl="DONE", acc="ACCOMPLISHING")),
    ("And nobody knows.", "chairs", dict(n=6, lbl="NOBODY KNOWS", acc="NOBODY")),
    ("You learn something.", "book", dict(chapter="LEARNED", acc="LEARN")),
    ("You improve.", "chart", dict(kind="up", lbl="YOU", acc="IMPROVE")),
    ("You finish a project.", "doc", dict(title="PROJECT", empty=False, stamp="DONE", acc="PROJECT")),
    ("You help someone.", "crowd", dict(n=3, highlight=1, highlight_label="HELPED", acc="HELP")),
    ("You create something meaningful.", "bricks", dict(rows=4, lbl="MEANINGFUL", uneven=False, acc="MEANINGFUL")),
    ("But you don't post it.", "list", dict(items=["POST IT"], mode="strike", acc="POST")),
    ("You don't announce it.", "list", dict(items=["POST IT", "ANNOUNCE IT"], mode="strike", acc="ANNOUNCE")),
    ("You don't take a picture.", "list", dict(items=["POST IT", "ANNOUNCE IT", "TAKE A PICTURE"], mode="strike", acc="PICTURE")),
    ("You don't turn it into content.", "list", dict(items=["POST IT", "ANNOUNCE IT", "TAKE A PICTURE", "MAKE CONTENT"], mode="strike", acc="CONTENT")),
    ("And the accomplishment still exists.", "crown", dict(lbl="STILL REAL", drop=True, acc="STILL EXISTS")),
    ("This is important because social media can quietly teach us to experience life through the expectation of sharing it.", "phone", dict(lbl="LIVING FOR THE POST", acc="SOCIAL QUIETLY SHARING")),
    ("We begin thinking about the post before the moment.", "timeline", dict(n=6, progress=0.2, tag="THE POST FIRST", acc="POST MOMENT")),
    ("The picture before the experience.", "frame", dict(who="THE PICTURE", acc="PICTURE EXPERIENCE")),
    ("The reaction before the achievement.", "hud", dict(lbl="LIKES", start=0, end=80, icons="heart", acc="REACTION ACHIEVEMENT")),
    ("But not everything needs an audience.", "stage", dict(lbl="NO AUDIENCE", empty=True, acc="AUDIENCE")),
    ("Some experiences can belong entirely to you.", "key", dict(lbl="YOURS", acc="BELONG ENTIRELY")),
    ("Some progress can remain private.", "progress", dict(lbl="PRIVATE PROGRESS", value=0.6, invisible=True, acc="PRIVATE")),
    ("Some moments become more meaningful when you're not trying to capture them for someone else.", "sunrise", dict(acc="MEANINGFUL CAPTURE")),
    ("What's something you enjoy doing even when nobody sees it?", "alone", dict(tag="JUST FOR ME", acc="ENJOY NOBODY")),
    ("Share it.", "cta", dict(kind="comment", lbl="YOUR UNPOSTED JOY", acc="SHARE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="POSTED", start=0, end=0, lbl2="STILL MATTERS", start2=10, end2=100, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
