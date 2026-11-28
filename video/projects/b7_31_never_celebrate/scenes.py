from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO NEVER", "CELEBRATE YOUR SUCCESS")
OUTPUT = "231_The_People_Who_Never_Celebrate_Your_Success_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes you accomplish something…", "crown", dict(lbl="YOU DID IT", acc="ACCOMPLISH")),
    ("And the people you expected to celebrate with you barely react.", "hud", dict(lbl="THEIR REACTION", start=0, end=6, icons=None, crowd=6, acc="CELEBRATE BARELY")),
    ("Maybe they change the subject.", "bubbles", dict(texts=["ANYWAY, DID YOU SEE...?"], acc="SUBJECT")),
    ("Maybe they minimize it.", "bubbles", dict(texts=["OH, THAT'S EASY THOUGH."], acc="MINIMIZE")),
    ("Maybe they immediately compare it to their own achievements.", "timeline", dict(compare=True, acc="COMPARE ACHIEVEMENTS")),
    ("Maybe they act like it wasn't important.", "list", dict(items=["IMPORTANT"], mode="strike", acc="IMPORTANT")),
    ("That can hurt.", "pulse", dict(acc="HURT")),
    ("But remember…", "key", dict(lbl="REMEMBER", acc="REMEMBER")),
    ("Not everyone will understand why something matters to you.", "iceberg", dict(top="THE RESULT", bottom="WHY IT MATTERS", acc="UNDERSTAND MATTERS")),
    ("Not everyone will be emotionally available to celebrate.", "battery", dict(lbl="THEIR CAPACITY", start=0.3, end=0.1, drains=0, acc="EMOTIONALLY AVAILABLE")),
    ("And not every achievement will receive the recognition you imagined.", "stage", dict(lbl="IMAGINED APPLAUSE", empty=True, acc="RECOGNITION IMAGINED")),
    ("You don't need to turn every disappointing reaction into a conflict.", "list", dict(items=["START A CONFLICT"], mode="strike", acc="DISAPPOINTING CONFLICT")),
    ("But you should learn to recognize the people who genuinely share your happiness.", "crowd", dict(n=7, highlight=5, highlight_label="GENUINELY HAPPY", acc="RECOGNIZE GENUINELY HAPPINESS")),
    ("The people who don't need to compete.", "list", dict(items=["DON'T COMPETE"], mode="check", acc="COMPETE")),
    ("The people who can say, \"I'm proud of you,\" without making it about themselves.", "bubbles", dict(texts=["I'M PROUD OF YOU."], drop=True, acc="PROUD THEMSELVES")),
    ("Those relationships are worth appreciating.", "hud", dict(lbl="WORTH IT", start=40, end=100, icons="heart", crowd=2, acc="WORTH APPRECIATING")),
    ("Tag or send this to someone who genuinely celebrates your wins, no matter how small.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="TAG SEND CELEBRATES WINS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="YOUR WIN", start=10, end=100, lbl2="THEIR EXCITEMENT", start2=5, end2=3, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
