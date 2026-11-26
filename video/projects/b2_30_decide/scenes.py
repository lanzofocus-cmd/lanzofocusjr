from kit import build, follow_sub

TITLE = ("WHAT IF YOUR LIFE IS", "WAITING FOR YOU TO DECIDE?")
OUTPUT = "40_What_If_Your_Life_Is_Waiting_For_You_To_Decide_16x9.mp4"
SPEC = [
    ("What if the biggest thing holding you back…", "cage", dict(words=["?"], acc="BIGGEST BACK…")),
    ("Isn't a lack of opportunity?", "door", dict(lbl="OPPORTUNITY", acc="OPPORTUNITY?")),
    ("Isn't a lack of talent?", "gauge", dict(lbl="TALENT", start=0.6, end=0.65, acc="TALENT?")),
    ("Isn't a lack of time?", "hourglass", dict(acc="TIME?")),
    ("What if it's simply that you haven't made a decision…", "path", dict(kind="fork", labels=("STAY", "GO"), acc="HAVEN'T DECISION…")),
    ("That you're willing to follow through on?", "doc", dict(title="DECISION", empty=False, stamp="COMMITTED", acc="FOLLOW THROUGH")),
    ("Because once you decide…", "big", dict(text="DECIDE", acc="DECIDE…")),
    ("Your excuses become clearer.", "sticker", dict(tags=["TOO BUSY", "NOT READY", "LATER"], strike=True, acc="EXCUSES CLEARER.")),
    ("Your priorities become easier to recognize.", "network", dict(nodes=["NOISE", "NOISE", "PRIORITY", "NOISE", "NOISE"], focus=2, tangled=False, acc="PRIORITIES EASIER")),
    ("Your next step becomes easier to see.", "stairs", dict(n=6, climb=0, highlight=0, acc="NEXT STEP")),
    ("You don't need to know every step of the journey.", "path", dict(kind="dashed", fog=True, acc="EVERY STEP")),
    ("You need to decide that you're no longer standing still.", "alone", dict(tag="NOT STANDING STILL", acc="DECIDE NO LONGER")),
    ("And then…", "pulse", dict()),
    ("Take the first step.", "stairs", dict(n=6, climb=1, acc="FIRST STEP.")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
