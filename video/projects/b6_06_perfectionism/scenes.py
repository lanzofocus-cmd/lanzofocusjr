from kit import build, follow_sub, hook

TITLE = ("THE PROBLEM WITH", "PERFECTIONISM")
OUTPUT = "196_The_Problem_With_Perfectionism_16x9.mp4"
MUSIC = "vyzee"
SPEC = [
    ("Perfectionism doesn't always look like someone working extremely hard.", "bricks", dict(rows=5, lbl="WORKING HARD?", uneven=False, acc="PERFECTIONISM HARD")),
    ("Sometimes it looks like someone doing absolutely nothing.", "progress", dict(lbl="FINISHED", value=0.0, acc="ABSOLUTELY NOTHING")),
    ("They have an idea.", "brain", dict(says="WHAT IF...", acc="IDEA")),
    ("They want to create something.", "doc", dict(title="DRAFT", empty=True, acc="CREATE")),
    ("They want to start a project.", "startline", dict(behind=False, acc="START PROJECT")),
    ("But every time they begin…", "doc", dict(title="DRAFT", empty=False, acc="BEGIN")),
    ("They notice something wrong.", "puzzle", dict(missing=True, lbl="SOMETHING'S OFF", acc="WRONG")),
    ("The design isn't perfect.", "frame", dict(who="THE DESIGN", dashed_fig=True, acc="DESIGN PERFECT")),
    ("The writing isn't good enough.", "doc", dict(title="WRITING", empty=False, stamp="NOT ENOUGH", acc="WRITING ENOUGH")),
    ("The result doesn't match what they imagined.", "scale", dict(left="IMAGINED", right="REAL", tip=-1, acc="RESULT IMAGINED")),
    ("So they restart.", "loop", dict(items=["START", "NOTICE A FLAW", "DELETE", "RESTART"], acc="RESTART")),
    ("Edit.", "list", dict(items=["EDIT"], mode="check", acc="EDIT")),
    ("Delete.", "list", dict(items=["EDIT", "DELETE"], mode="check", acc="DELETE")),
    ("Wait.", "list", dict(items=["EDIT", "DELETE", "WAIT"], mode="check", acc="WAIT")),
    ("And eventually, the project never gets finished.", "hud", dict(lbl="PROJECT FINISHED", start=0, end=0, icons=None, crowd=0, tag="NEVER", acc="NEVER FINISHED")),
    ("Here's the strange thing.", "question", dict(acc="STRANGE")),
    ("Perfectionism can make you feel productive because you're constantly improving the plan.", "doc", dict(title="PLAN V27", empty=False, acc="PRODUCTIVE IMPROVING PLAN")),
    ("But planning isn't the same as producing.", "scale", dict(left="PLANNING", right="PRODUCING", tip=1, acc="PLANNING PRODUCING")),
    ("Editing isn't the same as finishing.", "scale", dict(left="EDITING", right="FINISHING", tip=1, acc="EDITING FINISHING")),
    ("And imagining the perfect result isn't the same as creating a real one.", "scale", dict(left="IMAGINING", right="CREATING", tip=1, acc="IMAGINING CREATING REAL")),
    ("The first version of almost anything is supposed to reveal problems.", "doc", dict(title="VERSION 1", empty=False, stamp="PROBLEMS FOUND", acc="FIRST VERSION REVEAL PROBLEMS")),
    ("You can't fix problems you haven't discovered yet.", "fog", dict(lbl="UNDISCOVERED", acc="FIX DISCOVERED")),
    ("You can't improve something that doesn't exist.", "frame", dict(who="NOTHING YET", dashed_fig=True, acc="IMPROVE EXIST")),
    ("And you can't gain experience from an idea that remains permanently inside your head.", "cage", dict(words=["THE IDEA"], acc="EXPERIENCE INSIDE HEAD")),
    ("Instead of asking:", "arrows", dict(items=["THE QUESTION"], acc="INSTEAD")),
    ("\"How do I make this perfect?\"", "quote", dict(text="HOW DO I MAKE THIS PERFECT?", acc="PERFECT")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"How do I make this real enough to improve?\"", "quote", dict(text="HOW DO I MAKE THIS REAL ENOUGH TO IMPROVE?", acc="REAL IMPROVE")),
    ("The goal isn't to become someone who produces flawless work immediately.", "list", dict(items=["FLAWLESS, IMMEDIATELY"], mode="strike", acc="FLAWLESS IMMEDIATELY")),
    ("The goal is to become someone who can create, evaluate, learn, and improve.", "loop", dict(items=["CREATE", "EVALUATE", "LEARN", "IMPROVE"], lbl="THE REAL LOOP", acc="CREATE EVALUATE LEARN IMPROVE")),
    ("Because finished work gives you something perfectionism never can.", "doc", dict(title="FINISHED", empty=False, stamp="DONE", acc="FINISHED PERFECTIONISM NEVER")),
    ("Progress you can actually see.", "chart", dict(kind="up", lbl="VISIBLE PROGRESS", acc="PROGRESS SEE")),
    ("What's something you've been delaying because you want it to be perfect?", "hourglass", dict(acc="DELAYING PERFECT")),
    ("Name it in the comments.", "cta", dict(kind="comment", lbl="NAME IT", acc="NAME COMMENTS")),
    ("And consider making your first imperfect version today.", "doc", dict(title="VERSION 1", empty=False, stamp="TODAY", acc="FIRST IMPERFECT TODAY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PERFECT PLAN", start=20, end=100, lbl2="FINISHED", start2=0, end2=0, icons=None, crowd=4, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
