from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH", "ALWAYS BEING RIGHT")
OUTPUT = "179_The_Problem_With_Always_Being_Right_16x9.mp4"
SPEC = [
    ("If being right is more important than learning…", "scale", dict(left="BEING RIGHT", right="LEARNING", tip=-1, acc="RIGHT LEARNING")),
    ("You eventually stop growing.", "plant", dict(height=0.25, roots=False, lbl="STOPPED GROWING", acc="STOP GROWING")),
    ("You defend your opinions.", "shield", dict(front="MY OPINION", back="EGO", acc="DEFEND OPINIONS")),
    ("Ignore evidence.", "doc", dict(title="EVIDENCE", empty=False, stamp="IGNORED", acc="IGNORE EVIDENCE")),
    ("Turn conversations into competitions.", "bubbles", dict(texts=["I'M RIGHT.", "NO, I'M RIGHT."], acc="COMPETITIONS")),
    ("But changing your mind isn't weakness.", "brain", dict(says="I WAS WRONG.", acc="CHANGING WEAKNESS")),
    ("It's what happens when new information is more important than protecting your ego.", "scale", dict(left="NEW INFORMATION", right="EGO", tip=-1, acc="INFORMATION EGO")),
    ("Comment \"LEARN\" if you'd rather improve your thinking than win every argument.", "cta", dict(kind="comment", lbl="COMMENT \"LEARN\"", acc="LEARN IMPROVE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
