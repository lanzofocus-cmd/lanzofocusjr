from kit import build, follow_sub, hook

TITLE = ("WHY BEING INTELLIGENT", "ISN'T ENOUGH")
OUTPUT = "255_Why_Being_Intelligent_Isnt_Enough_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You can be intelligent…", "brain", dict(says="I KNOW THIS.", acc="INTELLIGENT")),
    ("And still make terrible decisions.", "path", dict(kind="fork", labels=("WISE", "TERRIBLE"), acc="TERRIBLE DECISIONS")),
    ("You can understand complicated concepts…", "network", dict(nodes=["THEORY", "SYSTEMS", "MATH", "LOGIC"], tangled=True, acc="COMPLICATED")),
    ("And still misunderstand people.", "question", dict(a_lbl="WHAT DID", b_lbl="THEY MEAN?", acc="MISUNDERSTAND")),
    ("You can know what you should do…", "doc", dict(title="WHAT TO DO", empty=False, acc="KNOW SHOULD")),
    ("And still fail to do it.", "doc", dict(title="WHAT TO DO", empty=False, stamp="NOT DONE", acc="FAIL")),
    ("Intelligence can help you solve problems.", "key", dict(lbl="INTELLIGENCE", acc="SOLVE")),
    ("But it doesn't automatically make you emotionally mature.", "list", dict(items=["EMOTIONALLY MATURE"], mode="empty", acc="EMOTIONALLY MATURE")),
    ("It doesn't automatically make you disciplined.", "list", dict(items=["EMOTIONALLY MATURE", "DISCIPLINED"], mode="empty", acc="DISCIPLINED")),
    ("It doesn't automatically make you honest.", "list", dict(items=["EMOTIONALLY MATURE", "DISCIPLINED", "HONEST"], mode="empty", acc="HONEST")),
    ("It doesn't automatically make you a good communicator.", "list", dict(items=["EMOTIONALLY MATURE", "DISCIPLINED", "HONEST", "A GOOD COMMUNICATOR"], mode="empty", acc="COMMUNICATOR")),
    ("And sometimes intelligent people can become particularly good at explaining their mistakes.", "bubbles", dict(texts=["WELL, TECHNICALLY..."], acc="EXPLAINING MISTAKES")),
    ("They create complicated reasons for simple problems.", "tangle", dict(lbl="COMPLICATED REASONS", acc="COMPLICATED SIMPLE")),
    ("They defend decisions that clearly aren't working.", "shield", dict(front="MY DECISION", back="EGO", acc="DEFEND WORKING")),
    ("They use their intelligence to justify what they already want to believe.", "brain", dict(says="PROVE I'M RIGHT.", acc="JUSTIFY BELIEVE")),
    ("Being smart isn't only about having answers.", "list", dict(items=["HAVING ANSWERS"], mode="tag", tag="NOT ENOUGH", acc="SMART ANSWERS")),
    ("It's also about recognizing when your answers are wrong.", "quote", dict(text="I WAS WRONG.", acc="RECOGNIZING WRONG")),
    ("It's about knowing when to listen.", "list", dict(items=["LISTEN"], mode="check", acc="LISTEN")),
    ("When to reconsider.", "list", dict(items=["LISTEN", "RECONSIDER"], mode="check", acc="RECONSIDER")),
    ("When to admit that you don't understand.", "list", dict(items=["LISTEN", "RECONSIDER", "ADMIT IT"], mode="check", acc="ADMIT UNDERSTAND")),
    ("When to stop trying to win and start trying to learn.", "scale", dict(left="WIN", right="LEARN", tip=1, acc="WIN LEARN")),
    ("Intelligence gives you tools.", "receipt", dict(items=[("LOGIC", "TOOL"), ("MEMORY", "TOOL"), ("KNOWLEDGE", "TOOL")], acc="INTELLIGENCE TOOLS")),
    ("Character determines how you use them.", "compass", dict(lbl="CHARACTER", drop=True, acc="CHARACTER DETERMINES")),
    ("What quality do you think matters just as much as intelligence, or even more?", "brain", dict(says="JUST AS IMPORTANT:", acc="QUALITY INTELLIGENCE")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="THE OTHER QUALITY", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="INTELLIGENCE", start=40, end=98, lbl2="WISDOM", start2=40, end2=15, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
