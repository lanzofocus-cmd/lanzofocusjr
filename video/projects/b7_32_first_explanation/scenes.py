from kit import build, follow_sub, hook

TITLE = ("QUESTION YOUR", "FIRST EXPLANATION")
OUTPUT = "232_Why_You_Should_Question_Your_First_Explanation_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Something goes wrong.", "chart", dict(kind="down", lbl="SOMETHING", acc="WRONG")),
    ("Your brain immediately searches for an explanation.", "brain", dict(says="WHY?!", acc="IMMEDIATELY EXPLANATION")),
    ("\"They don't respect me.\"", "quote", dict(text="THEY DON'T RESPECT ME.", acc="RESPECT")),
    ("\"I'm unlucky.\"", "quote", dict(text="I'M UNLUCKY.", acc="UNLUCKY")),
    ("\"I always make mistakes.\"", "quote", dict(text="I ALWAYS MAKE MISTAKES.", acc="ALWAYS")),
    ("\"It's because of this person.\"", "quote", dict(text="IT'S BECAUSE OF THEM.", acc="PERSON")),
    ("But the first explanation isn't necessarily the correct one.", "doc", dict(title="EXPLANATION #1", empty=False, stamp="UNVERIFIED", acc="FIRST CORRECT")),
    ("Your brain wants a quick answer.", "gauge", dict(lbl="SPEED", start=0.3, end=0.95, acc="QUICK")),
    ("A simple story.", "book", dict(chapter="SIMPLE STORY", acc="SIMPLE")),
    ("Something that makes the situation feel understandable.", "puzzle", dict(missing=False, lbl="FEELS SOLVED", acc="UNDERSTANDABLE")),
    ("But reality can be more complicated.", "network", dict(nodes=["TIMING", "MISTAKES", "OTHERS", "LUCK", "CONTEXT"], tangled=True, acc="REALITY COMPLICATED")),
    ("Maybe there were several factors.", "list", dict(items=["SEVERAL FACTORS"], mode="check", acc="SEVERAL")),
    ("Maybe you misunderstood.", "list", dict(items=["SEVERAL FACTORS", "A MISUNDERSTANDING"], mode="check", acc="MISUNDERSTOOD")),
    ("Maybe the timing was bad.", "list", dict(items=["SEVERAL FACTORS", "A MISUNDERSTANDING", "BAD TIMING"], mode="check", acc="TIMING")),
    ("Maybe you made a mistake.", "list", dict(items=["SEVERAL FACTORS", "A MISUNDERSTANDING", "BAD TIMING", "YOUR MISTAKE"], mode="check", acc="MISTAKE")),
    ("Maybe something outside your control happened.", "list", dict(items=["SEVERAL FACTORS", "A MISUNDERSTANDING", "BAD TIMING", "YOUR MISTAKE", "OUT OF YOUR CONTROL"], mode="check", acc="OUTSIDE CONTROL")),
    ("The first explanation can feel emotionally satisfying…", "hud", dict(lbl="SATISFYING", start=20, end=90, icons=None, crowd=0, acc="EMOTIONALLY SATISFYING")),
    ("Without being accurate.", "hud", dict(lbl="SATISFYING", start=90, end=90, lbl2="ACCURATE", start2=10, end2=12, icons=None, crowd=0, acc="ACCURATE")),
    ("Before deciding why something happened…", "hourglass", dict(acc="DECIDING WHY")),
    ("Give yourself permission to investigate.", "key", dict(lbl="INVESTIGATE", acc="PERMISSION INVESTIGATE")),
    ("Understanding is more useful than immediately choosing someone to blame.", "scale", dict(left="UNDERSTANDING", right="BLAME", tip=-1, drop=True, acc="UNDERSTANDING USEFUL BLAME")),
    ("Comment \"INVESTIGATE\" if you think people should question their assumptions before blaming.", "cta", dict(kind="comment", lbl="COMMENT \"INVESTIGATE\"", acc="INVESTIGATE ASSUMPTIONS BLAMING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="BLAME", start=10, end=98, lbl2="ACTUAL FACTS", start2=5, end2=5, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
