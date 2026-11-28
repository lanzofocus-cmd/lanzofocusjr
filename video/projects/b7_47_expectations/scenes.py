from kit import build, follow_sub, hook

TITLE = ("YOUR EXPECTATIONS CAN DESTROY", "GOOD EXPERIENCES")
OUTPUT = "247_Why_Your_Expectations_Can_Destroy_Good_Experiences_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine going into an experience expecting it to be perfect.", "frame", dict(who="THE PERFECT VERSION", acc="EXPECTING PERFECT")),
    ("The trip.", "list", dict(items=["THE TRIP"], mode="check", acc="TRIP")),
    ("The event.", "list", dict(items=["THE TRIP", "THE EVENT"], mode="check", acc="EVENT")),
    ("The relationship.", "list", dict(items=["THE TRIP", "THE EVENT", "THE RELATIONSHIP"], mode="check", acc="RELATIONSHIP")),
    ("The achievement.", "list", dict(items=["THE TRIP", "THE EVENT", "THE RELATIONSHIP", "THE ACHIEVEMENT"], mode="check", acc="ACHIEVEMENT")),
    ("The day.", "list", dict(items=["THE TRIP", "THE EVENT", "THE RELATIONSHIP", "THE ACHIEVEMENT", "THE DAY"], mode="check", acc="DAY")),
    ("You create an image in your mind.", "brain", dict(says="IT'LL BE PERFECT.", acc="IMAGE MIND")),
    ("Then reality arrives.", "door", dict(open_=True, lbl="REALITY", acc="REALITY")),
    ("Something goes wrong.", "chart", dict(kind="down", lbl="THE PLAN", acc="WRONG")),
    ("The weather changes.", "fog", dict(lbl="RAIN", acc="WEATHER")),
    ("Someone behaves differently.", "bubbles", dict(texts=["I'M NOT IN THE MOOD."], acc="BEHAVES DIFFERENTLY")),
    ("The experience isn't exactly what you imagined.", "scale", dict(left="IMAGINED", right="REAL", tip=-1, acc="EXACTLY IMAGINED")),
    ("And suddenly, you're disappointed.", "gauge", dict(lbl="DISAPPOINTMENT", start=0.1, end=0.85, acc="DISAPPOINTED")),
    ("But sometimes the experience itself wasn't bad.", "list", dict(items=["THE EXPERIENCE WAS BAD"], mode="strike", acc="EXPERIENCE BAD")),
    ("Your expectation simply left no room for reality.", "cage", dict(words=["PERFECT OR NOTHING"], drop=True, acc="EXPECTATION ROOM REALITY")),
    ("This doesn't mean you should have no standards.", "list", dict(items=["NO STANDARDS"], mode="strike", acc="STANDARDS")),
    ("It means expectations should leave space for unexpected things.", "puzzle", dict(missing=True, lbl="ROOM FOR SURPRISES", acc="SPACE UNEXPECTED")),
    ("You can hope for something wonderful…", "sunrise", dict(acc="HOPE WONDERFUL")),
    ("Without requiring every detail to match the image in your head.", "frame", dict(who="THE IMAGE", fade=True, acc="REQUIRING DETAIL IMAGE")),
    ("Sometimes a good experience looks different from the one you planned.", "path", dict(kind="fork", labels=("PLANNED", "WHAT HAPPENED"), acc="GOOD DIFFERENT PLANNED")),
    ("Have you ever had an experience that was completely different from what you expected, but still meaningful?", "cta", dict(kind="comment", lbl="DIFFERENT, STILL GOOD", acc="DIFFERENT EXPECTED MEANINGFUL")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EXPECTATIONS", start=40, end=100, lbl2="ENJOYMENT", start2=80, end2=12, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
