from kit import build, follow_sub, hook

TITLE = ("LEARN TO HANDLE", "DISAPPOINTMENT")
OUTPUT = "252_Why_You_Should_Learn_To_Handle_Disappointment_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Disappointment is strange.", "pulse", dict(acc="DISAPPOINTMENT")),
    ("You can work toward something for a long time.", "stairs", dict(n=7, climb=5, acc="WORK LONG")),
    ("Imagine the result.", "frame", dict(who="THE RESULT", acc="RESULT")),
    ("Prepare yourself.", "list", dict(items=["PREPARED"], mode="check", acc="PREPARE")),
    ("Expect things to go a certain way.", "map", dict(a_lbl="NOW", b_lbl="THE PLAN", acc="EXPECT")),
    ("And then…", "pulse", dict(acc="")),
    ("It doesn't happen.", "big", dict(text="NO.", acc="DOESN'T")),
    ("The opportunity disappears.", "door", dict(closing=True, lbl="GONE", acc="DISAPPEARS")),
    ("The result isn't what you wanted.", "scale", dict(left="WANTED", right="GOT", tip=-1, acc="WANTED")),
    ("Someone lets you down.", "bubbles", dict(texts=["SORRY, I CAN'T."], acc="DOWN")),
    ("The plan changes.", "path", dict(kind="fork", labels=("THE PLAN", "REALITY"), acc="CHANGES")),
    ("And suddenly, you're not only disappointed about what happened.", "chart", dict(kind="down", lbl="WHAT HAPPENED", acc="DISAPPOINTED HAPPENED")),
    ("You're disappointed about the future you imagined.", "frame", dict(who="THE IMAGINED FUTURE", fade=True, acc="FUTURE IMAGINED")),
    ("That's why disappointment can feel so heavy.", "scale", dict(left="DISAPPOINTMENT", right="YOU", tip=-1, acc="HEAVY")),
    ("You're losing something that may never have actually existed.", "frame", dict(who="NEVER EXISTED", dashed_fig=True, acc="LOSING NEVER EXISTED")),
    ("The version of the future you expected.", "list", dict(items=["THE FUTURE YOU EXPECTED"], mode="strike", acc="EXPECTED")),
    ("The outcome you pictured.", "list", dict(items=["THE FUTURE YOU EXPECTED", "THE OUTCOME YOU PICTURED"], mode="strike", acc="PICTURED")),
    ("The conversation you hoped would happen.", "list", dict(items=["THE FUTURE YOU EXPECTED", "THE OUTCOME YOU PICTURED", "THE CONVERSATION"], mode="strike", acc="HOPED")),
    ("The achievement you thought was guaranteed.", "list", dict(items=["THE FUTURE YOU EXPECTED", "THE OUTCOME YOU PICTURED", "THE CONVERSATION", "THE \"SURE THING\""], mode="strike", acc="GUARANTEED")),
    ("But disappointment doesn't mean your entire effort was worthless.", "bricks", dict(rows=4, lbl="STILL BUILT", uneven=False, acc="EFFORT WORTHLESS")),
    ("It doesn't mean you're incapable.", "sticker", dict(tags=["INCAPABLE"], strike=True, acc="INCAPABLE")),
    ("It doesn't mean you should stop hoping.", "sunrise", dict(acc="HOPING")),
    ("It means reality didn't match your expectation.", "scale", dict(left="REALITY", right="EXPECTATION", tip=0, acc="REALITY EXPECTATION")),
    ("And now you have a choice.", "path", dict(kind="fork", labels=("FORCE IT", "MOVE FORWARD"), acc="CHOICE")),
    ("You can spend all your energy trying to force reality to match the picture you created…", "battery", dict(lbl="YOUR ENERGY", start=0.9, end=0.1, drains=1, acc="FORCE REALITY PICTURE")),
    ("Or you can acknowledge what happened and decide what comes next.", "stairs", dict(n=6, climb=1, acc="ACKNOWLEDGE NEXT")),
    ("You don't have to pretend disappointment doesn't hurt.", "list", dict(items=["PRETEND IT DOESN'T HURT"], mode="strike", acc="PRETEND HURT")),
    ("But you don't have to let disappointment become your permanent direction.", "compass", dict(lbl="NOT PERMANENT", acc="PERMANENT DIRECTION")),
    ("Sometimes the most important skill isn't avoiding disappointment.", "list", dict(items=["AVOID DISAPPOINTMENT"], mode="strike", acc="SKILL AVOIDING")),
    ("It's learning how to move forward after it.", "beam", dict(lbl="FORWARD", tags=("WHAT I EXPECTED",), drop=True, acc="MOVE FORWARD AFTER")),
    ("What has disappointment taught you that success probably couldn't?", "book", dict(chapter="WHAT IT TAUGHT ME", acc="TAUGHT SUCCESS")),
    ("Share your lesson in the comments.", "cta", dict(kind="comment", lbl="YOUR LESSON", acc="LESSON COMMENTS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EXPECTATION", start=40, end=100, lbl2="REALITY", start2=40, end2=12, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
