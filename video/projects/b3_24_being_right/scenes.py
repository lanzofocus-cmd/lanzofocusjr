from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH ALWAYS", "NEEDING TO BE RIGHT")
OUTPUT = "64_The_Problem_With_Always_Needing_To_Be_Right_16x9.mp4"
SPEC = [
    ("Being right feels good.", "list", dict(items=["I WAS RIGHT"], mode="check", acc="RIGHT GOOD.")),
    ("But sometimes…", "pulse", dict()),
    ("Being right becomes more important than understanding.", "scale", dict(left="BEING RIGHT", right="UNDERSTANDING", tip=-1, acc="RIGHT UNDERSTANDING.")),
    ("You stop listening.", "bubbles", dict(texts=["BUT LISTEN-", "ACTUALLY-"], acc="STOP LISTENING.")),
    ("You search for weaknesses in someone's argument.", "doc", dict(title="THEIR POINT", empty=False, stamp="FLAWS?", acc="WEAKNESSES")),
    ("You prepare your response while they are still speaking.", "brain", dict(says="MY COMEBACK...", acc="PREPARE STILL SPEAKING.")),
    ("And the conversation becomes a competition.", "scale", dict(left="ME", right="YOU", tip=0, acc="COMPETITION.")),
    ("But imagine how much you could learn…", "book", dict(chapter="WHAT YOU'D LEARN", acc="LEARN…")),
    ("If you didn't need every disagreement to end with you winning.", "list", dict(items=["WIN EVERY ARGUMENT"], mode="strike", acc="WINNING.")),
    ("What if you could say…", "pulse", dict(acc="SAY…")),
    ("\"I hadn't thought about that.\"", "quote", dict(text="I HADN'T THOUGHT OF THAT.", acc="THOUGHT")),
    ("\"What evidence would change my mind?\"", "quote", dict(text="WHAT WOULD CHANGE MY MIND?", acc="EVIDENCE MIND?\"")),
    ("\"Maybe I misunderstood.\"", "quote", dict(text="MAYBE I MISUNDERSTOOD.", acc="MISUNDERSTOOD.\"")),
    ("That's not weakness.", "sticker", dict(tags=["WEAK"], strike=True, acc="NOT WEAKNESS.")),
    ("That's intellectual strength.", "brain", dict(says="STRENGTH", acc="INTELLECTUAL STRENGTH.")),
    ("The smartest person isn't necessarily the person who knows the most.", "crowd", dict(n=5, highlight=2, highlight_label="KNOWS MOST?", acc="SMARTEST ISN'T MOST.")),
    ("Sometimes it's the person who can change their mind when the evidence changes.", "arrows", dict(items=["NEW EVIDENCE", "NEW MIND"], acc="CHANGE MIND EVIDENCE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
