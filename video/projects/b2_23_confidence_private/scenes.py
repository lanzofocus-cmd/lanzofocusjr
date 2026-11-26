from kit import build, follow_sub

TITLE = ("YOUR CONFIDENCE IS", "BUILT IN PRIVATE")
OUTPUT = "33_Your_Confidence_Is_Built_In_Private_16x9.mp4"
SPEC = [
    ("Confidence isn't always loud.", "stage", dict(empty=True, performing=False, acc="ISN'T LOUD.")),
    ("Sometimes it looks like keeping a promise nobody knows you made.", "doc", dict(title="PROMISE", empty=False, stamp="KEPT", acc="PROMISE NOBODY")),
    ("Studying when nobody checks.", "book", dict(chapter="2:00 AM", acc="STUDYING NOBODY")),
    ("Practicing when nobody watches.", "chairs", dict(lbl="NOBODY WATCHING", acc="PRACTICING NOBODY")),
    ("Doing what you said you'd do…", "list", dict(items=["SAID IT", "DID IT"], mode="check", acc="SAID DO…")),
    ("Even when there is no reward waiting.", "receipt", dict(items=[("REWARD", "$0"), ("APPLAUSE", "0")], acc="NO REWARD")),
    ("Every time you keep a promise to yourself…", "list", dict(items=["PROMISE KEPT", "PROMISE KEPT", "PROMISE KEPT"], mode="check", acc="PROMISE YOURSELF…")),
    ("You create evidence.", "doc", dict(title="EVIDENCE", empty=False, acc="EVIDENCE.")),
    ("Evidence that you can trust yourself.", "mirror", dict(reflect="solid", lbl="TRUSTED", acc="TRUST YOURSELF.")),
    ("And eventually…", "pulse", dict()),
    ("Confidence stops being something you try to convince yourself you have.", "gauge", dict(lbl="CONFIDENCE", start=0.3, end=0.5, acc="CONVINCE")),
    ("It becomes something you've earned through your own actions.", "gauge", dict(lbl="EARNED CONFIDENCE", start=0.5, end=0.95, acc="EARNED ACTIONS.")),
    ("Follow LanzoFocus for ideas that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
