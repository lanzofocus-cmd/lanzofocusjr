from kit import build, follow_sub

TITLE = ("THE THINGS THAT MAKE", "YOU INTERESTING")
OUTPUT = "177_The_Things_That_Make_You_Interesting_16x9.mp4"
SPEC = [
    ("You don't become interesting by trying to impress everyone.", "stage", dict(lbl="IMPRESS EVERYONE", acc="INTERESTING IMPRESS")),
    ("You become interesting by being genuinely interested.", "question", dict(a_lbl="TELL ME", b_lbl="MORE", acc="GENUINELY INTERESTED")),
    ("In ideas.", "network", dict(nodes=["IDEAS"], tangled=False, acc="IDEAS")),
    ("In people.", "network", dict(nodes=["IDEAS", "PEOPLE"], tangled=False, acc="PEOPLE")),
    ("In experiences.", "network", dict(nodes=["IDEAS", "PEOPLE", "EXPERIENCES"], tangled=False, acc="EXPERIENCES")),
    ("In things you don't understand yet.", "network", dict(nodes=["IDEAS", "PEOPLE", "EXPERIENCES", "THE UNKNOWN"], tangled=False, acc="UNDERSTAND YET")),
    ("The world becomes smaller when you believe you've already seen enough.", "cage", dict(words=["SEEN IT ALL"], acc="SMALLER ENOUGH")),
    ("Stay curious.", "compass", dict(lbl="CURIOSITY", acc="CURIOUS")),
    ("Ask questions.", "question", dict(a_lbl="WHY?", b_lbl="HOW?", acc="QUESTIONS")),
    ("Explore things without needing to become an expert immediately.", "map", dict(a_lbl="BEGINNER", b_lbl="EXPLORER", acc="EXPLORE EXPERT")),
    ("What's something you're genuinely curious about right now?", "brain", dict(says="I WONDER...", acc="CURIOUS")),
    ("Let's see what people are interested in.", "cta", dict(kind="comment", lbl="WHAT YOU'RE CURIOUS ABOUT", acc="INTERESTED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
