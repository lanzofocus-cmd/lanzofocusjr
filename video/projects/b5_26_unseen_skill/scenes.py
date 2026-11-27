from kit import build, follow_sub

TITLE = ("THE UNSEEN", "SKILL")
OUTPUT = "166_The_Unseen_Skill_16x9.mp4"
SPEC = [
    ("The most valuable skills aren't always impressive to watch.", "stage", dict(lbl="NOT IMPRESSIVE", empty=True, acc="VALUABLE IMPRESSIVE")),
    ("Listening.", "list", dict(items=["LISTENING"], mode="check", acc="LISTENING")),
    ("Communicating.", "list", dict(items=["LISTENING", "COMMUNICATING"], mode="check", acc="COMMUNICATING")),
    ("Managing your time.", "list", dict(items=["LISTENING", "COMMUNICATING", "MANAGING TIME"], mode="check", acc="TIME")),
    ("Admitting mistakes.", "list", dict(items=["LISTENING", "COMMUNICATING", "MANAGING TIME", "ADMITTING MISTAKES"], mode="check", acc="MISTAKES")),
    ("Staying calm.", "list", dict(items=["LISTENING", "COMMUNICATING", "MANAGING TIME", "ADMITTING MISTAKES", "STAYING CALM"], mode="check", acc="CALM")),
    ("Asking better questions.", "question", dict(a_lbl="A BETTER", b_lbl="QUESTION", acc="BETTER QUESTIONS")),
    ("These skills rarely make dramatic videos.", "chairs", dict(n=7, lbl="NO AUDIENCE", acc="RARELY DRAMATIC")),
    ("But they quietly influence almost every part of your life.", "network", dict(nodes=["WORK", "FRIENDS", "FAMILY", "GOALS", "HEALTH"], tangled=False, acc="QUIETLY INFLUENCE EVERY")),
    ("Don't ignore the skills that make everything else easier.", "key", dict(lbl="EVERYTHING ELSE", acc="IGNORE EASIER")),
    ("Which underrated skill do you think everyone should learn?", "brain", dict(says="UNDERRATED SKILL?", acc="UNDERRATED SKILL")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="THE MOST UNDERRATED SKILL", acc="COMMENT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
