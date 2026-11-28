from kit import build, follow_sub, hook

TITLE = ("THE PROBLEM WITH ALWAYS", "NEEDING A REASON")
OUTPUT = "219_The_Problem_With_Always_Needing_A_Reason_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes you don't need a complicated reason to change something.", "key", dict(lbl="SIMPLE REASON", acc="COMPLICATED CHANGE")),
    ("You don't need a dramatic event.", "list", dict(items=["DRAMATIC EVENT"], mode="strike", acc="DRAMATIC")),
    ("You don't need to reach a breaking point.", "list", dict(items=["DRAMATIC EVENT", "BREAKING POINT"], mode="strike", acc="BREAKING")),
    ("You don't need everyone to understand why.", "list", dict(items=["DRAMATIC EVENT", "BREAKING POINT", "EVERYONE'S APPROVAL"], mode="strike", acc="EVERYONE WHY")),
    ("Maybe you simply realized that something wasn't working.", "chart", dict(kind="flat", lbl="NOT WORKING", acc="WORKING")),
    ("Maybe you wanted to try something different.", "path", dict(kind="fork", labels=("SAME", "DIFFERENT"), acc="DIFFERENT")),
    ("Maybe your priorities changed.", "shed", dict(old="OLD PRIORITIES", new="NEW PRIORITIES", acc="PRIORITIES")),
    ("Maybe you learned something new.", "book", dict(chapter="SOMETHING NEW", acc="LEARNED")),
    ("People sometimes wait for a huge reason because they believe small reasons aren't valid enough.", "scale", dict(left="SMALL REASON", right="HUGE REASON", tip=1, acc="HUGE SMALL VALID")),
    ("But your life is made of small decisions.", "bricks", dict(rows=5, lbl="SMALL DECISIONS", uneven=False, drop=True, acc="SMALL DECISIONS")),
    ("You can improve something before it becomes a disaster.", "gauge", dict(lbl="PROBLEM", start=0.3, end=0.3, acc="IMPROVE DISASTER")),
    ("You can leave a habit before it destroys something.", "door", dict(open_=True, lbl="LEAVE EARLY", acc="LEAVE HABIT")),
    ("You can adjust your direction before you're completely lost.", "compass", dict(lbl="ADJUST NOW", acc="ADJUST LOST")),
    ("You don't have to wait until the situation becomes unbearable before you take it seriously.", "hud", dict(lbl="HOW BAD IT IS", start=10, end=30, icons=None, crowd=0, tag="ACT NOW", acc="UNBEARABLE SERIOUSLY")),
    ("What's something you believe people should improve before it becomes a major problem?", "cta", dict(kind="comment", lbl="FIX IT EARLY", acc="IMPROVE MAJOR")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="WAITING FOR A REASON", start=5, end=96, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
