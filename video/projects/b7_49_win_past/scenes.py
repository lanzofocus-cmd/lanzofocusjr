from kit import build, follow_sub, hook

TITLE = ("STOP TRYING TO", "WIN THE PAST")
OUTPUT = "249_Why_You_Should_Stop_Trying_To_Win_The_Past_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes we spend so much time thinking about the past…", "timeline", dict(n=10, progress=0.2, tag="BACK THEN", acc="PAST")),
    ("Trying to imagine what we should have said.", "bubbles", dict(texts=["I SHOULD HAVE SAID..."], acc="SAID")),
    ("What we should have done.", "brain", dict(says="IF ONLY I HAD...", acc="DONE")),
    ("What we could have changed.", "path", dict(kind="fork", labels=("WHAT HAPPENED", "WHAT IF"), acc="CHANGED")),
    ("We replay the conversation.", "loop", dict(items=["REPLAY", "REWRITE", "REGRET", "REPLAY"], acc="REPLAY")),
    ("Rewrite the decision.", "doc", dict(title="DECISION V12", empty=False, acc="REWRITE")),
    ("Create a different ending in our minds.", "book", dict(chapter="ALTERNATE ENDING", acc="DIFFERENT ENDING")),
    ("But the past cannot be edited.", "lock", dict(lbl="THE PAST", drop=True, acc="CANNOT EDITED")),
    ("You can learn from it.", "list", dict(items=["LEARN"], mode="check", acc="LEARN")),
    ("You can apologize.", "list", dict(items=["LEARN", "APOLOGIZE"], mode="check", acc="APOLOGIZE")),
    ("You can make repairs where possible.", "list", dict(items=["LEARN", "APOLOGIZE", "REPAIR"], mode="check", acc="REPAIRS")),
    ("You can understand what happened.", "list", dict(items=["LEARN", "APOLOGIZE", "REPAIR", "UNDERSTAND"], mode="check", acc="UNDERSTAND")),
    ("But you cannot repeatedly revisit yesterday and expect it to become different.", "loop", dict(items=["YESTERDAY", "YESTERDAY", "YESTERDAY", "YESTERDAY"], lbl="STILL THE SAME", acc="REVISIT YESTERDAY DIFFERENT")),
    ("Eventually, you need to take the lesson…", "key", dict(lbl="THE LESSON", acc="LESSON")),
    ("And bring it into the present.", "map", dict(a_lbl="THE PAST", b_lbl="NOW", acc="PRESENT")),
    ("The past is useful when it informs your future.", "compass", dict(lbl="INFORMED BY THE PAST", acc="USEFUL INFORMS FUTURE")),
    ("It becomes a problem when it prevents you from living your current life.", "cage", dict(words=["WHAT IF", "IF ONLY"], acc="PREVENTS CURRENT")),
    ("What's a lesson from your past that you're trying to carry forward instead of constantly replaying?", "cta", dict(kind="comment", lbl="CARRY IT FORWARD", acc="LESSON FORWARD REPLAYING")),
    ("", "follow"),
]
_HOOK = ("loop", dict(items=["REPLAY", "REWRITE", "REGRET", "REPLAY"]))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
