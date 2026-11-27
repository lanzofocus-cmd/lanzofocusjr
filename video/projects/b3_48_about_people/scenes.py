from kit import build, follow_sub

TITLE = ("THE MOST IMPORTANT THING", "TO LEARN ABOUT PEOPLE")
OUTPUT = "88_The_Most_Important_Thing_To_Learn_About_People_16x9.mp4"
SPEC = [
    ("People are complicated.", "tangle", dict(lbl="PEOPLE", acc="COMPLICATED.")),
    ("Someone can be kind…", "sticker", dict(tags=["KIND"], acc="KIND…")),
    ("And still disappoint you.", "sticker", dict(tags=["KIND", "DISAPPOINTING"], acc="DISAPPOINT")),
    ("Someone can care…", "sticker", dict(tags=["CARING"], acc="CARE…")),
    ("And still make mistakes.", "sticker", dict(tags=["CARING", "MISTAKES"], acc="MISTAKES.")),
    ("Someone can have good intentions…", "sticker", dict(tags=["GOOD INTENTIONS"], acc="GOOD INTENTIONS…")),
    ("And still hurt someone.", "sticker", dict(tags=["GOOD INTENTIONS", "HURT SOMEONE"], acc="HURT")),
    ("Someone can be wrong…", "sticker", dict(tags=["WRONG"], acc="WRONG…")),
    ("Without being entirely bad.", "scale", dict(left="WRONG", right="BAD", tip=0, acc="ENTIRELY BAD.")),
    ("And someone can be charming…", "stage", dict(lbl="CHARMING", acc="CHARMING…")),
    ("Without being trustworthy.", "lock", dict(lbl="TRUST?", acc="TRUSTWORTHY.")),
    ("If you reduce people to one moment…", "frame", dict(who="ONE MOMENT", acc="REDUCE ONE")),
    ("You'll misunderstand them.", "bubbles", dict(texts=["THEY'RE AWFUL."], acc="MISUNDERSTAND")),
    ("But if you ignore every pattern…", "dots", dict(connect=True, acc="IGNORE PATTERN…")),
    ("You'll misunderstand them, too.", "bubbles", dict(texts=["THEY'RE PERFECT."], acc="MISUNDERSTAND")),
    ("Learn to see people clearly.", "mirror", dict(reflect="solid", lbl="CLEARLY", acc="CLEARLY.")),
    ("Not as perfect heroes.", "crown", dict(lbl="HERO?", acc="NOT HEROES.")),
    ("Not as permanent villains.", "sticker", dict(tags=["VILLAIN"], strike=True, acc="NOT VILLAINS.")),
    ("But as human beings…", "crowd", dict(n=7, acc="HUMAN BEINGS…")),
    ("Whose actions deserve to be understood and evaluated honestly.", "scale", dict(left="UNDERSTOOD", right="EVALUATED", tip=0, acc="UNDERSTOOD EVALUATED HONESTLY.")),
    ("Judge patterns.", "dots", dict(connect=True, acc="PATTERNS.")),
    ("Not just promises.", "bubbles", dict(texts=["I PROMISE."], acc="NOT PROMISES.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
