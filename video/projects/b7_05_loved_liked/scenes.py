from kit import build, follow_sub, hook

TITLE = ("BEING LOVED VS", "BEING LIKED")
OUTPUT = "205_The_Difference_Between_Being_Loved_And_Being_Liked_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes people confuse being liked by everyone with being a good person.", "hud", dict(lbl="LIKED BY EVERYONE", start=40, end=100, icons="thumb", tag="GOOD PERSON?", acc="LIKED EVERYONE GOOD")),
    ("They avoid disagreement.", "list", dict(items=["AVOID DISAGREEMENT"], mode="check", acc="DISAGREEMENT")),
    ("They hide their opinions.", "list", dict(items=["AVOID DISAGREEMENT", "HIDE OPINIONS"], mode="check", acc="OPINIONS")),
    ("They say yes when they mean no.", "bubbles", dict(texts=["YES, OF COURSE!"], acc="YES NO")),
    ("They change themselves depending on who is watching.", "sticker", dict(tags=["FOR THEM", "FOR HER", "FOR HIM", "FOR WORK"], acc="CHANGE WATCHING")),
    ("Eventually, they become incredibly easy to like…", "hud", dict(lbl="EASY TO LIKE", start=60, end=100, icons="heart", acc="EASY LIKE")),
    ("But incredibly difficult to know.", "hud", dict(lbl="EASY TO LIKE", start=100, end=100, lbl2="EASY TO KNOW", start2=30, end2=4, icons="q", acc="DIFFICULT KNOW")),
    ("Because nobody sees the real person underneath all the adjustments.", "iceberg", dict(top="THE ADJUSTMENTS", bottom="THE REAL PERSON", acc="REAL UNDERNEATH")),
    ("Being liked can feel comforting.", "gauge", dict(lbl="COMFORT", start=0.3, end=0.8, acc="COMFORTING")),
    ("But genuine connection requires honesty.", "key", dict(lbl="HONESTY", acc="GENUINE HONESTY")),
    ("People cannot truly know you if you constantly edit yourself to prevent every possible disagreement.", "doc", dict(title="YOU (EDITED)", empty=False, stamp="REDACTED", drop=True, acc="TRULY KNOW EDIT")),
    ("You don't need to become rude.", "list", dict(items=["BE RUDE"], mode="strike", acc="RUDE")),
    ("You don't need to intentionally upset people.", "list", dict(items=["BE RUDE", "UPSET PEOPLE"], mode="strike", acc="UPSET")),
    ("You simply need to understand that being honest about who you are will sometimes mean someone doesn't agree with you.", "scale", dict(left="HONEST", right="AGREED WITH", tip=-1, acc="HONEST AGREE")),
    ("And that's okay.", "list", dict(items=["THAT'S OKAY"], mode="check", acc="OKAY")),
    ("The goal isn't to make everyone approve of you.", "hud", dict(lbl="APPROVAL", start=100, end=60, icons=None, crowd=4, cross=True, acc="EVERYONE APPROVE")),
    ("The goal is to build relationships where you don't have to pretend to be someone else to belong.", "ring", dict(center_tag="THE REAL YOU", acc="PRETEND BELONG")),
    ("What's something you believe people should stop doing just to be liked?", "brain", dict(says="STOP DOING...", acc="STOP LIKED")),
    ("Let's discuss it in the comments.", "cta", dict(kind="comment", lbl="STOP DOING THIS", acc="DISCUSS COMMENTS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="BEING LIKED", start=10, end=100, lbl2="BEING KNOWN", start2=90, end2=5, icons="thumb", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
