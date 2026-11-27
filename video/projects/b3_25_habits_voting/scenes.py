from kit import build, follow_sub

TITLE = ("YOUR HABITS ARE VOTING", "FOR YOUR FUTURE")
OUTPUT = "65_Your_Habits_Are_Voting_For_Your_Future_16x9.mp4"
SPEC = [
    ("Your habits aren't just things you do.", "list", dict(items=["HABIT", "HABIT", "HABIT"], mode="check", acc="HABITS AREN'T")),
    ("They're repeated decisions about the kind of life you're creating.", "bricks", dict(rows=4, lbl="YOUR LIFE", uneven=False, acc="REPEATED DECISIONS CREATING.")),
    ("Every time you practice…", "stairs", dict(n=6, climb=1, acc="PRACTICE…")),
    ("You're voting for improvement.", "doc", dict(title="BALLOT", empty=False, stamp="IMPROVEMENT", acc="VOTING IMPROVEMENT.")),
    ("Every time you read…", "book", dict(chapter="READING", acc="READ…")),
    ("You're voting for curiosity.", "doc", dict(title="BALLOT", empty=False, stamp="CURIOSITY", acc="VOTING CURIOSITY.")),
    ("Every time you avoid something important…", "list", dict(items=["THE IMPORTANT THING"], mode="tag", tag="AVOIDED", acc="AVOID IMPORTANT…")),
    ("You're voting for avoidance.", "doc", dict(title="BALLOT", empty=False, stamp="AVOIDANCE", acc="VOTING AVOIDANCE.")),
    ("But here's the important part.", "pulse", dict(acc="IMPORTANT")),
    ("One vote doesn't decide an election.", "scale", dict(left="ONE VOTE", right="THE PATTERN", tip=1, acc="ONE DOESN'T ELECTION.")),
    ("One bad day doesn't define you.", "chart", dict(kind="invest", lbl="ONE BAD DAY", acc="BAD DOESN'T")),
    ("One good day doesn't transform you.", "chart", dict(kind="flat", lbl="ONE GOOD DAY", acc="GOOD DOESN'T")),
    ("It's the pattern that matters.", "dots", dict(connect=True, acc="PATTERN")),
    ("You don't need every decision to be perfect.", "list", dict(items=["PERFECT", "PERFECT"], mode="strike", acc="PERFECT.")),
    ("You need enough decisions pointing in the direction you want to go.", "compass", dict(lbl="YOUR DIRECTION", acc="ENOUGH DIRECTION")),
    ("Save this as a reminder that your next choice still matters.", "cta", dict(kind="save", lbl="YOUR NEXT CHOICE", acc="SAVE NEXT MATTERS.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
