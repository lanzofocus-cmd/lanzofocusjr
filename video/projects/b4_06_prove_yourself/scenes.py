from kit import build, follow_sub

TITLE = ("THE PERSON YOU KEEP TRYING", "TO PROVE YOURSELF TO")
OUTPUT = "96_The_Person_You_Keep_Trying_To_Prove_Yourself_To_16x9.mp4"
SPEC = [
    ("You might be spending years trying to prove something…", "timeline", dict(n=10, progress=0.7, tag="PROVING IT", acc="YEARS PROVE")),
    ("To someone who isn't even paying attention anymore.", "chairs", dict(lbl="THEY LEFT", acc="ISN'T ATTENTION ANYMORE.")),
    ("Maybe they doubted you.", "quote", dict(text="YOU WON'T MAKE IT.", acc="DOUBTED")),
    ("Maybe they rejected you.", "door", dict(closing=True, lbl="REJECTED", acc="REJECTED")),
    ("Maybe they made you feel incapable.", "sticker", dict(tags=["INCAPABLE"], acc="INCAPABLE.")),
    ("And now every achievement is secretly an attempt to answer them.", "list", dict(items=["ACHIEVED → FOR THEM", "ACHIEVED → FOR THEM"], mode="check", acc="SECRETLY ANSWER")),
    ("But what happens when you finally succeed?", "stage", dict(lbl="YOU MADE IT", acc="FINALLY SUCCEED?")),
    ("Will you feel satisfied…", "gauge", dict(lbl="SATISFIED?", start=0.3, end=0.5, acc="SATISFIED…")),
    ("Or will you still need another person to acknowledge it?", "crowd", dict(n=5, dim=True, acc="STILL ACKNOWLEDGE")),
    ("At some point…", "pulse", dict()),
    ("You have to stop building your life as a response to someone else's opinion.", "bricks", dict(rows=3, lbl="BUILT FOR THEM?", uneven=True, acc="STOP RESPONSE OPINION.")),
    ("Your success should eventually belong to you—not to the person you wanted to impress.", "crown", dict(lbl="YOURS", acc="BELONG")),
    ("Save this if you're ready to stop chasing approval.", "cta", dict(kind="save", acc="SAVE APPROVAL.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
