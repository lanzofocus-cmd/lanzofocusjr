from kit import build, follow_sub

TITLE = ("THE MOMENT YOU REALIZE", "YOU HAVE OPTIONS")
OUTPUT = "84_The_Moment_You_Realize_You_Have_Options_16x9.mp4"
SPEC = [
    ("Sometimes…", "pulse", dict()),
    ("You feel trapped because you can only see one possible path.", "path", dict(kind="straight", acc="TRAPPED ONE PATH.")),
    ("One way to succeed.", "list", dict(items=["ONE WAY TO SUCCEED"], mode="empty", acc="ONE")),
    ("One way to be happy.", "list", dict(items=["ONE WAY TO SUCCEED", "ONE WAY TO BE HAPPY"], mode="empty", acc="ONE")),
    ("One way to solve the problem.", "list", dict(items=["ONE WAY TO SUCCEED", "ONE WAY TO BE HAPPY", "ONE SOLUTION"], mode="empty", acc="ONE")),
    ("One way your life should look.", "frame", dict(who="THE ONE WAY", acc="ONE")),
    ("But what if there are more options than you've considered?", "network", dict(nodes=["OPTION A", "OPTION B", "OPTION C", "OPTION D", "OPTION E"], tangled=False, acc="MORE OPTIONS")),
    ("What if the path isn't working…", "path", dict(kind="winding", acc="ISN'T WORKING…")),
    ("Because you're trying to force yourself through the wrong door?", "door", dict(lbl="WRONG DOOR", acc="FORCE WRONG DOOR?")),
    ("You don't always need to work harder.", "gauge", dict(lbl="EFFORT", start=0.9, end=0.9, acc="HARDER.")),
    ("Sometimes you need to look around.", "compass", dict(lbl="LOOK AROUND", settle=False, acc="LOOK AROUND.")),
    ("Ask different questions.", "question", dict(acc="DIFFERENT QUESTIONS.")),
    ("Consider alternatives.", "path", dict(kind="fork", labels=("THE OLD ROAD", "ANOTHER ROAD"), acc="ALTERNATIVES.")),
    ("Being determined to reach your destination…", "map", dict(a_lbl="YOU", b_lbl="DESTINATION", acc="DETERMINED DESTINATION…")),
    ("Doesn't mean you must take the same road forever.", "map", dict(a_lbl="SAME ROAD?", b_lbl="SAME DESTINATION", acc="SAME ROAD FOREVER.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
