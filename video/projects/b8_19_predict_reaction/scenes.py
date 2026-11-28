from kit import build, follow_sub, hook

TITLE = ("STOP TRYING TO PREDICT", "EVERYONE'S REACTION")
OUTPUT = "269_Why_You_Should_Stop_Trying_To_Predict_Everyones_Reaction_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Before you say something…", "bubbles", dict(texts=["..."], acc="SAY")),
    ("You imagine how people might react.", "crowd", dict(n=7, highlight=3, highlight_label="?", acc="IMAGINE REACT")),
    ("Before you make a decision…", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="DECISION")),
    ("You imagine what people might think.", "brain", dict(says="WHAT WILL", says2="THEY THINK?", acc="THINK")),
    ("Before you try something…", "startline", dict(behind=False, acc="TRY")),
    ("You imagine whether someone might judge you.", "hud", dict(lbl="IMAGINED JUDGMENT", start=10, end=90, icons="thumbdown", acc="JUDGE")),
    ("And eventually, you're making decisions based on reactions that haven't even happened.", "frame", dict(who="IMAGINED REACTION", dashed_fig=True, acc="REACTIONS HAPPENED")),
    ("This can become exhausting.", "battery", dict(lbl="ENERGY", start=0.9, end=0.1, drains=0, acc="EXHAUSTING")),
    ("Because you are trying to control something that hasn't occurred…", "fog", dict(lbl="NOT YET REAL", acc="CONTROL OCCURRED")),
    ("And may never occur.", "frame", dict(who="NEVER HAPPENED", dashed_fig=True, fade=True, acc="NEVER")),
    ("Some people might approve.", "hud", dict(lbl="APPROVE", start=0, end=33, icons="thumb", crowd=2, acc="APPROVE")),
    ("Some might disagree.", "hud", dict(lbl="DISAGREE", start=0, end=33, icons="thumbdown", crowd=2, acc="DISAGREE")),
    ("Some might not care at all.", "crowd", dict(n=7, dim=True, acc="CARE")),
    ("You cannot accurately predict every reaction.", "question", dict(a_lbl="THEIR", b_lbl="REACTION", acc="ACCURATELY PREDICT")),
    ("And even if you could…", "pulse", dict(acc="")),
    ("You shouldn't automatically allow every imagined reaction to determine your choices.", "cage", dict(words=["WHAT IF THEY...", "THEY'LL THINK..."], drop=True, acc="IMAGINED DETERMINE CHOICES")),
    ("Consider the consequences.", "list", dict(items=["CONSIDER CONSEQUENCES"], mode="check", acc="CONSEQUENCES")),
    ("Be thoughtful.", "list", dict(items=["CONSIDER CONSEQUENCES", "BE THOUGHTFUL"], mode="check", acc="THOUGHTFUL")),
    ("Be respectful.", "list", dict(items=["CONSIDER CONSEQUENCES", "BE THOUGHTFUL", "BE RESPECTFUL"], mode="check", acc="RESPECTFUL")),
    ("But don't allow hypothetical opinions to become the authority over your entire life.", "crown", dict(lbl="YOU DECIDE", acc="HYPOTHETICAL AUTHORITY")),
    ("Save this if you've ever overthought something because of what you imagined other people might say.", "cta", dict(kind="save", lbl="THEY MIGHT NOT EVEN CARE", acc="SAVE OVERTHOUGHT IMAGINED")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="REACTIONS IMAGINED", start=5, end=99, lbl2="REACTIONS THAT HAPPENED", start2=0, end2=2, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
