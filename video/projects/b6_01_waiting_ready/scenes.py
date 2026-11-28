from kit import build, follow_sub, hook

TITLE = ("THE TRAP OF WAITING", "UNTIL YOU'RE READY")
OUTPUT = "191_The_Trap_Of_Waiting_Until_Youre_Ready_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("There is a dangerous sentence that sounds responsible.", "doc", dict(title="RESPONSIBLE?", empty=True, acc="DANGEROUS RESPONSIBLE")),
    ("\"I'm just waiting until I'm ready.\"", "quote", dict(text="I'M JUST WAITING UNTIL I'M READY.", acc="WAITING READY")),
    ("Waiting until you're more confident.", "hud", dict(lbl="CONFIDENCE", start=10, end=34, icons=None, crowd=0, acc="CONFIDENT")),
    ("Waiting until you understand everything.", "book", dict(chapter="EVERYTHING", text="PAGE 1 OF 900", acc="UNDERSTAND EVERYTHING")),
    ("Waiting until you have the perfect plan.", "doc", dict(title="THE PLAN", empty=False, stamp="NOT PERFECT", acc="PERFECT PLAN")),
    ("Waiting until the fear disappears.", "fog", dict(lbl="FEAR", acc="FEAR DISAPPEARS")),
    ("And the problem is…", "pulse", dict(acc="PROBLEM")),
    ("Readiness is often something you expect to feel before doing something that can only teach you how to become ready.", "loop", dict(items=["FEEL READY", "START", "LEARN", "BECOME READY"], lbl="BACKWARDS?", acc="READINESS FEEL TEACH READY")),
    ("Think about learning to swim.", "water", dict(lbl="LEARNING TO SWIM", acc="SWIM")),
    ("You can watch videos about swimming for months.", "frame", dict(who="SWIM TUTORIAL #48", acc="WATCH MONTHS")),
    ("You can understand the movements.", "brain", dict(says="KICK. BREATHE. REACH.", acc="UNDERSTAND MOVEMENTS")),
    ("You can memorize the techniques.", "list", dict(items=["FREESTYLE", "BREATHING", "KICKING"], mode="check", acc="MEMORIZE TECHNIQUES")),
    ("But eventually, you have to get into the water.", "water", dict(inside=True, ripples=True, acc="WATER")),
    ("And the first time won't be perfect.", "chart", dict(kind="wave", lbl="ATTEMPT #1", acc="FIRST PERFECT")),
    ("You'll make mistakes.", "list", dict(items=["MISTAKE"], mode="strike", acc="MISTAKES")),
    ("You'll feel uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.8, acc="UNCOMFORTABLE")),
    ("You'll discover things that no tutorial could have prepared you for.", "iceberg", dict(top="THE TUTORIAL", bottom="THE REAL THING", acc="DISCOVER TUTORIAL")),
    ("That's how almost everything meaningful works.", "network", dict(nodes=["SKILLS", "CAREERS", "FRIENDSHIPS", "IDEAS", "DREAMS"], tangled=False, acc="EVERYTHING MEANINGFUL")),
    ("You don't become confident before every challenge.", "hud", dict(lbl="CONFIDENCE", start=12, end=12, icons=None, crowd=0, tag="BEFORE", acc="CONFIDENT BEFORE")),
    ("Sometimes confidence is the result of surviving the challenge.", "hud", dict(lbl="CONFIDENCE", start=12, end=88, icons=None, crowd=0, tag="AFTER", acc="CONFIDENCE RESULT SURVIVING")),
    ("You don't become experienced before starting.", "startline", dict(behind=False, acc="EXPERIENCED STARTING")),
    ("Starting is how experience begins.", "stairs", dict(n=7, climb=2, acc="STARTING EXPERIENCE BEGINS")),
    ("You don't need to know every step of the journey.", "path", dict(kind="winding", fog=True, acc="EVERY STEP")),
    ("You need to know enough to take the first one.", "stairs", dict(n=7, climb=1, highlight=0, acc="ENOUGH FIRST")),
    ("Because the person waiting for perfect readiness and the person taking imperfect action are both uncertain.", "fog", dict(lbl="BOTH UNCERTAIN", acc="WAITING IMPERFECT BOTH UNCERTAIN")),
    ("But only one of them is learning.", "beam", dict(drop=True, lbl="LEARNING", crowd=1, acc="ONLY LEARNING")),
    ("So stop treating uncertainty like a stop sign.", "door", dict(open_=True, lbl="UNCERTAINTY", acc="UNCERTAINTY STOP")),
    ("Sometimes it's simply the beginning.", "sunrise", dict(acc="BEGINNING")),
    ("What's something you've been waiting to feel ready for?", "hourglass", dict(acc="WAITING READY")),
    ("Tell us in the comments.", "cta", dict(kind="comment", lbl="WHAT YOU'RE WAITING FOR", acc="COMMENTS")),
    ("And follow LanzoFocus for ideas that help you think differently and move forward.", "follow"),
]
_HOOK = ("hud", dict(lbl="READY", start=0, end=99, icons=None, crowd=6, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
