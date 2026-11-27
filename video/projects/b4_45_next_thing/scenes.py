from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH ALWAYS", "LOOKING FOR THE NEXT THING")
OUTPUT = "135_Always_Looking_For_The_Next_Thing_16x9.mp4"
SPEC = [
    ("You're watching something…", "phone", dict(content="highlight", acc="WATCHING")),
    ("But thinking about what comes next.", "brain", dict(says="WHAT'S NEXT?", acc="NEXT.")),
    ("You're working…", "bricks", dict(rows=2, lbl="WORKING", uneven=False, acc="WORKING…")),
    ("But thinking about the next goal.", "brain", dict(says="THE NEXT GOAL...", acc="NEXT GOAL.")),
    ("You're talking to someone…", "crowd", dict(n=2, acc="TALKING")),
    ("But checking what happened on your phone.", "notifs", dict(items=["NEW POST", "NEW MESSAGE"], acc="CHECKING PHONE.")),
    ("Your attention is constantly leaving the moment.", "compass", dict(lbl="ATTENTION", settle=False, acc="CONSTANTLY LEAVING")),
    ("And eventually…", "pulse", dict()),
    ("You realize you've been physically present…", "alone", dict(tag="HERE", acc="PHYSICALLY PRESENT…")),
    ("But mentally somewhere else.", "map", dict(a_lbl="YOUR BODY", b_lbl="YOUR MIND", acc="MENTALLY ELSE.")),
    ("Practice being where you are.", "alone", dict(tag="RIGHT HERE", acc="PRACTICE WHERE")),
    ("Listen.", "list", dict(items=["LISTEN"], mode="check", acc="LISTEN.")),
    ("Notice.", "list", dict(items=["LISTEN", "NOTICE"], mode="check", acc="NOTICE.")),
    ("Experience.", "list", dict(items=["LISTEN", "NOTICE", "EXPERIENCE"], mode="check", acc="EXPERIENCE.")),
    ("The future matters.", "sunrise", dict(acc="FUTURE")),
    ("But you can't experience your present from somewhere else.", "pulse", dict(acc="CAN'T PRESENT ELSE.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
