from kit import build, follow_sub

TITLE = ("YOUR EXCUSES ARE", "BECOMING YOUR IDENTITY")
OUTPUT = "06_Your_Excuses_Are_Becoming_Your_Identity_16x9.mp4"
SPEC = [
    ("At first, an excuse is just something you say.", "quote", dict(text="JUST THIS ONCE.", acc="EXCUSE SAY.")),
    ("\"I'm tired.\"", "quote", dict(text="I'M TIRED.", acc="TIRED.")),
    ("\"I'll do it tomorrow.\"", "quote", dict(text="I'LL DO IT TOMORROW.", acc="TOMORROW.")),
    ("\"It's not the right time.\"", "quote", dict(text="NOT THE RIGHT TIME.", acc="RIGHT TIME.")),
    ("But repeat those words long enough…", "bubbles", dict(texts=["I'M TIRED.", "TOMORROW.", "NOT NOW.", "MAYBE LATER."], acc="REPEAT")),
    ("And they stop sounding like excuses.", "bubbles", dict(texts=["I'M TIRED.", "TOMORROW."], inverted=True, acc="EXCUSES.")),
    ("They start sounding like your identity.", "sticker", dict(tags=["TIRED", "LATER"], acc="IDENTITY.")),
    ("You begin believing you're someone who can't.", "sticker", dict(tags=["TIRED", "LATER", "CAN'T"], acc="CAN'T.")),
    ("Someone who always delays.", "sticker", dict(tags=["TIRED", "LATER", "CAN'T", "DELAYS"], acc="DELAYS.")),
    ("Someone who never finishes.", "sticker", dict(tags=["TIRED", "LATER", "CAN'T", "DELAYS", "UNFINISHED"], acc="NEVER FINISHES.")),
    ("And that's dangerous.", "big", dict(text="DANGEROUS", acc="DANGEROUS.")),
    ("Because the words you repeatedly use to explain your life…", "bubbles", dict(texts=["I'M JUST LIKE THAT.", "THAT'S NOT ME."], acc="WORDS")),
    ("Can eventually become the limits you live inside.", "cage", dict(words=["CAN'T", "LATER", "TIRED"], acc="LIMITS INSIDE.")),
    ("Be honest with yourself.", "mirror", dict(reflect="solid", lbl="HONEST?", acc="HONEST")),
    ("Are your reasons protecting you…", "shield", dict(front="PROTECTING?", back="YOUR GOALS", acc="PROTECTING")),
    ("Or preventing you?", "shield", dict(front="OR PREVENTING?", back="BLOCKED", acc="PREVENTING")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
