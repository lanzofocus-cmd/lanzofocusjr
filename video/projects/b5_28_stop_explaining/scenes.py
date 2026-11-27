from kit import build, follow_sub

TITLE = ("THE MOMENT YOU", "STOP EXPLAINING")
OUTPUT = "168_The_Moment_You_Stop_Explaining_16x9.mp4"
SPEC = [
    ("There comes a point when explaining yourself becomes more exhausting than being misunderstood.", "scale", dict(left="EXPLAINING", right="MISUNDERSTOOD", tip=-1, acc="EXPLAINING EXHAUSTING MISUNDERSTOOD")),
    ("You explain your intentions.", "bubbles", dict(texts=["I MEANT WELL."], acc="INTENTIONS")),
    ("Your decisions.", "bubbles", dict(texts=["I MEANT WELL.", "HERE'S WHY I CHOSE IT."], acc="DECISIONS")),
    ("Your boundaries.", "shield", dict(front="BOUNDARIES", back="YOU", acc="BOUNDARIES")),
    ("Your entire perspective.", "brain", dict(says="LET ME EXPLAIN...", says2="AGAIN...", acc="ENTIRE PERSPECTIVE")),
    ("And the other person still chooses to misunderstand.", "question", dict(a_lbl="STILL", b_lbl="NOT LISTENING", acc="CHOOSES MISUNDERSTAND")),
    ("Not every situation deserves another explanation.", "list", dict(items=["ANOTHER EXPLANATION"], mode="strike", acc="ANOTHER EXPLANATION")),
    ("Sometimes your peace is found in knowing…", "sunrise", dict(acc="PEACE")),
    ("You already said enough.", "quote", dict(text="ENOUGH.", acc="ENOUGH")),
    ("Save this for when you feel the urge to explain yourself to someone who isn't listening.", "cta", dict(kind="save", lbl="YOU SAID ENOUGH", acc="SAVE EXPLAIN LISTENING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
