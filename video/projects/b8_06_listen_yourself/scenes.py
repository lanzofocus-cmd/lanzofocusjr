from kit import build, follow_sub, hook

TITLE = ("YOU'RE NOT LISTENING", "TO YOURSELF")
OUTPUT = "256_The_Moment_You_Realize_Youre_Not_Listening_To_Yourself_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You spend a lot of time listening to other people.", "ring", dict(tags=["ADVICE", "OPINIONS", "EXPECTATIONS", "CRITICISM"], acc="LISTENING OTHER")),
    ("Their advice.", "bubbles", dict(texts=["YOU SHOULD..."], acc="ADVICE")),
    ("Their opinions.", "bubbles", dict(texts=["YOU SHOULD...", "I THINK..."], acc="OPINIONS")),
    ("Their expectations.", "sticker", dict(tags=["DOCTOR", "STABLE JOB"], acc="EXPECTATIONS")),
    ("Their criticism.", "bubbles", dict(texts=["THAT'S A BAD IDEA."], acc="CRITICISM")),
    ("Their predictions about your future.", "doc", dict(title="YOUR FUTURE", empty=False, stamp="THEIR VERSION", acc="PREDICTIONS FUTURE")),
    ("But when was the last time you actually sat down and asked yourself what you think?", "alone", dict(tag="WHAT DO I THINK?", acc="ASKED YOURSELF THINK")),
    ("Not what would sound impressive.", "list", dict(items=["SOUNDS IMPRESSIVE"], mode="strike", acc="IMPRESSIVE")),
    ("Not what would make someone else happy.", "list", dict(items=["SOUNDS IMPRESSIVE", "MAKES THEM HAPPY"], mode="strike", acc="HAPPY")),
    ("Not what people expect you to say.", "list", dict(items=["SOUNDS IMPRESSIVE", "MAKES THEM HAPPY", "WHAT'S EXPECTED"], mode="strike", acc="EXPECT")),
    ("What do you genuinely believe?", "question", dict(a_lbl="WHAT DO", b_lbl="YOU BELIEVE?", acc="GENUINELY BELIEVE")),
    ("What do you actually want to learn?", "book", dict(chapter="?", acc="LEARN")),
    ("What matters to you?", "compass", dict(lbl="?", settle=False, acc="MATTERS")),
    ("What kind of life would feel meaningful?", "house", dict(progress=0.4, watchers=False, lbl="MEANINGFUL?", acc="MEANINGFUL")),
    ("What are you doing simply because everyone around you is doing it?", "crowd", dict(n=9, highlight=4, highlight_label="YOU?", acc="EVERYONE")),
    ("Sometimes people become so surrounded by external opinions…", "ring", dict(tags=["DO THIS", "NOT THAT", "BE REALISTIC", "TRUST ME", "YOU SHOULD"], acc="SURROUNDED EXTERNAL")),
    ("That they lose the ability to hear their own.", "hud", dict(lbl="THEIR VOICES", start=40, end=98, lbl2="YOUR VOICE", start2=40, end2=3, icons=None, crowd=0, acc="LOSE HEAR OWN")),
    ("And this doesn't mean you should ignore advice.", "list", dict(items=["IGNORE ADVICE"], mode="strike", acc="IGNORE ADVICE")),
    ("Other people's perspectives can be incredibly valuable.", "network", dict(nodes=["MENTOR", "FRIEND", "PARENT"], tangled=False, acc="PERSPECTIVES VALUABLE")),
    ("But advice should help you think.", "brain", dict(says="LET ME THINK.", acc="ADVICE THINK")),
    ("It shouldn't replace your thinking.", "list", dict(items=["REPLACE YOUR THINKING"], mode="strike", drop=True, acc="REPLACE THINKING")),
    ("You need to develop the ability to consider different perspectives…", "network", dict(nodes=["VIEW A", "VIEW B", "VIEW C", "VIEW D"], tangled=False, acc="CONSIDER PERSPECTIVES")),
    ("And still make your own decisions.", "compass", dict(lbl="YOUR DECISION", acc="OWN DECISIONS")),
    ("Because eventually, you are the person who has to live with the life you choose.", "key", dict(lbl="YOUR LIFE", acc="LIVE CHOOSE")),
    ("What's a decision you made after finally listening to your own thoughts instead of everyone else's opinions?", "cta", dict(kind="comment", lbl="YOUR OWN DECISION", acc="DECISION OWN THOUGHTS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="OTHER PEOPLE'S VOICES", start=20, end=100, lbl2="YOUR OWN VOICE", start2=60, end2=4, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
