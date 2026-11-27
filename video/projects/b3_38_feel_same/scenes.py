from kit import build, follow_sub

TITLE = ("YOU'RE NOT GOING TO", "FEEL THE SAME FOREVER")
OUTPUT = "78_Youre_Not_Going_To_Feel_The_Same_Forever_16x9.mp4"
SPEC = [
    ("The feeling you're experiencing right now…", "pulse", dict(acc="FEELING NOW…")),
    ("Will change.", "chart", dict(kind="wave", lbl="FEELINGS", acc="CHANGE.")),
    ("The excitement.", "list", dict(items=["EXCITEMENT"], mode="empty", acc="EXCITEMENT.")),
    ("The disappointment.", "list", dict(items=["EXCITEMENT", "DISAPPOINTMENT"], mode="empty", acc="DISAPPOINTMENT.")),
    ("The frustration.", "list", dict(items=["EXCITEMENT", "DISAPPOINTMENT", "FRUSTRATION"], mode="empty", acc="FRUSTRATION.")),
    ("The uncertainty.", "list", dict(items=["EXCITEMENT", "DISAPPOINTMENT", "FRUSTRATION", "UNCERTAINTY"], mode="empty", acc="UNCERTAINTY.")),
    ("Even when a feeling seems permanent…", "hourglass", dict(acc="PERMANENT…")),
    ("It isn't necessarily a permanent condition.", "doc", dict(title="FOREVER?", empty=True, stamp="TEMPORARY", acc="ISN'T PERMANENT")),
    ("Emotions are influenced by circumstances.", "network", dict(nodes=["CIRCUMSTANCES"], tangled=False, acc="CIRCUMSTANCES.")),
    ("Experiences.", "network", dict(nodes=["CIRCUMSTANCES", "EXPERIENCES"], tangled=False, acc="EXPERIENCES.")),
    ("Sleep.", "network", dict(nodes=["CIRCUMSTANCES", "EXPERIENCES", "SLEEP"], tangled=False, acc="SLEEP.")),
    ("Stress.", "network", dict(nodes=["CIRCUMSTANCES", "EXPERIENCES", "SLEEP", "STRESS"], tangled=False, acc="STRESS.")),
    ("People.", "network", dict(nodes=["CIRCUMSTANCES", "EXPERIENCES", "SLEEP", "STRESS", "PEOPLE"], tangled=False, acc="PEOPLE.")),
    ("Time.", "network", dict(nodes=["CIRCUMSTANCES", "EXPERIENCES", "SLEEP", "STRESS", "PEOPLE", "TIME"], tangled=False, acc="TIME.")),
    ("And things you haven't experienced yet.", "door", dict(open_=True, lbl="NOT YET", acc="HAVEN'T YET.")),
    ("You don't need to make every major decision based on how you feel in one moment.", "path", dict(kind="fork", labels=("RIGHT NOW", "LATER"), acc="EVERY MAJOR ONE MOMENT.")),
    ("Sometimes…", "pulse", dict()),
    ("You need time for the feeling to change before you decide what it means.", "hourglass", dict(acc="TIME BEFORE MEANS.")),
    ("Don't mistake a temporary emotional state for the permanent truth of your life.", "scale", dict(left="A FEELING", right="THE TRUTH", tip=0, acc="TEMPORARY PERMANENT TRUTH")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
