from kit import build, follow_sub, hook

TITLE = ("BE CAREFUL WITH", "YOUR OWN STORIES")
OUTPUT = "222_Why_You_Should_Be_Careful_With_Your_Own_Stories_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Your mind is constantly creating stories.", "book", dict(chapter="MY STORY", acc="STORIES")),
    ("\"This always happens to me.\"", "quote", dict(text="THIS ALWAYS HAPPENS TO ME.", acc="ALWAYS")),
    ("\"Nobody cares.\"", "quote", dict(text="NOBODY CARES.", acc="NOBODY")),
    ("\"I never get opportunities.\"", "quote", dict(text="I NEVER GET OPPORTUNITIES.", acc="NEVER")),
    ("\"I'm terrible at this.\"", "quote", dict(text="I'M TERRIBLE AT THIS.", acc="TERRIBLE")),
    ("\"Everything goes wrong.\"", "quote", dict(text="EVERYTHING GOES WRONG.", acc="EVERYTHING")),
    ("But words like always, never, and everybody can turn individual experiences into permanent conclusions.", "cage", dict(words=["ALWAYS", "NEVER", "EVERYBODY"], acc="ALWAYS NEVER EVERYBODY PERMANENT")),
    ("One bad day becomes \"my life is terrible.\"", "scale", dict(left="ONE BAD DAY", right="MY WHOLE LIFE", tip=-1, acc="ONE TERRIBLE")),
    ("One rejection becomes \"nobody wants me.\"", "scale", dict(left="ONE NO", right="NOBODY", tip=-1, acc="REJECTION NOBODY")),
    ("One mistake becomes \"I'm incapable.\"", "scale", dict(left="ONE MISTAKE", right="INCAPABLE", tip=-1, acc="MISTAKE INCAPABLE")),
    ("Your brain may be trying to make sense of an experience…", "brain", dict(says="MAKING SENSE...", acc="SENSE")),
    ("But the story it creates might be larger than the evidence.", "iceberg", dict(top="THE EVIDENCE", bottom="THE STORY", acc="LARGER EVIDENCE")),
    ("When you catch yourself using absolute language…", "list", dict(items=["ALWAYS", "NEVER", "EVERYONE"], mode="strike", acc="ABSOLUTE")),
    ("Pause.", "big", dict(text="PAUSE.", acc="PAUSE")),
    ("Ask whether the statement is actually true.", "doc", dict(title="STATEMENT", empty=False, stamp="TRUE?", acc="ACTUALLY TRUE")),
    ("Or whether you're describing how you feel in the moment.", "gauge", dict(lbl="FEELING", start=0.3, end=0.8, acc="FEEL MOMENT")),
    ("You can acknowledge a difficult experience without turning it into a permanent identity.", "sticker", dict(tags=["A HARD DAY", "NOT WHO I AM"], drop=True, acc="ACKNOWLEDGE PERMANENT IDENTITY")),
    ("Save this for when your thoughts begin using words like \"always,\" \"never,\" or \"everyone.\"", "cta", dict(kind="save", lbl="CATCH THE ABSOLUTES", acc="SAVE ALWAYS NEVER EVERYONE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="\"ALWAYS\" \"NEVER\"", start=5, end=98, lbl2="EVIDENCE", start2=10, end2=10, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
