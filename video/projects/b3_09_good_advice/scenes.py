from kit import build, follow_sub

TITLE = ("WHY GOOD ADVICE", "DOESN'T CHANGE YOU")
OUTPUT = "49_Why_Good_Advice_Doesnt_Change_You_16x9.mp4"
SPEC = [
    ("You already know a lot of things you should do.", "brain", dict(says="I KNOW.", acc="ALREADY KNOW")),
    ("You know you should sleep better.", "list", dict(items=["SLEEP BETTER"], mode="empty", acc="SLEEP")),
    ("You know you should practice.", "list", dict(items=["SLEEP BETTER", "PRACTICE"], mode="empty", acc="PRACTICE.")),
    ("You know you should stop procrastinating.", "list", dict(items=["SLEEP BETTER", "PRACTICE", "STOP DELAYING"], mode="empty", acc="PROCRASTINATING.")),
    ("You know you should make better decisions.", "list", dict(items=["SLEEP BETTER", "PRACTICE", "STOP DELAYING", "DECIDE BETTER"], mode="empty", acc="BETTER DECISIONS.")),
    ("So why hasn't knowing changed everything?", "question", dict(a_lbl="KNOWING", b_lbl="CHANGING", acc="KNOWING")),
    ("Because information and transformation are not the same thing.", "scale", dict(left="INFORMATION", right="TRANSFORMATION", tip=0, acc="INFORMATION TRANSFORMATION")),
    ("You can watch a thousand videos about swimming…", "phone", dict(content="highlight", acc="THOUSAND SWIMMING…")),
    ("And still be unable to swim.", "alone", dict(tag="CAN'T SWIM", acc="UNABLE SWIM.")),
    ("You can understand every principle of discipline…", "book", dict(chapter="DISCIPLINE 101", acc="UNDERSTAND PRINCIPLE")),
    ("And still struggle to apply one.", "list", dict(items=["APPLY IT"], mode="empty", acc="STRUGGLE APPLY")),
    ("Knowledge becomes useful only when it enters your behavior.", "arrows", dict(items=["KNOWLEDGE → ACTION"], acc="ONLY BEHAVIOR.")),
    ("The information you haven't acted on is still just information.", "doc", dict(title="UNUSED", empty=False, stamp="NOT ACTED ON", acc="HAVEN'T JUST")),
    ("Don't collect another lesson today.", "bricks", dict(rows=3, lbl="LESSONS COLLECTED", uneven=True, acc="DON'T COLLECT")),
    ("Use one you've already learned.", "list", dict(items=["ONE LESSON, USED"], mode="check", acc="USE ALREADY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
