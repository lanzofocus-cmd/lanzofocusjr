from kit import build, follow_sub, hook

TITLE = ("THE CONVERSATION", "YOU'RE AVOIDING")
OUTPUT = "199_The_Conversation_Youre_Avoiding_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes the biggest problem in your life isn't the situation itself.", "iceberg", dict(top="THE SITUATION", bottom="THE SILENCE", acc="BIGGEST PROBLEM SITUATION")),
    ("It's the conversation you're avoiding about the situation.", "bubbles", dict(texts=["WE NEED TO TALK."], acc="CONVERSATION AVOIDING")),
    ("You know something needs to be said.", "brain", dict(says="I SHOULD SAY IT.", acc="SAID")),
    ("You know a misunderstanding exists.", "question", dict(a_lbl="YOU", b_lbl="THEM", acc="MISUNDERSTANDING")),
    ("You know someone needs to hear the truth.", "key", dict(lbl="THE TRUTH", acc="TRUTH")),
    ("But you keep postponing it.", "list", dict(items=["TALK TODAY", "TALK TOMORROW", "TALK NEXT WEEK"], mode="strike", acc="POSTPONING")),
    ("You imagine every possible outcome.", "network", dict(nodes=["ANGER", "TEARS", "SILENCE", "BLAME", "DISTANCE"], tangled=True, acc="IMAGINE EVERY OUTCOME")),
    ("They might get angry.", "gauge", dict(lbl="ANGER", start=0.2, end=0.85, acc="ANGRY")),
    ("They might misunderstand.", "bubbles", dict(texts=["THAT'S NOT WHAT I MEANT."], acc="MISUNDERSTAND")),
    ("They might disagree.", "scale", dict(left="YOU", right="THEM", tip=0, acc="DISAGREE")),
    ("They might react in a way you don't like.", "pulse", dict(acc="REACT")),
    ("So you stay silent.", "big", dict(text="...", sub="SILENCE", acc="SILENT")),
    ("And the silence begins creating its own problems.", "tangle", dict(lbl="SILENCE", acc="SILENCE PROBLEMS")),
    ("The misunderstanding grows.", "hud", dict(lbl="MISUNDERSTANDING", start=20, end=70, icons=None, crowd=0, acc="GROWS")),
    ("The frustration builds.", "hud", dict(lbl="MISUNDERSTANDING", start=70, end=80, lbl2="FRUSTRATION", start2=10, end2=75, icons=None, crowd=0, acc="FRUSTRATION BUILDS")),
    ("The distance increases.", "map", dict(a_lbl="YOU", b_lbl="THEM", acc="DISTANCE INCREASES")),
    ("Eventually, the conversation becomes even harder because now you're carrying weeks or months of things you never said.", "bricks", dict(rows=6, lbl="UNSAID", uneven=True, acc="HARDER CARRYING NEVER SAID")),
    ("Communication doesn't guarantee that everything will be fixed.", "list", dict(items=["EVERYTHING FIXED"], mode="strike", acc="COMMUNICATION GUARANTEE")),
    ("Some conversations will be uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.65, acc="UNCOMFORTABLE")),
    ("Some people won't respond the way you hoped.", "bubbles", dict(texts=["I DON'T SEE IT THAT WAY."], acc="RESPOND HOPED")),
    ("But avoiding a conversation doesn't automatically protect a relationship.", "shield", dict(front="SILENCE", back="RELATIONSHIP", acc="AVOIDING PROTECT")),
    ("Sometimes it slowly damages it.", "plant", dict(height=0.2, roots=False, lbl="WILTING", acc="SLOWLY DAMAGES")),
    ("The goal isn't to speak carelessly.", "list", dict(items=["SPEAK CARELESSLY"], mode="strike", acc="CARELESSLY")),
    ("It's to speak honestly, respectfully, and at the right time.", "list", dict(items=["HONESTLY", "RESPECTFULLY", "AT THE RIGHT TIME"], mode="check", acc="HONESTLY RESPECTFULLY TIME")),
    ("You don't have to attack someone.", "list", dict(items=["ATTACK"], mode="strike", acc="ATTACK")),
    ("You don't have to win.", "list", dict(items=["ATTACK", "WIN"], mode="strike", acc="WIN")),
    ("You simply have to stop assuming that silence is always the safest option.", "lock", dict(lbl="SILENCE = SAFE?", opening=True, acc="SILENCE SAFEST")),
    ("Sometimes the conversation you've been avoiding…", "bubbles", dict(drop=True, texts=["CAN WE TALK?"], acc="CONVERSATION AVOIDING")),
    ("Is the first step toward understanding.", "stairs", dict(n=6, climb=1, acc="FIRST STEP UNDERSTANDING")),
    ("What's one thing you think people need to communicate more honestly about?", "brain", dict(says="BE HONEST ABOUT...", acc="COMMUNICATE HONESTLY")),
    ("Comment below.", "cta", dict(kind="comment", lbl="SAY IT HONESTLY", acc="COMMENT")),
    ("And share this with someone who believes difficult conversations are always worth avoiding.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE DIFFICULT AVOIDING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="THINGS LEFT UNSAID", start=5, end=97, icons="q", crowd=4, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
