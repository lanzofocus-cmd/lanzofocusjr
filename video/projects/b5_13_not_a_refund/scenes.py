from kit import build, follow_sub

TITLE = ("YOUR FUTURE IS", "NOT A REFUND")
OUTPUT = "153_Your_Future_Is_Not_A_Refund_16x9.mp4"
SPEC = [
    ("You can't get yesterday back.", "hourglass", dict(acc="CAN'T YESTERDAY")),
    ("You can't refund the hours.", "receipt", dict(items=[("YESTERDAY", "SPENT"), ("THOSE HOURS", "SPENT")], total="NO REFUNDS", acc="REFUND HOURS")),
    ("You can't reopen every opportunity.", "door", dict(closing=True, lbl="THAT CHANCE", acc="REOPEN OPPORTUNITY")),
    ("But you can stop spending tomorrow trying to recover yesterday.", "map", dict(a_lbl="YESTERDAY", b_lbl="TOMORROW", acc="TOMORROW RECOVER YESTERDAY")),
    ("Regret becomes useful when it changes your next decision.", "key", dict(lbl="NEXT DECISION", acc="REGRET USEFUL NEXT")),
    ("Otherwise, it becomes another way to lose time.", "progress", dict(lbl="TIME LEFT", value=0.3, acc="LOSE TIME")),
    ("What's one lesson from your past that changed how you spend your time now?", "cta", dict(kind="comment", lbl="YOUR LESSON", acc="LESSON PAST NOW")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
