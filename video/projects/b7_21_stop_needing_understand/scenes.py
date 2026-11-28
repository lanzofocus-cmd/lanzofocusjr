from kit import build, follow_sub, hook

TITLE = ("WHEN YOU STOP NEEDING", "EVERYONE TO UNDERSTAND")
OUTPUT = "221_The_Moment_You_Stop_Needing_Everyone_To_Understand_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You can explain your decision perfectly…", "doc", dict(title="MY DECISION", empty=False, acc="EXPLAIN DECISION")),
    ("And someone can still disagree.", "bubbles", dict(texts=["I DON'T AGREE."], acc="DISAGREE")),
    ("You can explain your intentions…", "doc", dict(title="MY INTENTIONS", empty=False, acc="INTENTIONS")),
    ("And someone can still misunderstand.", "question", dict(a_lbl="YOU MEANT", b_lbl="WHAT?", acc="MISUNDERSTAND")),
    ("You can explain your feelings…", "pulse", dict(acc="FEELINGS")),
    ("And someone can still see things differently.", "mirror", dict(reflect="dashed", lbl="THEIR VIEW", acc="DIFFERENTLY")),
    ("At some point, you need to accept that understanding isn't always guaranteed.", "lock", dict(lbl="NO GUARANTEE", acc="ACCEPT GUARANTEED")),
    ("You can communicate clearly.", "list", dict(items=["COMMUNICATE CLEARLY"], mode="check", acc="CLEARLY")),
    ("You can be respectful.", "list", dict(items=["COMMUNICATE CLEARLY", "BE RESPECTFUL"], mode="check", acc="RESPECTFUL")),
    ("You can provide context.", "list", dict(items=["COMMUNICATE CLEARLY", "BE RESPECTFUL", "GIVE CONTEXT"], mode="check", acc="CONTEXT")),
    ("But you cannot control how another person interprets everything.", "brain", dict(says="THEIR INTERPRETATION", acc="CONTROL INTERPRETS")),
    ("If you spend your entire life trying to eliminate every misunderstanding…", "loop", dict(items=["EXPLAIN", "MISUNDERSTOOD", "RE-EXPLAIN", "STILL MISUNDERSTOOD"], acc="ELIMINATE MISUNDERSTANDING")),
    ("You will exhaust yourself.", "battery", dict(lbl="YOUR ENERGY", start=0.9, end=0.05, drains=3, acc="EXHAUST")),
    ("Your responsibility is to communicate honestly.", "key", dict(lbl="YOUR PART", drop=True, acc="RESPONSIBILITY HONESTLY")),
    ("Their interpretation is not completely under your control.", "list", dict(items=["THEIR INTERPRETATION"], mode="tag", tag="NOT YOURS", acc="INTERPRETATION CONTROL")),
    ("What's something you've learned about trying to explain yourself to others?", "book", dict(chapter="THE LESSON", acc="LEARNED EXPLAIN")),
    ("Share the lesson.", "cta", dict(kind="comment", lbl="YOUR LESSON", acc="LESSON")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EXPLAINING", start=10, end=100, lbl2="UNDERSTOOD", start2=20, end2=22, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
