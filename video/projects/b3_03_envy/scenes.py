from kit import build, follow_sub

TITLE = ("THE LIFE YOU ENVY MAY NOT", "BE THE LIFE YOU WANT")
OUTPUT = "43_The_Life_You_Envy_May_Not_Be_The_Life_You_Want_16x9.mp4"
SPEC = [
    ("You see someone else's life…", "phone", dict(content="highlight", lbl="YOU", acc="SOMEONE LIFE…")),
    ("And suddenly yours feels smaller.", "frame", dict(who="YOUR LIFE", fade=True, acc="SMALLER.")),
    ("Their money.", "coins", dict(lbl="THEIRS", acc="MONEY.")),
    ("Their confidence.", "gauge", dict(lbl="THEIR CONFIDENCE", start=0.8, end=0.9, acc="CONFIDENCE.")),
    ("Their achievements.", "list", dict(items=["ACHIEVED", "ACHIEVED", "ACHIEVED"], mode="check", acc="ACHIEVEMENTS.")),
    ("Their freedom.", "key", dict(lbl="FREEDOM", acc="FREEDOM.")),
    ("But here's a question nobody asks:", "question", dict(acc="QUESTION NOBODY")),
    ("Do you actually want their life…", "question", dict(a_lbl="THEIR LIFE", acc="ACTUALLY THEIR")),
    ("Or do you want the feeling you imagine their life gives them?", "question", dict(a_lbl="THEIR LIFE", b_lbl="THE FEELING", acc="FEELING IMAGINE")),
    ("Maybe you don't want their career.", "list", dict(items=["THEIR CAREER"], mode="strike", acc="CAREER.")),
    ("You want security.", "lock", dict(lbl="SECURITY", acc="SECURITY.")),
    ("Maybe you don't want their popularity.", "stage", dict(lbl="POPULAR", acc="POPULARITY.")),
    ("You want to feel accepted.", "ring", dict(center_tag="ACCEPTED", acc="ACCEPTED.")),
    ("Maybe you don't want their possessions.", "receipt", dict(items=[("CAR", "$$$"), ("WATCH", "$$$")], acc="POSSESSIONS.")),
    ("You want the freedom you think they represent.", "key", dict(lbl="FREEDOM", acc="FREEDOM REPRESENT.")),
    ("And if you mistake the symbol for the actual desire…", "scale", dict(left="THE SYMBOL", right="THE DESIRE", tip=-1, acc="SYMBOL DESIRE…")),
    ("You might spend years chasing something that never satisfies the real need.", "timeline", dict(n=10, progress=0.9, tag="STILL EMPTY", acc="YEARS NEVER NEED.")),
    ("Before chasing someone else's life…", "path", dict(kind="fork", labels=("THEIR LIFE", "YOUR NEED"), acc="CHASING")),
    ("Figure out what you're actually looking for.", "compass", dict(lbl="WHAT YOU NEED", acc="ACTUALLY LOOKING")),
    ("Comment one thing you want—and the feeling you're hoping it gives you.", "cta", dict(kind="comment", lbl="WANT → FEELING", acc="COMMENT FEELING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
