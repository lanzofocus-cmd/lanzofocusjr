from kit import build, follow_sub, hook

TITLE = ("THE COST OF", "NEVER SAYING NO")
OUTPUT = "258_The_Cost_Of_Never_Saying_No_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine someone who says yes to everything.", "bubbles", dict(texts=["YES!"], acc="YES EVERYTHING")),
    ("Yes to helping.", "list", dict(items=["HELPING"], mode="check", acc="HELPING")),
    ("Yes to extra responsibilities.", "list", dict(items=["HELPING", "EXTRA WORK"], mode="check", acc="RESPONSIBILITIES")),
    ("Yes to plans.", "list", dict(items=["HELPING", "EXTRA WORK", "PLANS"], mode="check", acc="PLANS")),
    ("Yes to requests.", "list", dict(items=["HELPING", "EXTRA WORK", "PLANS", "REQUESTS"], mode="check", acc="REQUESTS")),
    ("Yes to things they don't really want to do.", "list", dict(items=["HELPING", "EXTRA WORK", "PLANS", "REQUESTS", "THINGS THEY HATE"], mode="check", acc="WANT")),
    ("At first, everyone sees them as helpful.", "hud", dict(lbl="SEEN AS HELPFUL", start=30, end=100, icons="thumb", acc="HELPFUL")),
    ("Reliable.", "list", dict(items=["RELIABLE"], mode="check", acc="RELIABLE")),
    ("Available.", "list", dict(items=["RELIABLE", "AVAILABLE"], mode="check", acc="AVAILABLE")),
    ("But eventually…", "pulse", dict(acc="EVENTUALLY")),
    ("Their own priorities begin disappearing.", "list", dict(items=["MY GOALS", "MY HEALTH", "MY REST"], mode="strike", acc="PRIORITIES DISAPPEARING")),
    ("They have no time for the things they wanted to accomplish.", "receipt", dict(items=[("FAVORS", "6 HRS"), ("EXTRA WORK", "5 HRS"), ("PLANS", "4 HRS"), ("MY GOALS", "0")], total="NO TIME LEFT", acc="NO TIME ACCOMPLISH")),
    ("They're constantly tired.", "battery", dict(lbl="ENERGY", start=0.6, end=0.05, drains=5, acc="TIRED")),
    ("They begin feeling frustrated with people they originally agreed to help.", "gauge", dict(lbl="RESENTMENT", start=0.1, end=0.75, acc="FRUSTRATED HELP")),
    ("And they wonder why their life feels so crowded.", "crowd", dict(n=9, highlight=4, highlight_label="YOU", acc="CROWDED")),
    ("The problem isn't kindness.", "list", dict(items=["KINDNESS"], mode="check", acc="KINDNESS")),
    ("The problem is believing kindness requires unlimited availability.", "progress", dict(lbl="AVAILABILITY", value=1.0, acc="KINDNESS UNLIMITED AVAILABILITY")),
    ("You can help someone without accepting every request.", "list", dict(items=["ACCEPT EVERY REQUEST"], mode="strike", acc="HELP EVERY")),
    ("You can care without abandoning your own responsibilities.", "scale", dict(left="THEIR NEEDS", right="YOUR LIFE", tip=0, acc="CARE ABANDONING")),
    ("You can be generous without allowing every person to control your schedule.", "doc", dict(title="YOUR SCHEDULE", empty=False, stamp="YOURS", acc="GENEROUS SCHEDULE")),
    ("Saying no isn't always selfish.", "sticker", dict(tags=["SELFISH"], strike=True, acc="NO SELFISH")),
    ("Sometimes it's necessary to protect the commitments you've already made.", "shield", dict(front="NO", back="COMMITMENTS", acc="PROTECT COMMITMENTS")),
    ("A yes to everything eventually becomes a no to something.", "scale", dict(left="YES TO ALL", right="NO TO SOMETHING", tip=0, drop=True, acc="YES EVERYTHING NO SOMETHING")),
    ("And sometimes that something is your own life.", "house", dict(progress=0.2, watchers=False, lbl="YOUR LIFE", acc="OWN LIFE")),
    ("What's something people need to become more comfortable saying no to?", "list", dict(items=["SAY NO TO..."], mode="empty", acc="NO")),
    ("Let's discuss.", "cta", dict(kind="comment", lbl="SAY NO TO...", acc="DISCUSS")),
    ("", "follow"),
]
_HOOK = ("battery", dict(lbl="YES, YES, YES...", start=1.0, end=0.04, drains=5))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
