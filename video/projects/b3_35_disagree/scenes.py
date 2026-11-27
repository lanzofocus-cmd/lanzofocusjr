from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO", "DISAGREE WITH YOU")
OUTPUT = "75_The_People_Who_Disagree_With_You_16x9.mp4"
SPEC = [
    ("If everyone agrees with you…", "bubbles", dict(texts=["AGREED.", "SO TRUE.", "EXACTLY."], inverted=True, acc="EVERYONE AGREES")),
    ("You might not be learning very much.", "progress", dict(lbl="LEARNING", value=0.05, acc="NOT LEARNING")),
    ("Disagreement can be uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.7, acc="DISAGREEMENT UNCOMFORTABLE.")),
    ("Especially when someone challenges something you've believed for years.", "frame", dict(who="AN OLD BELIEF", acc="CHALLENGES YEARS.")),
    ("But disagreement isn't automatically disrespect.", "scale", dict(left="DISAGREEMENT", right="DISRESPECT", tip=0, acc="ISN'T DISRESPECT.")),
    ("Sometimes another perspective reveals something you couldn't see from your own position.", "iceberg", dict(top="YOUR VIEW", bottom="WHAT THEY SEE", acc="PERSPECTIVE COULDN'T POSITION.")),
    ("You don't have to accept every opinion.", "list", dict(items=["EVERY OPINION"], mode="strike", acc="DON'T EVERY")),
    ("You don't have to abandon your beliefs.", "shield", dict(front="YOUR BELIEFS", back="", acc="DON'T ABANDON")),
    ("But you should be willing to examine them.", "doc", dict(title="EXAMINE", empty=False, acc="WILLING EXAMINE")),
    ("A belief that cannot survive a question…", "question", dict(a_lbl="A BELIEF", acc="CANNOT SURVIVE QUESTION…")),
    ("May not be as strong as you think.", "bricks", dict(rows=2, lbl="AS STRONG AS YOU THINK?", uneven=True, acc="STRONG")),
    ("The next time someone challenges your perspective…", "bubbles", dict(texts=["I SEE IT DIFFERENTLY."], acc="CHALLENGES")),
    ("Listen before defending it.", "list", dict(items=["1. LISTEN", "2. THEN RESPOND"], mode="check", acc="LISTEN BEFORE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
