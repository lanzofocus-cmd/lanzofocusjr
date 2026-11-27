from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN", "A DREAM AND A DIRECTION")
OUTPUT = "54_The_Difference_Between_A_Dream_And_A_Direction_16x9.mp4"
SPEC = [
    ("A dream tells you where you want to go.", "map", dict(a_lbl="YOU", b_lbl="THE DREAM", acc="DREAM WHERE")),
    ("A direction tells you what to do today.", "compass", dict(lbl="TODAY", acc="DIRECTION TODAY.")),
    ("You can dream about becoming successful.", "brain", dict(says="ONE DAY...", acc="DREAM SUCCESSFUL.")),
    ("But what does that mean on a random Wednesday?", "big", dict(text="WEDNESDAY", sub="7:42 AM", acc="RANDOM WEDNESDAY?")),
    ("What does it mean when nobody is watching?", "chairs", dict(lbl="NOBODY WATCHING", acc="NOBODY WATCHING?")),
    ("What does it mean when the next step is boring?", "stairs", dict(n=6, climb=1, highlight=1, acc="BORING?")),
    ("A dream can inspire you.", "sunrise", dict(acc="INSPIRE")),
    ("But a direction can guide you.", "compass", dict(lbl="GUIDE", acc="GUIDE")),
    ("Instead of asking…", "pulse", dict()),
    ("\"How do I become successful?\"", "quote", dict(text="HOW DO I BECOME SUCCESSFUL?", acc="SUCCESSFUL?\"")),
    ("Ask…", "pulse", dict(acc="ASK…")),
    ("\"What would moving one step in that direction look like today?\"", "quote", dict(text="WHAT'S ONE STEP TODAY?", acc="ONE STEP TODAY?\"")),
    ("Because you don't need to see the entire staircase.", "stairs", dict(n=6, climb=0, acc="ENTIRE STAIRCASE.")),
    ("You need to know which step you're standing on…", "stairs", dict(n=6, climb=2, acc="STANDING")),
    ("And which one comes next.", "stairs", dict(n=6, climb=2, highlight=2, acc="NEXT.")),
    ("A dream becomes real when it starts influencing your ordinary decisions.", "list", dict(items=["TODAY'S CHOICE", "TOMORROW'S CHOICE", "EVERY ORDINARY DAY"], mode="check", acc="REAL ORDINARY DECISIONS.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
