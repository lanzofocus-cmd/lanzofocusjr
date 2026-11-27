from kit import build, follow_sub

TITLE = ("YOU CAN'T OUTRUN A PROBLEM", "YOU REFUSE TO FACE")
OUTPUT = "97_You_Cant_Outrun_A_Problem_You_Refuse_To_Face_16x9.mp4"
SPEC = [
    ("You can stay busy.", "notifs", dict(items=["BUSY", "BUSY"], acc="BUSY.")),
    ("You can fill your schedule.", "timeline", dict(n=10, progress=1.0, tag="FULL", acc="SCHEDULE.")),
    ("You can distract yourself.", "phone", dict(content="highlight", acc="DISTRACT")),
    ("You can constantly move from one thing to another.", "path", dict(kind="winding", acc="CONSTANTLY")),
    ("But the problem you refuse to face…", "fog", dict(lbl="THE PROBLEM", acc="REFUSE FACE…")),
    ("Often follows you.", "timeline", dict(compare=True, acc="FOLLOWS")),
    ("Because changing your surroundings doesn't automatically change your patterns.", "map", dict(a_lbl="OLD PLACE", b_lbl="NEW PLACE, SAME YOU", acc="SURROUNDINGS PATTERNS.")),
    ("You can leave a situation…", "door", dict(open_=True, lbl="EXIT", acc="LEAVE")),
    ("And carry the same habits into the next one.", "receipt", dict(items=[("OLD HABITS", "PACKED"), ("SAME PATTERNS", "PACKED")], acc="CARRY SAME HABITS")),
    ("You can start over…", "startline", dict(behind=False, acc="START OVER…")),
    ("And repeat the same mistakes.", "list", dict(items=["SAME MISTAKE", "SAME MISTAKE"], mode="strike", acc="REPEAT SAME MISTAKES.")),
    ("Sometimes the real change isn't moving somewhere new.", "map", dict(a_lbl="HERE", b_lbl="SOMEWHERE NEW", acc="ISN'T SOMEWHERE")),
    ("It's learning to do something differently.", "arrows", dict(items=["BEHAVIOR"], acc="DIFFERENTLY.")),
    ("You don't escape every problem by changing your location.", "compass", dict(lbl="LOCATION", settle=False, acc="ESCAPE LOCATION.")),
    ("Sometimes you escape it by changing your behavior.", "shed", dict(old="OLD PATTERN", new="NEW BEHAVIOR", acc="CHANGING BEHAVIOR.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
