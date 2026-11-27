from kit import build, follow_sub

TITLE = ("YOU DON'T HAVE TO", "RESPOND TO EVERYTHING")
OUTPUT = "53_You_Dont_Have_To_Respond_To_Everything_16x9.mp4"
SPEC = [
    ("Someone misunderstands you.", "bubbles", dict(texts=["THAT'S NOT WHAT I MEANT."], acc="MISUNDERSTANDS")),
    ("Someone makes a comment.", "notifs", dict(items=["NEW COMMENT"], acc="COMMENT.")),
    ("Someone disagrees.", "notifs", dict(items=["NEW COMMENT", "\"YOU'RE WRONG.\""], acc="DISAGREES.")),
    ("Someone tries to provoke you.", "notifs", dict(items=["NEW COMMENT", "\"YOU'RE WRONG.\"", "\"PROVE IT.\""], acc="PROVOKE")),
    ("And suddenly…", "pulse", dict()),
    ("Your entire day becomes about finding the perfect response.", "brain", dict(says="I SHOULD HAVE SAID...", acc="ENTIRE PERFECT RESPONSE.")),
    ("But not every situation deserves your attention.", "key", dict(lbl="YOUR ATTENTION", acc="NOT DESERVES")),
    ("Sometimes…", "pulse", dict()),
    ("Responding gives the situation more importance than it deserves.", "scale", dict(left="THE COMMENT", right="YOUR PEACE", tip=1, acc="IMPORTANCE")),
    ("Sometimes explaining yourself changes nothing.", "lock", dict(lbl="MIND ALREADY MADE UP", acc="NOTHING.")),
    ("Sometimes the best response isn't silence because you're afraid…", "shield", dict(front="NOT FEAR", back="", acc="SILENCE AFRAID…")),
    ("It's silence because you've decided your energy is more valuable.", "progress", dict(lbl="YOUR ENERGY", value=0.95, acc="ENERGY VALUABLE.")),
    ("You don't have to attend every argument you're invited to.", "door", dict(lbl="ARGUMENT", figure=True, acc="ATTEND ARGUMENT INVITED")),
    ("And you don't have to prove yourself to every person who questions you.", "doc", dict(title="PROOF", empty=True, stamp="NOT OWED", acc="PROVE QUESTIONS")),
    ("Save this reminder.", "cta", dict(kind="save", acc="SAVE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
