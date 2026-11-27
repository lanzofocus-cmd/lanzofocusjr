from kit import build, follow_sub

TITLE = ("THE PEOPLE YOU", "WILL NEVER MEET")
OUTPUT = "60_The_People_You_Havent_Met_Yet_16x9.mp4"
SPEC = [
    ("Some of the most important people in your life…", "crowd", dict(n=7, dim=True, acc="IMPORTANT PEOPLE")),
    ("Haven't entered it yet.", "door", dict(lbl="NOT YET", acc="HAVEN'T YET.")),
    ("The friend who will understand you.", "crowd", dict(n=3, highlight=1, highlight_label="THE FRIEND", acc="FRIEND")),
    ("The teacher who will change your perspective.", "book", dict(chapter="NEW PERSPECTIVE", acc="TEACHER PERSPECTIVE.")),
    ("The person who introduces you to an opportunity.", "door", dict(open_=True, lbl="OPPORTUNITY", acc="OPPORTUNITY.")),
    ("The stranger who says something you'll remember for years.", "quote", dict(text="SOMETHING YOU'LL KEEP.", acc="STRANGER REMEMBER")),
    ("They're somewhere…", "map", dict(a_lbl="YOU", b_lbl="THEM", acc="SOMEWHERE…")),
    ("Living their own life.", "alone", dict(acc="OWN LIFE.")),
    ("And you haven't met them yet.", "dots", dict(connect=False, acc="HAVEN'T YET.")),
    ("Which means your current world…", "ring", dict(acc="CURRENT WORLD…")),
    ("Isn't your entire world.", "sunrise", dict(acc="ISN'T ENTIRE")),
    ("Your current relationships aren't the final list.", "list", dict(items=["...", "...", "TO BE CONTINUED"], mode="empty", acc="AREN'T FINAL")),
    ("Your current circumstances aren't the complete picture.", "puzzle", dict(missing=True, lbl="MISSING PIECES", acc="AREN'T COMPLETE")),
    ("There are chapters of your life that cannot begin until you meet people who aren't here yet.", "book", dict(chapter="NEXT CHAPTER", text="NEW CHARACTERS", acc="CHAPTERS CANNOT BEGIN")),
    ("Stay open.", "door", dict(open_=True, lbl="OPEN", acc="OPEN.")),
    ("Your story is still meeting new characters.", "crowd", dict(n=9, highlight=4, highlight_label="NEW", acc="STILL NEW CHARACTERS.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
