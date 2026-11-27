from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED TO BUILD A", "DIFFERENT KIND OF SUCCESS")
OUTPUT = "133_A_Different_Kind_Of_Success_16x9.mp4"
SPEC = [
    ("Maybe success for you isn't fame.", "stage", dict(lbl="FAME?", acc="ISN'T FAME.")),
    ("Maybe it isn't being the richest person.", "coins", dict(lbl="RICHEST?", acc="RICHEST")),
    ("Maybe it isn't having the most impressive career.", "stairs", dict(n=6, climb=5, acc="IMPRESSIVE CAREER.")),
    ("Maybe it's having time.", "hourglass", dict(acc="TIME.")),
    ("Good relationships.", "ring", dict(acc="RELATIONSHIPS.")),
    ("Meaningful work.", "bricks", dict(rows=3, lbl="MEANINGFUL WORK", uneven=False, acc="MEANINGFUL")),
    ("Freedom to make decisions.", "key", dict(lbl="FREEDOM", acc="FREEDOM")),
    ("A peaceful life.", "sunrise", dict(acc="PEACEFUL")),
    ("Whatever success means to you…", "question", dict(acc="SUCCESS")),
    ("Make sure you actually chose it.", "doc", dict(title="YOUR DEFINITION", empty=False, stamp="CHOSEN", acc="ACTUALLY CHOSE")),
    ("Not simply inherited it from the expectations around you.", "ring", dict(tags=["BE RICH", "BE FAMOUS", "BE A DOCTOR", "BE MORE"], acc="INHERITED EXPECTATIONS")),
    ("A successful life isn't necessarily the one people admire most.", "stage", dict(lbl="ADMIRED", acc="ISN'T ADMIRE")),
    ("It's the one you can genuinely respect living.", "mirror", dict(reflect="solid", lbl="RESPECTED", acc="GENUINELY RESPECT LIVING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
