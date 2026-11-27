from kit import build, follow_sub

TITLE = ("YOU'RE NOT REQUIRED TO HAVE", "YOUR LIFE FIGURED OUT")
OUTPUT = "85_Youre_Not_Required_To_Have_Your_Life_Figured_Out_16x9.mp4"
SPEC = [
    ("Some people seem to know exactly what they're doing.", "crowd", dict(n=5, highlight=2, highlight_label="SO SURE", acc="EXACTLY")),
    ("Their goals.", "list", dict(items=["GOALS"], mode="check", acc="GOALS.")),
    ("Their plans.", "list", dict(items=["GOALS", "PLANS"], mode="check", acc="PLANS.")),
    ("Their future.", "list", dict(items=["GOALS", "PLANS", "FUTURE"], mode="check", acc="FUTURE.")),
    ("And you may feel like you're supposed to have the same certainty.", "lock", dict(lbl="CERTAINTY", acc="SUPPOSED CERTAINTY.")),
    ("But life doesn't require you to know everything in advance.", "doc", dict(title="REQUIREMENTS", empty=True, stamp="NOT REQUIRED", acc="DOESN'T ADVANCE.")),
    ("You can explore.", "map", dict(a_lbl="HERE", b_lbl="?", acc="EXPLORE.")),
    ("Change your mind.", "arrows", dict(items=["YOUR MIND"], acc="CHANGE")),
    ("Discover new interests.", "door", dict(open_=True, lbl="NEW INTEREST", acc="DISCOVER")),
    ("Learn what you don't want.", "list", dict(items=["NOT THIS", "NOT THAT"], mode="strike", acc="DON'T WANT.")),
    ("Make decisions with incomplete information.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="INCOMPLETE")),
    ("That's part of being human.", "alone", dict(tag="HUMAN", acc="HUMAN.")),
    ("You don't need a perfect five-year plan…", "doc", dict(title="5-YEAR PLAN", empty=True, acc="PERFECT FIVE-YEAR")),
    ("To make a meaningful decision today.", "list", dict(items=["ONE DECISION TODAY"], mode="check", acc="MEANINGFUL TODAY.")),
    ("You don't need certainty about your entire future.", "path", dict(kind="dashed", fog=True, acc="CERTAINTY ENTIRE")),
    ("You need enough clarity to take your next step.", "stairs", dict(n=6, climb=1, highlight=1, acc="CLARITY NEXT STEP.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
