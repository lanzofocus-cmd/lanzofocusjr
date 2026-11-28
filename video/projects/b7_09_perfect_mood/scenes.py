from kit import build, follow_sub, hook

TITLE = ("STOP WAITING FOR", "THE PERFECT MOOD")
OUTPUT = "209_Why_You_Should_Stop_Waiting_For_The_Perfect_Mood_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine having a goal that depends entirely on how you feel.", "gauge", dict(lbl="MOOD", start=0.5, end=0.5, acc="DEPENDS FEEL")),
    ("If you're excited, you work.", "hud", dict(lbl="MOOD", start=50, end=95, icons=None, crowd=0, tag="WORK", acc="EXCITED WORK")),
    ("If you're tired, you stop.", "hud", dict(lbl="MOOD", start=95, end=20, icons=None, crowd=0, tag="STOP", acc="TIRED STOP")),
    ("If you're confident, you try.", "hud", dict(lbl="MOOD", start=20, end=85, icons=None, crowd=0, tag="TRY", acc="CONFIDENT TRY")),
    ("If you're nervous, you postpone.", "hud", dict(lbl="MOOD", start=85, end=25, icons=None, crowd=0, tag="POSTPONE", acc="NERVOUS POSTPONE")),
    ("If everything feels perfect, you begin.", "startline", dict(behind=True, acc="PERFECT BEGIN")),
    ("That sounds reasonable…", "list", dict(items=["REASONABLE?"], mode="check", acc="REASONABLE")),
    ("Until you realize your emotions change constantly.", "chart", dict(kind="wave", lbl="EMOTIONS", acc="EMOTIONS CONSTANTLY")),
    ("You can wake up motivated and lose it by afternoon.", "battery", dict(lbl="MOTIVATION", start=1.0, end=0.2, drains=0, acc="MOTIVATED AFTERNOON")),
    ("You can feel confident one day and uncertain the next.", "chart", dict(kind="wave", lbl="CONFIDENCE", acc="CONFIDENT UNCERTAIN")),
    ("If your entire progress depends on maintaining one emotional state…", "lock", dict(lbl="ONE MOOD", acc="PROGRESS EMOTIONAL")),
    ("Your progress will constantly be interrupted.", "progress", dict(lbl="PROGRESS", value=0.2, acc="INTERRUPTED")),
    ("This doesn't mean ignoring your needs or pushing through every form of exhaustion.", "list", dict(items=["IGNORE YOUR NEEDS"], mode="strike", acc="NEEDS EXHAUSTION")),
    ("It means learning that feelings are information…", "doc", dict(title="FEELINGS", empty=False, stamp="INFO", drop=True, acc="FEELINGS INFORMATION")),
    ("Not always instructions.", "doc", dict(title="FEELINGS", empty=False, stamp="NOT ORDERS", acc="INSTRUCTIONS")),
    ("You can feel nervous and still take a reasonable step.", "stairs", dict(n=6, climb=1, acc="NERVOUS STEP")),
    ("You can feel uninspired and still complete something small.", "list", dict(items=["ONE SMALL THING"], mode="check", acc="UNINSPIRED SMALL")),
    ("You can feel uncertain and still learn.", "book", dict(chapter="STILL LEARNING", acc="UNCERTAIN LEARN")),
    ("The goal isn't to become emotionless.", "list", dict(items=["EMOTIONLESS"], mode="strike", acc="EMOTIONLESS")),
    ("It's to become capable of making thoughtful decisions even when your emotions aren't perfectly aligned with them.", "compass", dict(lbl="THOUGHTFUL", acc="CAPABLE THOUGHTFUL EMOTIONS")),
    ("Save this if you've ever abandoned something simply because the excitement disappeared.", "cta", dict(kind="save", lbl="KEEP GOING ANYWAY", acc="SAVE EXCITEMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="MOTIVATION", start=95, end=10, icons=None, tag="WAITING...", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
