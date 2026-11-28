from kit import build, follow_sub, hook

TITLE = ("STOP ASSUMING YOU", "KNOW PEOPLE")
OUTPUT = "215_Why_You_Should_Stop_Assuming_You_Know_People_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You see someone every day.", "crowd", dict(n=5, highlight=2, highlight_label="THEM", acc="EVERY DAY")),
    ("You know their name.", "list", dict(items=["NAME"], mode="check", acc="NAME")),
    ("You know their appearance.", "list", dict(items=["NAME", "APPEARANCE"], mode="check", acc="APPEARANCE")),
    ("You know how they act around certain people.", "list", dict(items=["NAME", "APPEARANCE", "HOW THEY ACT"], mode="check", acc="ACT")),
    ("And you begin believing you know who they are.", "hud", dict(lbl="HOW WELL YOU KNOW THEM", start=20, end=90, icons=None, crowd=0, acc="BELIEVING KNOW")),
    ("But what you see is only a fraction of their life.", "iceberg", dict(top="WHAT YOU SEE", bottom="THEIR WHOLE LIFE", acc="FRACTION")),
    ("You don't know what they're thinking about when they go home.", "brain", dict(says="...", acc="THINKING HOME")),
    ("You don't know what they're worried about.", "fog", dict(lbl="THEIR WORRIES", acc="WORRIED")),
    ("You don't know what they've experienced.", "book", dict(chapter="THEIR STORY", text="UNREAD", acc="EXPERIENCED")),
    ("You don't know what they're trying to figure out.", "puzzle", dict(missing=True, lbl="FIGURING IT OUT", acc="FIGURE")),
    ("The person who seems confident might be uncertain about something.", "iceberg", dict(top="CONFIDENT", bottom="UNCERTAIN", acc="CONFIDENT UNCERTAIN")),
    ("The person who seems quiet might have a thousand thoughts.", "iceberg", dict(top="QUIET", bottom="1,000 THOUGHTS", acc="QUIET THOUSAND")),
    ("The person who seems difficult might be dealing with something you know nothing about.", "iceberg", dict(top="DIFFICULT", bottom="DEALING WITH SOMETHING", acc="DIFFICULT NOTHING")),
    ("This doesn't mean every behavior should be excused.", "list", dict(items=["EXCUSE EVERYTHING"], mode="strike", acc="EXCUSED")),
    ("It means you should be careful about turning limited information into complete judgments.", "scale", dict(left="LIMITED INFO", right="FULL JUDGMENT", tip=-1, drop=True, acc="LIMITED COMPLETE JUDGMENTS")),
    ("You can observe someone…", "alone", dict(tag="OBSERVED", others=3, acc="OBSERVE")),
    ("Without pretending you understand their entire story.", "book", dict(chapter="PAGE 1", text="OF THEIR STORY", acc="PRETENDING ENTIRE STORY")),
    ("What is something people often misunderstand about others?", "question", dict(a_lbl="MISUNDERSTOOD", acc="MISUNDERSTAND")),
    ("Share your thoughts.", "cta", dict(kind="comment", lbl="YOUR THOUGHTS", acc="SHARE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="WHAT YOU SEE", start=10, end=10, lbl2="WHAT YOU ASSUME", start2=10, end2=100, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
