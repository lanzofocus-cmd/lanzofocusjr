from kit import build, follow_sub

TITLE = ("WHY YOU KEEP", "CHANGING YOUR GOALS")
OUTPUT = "47_Why_You_Keep_Changing_Your_Goals_16x9.mp4"
SPEC = [
    ("Every few weeks…", "timeline", dict(n=8, progress=0.5, acc="WEEKS…")),
    ("You discover a new version of success.", "door", dict(open_=True, lbl="NEW PLAN", acc="NEW SUCCESS.")),
    ("A new career.", "list", dict(items=["NEW CAREER"], mode="empty", acc="CAREER.")),
    ("A new skill.", "list", dict(items=["NEW CAREER", "NEW SKILL"], mode="empty", acc="SKILL.")),
    ("A new ambition.", "list", dict(items=["NEW CAREER", "NEW SKILL", "NEW AMBITION"], mode="empty", acc="AMBITION.")),
    ("A new plan.", "list", dict(items=["NEW CAREER", "NEW SKILL", "NEW AMBITION", "NEW PLAN"], mode="empty", acc="PLAN.")),
    ("And suddenly, the previous goal feels boring.", "gauge", dict(lbl="EXCITEMENT", start=0.9, end=0.1, acc="BORING.")),
    ("But what if you're not changing goals because you've discovered something better?", "question", dict(a_lbl="BETTER GOAL?", acc="NOT BETTER?")),
    ("What if you're changing them because the beginning is exciting…", "chart", dict(kind="down", lbl="EXCITEMENT", acc="BEGINNING EXCITING…")),
    ("And the middle is uncomfortable?", "path", dict(kind="winding", acc="MIDDLE UNCOMFORTABLE?")),
    ("Beginnings give you possibility.", "sunrise", dict(acc="POSSIBILITY.")),
    ("The middle gives you reality.", "bricks", dict(rows=2, lbl="REALITY", uneven=True, acc="MIDDLE REALITY.")),
    ("The middle is where progress becomes repetitive.", "stairs", dict(n=6, climb=2, acc="REPETITIVE.")),
    ("Where the excitement disappears.", "progress", dict(lbl="EXCITEMENT", value=0.05, acc="DISAPPEARS.")),
    ("Where improvement becomes difficult to measure.", "progress", dict(lbl="IMPROVEMENT", value=0.4, invisible=True, acc="DIFFICULT MEASURE.")),
    ("And that's exactly why many people never reach the end of anything.", "timeline", dict(n=10, progress=0.45, tag="QUIT HERE", acc="NEVER END")),
    ("Don't confuse losing the excitement with losing the purpose.", "scale", dict(left="EXCITEMENT", right="PURPOSE", tip=1, acc="EXCITEMENT PURPOSE.")),
    ("Before changing your goal again…", "compass", dict(lbl="YOUR GOAL", acc="AGAIN…")),
    ("Ask yourself whether the goal is wrong…", "question", dict(a_lbl="WRONG GOAL?", acc="WRONG…")),
    ("Or whether you've simply reached the part that requires patience.", "hourglass", dict(acc="PATIENCE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
