from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED TO", "PROTECT YOUR PEACE")
OUTPUT = "126_Youre_Allowed_To_Protect_Your_Peace_16x9.mp4"
SPEC = [
    ("You don't have to remain in every conversation.", "door", dict(open_=True, lbl="EXIT", acc="REMAIN EVERY")),
    ("You don't have to respond to every message immediately.", "notifs", dict(items=["NEW MESSAGE", "NEW MESSAGE", "NEW MESSAGE"], acc="RESPOND IMMEDIATELY.")),
    ("You don't have to accept every invitation.", "list", dict(items=["EVERY INVITATION"], mode="strike", acc="ACCEPT INVITATION.")),
    ("You don't have to constantly explain yourself.", "doc", dict(title="EXPLANATION", empty=True, stamp="NOT OWED", acc="CONSTANTLY EXPLAIN")),
    ("You can create boundaries.", "shield", dict(front="BOUNDARY", back="YOUR PEACE", acc="BOUNDARIES.")),
    ("You can take time.", "hourglass", dict(acc="TIME.")),
    ("You can choose where your energy goes.", "compass", dict(lbl="YOUR ENERGY", acc="CHOOSE ENERGY")),
    ("But remember…", "pulse", dict(acc="REMEMBER…")),
    ("Protecting your peace isn't avoiding every difficult situation.", "scale", dict(left="PEACE", right="AVOIDANCE", tip=0, acc="PEACE ISN'T AVOIDING")),
    ("Sometimes peace comes from addressing the problem…", "quote", dict(text="LET'S TALK ABOUT IT.", acc="PEACE ADDRESSING")),
    ("Instead of continuously avoiding it.", "path", dict(kind="winding", acc="CONTINUOUSLY AVOIDING")),
    ("Choose calm wisely.", "sunrise", dict(acc="CALM WISELY.")),
    ("Don't confuse peace with escape.", "scale", dict(left="PEACE", right="ESCAPE", tip=0, acc="PEACE ESCAPE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
