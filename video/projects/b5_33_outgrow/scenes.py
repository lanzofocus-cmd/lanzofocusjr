from kit import build, follow_sub

TITLE = ("THE PEOPLE", "YOU OUTGROW")
OUTPUT = "173_The_People_You_Outgrow_16x9.mp4"
SPEC = [
    ("Outgrowing someone doesn't always mean they did something wrong.", "list", dict(items=["SOMETHING WRONG"], mode="strike", acc="OUTGROWING WRONG")),
    ("Sometimes you simply begin moving in different directions.", "path", dict(kind="fork", labels=("YOU", "THEM"), walker=False, acc="DIFFERENT DIRECTIONS")),
    ("Different interests.", "list", dict(items=["INTERESTS"], mode="tag", tag="DIFFERENT", acc="INTERESTS")),
    ("Different priorities.", "list", dict(items=["INTERESTS", "PRIORITIES"], mode="tag", tag="DIFFERENT", acc="PRIORITIES")),
    ("Different conversations.", "list", dict(items=["INTERESTS", "PRIORITIES", "CONVERSATIONS"], mode="tag", tag="DIFFERENT", acc="CONVERSATIONS")),
    ("You can appreciate what someone meant to your life…", "frame", dict(who="WHAT THEY MEANT", acc="APPRECIATE MEANT")),
    ("Without forcing the relationship to remain exactly the same forever.", "lock", dict(lbl="THE SAME FOREVER", opening=True, acc="FORCING SAME FOREVER")),
    ("Not every ending needs a villain.", "book", dict(chapter="THE END", text="NO VILLAIN", acc="ENDING VILLAIN")),
    ("Save this if you're learning that change doesn't always mean betrayal.", "cta", dict(kind="save", lbl="CHANGE ISN'T BETRAYAL", acc="SAVE CHANGE BETRAYAL")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
