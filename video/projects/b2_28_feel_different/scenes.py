from kit import build, follow_sub

TITLE = ("STOP WAITING FOR YOUR", "LIFE TO FEEL DIFFERENT")
OUTPUT = "38_Stop_Waiting_For_Your_Life_To_Feel_Different_16x9.mp4"
SPEC = [
    ("You keep waiting for the feeling.", "hourglass", dict(acc="WAITING FEELING.")),
    ("The feeling of confidence.", "gauge", dict(lbl="CONFIDENCE", start=0.1, end=0.12, acc="CONFIDENCE.")),
    ("The feeling of excitement.", "gauge", dict(lbl="EXCITEMENT", start=0.1, end=0.12, acc="EXCITEMENT.")),
    ("The feeling that everything is finally changing.", "chart", dict(kind="flat", lbl="CHANGE", acc="FINALLY CHANGING.")),
    ("But feelings don't always arrive before action.", "timeline", dict(n=6, progress=0.2, tag="ACTION FIRST", acc="DON'T BEFORE ACTION.")),
    ("Sometimes…", "pulse", dict()),
    ("They arrive afterward.", "timeline", dict(n=6, progress=0.9, tag="FEELING", acc="AFTERWARD.")),
    ("You begin.", "stairs", dict(n=6, climb=1, acc="BEGIN.")),
    ("You struggle.", "stairs", dict(n=6, climb=2, acc="STRUGGLE.")),
    ("You learn.", "stairs", dict(n=6, climb=3, acc="LEARN.")),
    ("And slowly…", "pulse", dict(acc="SLOWLY…")),
    ("The feeling catches up.", "gauge", dict(lbl="CONFIDENCE", start=0.15, end=0.85, acc="CATCHES")),
    ("Don't wait for your life to feel different before you start making it different.", "shed", dict(old="WAITING", new="MAKING IT DIFFERENT", acc="DON'T WAIT MAKING")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
