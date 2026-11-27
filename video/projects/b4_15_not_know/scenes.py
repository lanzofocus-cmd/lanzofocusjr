from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED", "TO NOT KNOW")
OUTPUT = "105_Youre_Allowed_To_Not_Know_16x9.mp4"
SPEC = [
    ("There's pressure to have answers.", "gauge", dict(lbl="PRESSURE", start=0.3, end=0.9, acc="PRESSURE ANSWERS.")),
    ("To know what you want.", "list", dict(items=["WHAT YOU WANT"], mode="empty", acc="WANT.")),
    ("To understand yourself.", "list", dict(items=["WHAT YOU WANT", "WHO YOU ARE"], mode="empty", acc="UNDERSTAND")),
    ("To have a plan.", "list", dict(items=["WHAT YOU WANT", "WHO YOU ARE", "THE PLAN"], mode="empty", acc="PLAN.")),
    ("But sometimes…", "pulse", dict()),
    ("You genuinely don't know.", "question", dict(acc="GENUINELY DON'T KNOW.")),
    ("And pretending you do can lead you into decisions you haven't thought through.", "path", dict(kind="winding", acc="PRETENDING HAVEN'T")),
    ("It's okay to say…", "pulse", dict(acc="OKAY")),
    ("\"I'm still figuring it out.\"", "quote", dict(text="I'M STILL FIGURING IT OUT.", acc="FIGURING")),
    ("\"I'm not sure.\"", "quote", dict(text="I'M NOT SURE.", acc="NOT SURE.\"")),
    ("\"I need more time.\"", "quote", dict(text="I NEED MORE TIME.", acc="TIME.\"")),
    ("Those aren't failures.", "sticker", dict(tags=["FAILURE"], strike=True, acc="AREN'T FAILURES.")),
    ("They're honest answers.", "list", dict(items=["HONEST"], mode="check", acc="HONEST ANSWERS.")),
    ("And honest uncertainty is often more useful than false confidence.", "scale", dict(left="HONEST DOUBT", right="FALSE CONFIDENCE", tip=-1, acc="HONEST UNCERTAINTY FALSE CONFIDENCE.")),
    ("You don't need to invent certainty just to make other people comfortable.", "ring", dict(tags=["SO WHAT'S THE PLAN?", "DECIDED YET?"], acc="INVENT CERTAINTY COMFORTABLE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
