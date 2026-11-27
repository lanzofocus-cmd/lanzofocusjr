from kit import build, follow_sub

TITLE = ("THE COST OF", "BEING AVAILABLE")
OUTPUT = "143_The_Cost_Of_Being_Available_16x9.mp4"
SPEC = [
    ("You can be available to everyone…", "ring", dict(tags=["CAN YOU?", "QUICK FAVOR", "GOT A SEC?", "HELP ME"], acc="EVERYONE")),
    ("And unavailable to yourself.", "mirror", dict(reflect="dashed", lbl="YOU?", acc="UNAVAILABLE YOURSELF")),
    ("Every interruption.", "notifs", dict(items=["GOT A MINUTE?"], acc="INTERRUPTION")),
    ("Every unnecessary conversation.", "bubbles", dict(texts=["SO ANYWAY...", "AND THEN..."], acc="UNNECESSARY")),
    ("Every request you accept when you already know you need time.", "receipt", dict(items=[("FAVOR", "1 HR"), ("CALL", "2 HRS"), ("ERRAND", "3 HRS")], total="YOUR TIME", acc="REQUEST TIME")),
    ("Eventually, your own priorities become the things you keep postponing.", "list", dict(items=["MY GOALS", "MY HEALTH", "MY REST"], mode="tag", tag="LATER", acc="PRIORITIES POSTPONING")),
    ("Being a good person doesn't mean giving away every hour of your life.", "hourglass", dict(acc="GOOD EVERY HOUR")),
    ("What is one thing you've been postponing because you've given everyone else your time?", "brain", dict(says="LATER...", says2="ALWAYS LATER", acc="POSTPONING TIME")),
    ("Comment it.", "cta", dict(kind="comment", lbl="WHAT YOU'VE POSTPONED", acc="COMMENT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
