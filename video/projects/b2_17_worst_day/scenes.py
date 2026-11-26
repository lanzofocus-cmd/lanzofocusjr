from kit import build, follow_sub

TITLE = ("YOU'RE NOT", "YOUR WORST DAY")
OUTPUT = "27_Youre_Not_Your_Worst_Day_16x9.mp4"
SPEC = [
    ("One terrible day can make you question everything.", "chart", dict(kind="down", lbl="ONE BAD DAY", acc="TERRIBLE QUESTION")),
    ("One failure can make you feel incapable.", "sticker", dict(tags=["INCAPABLE"], acc="FAILURE INCAPABLE.")),
    ("One mistake can make you believe you've ruined your progress.", "progress", dict(lbl="PROGRESS", value=0.55, acc="RUINED PROGRESS.")),
    ("But your life is bigger than a single moment.", "timeline", dict(n=12, progress=0.5, tag="ONE MOMENT", acc="BIGGER SINGLE")),
    ("Your character isn't measured by whether you never fall short.", "doc", dict(title="MEASURE", empty=True, acc="ISN'T NEVER")),
    ("It's measured by what you do afterward.", "stairs", dict(n=6, climb=3, acc="AFTERWARD.")),
    ("Do you learn?", "book", dict(chapter="LESSON", acc="LEARN?")),
    ("Do you take responsibility?", "alone", dict(tag="MY RESPONSIBILITY", acc="RESPONSIBILITY?")),
    ("Do you try again?", "chart", dict(kind="invest", lbl="TRY AGAIN", acc="AGAIN?")),
    ("Don't allow one moment…", "pulse", dict(acc="ONE")),
    ("To become the definition of your entire life.", "book", dict(chapter="ONE PAGE", text="NOT THE WHOLE BOOK", acc="DEFINITION ENTIRE")),
    ("You are still becoming.", "plant", dict(height=0.7, roots=True, lbl="STILL GROWING", acc="STILL BECOMING.")),
    ("Follow LanzoFocus for ideas and lessons that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
