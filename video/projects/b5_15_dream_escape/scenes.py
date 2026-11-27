from kit import build, follow_sub

TITLE = ("A DREAM VS", "AN ESCAPE")
OUTPUT = "155_The_Difference_Between_A_Dream_And_An_Escape_16x9.mp4"
SPEC = [
    ("A dream gives you somewhere to go.", "map", dict(a_lbl="HERE", b_lbl="THE DREAM", acc="DREAM GO")),
    ("An escape gives you somewhere to hide.", "door", dict(open_=True, lbl="ESCAPE", acc="ESCAPE HIDE")),
    ("Sometimes we create huge goals because we're uncomfortable with the life we currently have.", "fog", dict(lbl="RIGHT NOW", acc="HUGE GOALS UNCOMFORTABLE")),
    ("But if you never learn to deal with the present…", "hourglass", dict(acc="PRESENT")),
    ("You'll carry the same problems into your future.", "scale", dict(left="SAME PROBLEMS", right="FUTURE", tip=-1, acc="SAME PROBLEMS FUTURE")),
    ("Build your future.", "bricks", dict(rows=4, lbl="YOUR FUTURE", uneven=False, acc="BUILD FUTURE")),
    ("But don't use it to avoid your current life.", "alone", dict(tag="YOUR LIFE NOW", acc="AVOID CURRENT")),
    ("Save this if you're building something while still learning to deal with where you are.", "cta", dict(kind="save", lbl="BUILD, BUT BE HERE", acc="SAVE BUILDING WHERE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
