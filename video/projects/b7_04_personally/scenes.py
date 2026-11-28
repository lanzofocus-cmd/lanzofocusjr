from kit import build, follow_sub, hook

TITLE = ("THE SKILL OF NOT TAKING", "EVERYTHING PERSONALLY")
OUTPUT = "204_The_Skill_Of_Not_Taking_Everything_Personally_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Someone doesn't reply to your message.", "phone", dict(lbl="SEEN 2:14 PM", acc="REPLY")),
    ("Your mind immediately creates a story.", "brain", dict(says="HERE WE GO...", acc="STORY")),
    ("They're ignoring you.", "sticker", dict(tags=["IGNORING ME"], acc="IGNORING")),
    ("They're angry.", "sticker", dict(tags=["IGNORING ME", "ANGRY"], acc="ANGRY")),
    ("They don't care.", "sticker", dict(tags=["IGNORING ME", "ANGRY", "DON'T CARE"], acc="CARE")),
    ("You said something wrong.", "sticker", dict(tags=["IGNORING ME", "ANGRY", "DON'T CARE", "I SAID IT WRONG"], acc="WRONG")),
    ("But you don't actually know.", "question", dict(a_lbl="YOU DON'T", b_lbl="KNOW", acc="ACTUALLY KNOW")),
    ("Maybe they're busy.", "list", dict(items=["BUSY"], mode="check", acc="BUSY")),
    ("Maybe they're tired.", "list", dict(items=["BUSY", "TIRED"], mode="check", acc="TIRED")),
    ("Maybe they haven't seen the message.", "list", dict(items=["BUSY", "TIRED", "HAVEN'T SEEN IT"], mode="check", acc="SEEN")),
    ("Maybe something completely unrelated is happening in their life.", "iceberg", dict(top="NO REPLY", bottom="THEIR WHOLE DAY", acc="UNRELATED")),
    ("The problem is that our minds hate uncertainty.", "fog", dict(lbl="UNCERTAINTY", acc="HATE UNCERTAINTY")),
    ("When information is missing, we often fill the gap with assumptions.", "puzzle", dict(missing=True, lbl="ASSUMPTION", acc="MISSING ASSUMPTIONS")),
    ("And those assumptions can create unnecessary stress.", "gauge", dict(lbl="STRESS", start=0.2, end=0.85, acc="UNNECESSARY STRESS")),
    ("Not every silence is rejection.", "list", dict(items=["SILENCE = REJECTION"], mode="strike", acc="SILENCE REJECTION")),
    ("Not every disagreement is disrespect.", "list", dict(items=["SILENCE = REJECTION", "DISAGREEMENT = DISRESPECT"], mode="strike", acc="DISAGREEMENT DISRESPECT")),
    ("Not every criticism is an attack.", "list", dict(items=["SILENCE = REJECTION", "DISAGREEMENT = DISRESPECT", "CRITICISM = ATTACK"], mode="strike", acc="CRITICISM ATTACK")),
    ("Learning not to take everything personally doesn't mean ignoring genuine mistreatment.", "shield", dict(front="BOUNDARIES", back="YOU", acc="PERSONALLY MISTREATMENT")),
    ("It means separating what actually happened from the story you automatically created around it.", "iceberg", dict(top="WHAT HAPPENED", bottom="THE STORY YOU ADDED", drop=True, acc="SEPARATING HAPPENED STORY")),
    ("Before reacting, ask yourself:", "hourglass", dict(acc="BEFORE REACTING")),
    ("\"What do I know?\"", "list", dict(items=["WHAT DO I KNOW?"], mode="empty", acc="KNOW")),
    ("\"What am I assuming?\"", "list", dict(items=["WHAT DO I KNOW?", "WHAT AM I ASSUMING?"], mode="empty", acc="ASSUMING")),
    ("\"What other explanations could exist?\"", "list", dict(items=["WHAT DO I KNOW?", "WHAT AM I ASSUMING?", "WHAT ELSE COULD IT BE?"], mode="empty", acc="EXPLANATIONS")),
    ("That small distinction can prevent a lot of unnecessary conflict.", "hud", dict(lbl="CONFLICT", start=80, end=10, icons=None, crowd=0, acc="DISTINCTION CONFLICT")),
    ("Save this for the next time your mind starts creating a story without enough evidence.", "cta", dict(kind="save", lbl="CHECK THE STORY", acc="SAVE STORY EVIDENCE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="ASSUMPTIONS", start=5, end=97, lbl2="FACTS", start2=5, end2=5, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
