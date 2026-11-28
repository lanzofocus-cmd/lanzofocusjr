from kit import build, follow_sub, hook

TITLE = ("AN EXCUSE VS", "AN EXPLANATION")
OUTPUT = "278_The_Difference_Between_An_Excuse_And_An_Explanation_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often confuse explanations with excuses.", "scale", dict(left="EXPLANATION", right="EXCUSE", tip=0, acc="CONFUSE EXPLANATIONS EXCUSES")),
    ("An explanation helps you understand why something happened.", "key", dict(lbl="EXPLANATION", acc="EXPLANATION UNDERSTAND")),
    ("An excuse is sometimes used to avoid responsibility.", "shield", dict(front="EXCUSE", back="RESPONSIBILITY", acc="EXCUSE AVOID RESPONSIBILITY")),
    ("But the difference isn't always obvious.", "fog", dict(lbl="BLURRY LINE", acc="DIFFERENCE OBVIOUS")),
    ("Imagine missing a deadline.", "doc", dict(title="DEADLINE", empty=False, stamp="MISSED", acc="DEADLINE")),
    ("You explain that you misunderstood the instructions.", "bubbles", dict(texts=["I MISREAD THE BRIEF."], acc="MISUNDERSTOOD INSTRUCTIONS")),
    ("That information can help you understand the problem.", "puzzle", dict(missing=False, lbl="UNDERSTOOD", acc="INFORMATION PROBLEM")),
    ("But if you use the misunderstanding to avoid taking responsibility for what happened…", "shield", dict(front="NOT MY FAULT", back="YOU", acc="AVOID RESPONSIBILITY")),
    ("Then the explanation becomes an excuse.", "shed", dict(old="EXPLANATION", new="EXCUSE", acc="EXPLANATION EXCUSE")),
    ("The purpose of understanding why something happened…", "question", dict(a_lbl="WHY", b_lbl="IT HAPPENED", acc="PURPOSE WHY")),
    ("Should be to help you make a better decision next time.", "stairs", dict(n=6, climb=2, drop=True, acc="BETTER NEXT")),
    ("You can acknowledge difficult circumstances.", "list", dict(items=["CIRCUMSTANCES"], mode="check", acc="ACKNOWLEDGE CIRCUMSTANCES")),
    ("You can recognize limitations.", "list", dict(items=["CIRCUMSTANCES", "LIMITATIONS"], mode="check", acc="LIMITATIONS")),
    ("You can explain what happened.", "list", dict(items=["CIRCUMSTANCES", "LIMITATIONS", "WHAT HAPPENED"], mode="check", acc="EXPLAIN")),
    ("And still take responsibility for the parts you control.", "list", dict(items=["CIRCUMSTANCES", "LIMITATIONS", "WHAT HAPPENED", "MY PART"], mode="check", acc="RESPONSIBILITY CONTROL")),
    ("Understanding the cause of a problem doesn't remove responsibility.", "iceberg", dict(top="THE CAUSE", bottom="YOUR RESPONSIBILITY", acc="CAUSE REMOVE RESPONSIBILITY")),
    ("It can make responsibility more effective.", "hud", dict(lbl="EFFECTIVENESS", start=20, end=90, icons=None, crowd=0, acc="RESPONSIBILITY EFFECTIVE")),
    ("What do you think is the clearest difference between explaining a mistake and making an excuse?", "cta", dict(kind="comment", lbl="EXPLAIN VS EXCUSE", acc="CLEAREST EXPLAINING EXCUSE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="REASONS GIVEN", start=10, end=95, lbl2="RESPONSIBILITY TAKEN", start2=60, end2=5, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
