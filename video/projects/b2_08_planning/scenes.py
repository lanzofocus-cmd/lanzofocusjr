from kit import build, follow_sub

TITLE = ("YOUR LIFE IS HAPPENING", "WHILE YOU'RE PLANNING IT")
OUTPUT = "18_Your_Life_Is_Happening_While_Youre_Planning_It_16x9.mp4"
SPEC = [
    ("You can plan your future so carefully…", "map", dict(a_lbl="NOW", b_lbl="THE PLAN", acc="PLAN CAREFULLY…")),
    ("That you forget to actually live toward it.", "alone", dict(tag="STILL PLANNING", acc="FORGET LIVE")),
    ("You can make lists.", "list", dict(items=["STEP 1", "STEP 2", "STEP 3"], mode="empty", acc="LISTS.")),
    ("Create schedules.", "timeline", dict(n=8, progress=0.0, acc="SCHEDULES.")),
    ("Watch tutorials.", "phone", dict(content="highlight", acc="TUTORIALS.")),
    ("Research every possibility.", "network", dict(nodes=["OPTION A", "OPTION B", "OPTION C", "OPTION D", "OPTION E"], tangled=True, acc="EVERY POSSIBILITY.")),
    ("And still never take the first step.", "stairs", dict(n=6, climb=0, highlight=0, acc="NEVER FIRST STEP.")),
    ("Planning feels productive because it gives you the feeling of progress.", "progress", dict(lbl="FEELS LIKE PROGRESS", value=0.9, invisible=True, acc="FEELING PROGRESS.")),
    ("But preparation has a limit.", "gauge", dict(lbl="PREPARATION", start=0.2, end=0.98, acc="LIMIT.")),
    ("Eventually…", "pulse", dict()),
    ("You have to leave the map.", "map", dict(a_lbl="THE MAP", b_lbl="THE REAL WORLD", acc="LEAVE MAP.")),
    ("And actually walk.", "path", dict(kind="straight", acc="WALK.")),
    ("You don't need another perfect plan.", "doc", dict(title="PLAN V27", empty=False, stamp="ENOUGH", acc="PERFECT")),
    ("You need an imperfect action.", "stairs", dict(n=6, climb=1, acc="IMPERFECT ACTION.")),
    ("Follow LanzoFocus for ideas and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
