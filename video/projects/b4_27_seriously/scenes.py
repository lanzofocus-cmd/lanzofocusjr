from kit import build, follow_sub

TITLE = ("THE MOMENT YOU STOP TAKING", "YOURSELF TOO SERIOUSLY")
OUTPUT = "117_Stop_Taking_Yourself_Too_Seriously_16x9.mp4"
SPEC = [
    ("You made a mistake.", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKE.")),
    ("You embarrassed yourself.", "stage", dict(lbl="EMBARRASSED", performing=False, acc="EMBARRASSED")),
    ("You said something awkward.", "quote", dict(text="...WHY DID I SAY THAT?", acc="AWKWARD.")),
    ("And suddenly…", "pulse", dict()),
    ("You act like the world has ended.", "chart", dict(kind="down", lbl="THE WORLD", acc="WORLD ENDED.")),
    ("But imagine how much easier life would be…", "sunrise", dict(acc="EASIER")),
    ("If you could laugh at yourself sometimes.", "bubbles", dict(texts=["HAHA, CLASSIC ME."], inverted=True, acc="LAUGH")),
    ("Not because mistakes don't matter.", "list", dict(items=["MISTAKES MATTER"], mode="check", acc="NOT MATTER.")),
    ("But because not every mistake deserves a permanent emotional punishment.", "cage", dict(words=["ONE MISTAKE"], acc="PERMANENT PUNISHMENT.")),
    ("You can learn.", "list", dict(items=["LEARN"], mode="check", acc="LEARN.")),
    ("Apologize if necessary.", "list", dict(items=["LEARN", "APOLOGIZE"], mode="check", acc="APOLOGIZE")),
    ("Improve.", "list", dict(items=["LEARN", "APOLOGIZE", "IMPROVE"], mode="check", acc="IMPROVE.")),
    ("And move forward.", "path", dict(kind="straight", acc="FORWARD.")),
    ("The ability to take yourself seriously when it matters…", "gauge", dict(lbl="SERIOUS", start=0.2, end=0.9, acc="SERIOUSLY MATTERS…")),
    ("And lightly when it doesn't…", "gauge", dict(lbl="LIGHT", start=0.9, end=0.15, acc="LIGHTLY DOESN'T…")),
    ("Is a valuable skill.", "key", dict(lbl="A RARE SKILL", acc="VALUABLE SKILL.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
