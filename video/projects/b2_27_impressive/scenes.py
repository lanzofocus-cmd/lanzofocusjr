from kit import build, follow_sub

TITLE = ("YOUR LIFE DOESN'T NEED", "TO LOOK IMPRESSIVE")
OUTPUT = "37_Your_Life_Doesnt_Need_To_Look_Impressive_16x9.mp4"
SPEC = [
    ("You don't need an impressive life…", "phone", dict(content="highlight", acc="IMPRESSIVE")),
    ("To have a meaningful one.", "key", dict(lbl="MEANING", acc="MEANINGFUL")),
    ("You don't need expensive things.", "price", dict(text="$$$$", sub="NOT REQUIRED", acc="EXPENSIVE")),
    ("Constant achievements.", "list", dict(items=["ACHIEVEMENT", "ACHIEVEMENT", "ACHIEVEMENT"], mode="check", acc="CONSTANT ACHIEVEMENTS.")),
    ("Thousands of people watching.", "stage", dict(acc="THOUSANDS WATCHING.")),
    ("A life that looks perfect from the outside.", "iceberg", dict(top="PERFECT OUTSIDE", bottom="REAL LIFE", acc="PERFECT OUTSIDE.")),
    ("Sometimes a meaningful life is built through ordinary moments.", "dots", dict(connect=True, acc="MEANINGFUL ORDINARY")),
    ("Learning something.", "book", dict(chapter="LEARNING", acc="LEARNING")),
    ("Helping someone.", "crowd", dict(n=3, highlight=1, highlight_label="HELPED", acc="HELPING")),
    ("Laughing with people you care about.", "bubbles", dict(texts=["HAHA", "HAHAHA"], inverted=True, acc="LAUGHING CARE")),
    ("Doing work you respect.", "bricks", dict(rows=3, lbl="WORK YOU RESPECT", uneven=False, acc="WORK RESPECT.")),
    ("Finding peace in things that don't need to be posted.", "notifs", dict(items=["NOT POSTED", "JUST LIVED"], acc="PEACE POSTED.")),
    ("Don't confuse a life worth living…", "sunrise", dict(acc="WORTH LIVING…")),
    ("With a life worth showing off.", "stage", dict(lbl="SHOWING OFF", acc="SHOWING OFF.")),
    ("Follow LanzoFocus for ideas and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
