from kit import build, follow_sub, hook

TITLE = ("A HABIT VS", "AN IDENTITY")
OUTPUT = "262_The_Difference_Between_A_Habit_And_An_Identity_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often describe themselves using their habits.", "sticker", dict(tags=["LAZY", "LATE"], acc="DESCRIBE HABITS")),
    ("\"I'm lazy.\"", "quote", dict(text="I'M LAZY.", acc="LAZY")),
    ("\"I'm disorganized.\"", "quote", dict(text="I'M DISORGANIZED.", acc="DISORGANIZED")),
    ("\"I'm bad at studying.\"", "quote", dict(text="I'M BAD AT STUDYING.", acc="STUDYING")),
    ("\"I'm always late.\"", "quote", dict(text="I'M ALWAYS LATE.", acc="LATE")),
    ("But sometimes these statements turn temporary behaviors into permanent identities.", "sticker", dict(tags=["LAZY", "DISORGANIZED", "BAD AT IT", "ALWAYS LATE"], acc="TEMPORARY PERMANENT IDENTITIES")),
    ("You missed a deadline.", "doc", dict(title="DEADLINE", empty=False, stamp="MISSED", acc="DEADLINE")),
    ("Therefore, you're lazy.", "sticker", dict(tags=["LAZY"], acc="LAZY")),
    ("You forgot something.", "fog", dict(lbl="FORGOT", acc="FORGOT")),
    ("Therefore, you're irresponsible.", "sticker", dict(tags=["IRRESPONSIBLE"], acc="IRRESPONSIBLE")),
    ("You struggled with a subject.", "book", dict(chapter="HARD SUBJECT", acc="STRUGGLED")),
    ("Therefore, you're bad at it.", "sticker", dict(tags=["BAD AT IT"], acc="BAD")),
    ("But a behavior is something you do.", "list", dict(items=["BEHAVIOR = WHAT YOU DO"], mode="check", acc="BEHAVIOR DO")),
    ("An identity is something you believe you are.", "list", dict(items=["BEHAVIOR = WHAT YOU DO", "IDENTITY = WHO YOU ARE"], mode="check", acc="IDENTITY BELIEVE")),
    ("And when you turn a behavior into an identity…", "sticker", dict(tags=["IT'S WHO I AM"], acc="BEHAVIOR IDENTITY")),
    ("You may begin treating it as impossible to change.", "cage", dict(words=["LAZY", "BAD AT IT"], acc="IMPOSSIBLE CHANGE")),
    ("Instead of saying:", "arrows", dict(items=["INSTEAD OF"], acc="INSTEAD")),
    ("\"I'm lazy.\"", "list", dict(items=["I'M LAZY."], mode="strike", acc="LAZY")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What made it difficult for me to begin?\"", "quote", dict(text="WHAT MADE IT HARD TO BEGIN?", acc="DIFFICULT BEGIN")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I'm disorganized.\"", "list", dict(items=["I'M DISORGANIZED."], mode="strike", acc="DISORGANIZED")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What system could help me remember?\"", "quote", dict(text="WHAT SYSTEM COULD HELP ME?", acc="SYSTEM REMEMBER")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I'm bad at this.\"", "list", dict(items=["I'M BAD AT THIS."], mode="strike", acc="BAD")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What part haven't I learned yet?\"", "puzzle", dict(missing=True, lbl="NOT LEARNED YET", acc="PART LEARNED")),
    ("The way you describe yourself matters.", "mirror", dict(reflect="solid", lbl="HOW YOU DESCRIBE IT", drop=True, acc="DESCRIBE MATTERS")),
    ("Not because words magically change your life.", "list", dict(items=["MAGIC WORDS"], mode="strike", acc="MAGICALLY")),
    ("But because descriptions influence the way you interpret your behavior.", "brain", dict(says="I CAN FIX THIS.", acc="DESCRIPTIONS INTERPRET")),
    ("And interpretations influence what you believe is possible.", "door", dict(open_=True, lbl="POSSIBLE", acc="INTERPRETATIONS POSSIBLE")),
    ("What's a label you've given yourself that you're beginning to question?", "sticker", dict(tags=["MY LABEL"], strike=True, acc="LABEL QUESTION")),
    ("Comment it.", "cta", dict(kind="comment", lbl="THE LABEL YOU'RE QUESTIONING", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="\"I'M JUST LAZY\"", start=10, end=96, lbl2="ACTUALLY CHANGEABLE", start2=96, end2=96, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
