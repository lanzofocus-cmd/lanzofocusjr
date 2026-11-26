from kit import build, follow_sub

TITLE = ("YOUR BRAIN IS", "LYING TO YOU")
OUTPUT = "02_Your_Brain_Is_Lying_To_You_16x9.mp4"
SPEC = [
    ("Your brain will convince you that you're not ready…", "brain", dict(says="YOU'RE NOT READY.", acc="BRAIN READY…")),
    ("That you're not talented enough…", "brain", dict(says="YOU'RE NOT READY.", says2="NOT TALENTED ENOUGH.", acc="TALENTED")),
    ("That you should wait until you feel confident.", "gauge", dict(lbl="CONFIDENCE", start=0.1, end=0.15, acc="WAIT CONFIDENT.")),
    ("But confidence isn't a prerequisite for beginning.", "doc", dict(title="REQUIREMENTS", empty=True, stamp="NONE", acc="ISN'T")),
    ("It's often the result of beginning.", "gauge", dict(lbl="CONFIDENCE", start=0.1, end=0.85, acc="RESULT")),
    ("Your brain wants certainty.", "lock", dict(lbl="CERTAINTY", acc="CERTAINTY.")),
    ("It wants safety.", "alone", dict(tag="SAFE ZONE", acc="SAFETY.")),
    ("It wants proof that everything will work out before you take the risk.", "doc", dict(title="PROOF", empty=True, acc="PROOF")),
    ("But life doesn't give you that proof.", "doc", dict(title="PROOF", empty=True, stamp="NOT INCLUDED", acc="DOESN'T")),
    ("You have to move without it.", "path", dict(kind="dashed", fog=True, acc="MOVE")),
    ("Because sometimes…", "pulse", dict()),
    ("The only thing standing between you and the person you could become…", "shed", dict(old="YOU NOW", new="WHO YOU COULD BE", acc="BETWEEN")),
    ("Is a thought you believed without questioning.", "bubbles", dict(texts=["I CAN'T."], center="brain", acc="THOUGHT QUESTIONING.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
