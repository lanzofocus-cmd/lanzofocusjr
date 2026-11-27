from kit import build, follow_sub

TITLE = ("THE THINGS YOU DON'T SAY CAN", "CHANGE YOUR RELATIONSHIPS")
OUTPUT = "103_The_Things_You_Dont_Say_16x9.mp4"
SPEC = [
    ("You assume people know how you feel.", "brain", dict(says="THEY KNOW.", acc="ASSUME FEEL.")),
    ("You assume they understand why you're upset.", "brain", dict(says="THEY KNOW.", says2="OBVIOUSLY.", acc="ASSUME UPSET.")),
    ("You assume they recognize what matters to you.", "list", dict(items=["WHAT MATTERS"], mode="empty", acc="ASSUME MATTERS")),
    ("But assumptions aren't communication.", "scale", dict(left="ASSUMPTION", right="COMMUNICATION", tip=0, acc="ASSUMPTIONS AREN'T COMMUNICATION.")),
    ("And silence can create a distance…", "crowd", dict(n=2, acc="SILENCE DISTANCE…")),
    ("That neither person intended.", "map", dict(a_lbl="YOU", b_lbl="THEM", acc="NEITHER INTENDED.")),
    ("A small misunderstanding becomes a pattern.", "dots", dict(connect=True, acc="MISUNDERSTANDING PATTERN.")),
    ("A pattern becomes resentment.", "cage", dict(words=["RESENTMENT"], acc="RESENTMENT.")),
    ("And eventually…", "pulse", dict()),
    ("Two people may be reacting to stories they created about each other.", "bubbles", dict(texts=["SHE DOESN'T CARE.", "HE'S IGNORING ME."], acc="STORIES CREATED")),
    ("If something matters…", "key", dict(lbl="IT MATTERS", acc="MATTERS…")),
    ("Say it.", "quote", dict(text="THIS MATTERS TO ME.", acc="SAY")),
    ("Not aggressively.", "list", dict(items=["AGGRESSIVELY"], mode="strike", acc="NOT AGGRESSIVELY.")),
    ("Not perfectly.", "list", dict(items=["AGGRESSIVELY", "PERFECTLY"], mode="strike", acc="NOT PERFECTLY.")),
    ("Honestly.", "list", dict(items=["HONESTLY"], mode="check", acc="HONESTLY.")),
    ("A conversation you avoid today can become a problem you carry tomorrow.", "receipt", dict(items=[("AVOIDED TODAY", "$0"), ("CARRIED TOMORROW", "$$$")], acc="AVOID CARRY TOMORROW.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
