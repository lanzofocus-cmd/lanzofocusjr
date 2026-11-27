from kit import build, follow_sub

TITLE = ("THE FUTURE IS BUILT BY", "BORING DECISIONS")
OUTPUT = "70_The_Future_Is_Built_By_Boring_Decisions_16x9.mp4"
SPEC = [
    ("Nobody makes a documentary about the ordinary decisions that build a life.", "stage", dict(empty=True, performing=False, acc="DOCUMENTARY ORDINARY")),
    ("The day you practiced even though it wasn't exciting.", "list", dict(items=["PRACTICED"], mode="check", acc="PRACTICED")),
    ("The time you saved instead of spending impulsively.", "coins", dict(lbl="SAVED", acc="SAVED")),
    ("The conversation you finally had.", "bubbles", dict(texts=["WE NEED TO TALK."], inverted=True, acc="CONVERSATION")),
    ("The assignment you completed before it became urgent.", "doc", dict(title="ASSIGNMENT", empty=False, stamp="DONE EARLY", acc="COMPLETED")),
    ("The habit you repeated when nothing dramatic happened.", "timeline", dict(n=10, progress=0.7, tag="AGAIN", acc="REPEATED")),
    ("These decisions rarely feel important.", "big", dict(text="BORING", acc="RARELY IMPORTANT.")),
    ("But that's exactly why they matter.", "key", dict(lbl="WHY THEY MATTER", acc="MATTER.")),
    ("They don't depend on excitement.", "gauge", dict(lbl="EXCITEMENT", start=0.1, end=0.1, acc="DON'T EXCITEMENT.")),
    ("They don't require a special moment.", "sunrise", dict(acc="DON'T SPECIAL")),
    ("They quietly accumulate.", "coins", dict(lbl="ACCUMULATING", acc="QUIETLY ACCUMULATE.")),
    ("And eventually…", "pulse", dict()),
    ("The life you thought would require one extraordinary decision…", "big", dict(text="ONE BIG MOMENT?", acc="ONE EXTRAORDINARY")),
    ("Was built by hundreds of ordinary ones.", "bricks", dict(rows=6, lbl="HUNDREDS OF ORDINARY DAYS", uneven=False, acc="HUNDREDS ORDINARY")),
    ("Don't underestimate what ordinary days can create.", "house" if False else "bricks", dict(rows=5, lbl="WHAT YOU BUILT", uneven=True, acc="UNDERESTIMATE ORDINARY CREATE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
