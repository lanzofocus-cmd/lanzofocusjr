from kit import build, follow_sub

TITLE = ("ONE DAY, THIS", "WILL MAKE SENSE")
OUTPUT = "10_One_Day_This_Will_Make_Sense_16x9.mp4"
SPEC = [
    ("One day…", "sunrise", dict(acc="ONE DAY…")),
    ("You'll look back at the things that frustrated you.", "dots", dict(connect=False, acc="LOOK BACK FRUSTRATED")),
    ("The opportunities you missed.", "door", dict(closing=True, lbl="MISSED", acc="MISSED.")),
    ("The plans that failed.", "list", dict(items=["PLAN A", "PLAN B", "PLAN C"], mode="strike", acc="FAILED.")),
    ("The moments you thought you were falling behind.", "timeline", dict(compare=True, acc="BEHIND.")),
    ("And some of them…", "pulse", dict()),
    ("Will make sense in ways you couldn't see at the time.", "dots", dict(connect=True, acc="SENSE")),
    ("Not every setback has a hidden lesson.", "puzzle", dict(missing=True, lbl="NOT EVERY PIECE FITS", acc="NOT LESSON.")),
    ("Not every disappointment leads somewhere better.", "path", dict(kind="dashed", walker=True, acc="NOT BETTER.")),
    ("But you can still learn from what happened.", "book", dict(chapter="WHAT HAPPENED", text="LESSON", acc="LEARN")),
    ("You can still grow through uncertainty.", "plant", dict(height=0.6, roots=False, acc="GROW UNCERTAINTY.")),
    ("And you can still create meaning…", "puzzle", dict(missing=False, lbl="MEANING", acc="CREATE MEANING…")),
    ("Even when life doesn't give you the explanation you wanted.", "doc", dict(title="WHY?", empty=True, acc="EXPLANATION")),
    ("You don't need to understand everything today.", "compass", dict(lbl="NOT EVERYTHING", settle=False, acc="UNDERSTAND")),
    ("You just need to keep moving with what you know.", "fog", dict(lbl="WHAT YOU KNOW", acc="KEEP MOVING")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
