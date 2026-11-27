from kit import build, follow_sub

TITLE = ("THE WORLD WILL CONTINUE", "WITHOUT YOUR PERMISSION")
OUTPUT = "56_The_World_Will_Continue_Without_Your_Permission_16x9.mp4"
SPEC = [
    ("You keep waiting until you're ready.", "hourglass", dict(acc="WAITING READY.")),
    ("Until you're confident.", "gauge", dict(lbl="CONFIDENCE", start=0.2, end=0.22, acc="CONFIDENT.")),
    ("Until the circumstances improve.", "chart", dict(kind="flat", lbl="CIRCUMSTANCES", acc="CIRCUMSTANCES")),
    ("Until the fear disappears.", "progress", dict(lbl="FEAR", value=0.8, acc="FEAR")),
    ("But while you're waiting…", "alone", dict(tag="WAITING", acc="WAITING…")),
    ("Time continues.", "hourglass", dict(acc="TIME")),
    ("Opportunities change.", "door", dict(closing=True, lbl="OPPORTUNITY", acc="OPPORTUNITIES")),
    ("People move forward.", "timeline", dict(compare=True, acc="FORWARD.")),
    ("Life doesn't pause because you're uncertain.", "timeline", dict(n=10, progress=0.8, acc="DOESN'T PAUSE")),
    ("And that's not meant to scare you.", "shield", dict(front="NOT FEAR", back="", acc="NOT SCARE")),
    ("It's meant to wake you up.", "sunrise", dict(acc="WAKE")),
    ("You don't have to be completely ready.", "progress", dict(lbl="READY", value=0.4, acc="COMPLETELY READY.")),
    ("You don't have to know everything.", "book", dict(chapter="NOT EVERYTHING", acc="EVERYTHING.")),
    ("You don't have to eliminate every doubt.", "bubbles", dict(texts=["WHAT IF?", "AM I SURE?"], center="brain", acc="ELIMINATE DOUBT.")),
    ("You just need to stop treating readiness like a requirement for movement.", "doc", dict(title="REQUIREMENTS", empty=True, stamp="NOT READINESS", acc="READINESS REQUIREMENT")),
    ("Sometimes the only way to become ready…", "stairs", dict(n=6, climb=0, acc="ONLY READY…")),
    ("Is to begin while you're still unsure.", "path", dict(kind="dashed", fog=True, acc="BEGIN UNSURE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
