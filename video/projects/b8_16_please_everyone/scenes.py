from kit import build, follow_sub, hook

TITLE = ("YOU CAN'T PLEASE", "EVERYONE")
OUTPUT = "266_The_Moment_You_Realize_You_Cant_Please_Everyone_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine making a decision.", "doc", dict(title="DECISION", empty=False, acc="DECISION")),
    ("One person agrees.", "hud", dict(lbl="APPROVAL", start=0, end=17, icons="thumb", crowd=2, acc="AGREES")),
    ("Another disagrees.", "hud", dict(lbl="APPROVAL", start=17, end=8, icons="thumbdown", crowd=2, acc="DISAGREES")),
    ("Someone thinks you're doing too much.", "bubbles", dict(texts=["TOO MUCH!"], acc="TOO MUCH")),
    ("Someone thinks you're not doing enough.", "bubbles", dict(texts=["TOO MUCH!", "NOT ENOUGH!"], acc="ENOUGH")),
    ("Someone thinks you should change.", "bubbles", dict(texts=["CHANGE!"], acc="CHANGE")),
    ("Someone thinks you should stay the same.", "bubbles", dict(texts=["CHANGE!", "STAY THE SAME!"], acc="SAME")),
    ("And suddenly…", "pulse", dict(acc="")),
    ("You're trying to create a decision that satisfies everyone.", "ring", dict(tags=["MORE", "LESS", "CHANGE", "STAY", "FASTER"], acc="SATISFIES EVERYONE")),
    ("But the problem is that people have different expectations.", "network", dict(nodes=["MORE", "LESS", "CHANGE", "STAY"], tangled=True, acc="DIFFERENT EXPECTATIONS")),
    ("And those expectations can contradict each other.", "scale", dict(left="TOO MUCH", right="NOT ENOUGH", tip=0, acc="CONTRADICT")),
    ("If you constantly try to satisfy every opinion…", "battery", dict(lbl="YOU", start=0.9, end=0.1, drains=5, acc="SATISFY EVERY")),
    ("You may end up making decisions that don't actually reflect your own priorities.", "compass", dict(lbl="YOUR PRIORITIES?", settle=False, acc="REFLECT PRIORITIES")),
    ("You become a person shaped entirely by reactions.", "sticker", dict(tags=["THEIR IDEA", "THEIR RULE", "THEIR WISH", "THEIR TASTE"], acc="SHAPED REACTIONS")),
    ("This doesn't mean you should ignore everyone.", "list", dict(items=["IGNORE EVERYONE"], mode="strike", acc="IGNORE")),
    ("Listen.", "list", dict(items=["LISTEN"], mode="check", acc="LISTEN")),
    ("Consider feedback.", "list", dict(items=["LISTEN", "CONSIDER FEEDBACK"], mode="check", acc="FEEDBACK")),
    ("Be respectful.", "list", dict(items=["LISTEN", "CONSIDER FEEDBACK", "BE RESPECTFUL"], mode="check", acc="RESPECTFUL")),
    ("But recognize that not every opinion can be followed.", "path", dict(kind="fork", labels=("THEIRS", "THEIRS TOO"), acc="EVERY FOLLOWED")),
    ("At some point, you have to make a decision based on your understanding of the situation.", "key", dict(lbl="YOUR CALL", acc="DECISION UNDERSTANDING")),
    ("And accept that someone may disagree.", "bubbles", dict(texts=["I DON'T AGREE."], acc="ACCEPT DISAGREE")),
    ("You don't need unanimous approval to make a reasonable choice.", "hud", dict(lbl="APPROVAL", start=100, end=60, icons=None, crowd=4, cross=True, drop=True, acc="UNANIMOUS APPROVAL REASONABLE")),
    ("What's one expectation people need to stop trying to satisfy from everyone?", "cta", dict(kind="comment", lbl="STOP TRYING TO...", acc="EXPECTATION SATISFY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PEOPLE PLEASED", start=10, end=55, lbl2="PEOPLE UPSET", start2=10, end2=55, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
