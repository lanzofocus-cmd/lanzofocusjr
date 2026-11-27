from kit import build, follow_sub

TITLE = ("THE INVISIBLE", "SCOREBOARD")
OUTPUT = "44_The_Invisible_Scoreboard_16x9.mp4"
SPEC = [
    ("You might be losing a competition…", "timeline", dict(compare=True, acc="LOSING COMPETITION…")),
    ("That nobody actually started.", "startline", dict(behind=True, acc="NOBODY STARTED.")),
    ("You see someone your age doing better.", "crowd", dict(n=5, highlight=1, highlight_label="SAME AGE", acc="BETTER.")),
    ("Someone getting more attention.", "stage", dict(acc="ATTENTION.")),
    ("Someone achieving something faster.", "timeline", dict(compare=True, acc="FASTER.")),
    ("And suddenly…", "pulse", dict()),
    ("You feel like you're falling behind.", "startline", dict(behind=True, acc="BEHIND.")),
    ("But where is the scoreboard?", "doc", dict(title="SCOREBOARD", empty=True, acc="SCOREBOARD?")),
    ("Who created the rankings?", "list", dict(items=["#1 ?", "#2 ?", "#3 ?"], mode="empty", acc="RANKINGS?")),
    ("Who decided that your life should be measured against theirs?", "scale", dict(left="YOUR LIFE", right="THEIRS", tip=0, acc="MEASURED")),
    ("You didn't enter the world with a deadline to become successful before someone else.", "hourglass", dict(acc="DEADLINE")),
    ("Their progress doesn't subtract from yours.", "progress", dict(lbl="YOUR PROGRESS", value=0.5, acc="DOESN'T SUBTRACT")),
    ("Their achievement isn't evidence of your failure.", "doc", dict(title="EVIDENCE", empty=True, stamp="NONE", acc="ISN'T EVIDENCE")),
    ("You can admire someone else's progress without turning it into a judgment of your own.", "crowd", dict(n=3, highlight=1, highlight_label="ADMIRE", acc="ADMIRE JUDGMENT")),
    ("Stop competing in imaginary races.", "path", dict(kind="dashed", walker=True, acc="IMAGINARY RACES.")),
    ("Build a life you actually want to live.", "bricks", dict(rows=4, lbl="YOUR LIFE", uneven=False, acc="BUILD WANT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
