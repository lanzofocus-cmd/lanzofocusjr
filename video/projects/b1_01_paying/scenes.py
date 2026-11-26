from kit import build, follow_sub

TITLE = ("YOU'RE PAYING", "FOR YOUR FUTURE")
OUTPUT = "01_Youre_Paying_For_Your_Future_16x9.mp4"
SPEC = [
    ("Every choice has a price.", "price", dict(text="$ ?", acc="PRICE.")),
    ("You just don't always pay it immediately.", "receipt", dict(items=[("TODAY", "$0"), ("LATER", "$ ? ? ?")], acc="IMMEDIATELY.")),
    ("Skip the work today…", "list", dict(items=["THE WORKOUT", "THE STUDYING", "THE PROJECT"], mode="strike", acc="SKIP")),
    ("And tomorrow, you pay with regret.", "price", dict(text="REGRET", acc="REGRET.")),
    ("Avoid the challenge…", "path", dict(kind="fork", labels=("AVOID", "CHALLENGE"), acc="AVOID")),
    ("And eventually, you pay with the opportunities you never took.", "door", dict(closing=True, lbl="OPPORTUNITY", acc="OPPORTUNITIES")),
    ("Choose comfort every time…", "scale", dict(left="COMFORT", right="GROWTH", tip=-1, acc="COMFORT")),
    ("And one day, you'll pay with a life that never changed.", "chart", dict(kind="flat", lbl="YOUR LIFE", lbl2="YEARS", acc="NEVER CHANGED.")),
    ("But the opposite is true, too.", "scale", dict(left="COMFORT", right="GROWTH", tip=1, acc="OPPOSITE")),
    ("Every difficult choice you make today…", "list", dict(items=["WAKE UP EARLY", "DO THE HARD THING", "SAY NO"], mode="check", acc="DIFFICULT")),
    ("Is an investment in a future you haven't seen yet.", "coins", dict(lbl="FUTURE YOU", acc="INVESTMENT")),
    ("So the question isn't whether your choices cost something.", "receipt", dict(items=[("EVERY CHOICE", "COSTS")], total="?", acc="COST")),
    ("It's whether you're willing to pay the price for the life you want.", "price", dict(text="THE LIFE YOU WANT", sub="ARE YOU WILLING?", acc="WILLING PRICE")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
