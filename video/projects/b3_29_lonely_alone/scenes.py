from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN", "LONELY AND ALONE")
OUTPUT = "69_The_Difference_Between_Lonely_And_Alone_16x9.mp4"
SPEC = [
    ("Being alone doesn't always mean being lonely.", "scale", dict(left="ALONE", right="LONELY", tip=0, acc="ALONE DOESN'T LONELY.")),
    ("Sometimes…", "pulse", dict()),
    ("Being alone gives you room to think.", "alone", dict(tag="ROOM TO THINK", acc="ROOM THINK.")),
    ("To discover what you like.", "key", dict(lbl="WHAT YOU LIKE", acc="DISCOVER")),
    ("To understand your emotions.", "brain", dict(says="I FEEL...", acc="EMOTIONS.")),
    ("To make decisions without constant influence.", "path", dict(kind="fork", labels=("THEIRS", "YOURS"), acc="WITHOUT INFLUENCE.")),
    ("But loneliness is different.", "big", dict(text="LONELY", acc="LONELINESS DIFFERENT.")),
    ("It's the feeling of wanting connection…", "crowd", dict(n=5, highlight=2, dim=False, acc="CONNECTION…")),
    ("And not finding it.", "alone", dict(others=4, acc="NOT FINDING")),
    ("And neither experience makes you weak.", "sticker", dict(tags=["WEAK"], strike=True, acc="NEITHER WEAK.")),
    ("You don't need to fill every quiet moment with people.", "chairs", dict(lbl="QUIET IS OKAY", acc="FILL QUIET")),
    ("But you also don't need to pretend you never need anyone.", "mirror", dict(reflect="solid", lbl="HONEST", acc="PRETEND NEVER")),
    ("Healthy independence isn't refusing connection.", "shield", dict(front="WALLS?", back="PEOPLE", acc="INDEPENDENCE ISN'T REFUSING")),
    ("It's knowing how to stand on your own…", "alone", dict(tag="ON YOUR OWN", acc="STAND OWN…")),
    ("While still allowing people into your life.", "door", dict(open_=True, lbl="OPEN", acc="ALLOWING")),
    ("You can be independent and still need connection.", "ring", dict(center_tag="BOTH", acc="INDEPENDENT CONNECTION.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
