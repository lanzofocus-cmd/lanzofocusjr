from kit import build, follow_sub, hook

TITLE = ("LISTEN WITHOUT PREPARING", "YOUR RESPONSE")
OUTPUT = "220_Why_You_Should_Learn_To_Listen_Without_Preparing_Your_Response_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever been in a conversation…", "bubbles", dict(texts=["SO I WAS THINKING..."], acc="CONVERSATION")),
    ("And realized you weren't actually listening?", "brain", dict(says="MY TURN SOON...", acc="LISTENING")),
    ("You were waiting.", "hourglass", dict(acc="WAITING")),
    ("Waiting for them to finish.", "progress", dict(lbl="THEM TALKING", value=0.7, acc="FINISH")),
    ("Preparing your answer.", "doc", dict(title="MY ANSWER", empty=False, acc="PREPARING")),
    ("Thinking about how to disagree.", "brain", dict(says="BUT ACTUALLY...", acc="DISAGREE")),
    ("Thinking about what you wanted to say next.", "brain", dict(says="BUT ACTUALLY...", says2="AND ALSO...", acc="NEXT")),
    ("And when they finally stopped talking…", "pulse", dict(acc="STOPPED")),
    ("You responded to the part you were already prepared for.", "doc", dict(title="MY ANSWER", empty=False, stamp="PRE-WRITTEN", acc="RESPONDED PREPARED")),
    ("Not necessarily to what they actually said.", "iceberg", dict(top="WHAT YOU HEARD", bottom="WHAT THEY SAID", acc="ACTUALLY SAID")),
    ("Listening is more difficult than it appears.", "gauge", dict(lbl="DIFFICULTY", start=0.2, end=0.75, acc="LISTENING DIFFICULT")),
    ("It requires you to temporarily put your own thoughts aside.", "door", dict(closing=True, lbl="YOUR THOUGHTS", acc="THOUGHTS ASIDE")),
    ("It requires curiosity.", "question", dict(a_lbl="TELL ME", b_lbl="MORE", acc="CURIOSITY")),
    ("It requires accepting that you might not immediately understand.", "fog", dict(lbl="NOT YET CLEAR", acc="ACCEPTING UNDERSTAND")),
    ("And sometimes…", "pulse", dict(acc="")),
    ("It requires asking another question instead of giving an answer.", "bubbles", dict(texts=["WHAT DO YOU MEAN BY THAT?"], acc="QUESTION ANSWER")),
    ("You don't have to agree with someone to understand them.", "scale", dict(left="AGREE", right="UNDERSTAND", tip=0, acc="AGREE UNDERSTAND")),
    ("But you cannot genuinely understand someone if you're constantly waiting for your turn to speak.", "hud", dict(lbl="LISTENING", start=20, end=95, lbl2="WAITING TO TALK", start2=90, end2=10, icons=None, crowd=0, drop=True, acc="GENUINELY UNDERSTAND TURN SPEAK")),
    ("Share this with someone who believes good communication starts with listening, not winning.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE LISTENING WINNING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="LISTENING", start=80, end=6, lbl2="PLANNING YOUR REPLY", start2=10, end2=97, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
