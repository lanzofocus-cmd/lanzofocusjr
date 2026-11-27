from kit import build, follow_sub

TITLE = ("YOU'RE NOT MISSING OUT ON", "AS MUCH AS YOU THINK")
OUTPUT = "92_Youre_Not_Missing_Out_On_As_Much_As_You_Think_16x9.mp4"
SPEC = [
    ("Your phone makes it look like everyone is living a better life than you.", "phone", dict(content="highlight", lbl="YOU", acc="PHONE BETTER")),
    ("Someone is traveling.", "notifs", dict(items=["✈ TRAVELING"], acc="TRAVELING.")),
    ("Someone is celebrating.", "notifs", dict(items=["✈ TRAVELING", "★ CELEBRATING"], acc="CELEBRATING.")),
    ("Someone is achieving something.", "notifs", dict(items=["✈ TRAVELING", "★ CELEBRATING", "✔ ACHIEVED IT"], acc="ACHIEVING")),
    ("Someone is having the best day of their life.", "notifs", dict(items=["✈ TRAVELING", "★ CELEBRATING", "✔ ACHIEVED IT", "BEST DAY EVER"], acc="BEST DAY")),
    ("And you're sitting there…", "alone", dict(acc="SITTING")),
    ("Watching all of it.", "phone", dict(content="highlight", lbl="WATCHING", acc="WATCHING")),
    ("But you're seeing moments.", "dots", dict(connect=False, acc="MOMENTS.")),
    ("Not entire lives.", "timeline", dict(n=12, progress=0.0, acc="NOT ENTIRE LIVES.")),
    ("You don't see the boring days.", "iceberg", dict(top="THE POST", bottom="THE BORING DAYS", acc="BORING")),
    ("The problems.", "iceberg", dict(top="THE POST", bottom="THE PROBLEMS", acc="PROBLEMS.")),
    ("The uncertainty.", "iceberg", dict(top="THE POST", bottom="THE UNCERTAINTY", acc="UNCERTAINTY.")),
    ("The things they don't post.", "iceberg", dict(top="THE POST", bottom="EVERYTHING ELSE", acc="DON'T POST.")),
    ("Your life isn't supposed to compete with a collection of edited moments.", "scale", dict(left="YOUR LIFE", right="EDITED MOMENTS", tip=0, acc="ISN'T COMPETE EDITED")),
    ("You don't need to be everywhere to have a life worth living.", "map", dict(a_lbl="HERE", b_lbl="", acc="EVERYWHERE WORTH LIVING.")),
    ("Put the phone down.", "phone", dict(content="none", acc="PHONE DOWN.")),
    ("Your own life is happening, too.", "sunrise", dict(acc="OWN HAPPENING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
