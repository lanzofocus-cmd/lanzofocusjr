from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO", "MAKE YOU THINK")
OUTPUT = "182_The_People_Who_Make_You_Think_16x9.mp4"
SPEC = [
    ("Some people don't motivate you by giving speeches.", "stage", dict(lbl="SPEECHES", acc="MOTIVATE SPEECHES")),
    ("They motivate you by making you think.", "brain", dict(says="HUH. I NEVER", says2="THOUGHT OF THAT.", acc="THINK")),
    ("They challenge your assumptions.", "lock", dict(lbl="ASSUMPTIONS", opening=True, acc="CHALLENGE ASSUMPTIONS")),
    ("Ask questions you never considered.", "question", dict(a_lbl="BUT WHY", b_lbl="DO YOU THINK THAT?", acc="QUESTIONS CONSIDERED")),
    ("Introduce perspectives that make your world bigger.", "network", dict(nodes=["NEW IDEA", "NEW VIEW", "NEW PLACE", "NEW QUESTION"], tangled=False, acc="PERSPECTIVES BIGGER")),
    ("You don't need people who agree with everything you say.", "bubbles", dict(texts=["YES.", "TOTALLY.", "AGREED."], acc="AGREE EVERYTHING")),
    ("You need people who help you become more thoughtful.", "crowd", dict(n=3, highlight=1, highlight_label="THOUGHTFUL", acc="THOUGHTFUL")),
    ("Tag someone who has genuinely changed the way you think.", "cta", dict(kind="share", lbl="TAG THEM", acc="TAG CHANGED THINK")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
