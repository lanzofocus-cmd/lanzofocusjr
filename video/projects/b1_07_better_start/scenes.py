from kit import build, follow_sub

TITLE = ("STOP WAITING FOR", "A BETTER START")
OUTPUT = "07_Stop_Waiting_For_A_Better_Start_16x9.mp4"
SPEC = [
    ("Maybe you didn't have the best opportunities.", "door", dict(lbl="OPPORTUNITY", figure=True, acc="OPPORTUNITIES.")),
    ("Maybe you started behind.", "startline", dict(behind=True, acc="BEHIND.")),
    ("Maybe nobody taught you what you needed to know.", "book", dict(chapter="THE MANUAL", text="PAGES MISSING", acc="NOBODY TAUGHT")),
    ("Maybe you have less support than the people around you.", "crowd", dict(n=7, highlight=3, highlight_label="ON YOUR OWN", acc="SUPPORT")),
    ("That's real.", "big", dict(text="REAL", acc="REAL.")),
    ("And pretending otherwise doesn't help.", "mirror", dict(reflect="solid", lbl="HONEST", acc="PRETENDING")),
    ("But your starting point…", "map", dict(a_lbl="STARTING POINT", b_lbl="", acc="STARTING")),
    ("Doesn't have to become your permanent destination.", "map", dict(a_lbl="START", b_lbl="DESTINATION", acc="PERMANENT DESTINATION.")),
    ("You may not control where you begin.", "dots", dict(connect=False, acc="BEGIN.")),
    ("But you can still influence where you go next.", "compass", dict(lbl="WHERE YOU GO NEXT", acc="NEXT.")),
    ("You don't need a perfect foundation.", "bricks", dict(rows=2, lbl="IMPERFECT FOUNDATION", uneven=True, acc="PERFECT")),
    ("You need a decision…", "big", dict(text="DECIDE", acc="DECISION…")),
    ("To start building with what you have.", "bricks", dict(rows=5, lbl="WHAT YOU HAVE", uneven=True, acc="BUILDING HAVE.")),
    ("Follow LanzoFocus for ideas and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
