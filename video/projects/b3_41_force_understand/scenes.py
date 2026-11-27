from kit import build, follow_sub

TITLE = ("YOU CAN'T FORCE SOMEONE", "TO UNDERSTAND YOU")
OUTPUT = "81_You_Cant_Force_Someone_To_Understand_You_16x9.mp4"
SPEC = [
    ("You can explain your intentions perfectly.", "quote", dict(text="HERE'S WHAT I MEANT.", acc="PERFECTLY.")),
    ("Choose every word carefully.", "doc", dict(title="EVERY WORD", empty=False, acc="CAREFULLY.")),
    ("Give every detail.", "list", dict(items=["DETAIL", "DETAIL", "DETAIL"], mode="check", acc="DETAIL.")),
    ("And someone can still misunderstand you.", "bubbles", dict(texts=["SO YOU'RE SAYING...?"], acc="STILL MISUNDERSTAND")),
    ("Because understanding isn't determined only by what you say.", "scale", dict(left="WHAT YOU SAY", right="WHAT THEY HEAR", tip=0, acc="ISN'T ONLY")),
    ("It's also influenced by what the other person believes.", "brain", dict(says="WHAT THEY BELIEVE", acc="BELIEVES.")),
    ("Their experiences.", "network", dict(nodes=["EXPERIENCES"], tangled=False, acc="EXPERIENCES.")),
    ("Their assumptions.", "network", dict(nodes=["EXPERIENCES", "ASSUMPTIONS"], tangled=False, acc="ASSUMPTIONS.")),
    ("Their expectations.", "network", dict(nodes=["EXPERIENCES", "ASSUMPTIONS", "EXPECTATIONS"], tangled=False, acc="EXPECTATIONS.")),
    ("You control your communication.", "key", dict(lbl="YOUR WORDS", acc="CONTROL COMMUNICATION.")),
    ("You don't completely control the interpretation.", "compass", dict(lbl="THEIR INTERPRETATION", settle=False, acc="DON'T INTERPRETATION.")),
    ("So communicate honestly.", "quote", dict(text="HONESTLY...", acc="HONESTLY.")),
    ("Clarify when necessary.", "quote", dict(text="LET ME CLARIFY.", acc="CLARIFY")),
    ("But recognize when you've done your part.", "list", dict(items=["MY PART"], mode="check", acc="DONE PART.")),
    ("You can offer an explanation.", "doc", dict(title="EXPLANATION", empty=False, acc="OFFER")),
    ("You cannot force someone to receive it.", "lock", dict(lbl="THEIR CHOICE", acc="CANNOT FORCE RECEIVE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
