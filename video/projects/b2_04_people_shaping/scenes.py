from kit import build, follow_sub

TITLE = ("THE PEOPLE AROUND YOU", "ARE SHAPING YOU")
OUTPUT = "14_The_People_Around_You_Are_Shaping_You_16x9.mp4"
SPEC = [
    ("You don't have to copy someone to become like them.", "ring", dict(acc="COPY LIKE")),
    ("Spend enough time around people who complain…", "ring", dict(tags=["UGH", "UNFAIR", "WHY ME", "SO TIRED"], acc="COMPLAIN…")),
    ("And complaining begins to feel normal.", "ring", dict(tags=["UGH", "UNFAIR", "WHY ME", "SO TIRED"], center_tag="UGH", acc="NORMAL.")),
    ("Spend enough time around people who never try…", "ring", dict(tags=["WHY BOTHER", "NOT WORTH IT", "MAYBE LATER", "MEH"], acc="NEVER TRY…")),
    ("And ambition starts feeling unnecessary.", "gauge", dict(lbl="AMBITION", start=0.7, end=0.15, acc="AMBITION UNNECESSARY.")),
    ("Spend enough time around people who take responsibility…", "ring", dict(tags=["MY FAULT", "I'LL FIX IT", "ON IT", "I'LL LEARN"], acc="RESPONSIBILITY…")),
    ("And suddenly, excuses become harder to believe.", "sticker", dict(tags=["EXCUSES", "LATER", "CAN'T"], strike=True, acc="EXCUSES HARDER")),
    ("Your environment doesn't control your future.", "compass", dict(lbl="YOUR DIRECTION", acc="DOESN'T CONTROL")),
    ("But it influences what you consider normal.", "scale", dict(left="THEIR NORMAL", right="YOUR NORMAL", tip=0, acc="INFLUENCES NORMAL.")),
    ("Pay attention to the standards you're surrounded by.", "bricks", dict(rows=3, lbl="THE STANDARD", uneven=True, acc="STANDARDS SURROUNDED")),
    ("They may be quietly becoming your standards, too.", "ring", dict(tags=["THEIRS", "THEIRS", "THEIRS"], center_tag="YOURS?", acc="QUIETLY STANDARDS")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
