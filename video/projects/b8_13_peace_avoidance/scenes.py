from kit import build, follow_sub, hook

TITLE = ("PEACE IS NOT", "AVOIDANCE")
OUTPUT = "263_Why_You_Should_Not_Confuse_Peace_With_Avoidance_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes people say they want peace…", "sunrise", dict(acc="PEACE")),
    ("But what they really want is to avoid anything uncomfortable.", "door", dict(closing=True, lbl="UNCOMFORTABLE", acc="AVOID UNCOMFORTABLE")),
    ("They don't want difficult conversations.", "list", dict(items=["HARD CONVERSATIONS"], mode="strike", acc="CONVERSATIONS")),
    ("They don't want feedback.", "list", dict(items=["HARD CONVERSATIONS", "FEEDBACK"], mode="strike", acc="FEEDBACK")),
    ("They don't want disagreements.", "list", dict(items=["HARD CONVERSATIONS", "FEEDBACK", "DISAGREEMENTS"], mode="strike", acc="DISAGREEMENTS")),
    ("They don't want to admit mistakes.", "list", dict(items=["HARD CONVERSATIONS", "FEEDBACK", "DISAGREEMENTS", "ADMITTING MISTAKES"], mode="strike", acc="MISTAKES")),
    ("They don't want to face problems.", "list", dict(items=["HARD CONVERSATIONS", "FEEDBACK", "DISAGREEMENTS", "ADMITTING MISTAKES", "FACING PROBLEMS"], mode="strike", acc="PROBLEMS")),
    ("But avoiding discomfort doesn't automatically create peace.", "scale", dict(left="AVOIDANCE", right="PEACE", tip=0, acc="AVOIDING PEACE")),
    ("Sometimes it simply delays the problem.", "hourglass", dict(acc="DELAYS")),
    ("A misunderstanding remains.", "list", dict(items=["MISUNDERSTANDING"], mode="tag", tag="STILL HERE", acc="MISUNDERSTANDING REMAINS")),
    ("A responsibility remains.", "list", dict(items=["MISUNDERSTANDING", "RESPONSIBILITY"], mode="tag", tag="STILL HERE", acc="RESPONSIBILITY")),
    ("A decision remains.", "list", dict(items=["MISUNDERSTANDING", "RESPONSIBILITY", "DECISION"], mode="tag", tag="STILL HERE", acc="DECISION")),
    ("And eventually, the thing you avoided becomes even more difficult.", "bricks", dict(rows=6, lbl="HARDER NOW", uneven=True, acc="AVOIDED DIFFICULT")),
    ("Real peace isn't always the absence of difficult situations.", "list", dict(items=["NO DIFFICULT SITUATIONS"], mode="strike", acc="REAL ABSENCE")),
    ("Sometimes it's the result of dealing with them properly.", "key", dict(lbl="DEALT WITH", drop=True, acc="RESULT DEALING PROPERLY")),
    ("Communicating.", "list", dict(items=["COMMUNICATE"], mode="check", acc="COMMUNICATING")),
    ("Setting boundaries.", "list", dict(items=["COMMUNICATE", "SET BOUNDARIES"], mode="check", acc="BOUNDARIES")),
    ("Taking responsibility.", "list", dict(items=["COMMUNICATE", "SET BOUNDARIES", "TAKE RESPONSIBILITY"], mode="check", acc="RESPONSIBILITY")),
    ("Making decisions.", "list", dict(items=["COMMUNICATE", "SET BOUNDARIES", "TAKE RESPONSIBILITY", "DECIDE"], mode="check", acc="DECISIONS")),
    ("Accepting things you cannot control.", "list", dict(items=["COMMUNICATE", "SET BOUNDARIES", "TAKE RESPONSIBILITY", "DECIDE", "ACCEPT"], mode="check", acc="ACCEPTING CONTROL")),
    ("You don't need to create unnecessary conflict.", "list", dict(items=["UNNECESSARY CONFLICT"], mode="strike", acc="UNNECESSARY CONFLICT")),
    ("But you shouldn't confuse avoiding every uncomfortable moment with living peacefully.", "iceberg", dict(top="LOOKS PEACEFUL", bottom="AVOIDED PROBLEMS", acc="CONFUSE AVOIDING PEACEFULLY")),
    ("Sometimes the path toward peace requires you to address what you've been avoiding.", "path", dict(kind="straight", acc="PATH PEACE ADDRESS")),
    ("What is the difference between protecting your peace and avoiding responsibility?", "scale", dict(left="PROTECTING PEACE", right="AVOIDING", tip=0, acc="PROTECTING AVOIDING")),
    ("Share your thoughts.", "cta", dict(kind="comment", lbl="WHERE'S THE LINE?", acc="SHARE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="LOOKS PEACEFUL", start=20, end=100, lbl2="PROBLEMS AVOIDED", start2=5, end2=90, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
