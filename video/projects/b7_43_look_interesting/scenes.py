from kit import build, follow_sub, hook

TITLE = ("STOP WAITING FOR YOUR LIFE", "TO LOOK INTERESTING")
OUTPUT = "243_Why_You_Should_Stop_Waiting_For_Your_Life_To_Look_Interesting_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Social media can make ordinary life feel disappointing.", "phone", dict(lbl="YOUR FEED", acc="ORDINARY DISAPPOINTING")),
    ("You see trips.", "list", dict(items=["TRIPS"], mode="tag", tag="THEIRS", acc="TRIPS")),
    ("Achievements.", "list", dict(items=["TRIPS", "ACHIEVEMENTS"], mode="tag", tag="THEIRS", acc="ACHIEVEMENTS")),
    ("Events.", "list", dict(items=["TRIPS", "ACHIEVEMENTS", "EVENTS"], mode="tag", tag="THEIRS", acc="EVENTS")),
    ("Beautiful locations.", "list", dict(items=["TRIPS", "ACHIEVEMENTS", "EVENTS", "LOCATIONS"], mode="tag", tag="THEIRS", acc="LOCATIONS")),
    ("Exciting experiences.", "list", dict(items=["TRIPS", "ACHIEVEMENTS", "EVENTS", "LOCATIONS", "EXPERIENCES"], mode="tag", tag="THEIRS", acc="EXPERIENCES")),
    ("And suddenly, your normal day feels like nothing.", "big", dict(text="TUESDAY", sub="FEELS LIKE NOTHING", acc="NORMAL NOTHING")),
    ("But you're comparing your everyday reality…", "timeline", dict(compare=True, acc="EVERYDAY REALITY")),
    ("To someone else's selected moments.", "frame", dict(who="SELECTED MOMENTS", acc="SELECTED MOMENTS")),
    ("The problem isn't that their experiences are fake.", "list", dict(items=["FAKE"], mode="strike", acc="FAKE")),
    ("The problem is that you're seeing a limited part of their life.", "iceberg", dict(top="THE POSTS", bottom="THE REST OF THEIR LIFE", acc="LIMITED PART")),
    ("Every exciting moment has ordinary moments surrounding it.", "dots", dict(connect=False, acc="EXCITING ORDINARY")),
    ("Every impressive achievement has routine behind it.", "iceberg", dict(top="ACHIEVEMENT", bottom="ROUTINE", acc="ACHIEVEMENT ROUTINE")),
    ("Every person has days that don't look interesting.", "crowd", dict(n=9, dim=True, acc="EVERY INTERESTING")),
    ("Your life doesn't need to constantly produce exciting content to be meaningful.", "phone", dict(lbl="NOT CONTENT", drop=True, acc="CONTENT MEANINGFUL")),
    ("A quiet day can still be a good day.", "sunrise", dict(acc="QUIET GOOD")),
    ("An ordinary experience can still matter.", "frame", dict(who="ORDINARY", acc="ORDINARY MATTER")),
    ("You don't need your life to look extraordinary every moment.", "stage", dict(lbl="EXTRAORDINARY?", empty=True, acc="EXTRAORDINARY")),
    ("You need to actually experience it.", "pulse", dict(acc="EXPERIENCE")),
    ("What's one ordinary part of your life that you genuinely appreciate?", "cta", dict(kind="comment", lbl="YOUR ORDINARY JOY", acc="ORDINARY APPRECIATE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="THEIR HIGHLIGHTS", start=20, end=100, lbl2="YOUR TUESDAY", start2=50, end2=8, icons="heart", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
