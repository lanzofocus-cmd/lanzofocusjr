from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO", "MAKE YOU FEEL SMALL")
OUTPUT = "107_The_People_Who_Make_You_Feel_Small_16x9.mp4"
SPEC = [
    ("Pay attention to how you feel after spending time with someone.", "gauge", dict(lbl="HOW YOU FEEL", start=0.5, end=0.3, acc="FEEL AFTER")),
    ("Not just whether they are funny.", "list", dict(items=["FUNNY"], mode="empty", acc="FUNNY.")),
    ("Popular.", "list", dict(items=["FUNNY", "POPULAR"], mode="empty", acc="POPULAR.")),
    ("Interesting.", "list", dict(items=["FUNNY", "POPULAR", "INTERESTING"], mode="empty", acc="INTERESTING.")),
    ("Or impressive.", "list", dict(items=["FUNNY", "POPULAR", "INTERESTING", "IMPRESSIVE"], mode="empty", acc="IMPRESSIVE.")),
    ("Do you feel comfortable being yourself?", "alone", dict(tag="YOURSELF?", acc="COMFORTABLE YOURSELF?")),
    ("Can you disagree?", "bubbles", dict(texts=["I SEE IT DIFFERENTLY."], acc="DISAGREE?")),
    ("Can you make mistakes?", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKES?")),
    ("Can you talk without constantly measuring your words?", "doc", dict(title="EVERY WORD", empty=False, stamp="MEASURED", acc="MEASURING WORDS?")),
    ("Some relationships make you feel like you have to shrink…", "frame", dict(who="SHRINKING", fade=True, acc="SHRINK…")),
    ("To keep the peace.", "scale", dict(left="YOU", right="PEACE", tip=1, acc="PEACE.")),
    ("But healthy connection shouldn't require you to become less of yourself.", "ring", dict(center_tag="FULLY YOU", acc="HEALTHY SHOULDN'T LESS")),
    ("Pay attention to the people around whom you don't have to perform.", "stage", dict(empty=True, performing=False, acc="DON'T PERFORM.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
