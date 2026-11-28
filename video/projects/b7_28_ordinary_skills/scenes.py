from kit import build, follow_sub, hook

TITLE = ("STOP UNDERESTIMATING", "ORDINARY SKILLS")
OUTPUT = "228_Why_You_Should_Stop_Underestimating_Ordinary_Skills_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Some skills look ordinary.", "list", dict(items=["ORDINARY"], mode="tag", tag="?", acc="ORDINARY")),
    ("Knowing how to communicate.", "list", dict(items=["COMMUNICATING"], mode="check", acc="COMMUNICATE")),
    ("Being organized.", "list", dict(items=["COMMUNICATING", "ORGANIZED"], mode="check", acc="ORGANIZED")),
    ("Showing up on time.", "list", dict(items=["COMMUNICATING", "ORGANIZED", "ON TIME"], mode="check", acc="TIME")),
    ("Managing money responsibly.", "list", dict(items=["COMMUNICATING", "ORGANIZED", "ON TIME", "MONEY"], mode="check", acc="MONEY")),
    ("Listening carefully.", "list", dict(items=["COMMUNICATING", "ORGANIZED", "ON TIME", "MONEY", "LISTENING"], mode="check", acc="LISTENING")),
    ("Admitting when you're wrong.", "quote", dict(text="I WAS WRONG.", acc="WRONG")),
    ("Handling disagreements.", "scale", dict(left="ME", right="YOU", tip=0, acc="DISAGREEMENTS")),
    ("But these ordinary skills influence nearly every area of your life.", "network", dict(nodes=["WORK", "MONEY", "FRIENDS", "FAMILY", "HEALTH"], tangled=False, acc="ORDINARY EVERY")),
    ("You can have incredible talent…", "crown", dict(lbl="TALENT", acc="TALENT")),
    ("And struggle because you can't communicate.", "bubbles", dict(texts=["...?"], acc="STRUGGLE COMMUNICATE")),
    ("You can have great ideas…", "brain", dict(says="GREAT IDEA!", acc="IDEAS")),
    ("And struggle because you can't organize them.", "tangle", dict(lbl="DISORGANIZED", acc="ORGANIZE")),
    ("You can be intelligent…", "book", dict(chapter="SMART", acc="INTELLIGENT")),
    ("And struggle because you refuse to listen.", "shield", dict(front="NOT LISTENING", back="EGO", acc="REFUSE LISTEN")),
    ("The skills that create a successful life aren't always the most exciting ones.", "stage", dict(lbl="NOT EXCITING", empty=True, acc="SUCCESSFUL EXCITING")),
    ("Sometimes they're the skills that quietly prevent problems.", "shield", dict(front="ORDINARY SKILLS", back="YOUR LIFE", drop=True, acc="QUIETLY PREVENT")),
    ("Don't only focus on becoming extraordinary at something.", "crown", dict(lbl="EXTRAORDINARY", acc="EXTRAORDINARY")),
    ("Learn how to become reliable at ordinary things too.", "bricks", dict(rows=4, lbl="RELIABLE", uneven=False, acc="RELIABLE ORDINARY")),
    ("Which ordinary skill do you think is secretly one of the most important skills in life?", "cta", dict(kind="comment", lbl="THE SECRET SKILL", acc="ORDINARY SECRETLY IMPORTANT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="LOOKS IMPRESSIVE", start=60, end=8, lbl2="ACTUALLY MATTERS", start2=20, end2=98, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
