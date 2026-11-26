from kit import build, follow_sub

TITLE = ("YOU DON'T NEED", "TO BE THE BEST")
OUTPUT = "23_You_Dont_Need_To_Be_The_Best_16x9.mp4"
SPEC = [
    ("You don't need to be the most talented person in the room.", "crowd", dict(n=7, highlight=3, highlight_label="MOST TALENTED?", acc="TALENTED")),
    ("You don't need to be the smartest.", "brain", dict(says="SMARTEST?", acc="SMARTEST.")),
    ("The fastest.", "timeline", dict(compare=True, acc="FASTEST.")),
    ("The most experienced.", "progress", dict(lbl="EXPERIENCE", value=0.3, acc="EXPERIENCED.")),
    ("Sometimes…", "pulse", dict()),
    ("You just need to be willing to keep learning after everyone else gets frustrated.", "crowd", dict(n=7, highlight=3, highlight_label="STILL LEARNING", acc="KEEP LEARNING FRUSTRATED.")),
    ("Talent can give someone a head start.", "startline", dict(behind=True, acc="TALENT HEAD START.")),
    ("But curiosity keeps you improving.", "chart", dict(kind="up", lbl="CURIOSITY", acc="CURIOSITY IMPROVING.")),
    ("Humility keeps you teachable.", "book", dict(chapter="STILL A STUDENT", acc="HUMILITY TEACHABLE.")),
    ("And consistency gives you more chances to get better.", "stairs", dict(n=6, climb=4, acc="CONSISTENCY CHANCES")),
    ("Stop worrying about being the best person in the room.", "trophy_free" if False else "question", dict(a_lbl="THE BEST", b_lbl="BETTER", acc="BEST")),
    ("Try becoming the person who leaves the room better than they entered it.", "door", dict(open_=True, lbl="LEAVE IT BETTER", acc="BETTER ENTERED")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
