from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN A", "BAD DAY AND A BAD LIFE")
OUTPUT = "113_A_Bad_Day_Vs_A_Bad_Life_16x9.mp4"
SPEC = [
    ("A bad day can convince you that everything is wrong.", "chart", dict(kind="down", lbl="ONE BAD DAY", acc="BAD DAY EVERYTHING")),
    ("You wake up frustrated.", "sunrise", dict(acc="FRUSTRATED.")),
    ("Something goes wrong.", "notifs", dict(items=["SOMETHING WENT WRONG"], acc="WRONG.")),
    ("Another problem appears.", "notifs", dict(items=["SOMETHING WENT WRONG", "ANOTHER PROBLEM"], acc="ANOTHER PROBLEM")),
    ("And suddenly…", "pulse", dict()),
    ("Your mind begins connecting every negative thing.", "dots", dict(connect=True, acc="CONNECTING NEGATIVE")),
    ("\"This always happens.\"", "quote", dict(text="THIS ALWAYS HAPPENS.", acc="ALWAYS")),
    ("\"Nothing works.\"", "quote", dict(text="NOTHING WORKS.", acc="NOTHING")),
    ("\"Everything is going wrong.\"", "quote", dict(text="EVERYTHING IS GOING WRONG.", acc="EVERYTHING")),
    ("But a day is a small part of a life.", "timeline", dict(n=14, progress=0.4, tag="ONE DAY", acc="DAY SMALL LIFE.")),
    ("And a difficult moment isn't an accurate summary of everything.", "doc", dict(title="SUMMARY", empty=True, stamp="INACCURATE", acc="ISN'T ACCURATE SUMMARY")),
    ("Take a step back.", "shed", dict(old="TOO CLOSE", new="STEP BACK", acc="STEP BACK.")),
    ("Don't make permanent conclusions…", "doc", dict(title="CONCLUSION", empty=True, stamp="NOT YET", acc="PERMANENT CONCLUSIONS…")),
    ("From temporary frustration.", "hourglass", dict(acc="TEMPORARY FRUSTRATION.")),
    ("Your life deserves a bigger perspective than your worst day.", "map", dict(a_lbl="WORST DAY", b_lbl="YOUR WHOLE LIFE", acc="BIGGER PERSPECTIVE WORST")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
