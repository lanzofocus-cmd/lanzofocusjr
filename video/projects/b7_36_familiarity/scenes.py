from kit import build, follow_sub, hook

TITLE = ("FAMILIARITY IS NOT", "HAPPINESS")
OUTPUT = "236_Why_You_Should_Stop_Confusing_Familiarity_With_Happiness_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes people remain in situations simply because they're familiar.", "chairs", dict(n=5, lbl="FAMILIAR", acc="REMAIN FAMILIAR")),
    ("They know how it works.", "list", dict(items=["KNOW HOW IT WORKS"], mode="check", acc="KNOW")),
    ("They know what to expect.", "list", dict(items=["KNOW HOW IT WORKS", "KNOW WHAT TO EXPECT"], mode="check", acc="EXPECT")),
    ("Even when it's uncomfortable…", "gauge", dict(lbl="DISCOMFORT", start=0.4, end=0.7, acc="UNCOMFORTABLE")),
    ("At least it's predictable.", "chart", dict(kind="flat", lbl="PREDICTABLE", acc="PREDICTABLE")),
    ("And the unknown feels more frightening than the familiar problem.", "scale", dict(left="THE UNKNOWN", right="FAMILIAR PROBLEM", tip=-1, acc="UNKNOWN FRIGHTENING FAMILIAR")),
    ("This is why change can be difficult.", "door", dict(open_=True, lbl="CHANGE", acc="CHANGE DIFFICULT")),
    ("You aren't only leaving a situation.", "path", dict(kind="fork", labels=("STAY", "LEAVE"), acc="LEAVING")),
    ("You're leaving the predictability surrounding it.", "fog", dict(lbl="UNPREDICTABLE", acc="PREDICTABILITY")),
    ("But familiarity doesn't automatically mean something is good for you.", "scale", dict(left="FAMILIAR", right="GOOD FOR YOU", tip=1, drop=True, acc="FAMILIARITY GOOD")),
    ("A routine can be familiar and still be unhelpful.", "loop", dict(items=["WAKE", "SCROLL", "RUSH", "REPEAT"], acc="ROUTINE UNHELPFUL")),
    ("A habit can feel normal and still be worth changing.", "list", dict(items=["THAT HABIT"], mode="tag", tag="NORMAL? CHANGE IT", acc="HABIT NORMAL CHANGING")),
    ("A situation can be predictable and still prevent you from growing.", "cage", dict(words=["SAFE", "PREDICTABLE"], acc="PREDICTABLE GROWING")),
    ("You don't need to change everything.", "list", dict(items=["CHANGE EVERYTHING"], mode="strike", acc="EVERYTHING")),
    ("But you should occasionally ask whether you're staying because something genuinely works…", "hud", dict(lbl="IT WORKS", start=20, end=40, icons=None, crowd=0, acc="STAYING GENUINELY WORKS")),
    ("Or because you've simply become used to it.", "hud", dict(lbl="IT WORKS", start=40, end=40, lbl2="USED TO IT", start2=20, end2=95, icons=None, crowd=0, acc="USED")),
    ("What is something people often keep doing simply because it's familiar?", "cta", dict(kind="comment", lbl="FAMILIAR, NOT GOOD", acc="DOING FAMILIAR")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="FAMILIAR", start=20, end=100, lbl2="HAPPY", start2=60, end2=10, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
