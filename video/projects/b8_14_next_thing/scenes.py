from kit import build, follow_sub, hook

TITLE = ("ALWAYS LOOKING FOR", "THE NEXT THING")
OUTPUT = "264_The_Problem_With_Always_Looking_For_The_Next_Thing_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You finish something.", "list", dict(items=["DONE"], mode="check", acc="FINISH")),
    ("Immediately, you begin thinking about the next thing.", "arrows", dict(items=["NEXT"], acc="IMMEDIATELY NEXT")),
    ("You complete a goal.", "stairs", dict(n=6, climb=6, acc="GOAL")),
    ("You create another.", "stairs", dict(n=9, climb=6, highlight=8, acc="ANOTHER")),
    ("You reach a milestone.", "timeline", dict(n=8, progress=0.6, tag="MILESTONE", acc="MILESTONE")),
    ("You move the finish line.", "timeline", dict(n=12, progress=0.4, tag="MOVED", acc="FINISH LINE")),
    ("You finally get something you wanted…", "crown", dict(lbl="GOT IT", acc="FINALLY WANTED")),
    ("And almost immediately, your attention shifts toward something else.", "compass", dict(lbl="SOMETHING ELSE", settle=False, acc="ATTENTION SHIFTS")),
    ("This can create a strange experience.", "question", dict(acc="STRANGE")),
    ("You spend months working toward something.", "timeline", dict(n=10, progress=0.9, tag="MONTHS", acc="MONTHS")),
    ("But when you achieve it…", "crown", dict(lbl="ACHIEVED", acc="ACHIEVE")),
    ("You barely experience the satisfaction.", "hud", dict(lbl="SATISFACTION", start=0, end=8, icons=None, crowd=0, acc="BARELY SATISFACTION")),
    ("Because your mind has already moved on.", "brain", dict(says="WHAT'S NEXT?", acc="MOVED")),
    ("Ambition is valuable.", "list", dict(items=["AMBITION"], mode="check", acc="AMBITION")),
    ("But constantly moving the goalpost can make achievement feel meaningless.", "progress", dict(lbl="FEELS MEANINGFUL", value=0.05, acc="GOALPOST MEANINGLESS")),
    ("You don't need to stop pursuing improvement.", "chart", dict(kind="up", lbl="KEEP GOING", acc="PURSUING IMPROVEMENT")),
    ("You need to learn how to recognize progress while it's happening.", "hud", dict(lbl="PROGRESS SEEN", start=10, end=90, icons="heart", crowd=0, drop=True, acc="RECOGNIZE PROGRESS HAPPENING")),
    ("Take a moment.", "hourglass", dict(acc="MOMENT")),
    ("Look at what changed.", "shed", dict(old="THEN", new="NOW", acc="CHANGED")),
    ("Remember where you started.", "startline", dict(behind=False, acc="STARTED")),
    ("Appreciate the effort.", "bricks", dict(rows=4, lbl="YOUR EFFORT", uneven=False, acc="EFFORT")),
    ("Then continue.", "path", dict(kind="straight", acc="CONTINUE")),
    ("You can be ambitious without being incapable of satisfaction.", "scale", dict(left="AMBITION", right="SATISFACTION", tip=0, acc="AMBITIOUS SATISFACTION")),
    ("What's a goal you've achieved that deserves more appreciation than you gave it at the time?", "cta", dict(kind="comment", lbl="IT DESERVED MORE", acc="ACHIEVED APPRECIATION")),
    ("", "follow"),
]
_HOOK = ("stairs", dict(n=10, climb=7, highlight=9))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
