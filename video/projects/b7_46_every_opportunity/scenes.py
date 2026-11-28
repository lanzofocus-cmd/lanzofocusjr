from kit import build, follow_sub, hook

TITLE = ("WHEN YOU STOP CHASING", "EVERY OPPORTUNITY")
OUTPUT = "246_The_Moment_You_Stop_Chasing_Every_Opportunity_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Not every opportunity is a good opportunity.", "door", dict(open_=True, lbl="OPPORTUNITY?", acc="EVERY GOOD")),
    ("Sometimes something looks attractive…", "crown", dict(lbl="ATTRACTIVE", acc="ATTRACTIVE")),
    ("But doesn't fit your priorities.", "puzzle", dict(missing=True, lbl="DOESN'T FIT", acc="FIT PRIORITIES")),
    ("Sometimes you accept because you're afraid another chance won't appear.", "gauge", dict(lbl="FEAR OF MISSING OUT", start=0.2, end=0.85, acc="AFRAID ANOTHER")),
    ("Sometimes you say yes because the opportunity sounds impressive.", "bubbles", dict(texts=["YES! OF COURSE!"], acc="YES IMPRESSIVE")),
    ("And suddenly, your life becomes filled with things you never had time to properly consider.", "tangle", dict(lbl="YES TO EVERYTHING", acc="FILLED CONSIDER")),
    ("Opportunity is valuable.", "list", dict(items=["OPPORTUNITY"], mode="check", acc="VALUABLE")),
    ("But so is the ability to choose.", "path", dict(kind="fork", labels=("YES", "NO"), drop=True, acc="ABILITY CHOOSE")),
    ("You don't need to accept everything.", "list", dict(items=["ACCEPT EVERYTHING"], mode="strike", acc="ACCEPT")),
    ("You don't need to pursue every possible direction.", "network", dict(nodes=["THIS", "THAT", "THAT TOO", "AND THIS"], tangled=True, acc="PURSUE EVERY DIRECTION")),
    ("Sometimes saying no to one thing allows you to give your attention to something more meaningful.", "scale", dict(left="NO", right="MEANINGFUL", tip=1, acc="NO ATTENTION MEANINGFUL")),
    ("The goal isn't to collect opportunities.", "coins", dict(stacks=6, lbl="COLLECTED?", acc="COLLECT")),
    ("It's to choose the opportunities that actually align with what you want to build.", "compass", dict(lbl="WHAT YOU'RE BUILDING", acc="CHOOSE ALIGN BUILD")),
    ("What's something people should learn to say no to more often?", "cta", dict(kind="comment", lbl="SAY NO TO...", acc="NO")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="OPPORTUNITIES ACCEPTED", start=5, end=100, lbl2="FOCUS", start2=90, end2=4, icons="thumb", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
