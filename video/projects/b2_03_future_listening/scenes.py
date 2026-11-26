from kit import build, follow_sub

TITLE = ("YOUR FUTURE", "IS LISTENING")
OUTPUT = "13_Your_Future_Is_Listening_16x9.mp4"
SPEC = [
    ("Imagine your future self could hear everything you say about yourself today.", "shed", dict(old="YOU TODAY", new="FUTURE YOU", acc="FUTURE HEAR")),
    ("Every time you say, \"I'm not good enough.\"", "quote", dict(text="I'M NOT GOOD ENOUGH.", acc="GOOD ENOUGH.\"")),
    ("Every time you say, \"I can't.\"", "quote", dict(text="I CAN'T.", acc="CAN'T.\"")),
    ("Every time you convince yourself that trying isn't worth it.", "quote", dict(text="WHY EVEN TRY?", acc="TRYING WORTH")),
    ("What would they tell you?", "question", dict(a_lbl="YOU TODAY", b_lbl="FUTURE YOU", acc="TELL")),
    ("Maybe they'd remind you that you haven't even seen what you're capable of yet.", "iceberg", dict(top="WHAT YOU'VE SEEN", bottom="WHAT YOU'RE CAPABLE OF", acc="CAPABLE YET.")),
    ("That your current situation isn't a permanent identity.", "frame", dict(who="RIGHT NOW", fade=True, acc="ISN'T PERMANENT")),
    ("And that you deserve the chance to prove yourself wrong.", "doc", dict(title="PROOF", empty=False, stamp="PROVEN WRONG", acc="DESERVE WRONG.")),
    ("Be careful what you repeatedly tell yourself.", "bubbles", dict(texts=["I CAN'T.", "NOT ENOUGH.", "WHY TRY?"], acc="CAREFUL REPEATEDLY")),
    ("Eventually, you start living like it's true.", "cage", dict(words=["CAN'T", "NOT ENOUGH", "WHY TRY"], acc="LIVING TRUE.")),
    ("Follow LanzoFocus for ideas that help you think differently.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
