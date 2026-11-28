from kit import build, follow_sub, hook

TITLE = ("A BAD DECISION VS", "A BAD PERSON")
OUTPUT = "216_The_Difference_Between_A_Bad_Decision_And_A_Bad_Person_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People sometimes make one mistake…", "list", dict(items=["ONE MISTAKE"], mode="strike", acc="ONE MISTAKE")),
    ("And begin believing the mistake defines them.", "sticker", dict(tags=["THE MISTAKE"], acc="DEFINES")),
    ("\"I did something wrong.\"", "quote", dict(text="I DID SOMETHING WRONG.", acc="WRONG")),
    ("Therefore…", "arrows", dict(items=["THEREFORE"], acc="THEREFORE")),
    ("\"I'm a terrible person.\"", "quote", dict(text="I'M A TERRIBLE PERSON.", acc="TERRIBLE")),
    ("But those are two different statements.", "scale", dict(left="I DID WRONG", right="I AM WRONG", tip=0, acc="TWO DIFFERENT")),
    ("A decision can be wrong.", "path", dict(kind="fork", labels=("RIGHT", "WRONG"), acc="DECISION WRONG")),
    ("A behavior can be harmful.", "gauge", dict(lbl="HARM", start=0.1, end=0.6, acc="HARMFUL")),
    ("A mistake can have consequences.", "chart", dict(kind="down", lbl="CONSEQUENCES", acc="CONSEQUENCES")),
    ("And you can still learn, take responsibility, and make different choices.", "list", dict(items=["LEARN", "TAKE RESPONSIBILITY", "CHOOSE DIFFERENTLY"], mode="check", acc="LEARN RESPONSIBILITY DIFFERENT")),
    ("The problem begins when you confuse accountability with permanent self-condemnation.", "scale", dict(left="ACCOUNTABILITY", right="CONDEMNATION", tip=0, acc="ACCOUNTABILITY PERMANENT SELF-CONDEMNATION")),
    ("If you believe you're incapable of becoming better…", "cage", dict(words=["INCAPABLE"], acc="INCAPABLE BETTER")),
    ("Why would you try to change?", "question", dict(acc="CHANGE")),
    ("If every mistake becomes evidence that you're fundamentally bad…", "doc", dict(title="EVIDENCE", empty=False, stamp="BAD?", acc="EVIDENCE FUNDAMENTALLY")),
    ("You may begin avoiding responsibility because facing it feels unbearable.", "door", dict(open_=True, lbl="AVOID IT", acc="AVOIDING UNBEARABLE")),
    ("But responsibility should lead somewhere.", "path", dict(kind="straight", acc="RESPONSIBILITY SOMEWHERE")),
    ("Understanding.", "stairs", dict(n=4, climb=1, acc="UNDERSTANDING")),
    ("Repair.", "stairs", dict(n=4, climb=2, acc="REPAIR")),
    ("Improvement.", "stairs", dict(n=4, climb=3, acc="IMPROVEMENT")),
    ("A better decision next time.", "stairs", dict(n=4, climb=4, acc="BETTER NEXT")),
    ("Your past behavior deserves honesty.", "frame", dict(who="PAST BEHAVIOR", acc="PAST HONESTY")),
    ("Your future behavior deserves effort.", "bricks", dict(rows=3, lbl="FUTURE EFFORT", uneven=False, acc="FUTURE EFFORT")),
    ("Don't use one mistake as an excuse to stop becoming better.", "beam", dict(lbl="BECOMING BETTER", tags=("ONE MISTAKE",), drop=True, acc="ONE MISTAKE BECOMING BETTER")),
    ("Save this reminder: accountability is about changing what you do, not permanently defining yourself by what you did.", "cta", dict(kind="save", lbl="CHANGE WHAT YOU DO", acc="SAVE ACCOUNTABILITY CHANGING DEFINING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="ONE MISTAKE", start=0, end=100, lbl2="SELF-WORTH", start2=100, end2=5, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
