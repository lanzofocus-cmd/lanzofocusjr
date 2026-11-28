from kit import build, follow_sub, hook

TITLE = ("LEARN TO HANDLE", "BORING TASKS")
OUTPUT = "267_Why_You_Should_Learn_To_Handle_Boring_Tasks_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Some of the most important things in life are boring.", "hud", dict(lbl="IMPORTANCE", start=20, end=95, lbl2="EXCITEMENT", start2=20, end2=10, icons=None, crowd=0, acc="IMPORTANT BORING")),
    ("Organizing.", "list", dict(items=["ORGANIZING"], mode="check", acc="ORGANIZING")),
    ("Cleaning.", "list", dict(items=["ORGANIZING", "CLEANING"], mode="check", acc="CLEANING")),
    ("Preparing.", "list", dict(items=["ORGANIZING", "CLEANING", "PREPARING"], mode="check", acc="PREPARING")),
    ("Practicing fundamentals.", "list", dict(items=["ORGANIZING", "CLEANING", "PREPARING", "FUNDAMENTALS"], mode="check", acc="FUNDAMENTALS")),
    ("Reviewing.", "list", dict(items=["ORGANIZING", "CLEANING", "PREPARING", "FUNDAMENTALS", "REVIEWING"], mode="check", acc="REVIEWING")),
    ("Repeating.", "loop", dict(items=["PRACTICE", "REVIEW", "REPEAT", "PRACTICE"], acc="REPEATING")),
    ("Checking details.", "doc", dict(title="DETAILS", empty=False, stamp="CHECKED", acc="DETAILS")),
    ("These tasks don't always feel exciting.", "gauge", dict(lbl="EXCITEMENT", start=0.3, end=0.08, acc="EXCITING")),
    ("They don't always produce immediate results.", "progress", dict(lbl="VISIBLE RESULTS", value=0.05, acc="IMMEDIATE RESULTS")),
    ("And they rarely look impressive.", "stage", dict(lbl="NOBODY CLAPS", empty=True, acc="IMPRESSIVE")),
    ("But they create the foundation for things that do.", "iceberg", dict(top="THE IMPRESSIVE PART", bottom="THE BORING FOUNDATION", acc="FOUNDATION")),
    ("Imagine building a house.", "house", dict(progress=0.2, watchers=False, lbl="THE HOUSE", acc="HOUSE")),
    ("You might be excited about the finished design.", "house", dict(progress=1.0, watchers=False, lbl="THE DESIGN", acc="EXCITED DESIGN")),
    ("But the foundation isn't glamorous.", "bricks", dict(rows=2, lbl="FOUNDATION", uneven=False, acc="FOUNDATION GLAMOROUS")),
    ("The structure isn't exciting to watch.", "bricks", dict(rows=4, lbl="STRUCTURE", uneven=False, acc="STRUCTURE")),
    ("The preparation doesn't look like the final result.", "scale", dict(left="PREPARATION", right="RESULT", tip=0, acc="PREPARATION FINAL")),
    ("Yet without it…", "pulse", dict(acc="WITHOUT")),
    ("The entire project becomes unstable.", "bricks", dict(rows=5, lbl="UNSTABLE", uneven=True, acc="UNSTABLE")),
    ("The same applies to many skills and goals.", "network", dict(nodes=["MUSIC", "SPORTS", "SCHOOL", "WORK", "ART"], tangled=False, acc="SKILLS GOALS")),
    ("You can't only enjoy the exciting parts.", "list", dict(items=["ONLY EXCITING PARTS"], mode="strike", acc="EXCITING")),
    ("You also need to learn how to handle the ordinary parts.", "list", dict(items=["THE ORDINARY PARTS"], mode="check", acc="ORDINARY")),
    ("Because the ordinary parts are often what make the extraordinary possible.", "crown", dict(lbl="BUILT ON ORDINARY", drop=True, acc="ORDINARY EXTRAORDINARY POSSIBLE")),
    ("What's a boring task you think people underestimate because it quietly makes everything else easier?", "cta", dict(kind="comment", lbl="THE UNDERRATED CHORE", acc="BORING UNDERESTIMATE EASIER")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EXCITING WORK", start=60, end=8, lbl2="WHAT BUILDS RESULTS", start2=30, end2=97, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
