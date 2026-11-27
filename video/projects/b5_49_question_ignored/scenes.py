from kit import build, follow_sub

TITLE = ("THE QUESTION", "OFTEN IGNORED")
OUTPUT = "189_The_Question_Often_Ignored_16x9.mp4"
SPEC = [
    ("Before asking whether something is worth your time…", "hourglass", dict(acc="WORTH TIME")),
    ("Ask whether it deserves your attention.", "brain", dict(says="DOES IT DESERVE", says2="MY ATTENTION?", acc="DESERVES ATTENTION")),
    ("Time is what you spend.", "coins", dict(stacks=4, lbl="TIME", acc="TIME SPEND")),
    ("Attention is what you give your mind.", "brain", dict(says="ATTENTION", acc="ATTENTION MIND")),
    ("You can physically be somewhere…", "alone", dict(tag="HERE", acc="PHYSICALLY SOMEWHERE")),
    ("While mentally giving your life to something completely different.", "mirror", dict(reflect="dashed", lbl="SOMEWHERE ELSE", acc="MENTALLY DIFFERENT")),
    ("Protect what you repeatedly think about.", "shield", dict(front="ATTENTION", back="YOUR MIND", acc="PROTECT REPEATEDLY")),
    ("Because eventually, your attention shapes your perspective.", "compass", dict(lbl="PERSPECTIVE", acc="ATTENTION SHAPES PERSPECTIVE")),
    ("Save this and ask yourself tonight:", "cta", dict(kind="save", lbl="ASK TONIGHT", acc="SAVE")),
    ("\"Where did my attention go today?\"", "quote", dict(text="WHERE DID MY ATTENTION GO TODAY?", acc="ATTENTION TODAY")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
