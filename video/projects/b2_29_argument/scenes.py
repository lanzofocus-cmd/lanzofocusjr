from kit import build, follow_sub

TITLE = ("YOU DON'T HAVE TO WIN", "EVERY ARGUMENT")
OUTPUT = "39_You_Dont_Have_To_Win_Every_Argument_16x9.mp4"
SPEC = [
    ("Some arguments aren't worth your energy.", "progress", dict(lbl="YOUR ENERGY", value=0.25, acc="AREN'T ENERGY.")),
    ("Some people aren't trying to understand you.", "bubbles", dict(texts=["YOU'RE WRONG.", "WHATEVER."], acc="AREN'T UNDERSTAND")),
    ("They're trying to win.", "chairs" if False else "scale", dict(left="UNDERSTAND", right="WIN", tip=1, acc="WIN.")),
    ("And if you keep explaining yourself…", "quote", dict(text="LET ME EXPLAIN AGAIN...", acc="EXPLAINING")),
    ("You may spend hours trying to convince someone who already decided what they believe.", "lock", dict(lbl="ALREADY DECIDED", acc="HOURS ALREADY DECIDED")),
    ("Not every misunderstanding requires a response.", "notifs", dict(items=["REPLY?", "REPLY?", "REPLY?"], acc="NOT RESPONSE.")),
    ("Not every opinion deserves your attention.", "bubbles", dict(texts=["MY OPINION:", "ACTUALLY...", "WELL..."], acc="NOT ATTENTION.")),
    ("Not every disagreement needs a winner.", "scale", dict(left="YOU", right="THEM", tip=0, acc="NOT WINNER.")),
    ("Sometimes…", "pulse", dict()),
    ("Peace is recognizing that you don't need to participate.", "door", dict(open_=True, lbl="WALK AWAY", acc="PEACE DON'T PARTICIPATE.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
