from kit import build, follow_sub, hook

TITLE = ("THE THINGS YOU", "CAN'T RECOVER")
OUTPUT = "214_The_Things_You_Cant_Recover_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("There are things in life you can replace.", "receipt", dict(items=[("REPLACEABLE", "YES")], acc="REPLACE")),
    ("Money.", "coins", dict(stacks=4, lbl="REPLACEABLE", acc="MONEY")),
    ("Objects.", "list", dict(items=["OBJECTS"], mode="tag", tag="REPLACEABLE", acc="OBJECTS")),
    ("Some opportunities.", "door", dict(open_=True, lbl="ANOTHER ONE", acc="OPPORTUNITIES")),
    ("Some mistakes can be corrected.", "list", dict(items=["MISTAKE"], mode="check", acc="CORRECTED")),
    ("But there are things you cannot recover in exactly the same form.", "hourglass", dict(acc="CANNOT RECOVER")),
    ("A conversation with someone who is no longer around.", "chairs", dict(n=3, lbl="NO LONGER HERE", acc="CONVERSATION LONGER")),
    ("A childhood moment.", "frame", dict(who="CHILDHOOD", fade=True, acc="CHILDHOOD")),
    ("A specific day.", "big", dict(text="ONE DAY", sub="ONLY ONCE", acc="SPECIFIC")),
    ("An opportunity that existed only once.", "door", dict(closing=True, lbl="ONLY ONCE", acc="ONLY ONCE")),
    ("A moment when someone needed you.", "crowd", dict(n=3, highlight=1, highlight_label="NEEDED YOU", acc="NEEDED")),
    ("This doesn't mean you should live constantly afraid of losing things.", "list", dict(items=["LIVE AFRAID"], mode="strike", acc="AFRAID LOSING")),
    ("It means you should pay attention while they're still present.", "pulse", dict(drop=True, acc="ATTENTION STILL PRESENT")),
    ("Sometimes we're so focused on improving the future…", "map", dict(a_lbl="NOW", b_lbl="THE FUTURE", acc="IMPROVING FUTURE")),
    ("That we forget to experience what is already happening.", "sunrise", dict(acc="EXPERIENCE ALREADY")),
    ("The people around you won't remain exactly the same forever.", "ring", dict(acc="SAME FOREVER")),
    ("Your circumstances will change.", "chart", dict(kind="wave", lbl="CIRCUMSTANCES", acc="CIRCUMSTANCES")),
    ("Your interests will change.", "shed", dict(old="THEN", new="NOW", acc="INTERESTS")),
    ("Your life will move.", "timeline", dict(n=10, progress=0.5, tag="MOVING", acc="MOVE")),
    ("You don't need to stop building your future.", "bricks", dict(rows=4, lbl="THE FUTURE", uneven=False, acc="BUILDING FUTURE")),
    ("But don't let the future become an excuse to ignore your present.", "scale", dict(left="FUTURE", right="PRESENT", tip=0, acc="EXCUSE PRESENT")),
    ("Send this to someone whose presence you genuinely appreciate.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND APPRECIATE")),
    ("", "follow"),
]
_HOOK = ("hourglass", dict())
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
