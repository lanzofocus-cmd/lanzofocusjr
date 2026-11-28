from kit import build, follow_sub, hook

TITLE = ("THE LIFE THAT LOOKS GOOD", "BUT FEELS WRONG")
OUTPUT = "233_The_Life_That_Looks_Good_But_Feels_Wrong_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine achieving everything you thought you wanted.", "stairs", dict(n=6, climb=6, acc="EVERYTHING WANTED")),
    ("The recognition.", "list", dict(items=["RECOGNITION"], mode="check", acc="RECOGNITION")),
    ("The lifestyle.", "list", dict(items=["RECOGNITION", "LIFESTYLE"], mode="check", acc="LIFESTYLE")),
    ("The achievements.", "list", dict(items=["RECOGNITION", "LIFESTYLE", "ACHIEVEMENTS"], mode="check", acc="ACHIEVEMENTS")),
    ("The attention.", "list", dict(items=["RECOGNITION", "LIFESTYLE", "ACHIEVEMENTS", "ATTENTION"], mode="check", acc="ATTENTION")),
    ("But something feels wrong.", "hud", dict(lbl="LOOKS GOOD", start=100, end=100, lbl2="FEELS GOOD", start2=50, end2=12, icons=None, crowd=0, acc="WRONG")),
    ("You aren't enjoying it.", "gauge", dict(lbl="ENJOYMENT", start=0.5, end=0.1, acc="ENJOYING")),
    ("You feel exhausted.", "battery", dict(lbl="ENERGY", start=0.5, end=0.05, drains=0, acc="EXHAUSTED")),
    ("You don't recognize the reasons you started.", "frame", dict(who="WHY YOU STARTED", fade=True, acc="RECOGNIZE STARTED")),
    ("This can happen when you build a life based entirely on what looks impressive.", "stage", dict(lbl="IMPRESSIVE", acc="ENTIRELY IMPRESSIVE")),
    ("You chase goals because they're admired.", "crown", dict(lbl="ADMIRED", acc="CHASE ADMIRED")),
    ("You make decisions because they sound successful.", "doc", dict(title="DECISION", empty=False, stamp="SOUNDS GOOD", acc="SOUND SUCCESSFUL")),
    ("You follow expectations because they seem reasonable.", "path", dict(kind="straight", acc="EXPECTATIONS REASONABLE")),
    ("But eventually, you need to ask:", "question", dict(acc="ASK")),
    ("\"Do I actually want this?\"", "quote", dict(text="DO I ACTUALLY WANT THIS?", drop=True, acc="ACTUALLY WANT")),
    ("Not:", "arrows", dict(items=["NOT"], acc="")),
    ("\"Would people be impressed?\"", "list", dict(items=["WOULD PEOPLE BE IMPRESSED?"], mode="strike", acc="IMPRESSED")),
    ("Not:", "arrows", dict(items=["NOT"], acc="")),
    ("\"Does this look successful?\"", "list", dict(items=["WOULD PEOPLE BE IMPRESSED?", "DOES THIS LOOK SUCCESSFUL?"], mode="strike", acc="SUCCESSFUL")),
    ("But:", "pulse", dict(acc="")),
    ("\"Is this something I genuinely value?\"", "compass", dict(lbl="WHAT I VALUE", acc="GENUINELY VALUE")),
    ("Your life isn't a performance for an imaginary audience.", "stage", dict(lbl="NO AUDIENCE", empty=True, acc="PERFORMANCE IMAGINARY AUDIENCE")),
    ("Make decisions that have meaning even when nobody is watching.", "alone", dict(tag="MEANINGFUL", acc="MEANING NOBODY WATCHING")),
    ("What is one thing people chase because it looks impressive but might not actually make them happy?", "cta", dict(kind="comment", lbl="LOOKS GOOD, FEELS EMPTY", acc="CHASE IMPRESSIVE HAPPY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="LOOKS SUCCESSFUL", start=20, end=100, lbl2="FEELS RIGHT", start2=80, end2=6, icons="thumb", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
