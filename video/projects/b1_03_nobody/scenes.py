from kit import build, follow_sub

TITLE = ("NOBODY CAN LIVE", "YOUR LIFE FOR YOU")
OUTPUT = "03_Nobody_Can_Live_Your_Life_For_You_16x9.mp4"
SPEC = [
    ("People can give you advice.", "bubbles", dict(texts=["DO THIS.", "TRY THAT.", "BE CAREFUL."], acc="ADVICE.")),
    ("They can encourage you.", "bubbles", dict(texts=["YOU GOT THIS!", "KEEP GOING!"], inverted=True, acc="ENCOURAGE")),
    ("They can believe in you when you don't believe in yourself.", "crowd", dict(n=5, highlight=2, highlight_label="YOU", acc="BELIEVE")),
    ("But nobody can take your place.", "alone", dict(tag="YOUR PLACE", others=4, acc="NOBODY PLACE.")),
    ("Nobody can make your decisions.", "path", dict(kind="fork", labels=("THIS WAY", "THAT WAY"), acc="DECISIONS.")),
    ("Nobody can do your work.", "list", dict(items=["YOUR WORK", "YOUR REPS", "YOUR HOURS"], mode="empty", acc="WORK.")),
    ("Nobody can live your days for you.", "timeline", dict(n=7, progress=0.6, tag="YOUR DAYS", acc="DAYS")),
    ("And that's not a lonely truth.", "alone", dict(acc="NOT LONELY")),
    ("That's freedom.", "key", dict(lbl="FREEDOM", acc="FREEDOM.")),
    ("Because the moment you realize your life is yours to build…", "bricks", dict(rows=4, lbl="YOURS TO BUILD", uneven=False, acc="YOURS BUILD…")),
    ("You stop waiting for permission.", "door", dict(open_=True, lbl="PERMISSION", acc="PERMISSION.")),
    ("You stop waiting for someone to choose you.", "crowd", dict(n=7, dim=True, acc="CHOOSE")),
    ("And you start choosing yourself.", "crown", dict(lbl="CHOSEN", acc="CHOOSING YOURSELF.")),
    ("Follow LanzoFocus for ideas that help you see life differently.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
