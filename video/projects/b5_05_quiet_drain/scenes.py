from kit import build, follow_sub

TITLE = ("THE QUIET", "DRAIN")
OUTPUT = "145_The_Quiet_Drain_16x9.mp4"
SPEC = [
    ("Not everything that drains you looks exhausting.", "gauge", dict(lbl="ENERGY", start=0.8, end=0.3, acc="DRAINS EXHAUSTING")),
    ("Some things quietly take your energy.", "progress", dict(lbl="ENERGY", value=0.25, acc="QUIETLY ENERGY")),
    ("Constantly checking.", "phone", dict(lbl="CHECKING", acc="CHECKING")),
    ("Constantly worrying.", "brain", dict(says="WHAT IF...?", acc="WORRYING")),
    ("Constantly explaining.", "bubbles", dict(texts=["WHAT I MEANT WAS...", "LET ME EXPLAIN..."], acc="EXPLAINING")),
    ("Constantly wondering what someone meant.", "question", dict(a_lbl="WHAT DID", b_lbl="THEY MEAN?", acc="WONDERING MEANT")),
    ("You may not notice the weight until you finally put it down.", "scale", dict(left="THE WEIGHT", right="YOU", tip=-1, acc="WEIGHT DOWN")),
    ("Pay attention to what consumes your mind even when nothing is happening.", "tangle", dict(lbl="YOUR MIND", acc="CONSUMES MIND NOTHING")),
    ("Share this with someone who needs to realize that mental exhaustion deserves attention too.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE MENTAL EXHAUSTION")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
