from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH", "PERFECT TIMING")
OUTPUT = "108_The_Problem_With_Perfect_Timing_16x9.mp4"
SPEC = [
    ("You're waiting for the perfect time.", "hourglass", dict(acc="PERFECT TIME.")),
    ("When you're less busy.", "list", dict(items=["LESS BUSY"], mode="empty", acc="BUSY.")),
    ("When you're more confident.", "list", dict(items=["LESS BUSY", "MORE CONFIDENT"], mode="empty", acc="CONFIDENT.")),
    ("When circumstances improve.", "list", dict(items=["LESS BUSY", "MORE CONFIDENT", "BETTER TIMES"], mode="empty", acc="IMPROVE.")),
    ("When everything is organized.", "list", dict(items=["LESS BUSY", "MORE CONFIDENT", "BETTER TIMES", "ORGANIZED"], mode="empty", acc="ORGANIZED.")),
    ("But perfect timing is often just a moving target.", "timeline", dict(n=8, progress=0.3, tag="ALWAYS AHEAD", acc="MOVING TARGET.")),
    ("You solve one problem…", "list", dict(items=["PROBLEM"], mode="check", acc="SOLVE")),
    ("And another appears.", "notifs", dict(items=["NEW PROBLEM"], acc="ANOTHER")),
    ("You wait for everything to settle…", "alone", dict(tag="WAITING", acc="SETTLE…")),
    ("And life keeps happening.", "timeline", dict(n=10, progress=0.8, acc="KEEPS HAPPENING.")),
    ("There will always be something.", "big", dict(text="ALWAYS", acc="ALWAYS SOMETHING.")),
    ("A responsibility.", "notifs", dict(items=["A RESPONSIBILITY"], acc="RESPONSIBILITY.")),
    ("A distraction.", "notifs", dict(items=["A RESPONSIBILITY", "A DISTRACTION"], acc="DISTRACTION.")),
    ("A challenge.", "notifs", dict(items=["A RESPONSIBILITY", "A DISTRACTION", "A CHALLENGE"], acc="CHALLENGE.")),
    ("You don't need perfect timing.", "doc", dict(title="PERFECT TIME", empty=True, stamp="NOT NEEDED", acc="DON'T PERFECT")),
    ("You need a realistic time—and the willingness to use it.", "timeline", dict(n=8, progress=0.25, tag="NOW", acc="REALISTIC WILLINGNESS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
