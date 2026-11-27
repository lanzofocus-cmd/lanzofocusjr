from kit import build, follow_sub

TITLE = ("WHY YOU KEEP", "REPLAYING CONVERSATIONS")
OUTPUT = "106_Why_You_Keep_Replaying_Conversations_16x9.mp4"
SPEC = [
    ("You said something.", "quote", dict(text="...WAIT, WHAT DID I SAY?", acc="SAID")),
    ("Then you replay it.", "brain", dict(says="REPLAY...", acc="REPLAY")),
    ("Could you have worded it differently?", "brain", dict(says="REPLAY...", says2="DIFFERENT WORDS?", acc="DIFFERENTLY?")),
    ("Did they misunderstand?", "bubbles", dict(texts=["REPLAY...", "DIFFERENT WORDS?", "DID THEY MISREAD?"], center="brain", acc="MISUNDERSTAND?")),
    ("Did you sound strange?", "bubbles", dict(texts=["REPLAY...", "DIFFERENT WORDS?", "DID THEY MISREAD?", "WAS I WEIRD?"], center="brain", acc="STRANGE?")),
    ("Did you make a mistake?", "bubbles", dict(texts=["REPLAY...", "DIFFERENT WORDS?", "DID THEY MISREAD?", "WAS I WEIRD?", "A MISTAKE?"], center="brain", acc="MISTAKE?")),
    ("And your mind keeps returning to the moment…", "timeline", dict(n=8, progress=0.3, tag="THAT MOMENT", acc="RETURNING")),
    ("As if replaying it enough times will change what happened.", "frame", dict(who="WHAT HAPPENED", acc="REPLAYING CHANGE")),
    ("But the conversation is over.", "book", dict(chapter="THE END", acc="OVER.")),
    ("You cannot edit the past by repeatedly reviewing it.", "doc", dict(title="THE PAST", empty=False, stamp="FINAL", acc="CANNOT EDIT PAST")),
    ("If you made a mistake…", "list", dict(items=["A MISTAKE?"], mode="empty", acc="MISTAKE…")),
    ("Learn from it.", "book", dict(chapter="LESSON", acc="LEARN")),
    ("If you didn't…", "list", dict(items=["NO MISTAKE"], mode="check", acc="DIDN'T…")),
    ("Let yourself move on.", "path", dict(kind="straight", acc="MOVE ON.")),
    ("Reflection helps you learn.", "mirror", dict(reflect="solid", lbl="REFLECT", acc="REFLECTION LEARN.")),
    ("Replaying helps you suffer through the same moment again.", "timeline", dict(n=8, progress=0.3, tag="AGAIN", acc="REPLAYING SUFFER AGAIN.")),
    ("Save this reminder for when your mind won't let something go.", "cta", dict(kind="save", acc="SAVE GO.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
