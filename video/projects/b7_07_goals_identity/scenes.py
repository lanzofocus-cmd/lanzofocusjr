from kit import build, follow_sub, hook

TITLE = ("WHEN YOUR GOALS BECOME", "YOUR ENTIRE IDENTITY")
OUTPUT = "207_When_Your_Goals_Become_Your_Entire_Identity_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Goals are important.", "compass", dict(lbl="GOALS", acc="GOALS")),
    ("They give you direction.", "path", dict(kind="straight", acc="DIRECTION")),
    ("They help you organize your effort.", "list", dict(items=["PLAN", "PRACTICE", "PROGRESS"], mode="check", acc="ORGANIZE")),
    ("They give you something to work toward.", "stairs", dict(n=6, climb=3, acc="WORK")),
    ("But there's a problem when your entire identity becomes attached to achieving them.", "sticker", dict(tags=["MY GOAL = ME"], acc="IDENTITY ATTACHED")),
    ("Imagine someone who defines themselves entirely by their grades.", "doc", dict(title="REPORT CARD", empty=False, acc="DEFINES GRADES")),
    ("What happens when they receive a bad result?", "doc", dict(title="REPORT CARD", empty=False, stamp="C-", acc="BAD RESULT")),
    ("Or someone who only sees themselves as an athlete.", "sticker", dict(tags=["ATHLETE"], acc="ATHLETE")),
    ("What happens when they can't play?", "sticker", dict(tags=["ATHLETE"], strike=True, acc="CAN'T PLAY")),
    ("Or someone who believes their worth depends on being successful.", "price", dict(text="WORTH = SUCCESS?", acc="WORTH SUCCESSFUL")),
    ("What happens when things don't go according to plan?", "chart", dict(kind="down", lbl="THE PLAN", acc="PLAN")),
    ("A goal should be something you're pursuing.", "map", dict(a_lbl="YOU", b_lbl="THE GOAL", acc="PURSUING")),
    ("It shouldn't be the only thing that makes you feel like you matter.", "hud", dict(lbl="YOUR WORTH", start=100, end=100, icons=None, crowd=0, tag="WITH OR WITHOUT IT", acc="ONLY MATTER")),
    ("You can care deeply about achievement…", "crown", dict(lbl="ACHIEVEMENT", acc="ACHIEVEMENT")),
    ("Without allowing achievement to define your entire existence.", "iceberg", dict(top="ACHIEVEMENTS", bottom="EVERYTHING ELSE YOU ARE", acc="DEFINE EXISTENCE")),
    ("You are more than your performance.", "list", dict(items=["PERFORMANCE"], mode="tag", tag="NOT ALL OF YOU", acc="PERFORMANCE")),
    ("More than your productivity.", "list", dict(items=["PERFORMANCE", "PRODUCTIVITY"], mode="tag", tag="NOT ALL OF YOU", acc="PRODUCTIVITY")),
    ("More than your results.", "list", dict(items=["PERFORMANCE", "PRODUCTIVITY", "RESULTS"], mode="tag", tag="NOT ALL OF YOU", acc="RESULTS")),
    ("Build your goals.", "bricks", dict(rows=4, lbl="YOUR GOALS", uneven=False, acc="BUILD")),
    ("Take them seriously.", "list", dict(items=["TAKE IT SERIOUSLY"], mode="check", acc="SERIOUSLY")),
    ("But remember that you're a human being living a life…", "pulse", dict(drop=True, acc="HUMAN LIFE")),
    ("Not a machine designed to produce achievements.", "progress", dict(lbl="OUTPUT", value=0.9, acc="MACHINE ACHIEVEMENTS")),
    ("What is something about yourself that matters beyond your achievements?", "network", dict(nodes=["KINDNESS", "HUMOR", "CURIOSITY", "LOYALTY"], tangled=False, acc="BEYOND ACHIEVEMENTS")),
    ("Share it below.", "cta", dict(kind="comment", lbl="WHAT MATTERS BEYOND", acc="SHARE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="GOAL PROGRESS", start=90, end=20, lbl2="SELF-WORTH", start2=90, end2=20, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
