from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO ONLY APPEAR", "WHEN YOU'RE USEFUL")
OUTPUT = "203_The_People_Who_Only_Appear_When_Youre_Useful_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("There's a difference between someone who values you…", "crowd", dict(n=3, highlight=1, highlight_label="YOU", acc="VALUES YOU")),
    ("And someone who values what you provide.", "receipt", dict(items=[("FAVORS", "YOU"), ("HELP", "YOU"), ("RIDES", "YOU")], total="WHAT YOU PROVIDE", acc="PROVIDE")),
    ("Maybe they only contact you when they need help.", "notifs", dict(items=["CAN YOU HELP ME?"], acc="ONLY NEED")),
    ("Maybe they disappear when you need support.", "alone", dict(tag="NEED SUPPORT", acc="DISAPPEAR SUPPORT")),
    ("Maybe every conversation somehow becomes about their problems, their goals, or their needs.", "bubbles", dict(texts=["ANYWAY, ABOUT ME...", "MY PROBLEM IS..."], acc="PROBLEMS GOALS NEEDS")),
    ("At first, you may not notice.", "fog", dict(lbl="HARD TO SEE", acc="NOTICE")),
    ("You might think you're simply being helpful.", "list", dict(items=["BEING HELPFUL"], mode="check", acc="HELPFUL")),
    ("But over time, you begin realizing that the relationship only seems to exist when you have something to offer.", "battery", dict(lbl="YOUR USEFULNESS", start=1.0, end=0.1, drains=3, acc="EXIST OFFER")),
    ("That's worth paying attention to.", "pulse", dict(acc="ATTENTION")),
    ("Relationships shouldn't feel like a transaction where your value depends on your usefulness.", "price", dict(text="YOUR VALUE?", sub="NOT A TRANSACTION", acc="TRANSACTION USEFULNESS")),
    ("You can help people.", "list", dict(items=["HELP"], mode="check", acc="HELP")),
    ("You can be generous.", "list", dict(items=["HELP", "BE GENEROUS"], mode="check", acc="GENEROUS")),
    ("You can be supportive.", "list", dict(items=["HELP", "BE GENEROUS", "BE SUPPORTIVE"], mode="check", acc="SUPPORTIVE")),
    ("But you also deserve relationships where people are interested in how you're doing when they don't need anything.", "bubbles", dict(texts=["HOW ARE YOU, REALLY?"], drop=True, acc="DESERVE INTERESTED ANYTHING")),
    ("Where your presence matters.", "crowd", dict(n=5, highlight=2, highlight_label="MATTERS", acc="PRESENCE")),
    ("Where someone remembers to check on you.", "notifs", dict(items=["JUST CHECKING ON YOU"], acc="CHECK")),
    ("Where you aren't constantly proving that you're worth keeping around.", "stage", dict(lbl="NO AUDITION", empty=True, acc="PROVING WORTH")),
    ("Pay attention to who makes space for you…", "ring", dict(tags=["MAKES SPACE"], acc="SPACE")),
    ("Not just who takes space from you.", "battery", dict(lbl="YOUR SPACE", start=0.9, end=0.2, drains=3, acc="TAKES")),
    ("What do you think makes a relationship genuinely valuable beyond what people can do for each other?", "cta", dict(kind="comment", lbl="WHAT MAKES IT VALUABLE", acc="GENUINELY VALUABLE")),
    ("", "follow"),
]
_HOOK = ("battery", dict(lbl="YOUR VALUE TO THEM", start=1.0, end=0.05, drains=5))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
