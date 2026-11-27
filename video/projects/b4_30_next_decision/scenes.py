from kit import build, follow_sub

TITLE = ("YOUR NEXT DECISION MATTERS", "MORE THAN YOUR LAST")
OUTPUT = "120_Your_Next_Decision_Matters_More_Than_Your_Last_16x9.mp4"
SPEC = [
    ("You've made decisions you regret.", "list", dict(items=["THAT DECISION"], mode="strike", acc="REGRET.")),
    ("Maybe they cost you time.", "hourglass", dict(acc="TIME.")),
    ("Maybe they created problems.", "tangle", dict(lbl="PROBLEMS", acc="PROBLEMS.")),
    ("Maybe they changed your direction.", "compass", dict(lbl="NEW DIRECTION", settle=False, acc="DIRECTION.")),
    ("But the past decision is already made.", "doc", dict(title="PAST DECISION", empty=False, stamp="FINAL", acc="ALREADY MADE.")),
    ("You cannot return to the moment.", "timeline", dict(n=8, progress=0.6, tag="CAN'T GO BACK", acc="CANNOT RETURN")),
    ("You can only decide what happens next.", "path", dict(kind="fork", labels=("SAME AGAIN", "SOMETHING NEW"), acc="NEXT.")),
    ("And sometimes…", "pulse", dict()),
    ("That next decision is more important than the one you're still regretting.", "scale", dict(left="LAST CHOICE", right="NEXT CHOICE", tip=1, acc="NEXT IMPORTANT REGRETTING.")),
    ("Learn from the past.", "book", dict(chapter="THE PAST", text="LESSON", acc="LEARN PAST.")),
    ("But don't let it make every future decision for you.", "cage", dict(words=["THE PAST"], acc="DON'T EVERY FUTURE")),
    ("You cannot change your previous choice.", "frame", dict(who="PREVIOUS CHOICE", acc="CANNOT PREVIOUS")),
    ("But you still have a choice to make today.", "stairs", dict(n=6, climb=0, highlight=0, acc="STILL CHOICE TODAY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
