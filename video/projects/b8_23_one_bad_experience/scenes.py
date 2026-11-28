from kit import build, follow_sub, hook

TITLE = ("ONE BAD EXPERIENCE DOESN'T", "DEFINE A CATEGORY")
OUTPUT = "273_Why_You_Should_Not_Let_One_Bad_Experience_Define_An_Entire_Category_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine having one bad experience with someone…", "crowd", dict(n=3, highlight=1, highlight_label="ONE PERSON", acc="ONE BAD")),
    ("Then deciding you can't trust anyone.", "crowd", dict(n=9, dim=True, acc="TRUST ANYONE")),
    ("One bad experience at school…", "book", dict(chapter="ONE BAD CLASS", acc="SCHOOL")),
    ("Then deciding you hate learning.", "sticker", dict(tags=["HATE LEARNING"], acc="HATE LEARNING")),
    ("One difficult attempt at a skill…", "chart", dict(kind="down", lbl="ATTEMPT #1", acc="DIFFICULT SKILL")),
    ("Then deciding you're not interested.", "sticker", dict(tags=["NOT INTERESTED"], acc="INTERESTED")),
    ("One disappointing opportunity…", "door", dict(closing=True, lbl="ONE DOOR", acc="DISAPPOINTING")),
    ("Then deciding opportunities aren't worth pursuing.", "list", dict(items=["ALL OPPORTUNITIES"], mode="strike", acc="OPPORTUNITIES PURSUING")),
    ("This is how individual experiences can become general conclusions.", "scale", dict(left="ONE EXPERIENCE", right="EVERYTHING", tip=-1, acc="INDIVIDUAL GENERAL")),
    ("But one experience is not necessarily a complete representation of an entire category.", "dots", dict(connect=False, n=12, drop=True, acc="ONE COMPLETE ENTIRE CATEGORY")),
    ("One person doesn't represent everyone.", "crowd", dict(n=9, highlight=4, highlight_label="ONE OF MANY", acc="EVERYONE")),
    ("One failure doesn't represent every future attempt.", "timeline", dict(n=10, progress=0.1, tag="ATTEMPT 1 OF MANY", acc="FAILURE FUTURE")),
    ("One difficult experience doesn't mean every similar experience will be the same.", "path", dict(kind="fork", labels=("SAME?", "DIFFERENT"), acc="SIMILAR SAME")),
    ("You should learn from what happened.", "book", dict(chapter="THE LESSON", acc="LEARN")),
    ("You should recognize genuine risks.", "shield", dict(front="CAUTION", back="YOU", acc="GENUINE RISKS")),
    ("But you shouldn't allow one experience to permanently close possibilities without examining them.", "door", dict(open_=True, lbl="STILL OPEN", acc="PERMANENTLY CLOSE EXAMINING")),
    ("Have you ever changed your opinion about something after giving it another chance?", "shed", dict(old="NEVER AGAIN", new="GLAD I TRIED", acc="CHANGED ANOTHER")),
    ("Tell us what happened.", "cta", dict(kind="comment", lbl="WHAT CHANGED YOUR MIND", acc="TELL")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="BAD EXPERIENCES", start=0, end=1, lbl2="\"ALL OF THEM ARE BAD\"", start2=0, end2=100, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
