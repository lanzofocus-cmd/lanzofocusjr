from kit import build, follow_sub

TITLE = ("YOU'RE MORE DISTRACTED", "THAN YOU REALIZE")
OUTPUT = "11_Youre_More_Distracted_Than_You_Realize_16x9.mp4"
SPEC = [
    ("Your biggest problem might not be a lack of discipline.", "gauge", dict(lbl="DISCIPLINE", start=0.5, end=0.55, acc="NOT DISCIPLINE.")),
    ("It might be that you've forgotten what it's like to focus.", "compass", dict(lbl="FOCUS", settle=False, acc="FORGOTTEN FOCUS.")),
    ("You've trained your mind to expect something new every few seconds.", "brain", dict(says="WHAT'S NEXT?", says2="SOMETHING NEW?", acc="EVERY SECONDS.")),
    ("A notification.", "notifs", dict(items=["NEW NOTIFICATION"], acc="NOTIFICATION.")),
    ("A video.", "notifs", dict(items=["NEW NOTIFICATION", "WATCH THIS VIDEO"], acc="VIDEO.")),
    ("A message.", "notifs", dict(items=["NEW NOTIFICATION", "WATCH THIS VIDEO", "1 NEW MESSAGE"], acc="MESSAGE.")),
    ("Something to keep you entertained.", "notifs", dict(items=["NEW NOTIFICATION", "WATCH THIS VIDEO", "1 NEW MESSAGE", "YOU'LL LOVE THIS"], acc="ENTERTAINED.")),
    ("And now, anything that requires patience feels unbearable.", "progress", dict(lbl="PATIENCE", value=0.06, acc="PATIENCE UNBEARABLE.")),
    ("But the things that change your life rarely happen in thirty seconds.", "hourglass", dict(acc="RARELY THIRTY SECONDS.")),
    ("Your attention is one of the most valuable things you own.", "price", dict(text="ATTENTION", sub="PRICELESS", acc="ATTENTION VALUABLE")),
    ("Be careful who—or what—you give it to.", "key", dict(lbl="YOUR ATTENTION", acc="CAREFUL")),
    ("Follow LanzoFocus for ideas and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
