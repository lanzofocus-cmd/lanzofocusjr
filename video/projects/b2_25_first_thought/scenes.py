from kit import build, follow_sub

TITLE = ("YOU CAN'T CONTROL", "THE FIRST THOUGHT")
OUTPUT = "35_You_Cant_Control_The_First_Thought_16x9.mp4"
SPEC = [
    ("A thought can appear without permission.", "brain", dict(says="WHAT IF...?", acc="THOUGHT PERMISSION.")),
    ("A doubt.", "brain", dict(says="A DOUBT", acc="DOUBT.")),
    ("A fear.", "brain", dict(says="A DOUBT", says2="A FEAR", acc="FEAR.")),
    ("A memory.", "bubbles", dict(texts=["A DOUBT", "A FEAR", "A MEMORY"], center="brain", acc="MEMORY.")),
    ("A negative assumption.", "bubbles", dict(texts=["A DOUBT", "A FEAR", "A MEMORY", "THEY HATE ME"], center="brain", acc="NEGATIVE ASSUMPTION.")),
    ("You don't always control what enters your mind.", "door", dict(open_=True, lbl="YOUR MIND", figure=False, acc="CONTROL ENTERS")),
    ("But you don't have to accept every thought as truth.", "doc", dict(title="TRUTH?", empty=True, stamp="UNVERIFIED", acc="ACCEPT TRUTH.")),
    ("A thought is not a fact.", "scale", dict(left="THOUGHT", right="FACT", tip=0, acc="NOT FACT.")),
    ("A feeling is not a prediction.", "scale", dict(left="FEELING", right="PREDICTION", tip=0, acc="NOT PREDICTION.")),
    ("And an assumption isn't proof.", "scale", dict(left="ASSUMPTION", right="PROOF", tip=0, acc="ISN'T PROOF.")),
    ("Instead of asking…", "pulse", dict()),
    ("\"Why am I thinking this?\"", "quote", dict(text="WHY AM I THINKING THIS?", acc="\"WHY")),
    ("Try asking…", "pulse", dict(acc="TRY")),
    ("\"Is this actually true?\"", "quote", dict(text="IS THIS ACTUALLY TRUE?", acc="TRUE?\"")),
    ("Sometimes the most powerful thing you can do…", "key", dict(lbl="POWER", acc="POWERFUL")),
    ("Is stop believing everything your mind tells you.", "bubbles", dict(texts=["YOU'LL FAIL.", "THEY HATE YOU."], center="brain", acc="STOP BELIEVING EVERYTHING")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
