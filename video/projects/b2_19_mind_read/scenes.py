from kit import build, follow_sub

TITLE = ("PEOPLE CAN'T", "READ YOUR MIND")
OUTPUT = "29_People_Cant_Read_Your_Mind_16x9.mp4"
SPEC = [
    ("You expect people to understand.", "brain", dict(says="THEY SHOULD KNOW.", acc="EXPECT UNDERSTAND.")),
    ("To notice.", "crowd", dict(n=5, highlight=2, highlight_label="NOTICE ME", acc="NOTICE.")),
    ("To know when you're upset.", "brain", dict(says="I'M UPSET.", says2="(UNSAID)", acc="UPSET.")),
    ("To recognize what you need.", "list", dict(items=["WHAT YOU NEED"], mode="empty", acc="NEED.")),
    ("But people aren't mind readers.", "big", dict(text="NOT MIND READERS", acc="AREN'T MIND READERS.")),
    ("Sometimes the problem isn't that they don't care.", "bubbles", dict(texts=["I CARE.", "WHAT'S WRONG?"], acc="ISN'T CARE.")),
    ("It's that you never communicated.", "doc", dict(title="MESSAGE", empty=True, stamp="NEVER SENT", acc="NEVER COMMUNICATED.")),
    ("Speak honestly.", "quote", dict(text="HERE'S HOW I FEEL.", acc="HONESTLY.")),
    ("Ask clearly.", "quote", dict(text="CAN YOU HELP ME?", acc="CLEARLY.")),
    ("Set boundaries.", "shield", dict(front="BOUNDARY", back="YOUR PEACE", acc="BOUNDARIES.")),
    ("Explain what matters.", "quote", dict(text="THIS MATTERS TO ME.", acc="MATTERS.")),
    ("Silence can protect you from an uncomfortable conversation…", "lock", dict(lbl="SILENCE", acc="SILENCE PROTECT")),
    ("But it can also create misunderstandings that never needed to exist.", "tangle", dict(lbl="MISUNDERSTANDINGS", acc="MISUNDERSTANDINGS NEVER")),
    ("Don't expect people to understand a message you never sent.", "notifs", dict(items=["DRAFT: UNSENT"], acc="MESSAGE NEVER SENT.")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
