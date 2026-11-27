from kit import build, follow_sub

TITLE = ("YOU'RE NOT AS POWERLESS", "AS YOU FEEL")
OUTPUT = "111_Youre_Not_As_Powerless_As_You_Feel_16x9.mp4"
SPEC = [
    ("You can't control everything.", "big", dict(text="EVERYTHING?", acc="CAN'T EVERYTHING.")),
    ("You can't control people's opinions.", "list", dict(items=["OPINIONS"], mode="strike", acc="OPINIONS.")),
    ("Their decisions.", "list", dict(items=["OPINIONS", "THEIR DECISIONS"], mode="strike", acc="DECISIONS.")),
    ("The past.", "list", dict(items=["OPINIONS", "THEIR DECISIONS", "THE PAST"], mode="strike", acc="PAST.")),
    ("Unexpected events.", "list", dict(items=["OPINIONS", "THEIR DECISIONS", "THE PAST", "SURPRISES"], mode="strike", acc="UNEXPECTED")),
    ("But sometimes…", "pulse", dict()),
    ("When you focus entirely on what you can't control…", "tangle", dict(lbl="OUT OF YOUR HANDS", acc="ENTIRELY CAN'T")),
    ("You forget the things you can.", "key", dict(lbl="WHAT YOU CAN", acc="FORGET CAN.")),
    ("Your response.", "list", dict(items=["YOUR RESPONSE"], mode="check", acc="RESPONSE.")),
    ("Your effort.", "list", dict(items=["YOUR RESPONSE", "YOUR EFFORT"], mode="check", acc="EFFORT.")),
    ("Your boundaries.", "list", dict(items=["YOUR RESPONSE", "YOUR EFFORT", "BOUNDARIES"], mode="check", acc="BOUNDARIES.")),
    ("Your next decision.", "list", dict(items=["YOUR RESPONSE", "YOUR EFFORT", "BOUNDARIES", "NEXT DECISION"], mode="check", acc="NEXT DECISION.")),
    ("Your willingness to learn.", "list", dict(items=["YOUR RESPONSE", "YOUR EFFORT", "BOUNDARIES", "NEXT DECISION", "LEARNING"], mode="check", acc="LEARN.")),
    ("You may not control the entire situation.", "network", dict(nodes=["PEOPLE", "EVENTS", "PAST", "LUCK", "TIMING"], tangled=True, acc="ENTIRE SITUATION.")),
    ("But that doesn't mean you have no influence.", "gauge", dict(lbl="YOUR INFLUENCE", start=0.0, end=0.55, acc="DOESN'T INFLUENCE.")),
    ("Don't let the things you cannot control…", "cage", dict(words=["CAN'T CONTROL"], acc="CANNOT CONTROL…")),
    ("Make you forget the things you still can.", "key", dict(lbl="STILL YOURS", acc="FORGET STILL CAN.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
