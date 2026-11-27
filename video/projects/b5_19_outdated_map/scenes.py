from kit import build, follow_sub

TITLE = ("THE OUTDATED", "MAP")
OUTPUT = "159_The_Outdated_Map_16x9.mp4"
SPEC = [
    ("A map can be accurate…", "map", dict(a_lbl="THE PLAN", b_lbl="THE GOAL", acc="MAP ACCURATE")),
    ("And still be useless if the world has changed.", "fog", dict(lbl="THE WORLD CHANGED", acc="USELESS CHANGED")),
    ("The same is true of your plans.", "doc", dict(title="PLAN", empty=False, acc="PLANS")),
    ("What worked last year may not work now.", "timeline", dict(n=8, progress=0.7, tag="NOW", acc="LAST YEAR NOW")),
    ("What you wanted at fifteen may not be what you want at twenty.", "shed", dict(old="AT 15", new="AT 20", acc="FIFTEEN TWENTY")),
    ("You don't have to follow an outdated plan just because you spent time creating it.", "doc", dict(title="OLD PLAN", empty=False, stamp="OUTDATED", acc="OUTDATED PLAN")),
    ("Adjusting isn't automatically quitting.", "path", dict(kind="fork", labels=("OLD ROUTE", "NEW ROUTE"), acc="ADJUSTING QUITTING")),
    ("Save this reminder: changing your direction doesn't mean your previous effort was wasted.", "cta", dict(kind="save", lbl="NOTHING WASTED", acc="SAVE DIRECTION WASTED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
