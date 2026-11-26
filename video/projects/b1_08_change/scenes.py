from kit import build, follow_sub

TITLE = ("YOU DON'T HAVE TO REMAIN", "THE SAME PERSON")
OUTPUT = "08_You_Dont_Have_To_Remain_The_Same_Person_16x9.mp4"
SPEC = [
    ("People may remember who you used to be.", "frame", dict(who="WHO YOU USED TO BE", acc="REMEMBER USED")),
    ("Your mistakes.", "list", dict(items=["THAT MISTAKE", "THAT ONE TOO"], mode="strike", acc="MISTAKES.")),
    ("Your weaknesses.", "sticker", dict(tags=["WEAK", "LAZY"], acc="WEAKNESSES.")),
    ("The things you said you'd never overcome.", "quote", dict(text="I'LL NEVER CHANGE.", acc="NEVER OVERCOME.")),
    ("But you're not obligated to remain that person.", "frame", dict(who="NOT ANYMORE", fade=True, acc="NOT OBLIGATED")),
    ("You can change your habits.", "arrows", dict(items=["HABITS"], acc="HABITS.")),
    ("Your beliefs.", "arrows", dict(items=["HABITS", "BELIEFS"], acc="BELIEFS.")),
    ("Your direction.", "arrows", dict(items=["HABITS", "BELIEFS", "DIRECTION"], acc="DIRECTION.")),
    ("Your priorities.", "arrows", dict(items=["HABITS", "BELIEFS", "DIRECTION", "PRIORITIES"], acc="PRIORITIES.")),
    ("You can outgrow things you once thought were permanent.", "shed", dict(old="THEN", new="NOW", acc="OUTGROW PERMANENT.")),
    ("And you don't need everyone to understand the transformation.", "crowd", dict(n=7, highlight=3, highlight_label="CHANGED", acc="TRANSFORMATION.")),
    ("Some people will keep treating you like your old self…", "bubbles", dict(texts=["YOU'LL NEVER CHANGE.", "SAME OLD YOU."], acc="OLD SELF…")),
    ("Because that's the version they know.", "frame", dict(who="THE VERSION THEY KNOW", acc="VERSION KNOW.")),
    ("But you don't have to live according to someone else's memory of you.", "frame", dict(who="THEIR MEMORY", dashed_fig=True, new="WHO YOU ARE NOW", acc="MEMORY")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
