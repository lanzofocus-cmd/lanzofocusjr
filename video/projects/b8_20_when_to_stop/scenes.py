from kit import build, follow_sub, hook

TITLE = ("THE VALUE OF KNOWING", "WHEN TO STOP")
OUTPUT = "270_The_Value_Of_Knowing_When_To_Stop_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Persistence is important.", "stairs", dict(n=7, climb=4, acc="PERSISTENCE")),
    ("But persistence doesn't mean continuing everything forever.", "list", dict(items=["CONTINUE EVERYTHING FOREVER"], mode="strike", acc="CONTINUING FOREVER")),
    ("Sometimes people keep working on a plan that clearly isn't effective.", "chart", dict(kind="flat", lbl="THE PLAN", acc="PLAN EFFECTIVE")),
    ("They continue an argument that isn't productive.", "bubbles", dict(texts=["NO!", "YES!"], acc="ARGUMENT PRODUCTIVE")),
    ("They keep pursuing an opportunity that no longer makes sense.", "door", dict(closing=True, lbl="CLOSED", acc="PURSUING SENSE")),
    ("They keep trying to force a situation that has already changed.", "puzzle", dict(missing=True, lbl="WON'T FIT", acc="FORCE CHANGED")),
    ("And they tell themselves that stopping would mean failure.", "sticker", dict(tags=["QUITTER"], acc="STOPPING FAILURE")),
    ("But sometimes stopping is simply recognizing new information.", "doc", dict(title="NEW INFO", empty=False, acc="STOPPING RECOGNIZING INFORMATION")),
    ("The important question isn't:", "question", dict(acc="QUESTION")),
    ("\"How do I continue no matter what?\"", "list", dict(items=["CONTINUE NO MATTER WHAT?"], mode="strike", acc="CONTINUE")),
    ("It's:", "pulse", dict(acc="")),
    ("\"Is continuing still the best decision?\"", "scale", dict(left="CONTINUE", right="STOP", tip=0, acc="CONTINUING BEST")),
    ("You should persist when the effort is worthwhile.", "stairs", dict(n=6, climb=4, acc="PERSIST WORTHWHILE")),
    ("You should adjust when the approach isn't working.", "path", dict(kind="fork", labels=("SAME WAY", "ADJUST"), acc="ADJUST APPROACH")),
    ("And sometimes you should stop when the direction no longer makes sense.", "door", dict(open_=True, lbl="STOP HERE", acc="STOP DIRECTION")),
    ("Persistence without reflection can become stubbornness.", "hud", dict(lbl="PERSISTENCE", start=60, end=100, lbl2="REFLECTION", start2=40, end2=3, icons=None, crowd=0, tag="STUBBORNNESS", drop=True, acc="PERSISTENCE REFLECTION STUBBORNNESS")),
    ("How do you personally distinguish persistence from stubbornness?", "scale", dict(left="PERSISTENCE", right="STUBBORNNESS", tip=0, acc="PERSISTENCE STUBBORNNESS")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="WHERE'S THE LINE?", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EFFORT", start=50, end=100, lbl2="RESULTS", start2=10, end2=10, icons="q", tag="STILL GOING?", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
