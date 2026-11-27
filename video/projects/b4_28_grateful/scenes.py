from kit import build, follow_sub

TITLE = ("YOU CAN BE GRATEFUL", "AND STILL WANT MORE")
OUTPUT = "118_You_Can_Be_Grateful_And_Still_Want_More_16x9.mp4"
SPEC = [
    ("People sometimes act like gratitude means you should stop wanting improvement.", "bubbles", dict(texts=["BE GRATEFUL.", "STOP WANTING MORE."], acc="GRATITUDE STOP")),
    ("But those things can coexist.", "scale", dict(left="GRATITUDE", right="AMBITION", tip=0, acc="COEXIST.")),
    ("You can appreciate what you have…", "list", dict(items=["WHAT YOU HAVE"], mode="check", acc="APPRECIATE")),
    ("And still want to learn.", "book", dict(chapter="STILL LEARNING", acc="LEARN.")),
    ("You can value your current life…", "frame", dict(who="YOUR LIFE NOW", acc="VALUE CURRENT")),
    ("And still pursue new goals.", "stairs", dict(n=6, climb=2, highlight=3, acc="PURSUE NEW GOALS.")),
    ("You can recognize your blessings…", "coins", dict(lbl="BLESSINGS", acc="BLESSINGS…")),
    ("Without pretending everything is perfect.", "puzzle", dict(missing=True, lbl="NOT PERFECT", acc="PRETENDING PERFECT.")),
    ("Gratitude isn't a command to stop growing.", "plant", dict(height=0.6, roots=False, acc="GRATITUDE ISN'T STOP GROWING.")),
    ("Ambition isn't a requirement to be dissatisfied.", "gauge", dict(lbl="SATISFIED", start=0.6, end=0.7, acc="AMBITION ISN'T DISSATISFIED.")),
    ("You can appreciate where you are…", "map", dict(a_lbl="WHERE YOU ARE", b_lbl="", acc="APPRECIATE ARE…")),
    ("While working toward where you want to go.", "map", dict(a_lbl="HERE", b_lbl="WHERE YOU'RE GOING", acc="WORKING GO.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
