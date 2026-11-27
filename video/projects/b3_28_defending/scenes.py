from kit import build, follow_sub

TITLE = ("THE THINGS YOU", "KEEP DEFENDING")
OUTPUT = "68_The_Things_You_Keep_Defending_16x9.mp4"
SPEC = [
    ("Sometimes…", "pulse", dict()),
    ("The things you defend the most…", "shield", dict(front="DEFENDING", back="?", acc="DEFEND MOST…")),
    ("Are the things you should examine the most.", "doc", dict(title="EXAMINE", empty=False, acc="EXAMINE")),
    ("Your excuses.", "list", dict(items=["EXCUSES"], mode="empty", acc="EXCUSES.")),
    ("Your habits.", "list", dict(items=["EXCUSES", "HABITS"], mode="empty", acc="HABITS.")),
    ("Your assumptions.", "list", dict(items=["EXCUSES", "HABITS", "ASSUMPTIONS"], mode="empty", acc="ASSUMPTIONS.")),
    ("Your decisions.", "list", dict(items=["EXCUSES", "HABITS", "ASSUMPTIONS", "DECISIONS"], mode="empty", acc="DECISIONS.")),
    ("Because if something is genuinely helping you…", "chart", dict(kind="up", lbl="HELPING", acc="GENUINELY HELPING")),
    ("You shouldn't need to constantly convince yourself it's helping.", "bubbles", dict(texts=["IT'S FINE.", "IT'S FINE.", "IT'S FINE."], acc="CONSTANTLY CONVINCE")),
    ("Maybe the habit isn't as harmless as you think.", "sticker", dict(tags=["HARMLESS?"], acc="HARMLESS")),
    ("Maybe the excuse isn't as valid as it sounds.", "doc", dict(title="EXCUSE", empty=False, stamp="VALID?", acc="VALID")),
    ("Maybe the belief you've held for years…", "frame", dict(who="AN OLD BELIEF", acc="BELIEF YEARS…")),
    ("Deserves another look.", "mirror", dict(reflect="solid", lbl="LOOK AGAIN", acc="ANOTHER LOOK.")),
    ("Growth requires more than defending what you already believe.", "plant", dict(height=0.5, roots=False, acc="GROWTH DEFENDING")),
    ("It requires the courage to question it.", "question", dict(acc="COURAGE QUESTION")),
    ("What if the thing you're protecting…", "shield", dict(front="PROTECTING", back="CHANGE", acc="PROTECTING…")),
    ("Is the thing preventing you from changing?", "cage", dict(words=["THE HABIT", "THE EXCUSE"], acc="PREVENTING CHANGING?")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
