from kit import build, follow_sub

TITLE = ("THE WORST THING YOU", "CAN DO IS BECOME NUMB")
OUTPUT = "91_The_Worst_Thing_You_Can_Do_Is_Become_Numb_16x9.mp4"
SPEC = [
    ("The most dangerous thing isn't always when your life goes wrong.", "chart", dict(kind="down", lbl="WHEN IT GOES WRONG", acc="DANGEROUS ISN'T")),
    ("Sometimes it's when things go wrong…", "chart", dict(kind="wave", lbl="LIFE", acc="WRONG…")),
    ("And you stop caring.", "gauge", dict(lbl="CARING", start=0.7, end=0.02, acc="STOP CARING.")),
    ("You stop expecting anything.", "list", dict(items=["EXPECTING"], mode="strike", acc="EXPECTING")),
    ("You stop trying to improve things.", "list", dict(items=["EXPECTING", "IMPROVING"], mode="strike", acc="IMPROVE")),
    ("You stop believing your choices matter.", "list", dict(items=["EXPECTING", "IMPROVING", "CHOICES MATTER"], mode="strike", acc="CHOICES MATTER.")),
    ("Not because you found peace…", "sunrise", dict(acc="NOT PEACE…")),
    ("But because disappointment taught you to expect nothing.", "progress", dict(lbl="EXPECTATIONS", value=0.02, acc="DISAPPOINTMENT NOTHING.")),
    ("And slowly, without noticing…", "pulse", dict(acc="SLOWLY")),
    ("You stop living with intention.", "compass", dict(lbl="INTENTION", settle=False, acc="INTENTION.")),
    ("You become a spectator in your own life.", "chairs", dict(lbl="SPECTATOR", acc="SPECTATOR OWN")),
    ("Don't confuse numbness with acceptance.", "scale", dict(left="NUMBNESS", right="ACCEPTANCE", tip=0, acc="NUMBNESS ACCEPTANCE.")),
    ("You can acknowledge that life is difficult…", "mirror", dict(reflect="solid", lbl="IT'S HARD", acc="ACKNOWLEDGE DIFFICULT…")),
    ("Without surrendering your ability to care.", "key", dict(lbl="YOU STILL CARE", acc="WITHOUT SURRENDERING CARE.")),
    ("If this hit something you've been feeling, save it.", "cta", dict(kind="save", acc="SAVE")),
    ("And remember: you don't have to stop caring just because things haven't gone your way.", "plant", dict(height=0.5, roots=True, lbl="STILL CARING", acc="DON'T STOP CARING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
