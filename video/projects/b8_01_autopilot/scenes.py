from kit import build, follow_sub, hook

TITLE = ("THE DANGER OF LIVING", "ON AUTOPILOT")
OUTPUT = "251_The_Danger_Of_Living_On_Autopilot_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever arrived somewhere…", "map", dict(a_lbl="HOME", b_lbl="ARRIVED", acc="ARRIVED")),
    ("And realized you barely remember the journey?", "path", dict(kind="dashed", acc="BARELY JOURNEY")),
    ("You were physically there.", "alone", dict(tag="BODY: HERE", acc="PHYSICALLY")),
    ("But your mind was somewhere else.", "mirror", dict(reflect="dashed", lbl="MIND: ELSEWHERE", acc="MIND ELSE")),
    ("Thinking about yesterday.", "timeline", dict(n=8, progress=0.3, tag="YESTERDAY", acc="YESTERDAY")),
    ("Worrying about tomorrow.", "timeline", dict(n=8, progress=0.8, tag="TOMORROW", acc="TOMORROW")),
    ("Scrolling through your phone.", "phone", dict(lbl="SCROLLING", acc="SCROLLING")),
    ("Repeating the same routine without really noticing it.", "loop", dict(items=["WAKE", "WORK", "SCROLL", "SLEEP"], acc="SAME ROUTINE NOTICING")),
    ("This is how life can quietly pass without feeling like you're actually participating in it.", "hourglass", dict(acc="QUIETLY PASS PARTICIPATING")),
    ("You wake up.", "loop", dict(items=["WAKE UP", "SAME THINGS", "SAME PROBLEMS", "SLEEP"], acc="WAKE")),
    ("Do the same things.", "list", dict(items=["SAME THINGS"], mode="check", acc="SAME")),
    ("React to the same problems.", "list", dict(items=["SAME THINGS", "SAME PROBLEMS"], mode="check", acc="REACT PROBLEMS")),
    ("Consume the same content.", "list", dict(items=["SAME THINGS", "SAME PROBLEMS", "SAME CONTENT"], mode="check", acc="CONSUME CONTENT")),
    ("Go to sleep.", "list", dict(items=["SAME THINGS", "SAME PROBLEMS", "SAME CONTENT", "SLEEP"], mode="check", acc="SLEEP")),
    ("Then repeat.", "big", dict(text="REPEAT", acc="REPEAT")),
    ("And eventually, your days begin blending together.", "dots", dict(connect=True, acc="BLENDING")),
    ("The problem isn't having routines.", "list", dict(items=["ROUTINES"], mode="check", acc="ROUTINES")),
    ("Routines can make life easier.", "stairs", dict(n=5, climb=3, acc="EASIER")),
    ("The problem is when you stop questioning whether the routines you're following are actually helping you live the life you want.", "compass", dict(lbl="THE LIFE YOU WANT", settle=False, acc="QUESTIONING HELPING WANT")),
    ("Are you doing something because it matters?", "scale", dict(left="IT MATTERS", right="HABIT", tip=0, acc="MATTERS")),
    ("Or because you've simply been doing it for a long time?", "hourglass", dict(acc="LONG")),
    ("Are you choosing your day?", "path", dict(kind="fork", labels=("CHOSEN", "DEFAULT"), acc="CHOOSING")),
    ("Or is your day being chosen by whatever happens to appear in front of you?", "notifs", dict(acc="CHOSEN APPEAR")),
    ("You don't need to completely change your life overnight.", "list", dict(items=["CHANGE EVERYTHING OVERNIGHT"], mode="strike", acc="OVERNIGHT")),
    ("Sometimes you simply need to become more aware of it.", "hud", dict(lbl="AWARENESS", start=10, end=85, icons=None, crowd=0, acc="AWARE")),
    ("Notice what you're doing.", "list", dict(items=["WHAT YOU DO"], mode="check", acc="NOTICE DOING")),
    ("Notice what you're thinking.", "list", dict(items=["WHAT YOU DO", "WHAT YOU THINK"], mode="check", acc="THINKING")),
    ("Notice where your time goes.", "list", dict(items=["WHAT YOU DO", "WHAT YOU THINK", "WHERE TIME GOES"], mode="check", acc="TIME")),
    ("Notice the people around you.", "ring", dict(acc="PEOPLE")),
    ("Notice the moments you usually ignore.", "frame", dict(who="AN IGNORED MOMENT", acc="MOMENTS IGNORE")),
    ("Because the first step toward changing your life isn't always making a new plan.", "doc", dict(title="NEW PLAN", empty=True, acc="FIRST STEP PLAN")),
    ("Sometimes it's finally paying attention to the life you're already living.", "sunrise", dict(drop=True, acc="ATTENTION ALREADY LIVING")),
    ("What part of your daily routine do you think you're doing completely on autopilot?", "loop", dict(items=["?", "?", "?", "?"], lbl="AUTOPILOT", acc="ROUTINE AUTOPILOT")),
    ("Tell us.", "cta", dict(kind="comment", lbl="YOUR AUTOPILOT HABIT", acc="TELL")),
    ("And follow LanzoFocus for ideas that help you become more intentional with your life.", "follow"),
]
_HOOK = ("hud", dict(lbl="DAYS ON AUTOPILOT", start=10, end=96, lbl2="DAYS YOU REMEMBER", start2=60, end2=5, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
