from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO DON'T", "NEED TO IMPRESS")
OUTPUT = "217_The_People_Who_Dont_Need_To_Be_Impressed_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine having a conversation with someone who isn't trying to impress you.", "bubbles", dict(texts=["SO, HOW ARE YOU?"], acc="IMPRESS")),
    ("They don't exaggerate.", "list", dict(items=["EXAGGERATING"], mode="strike", acc="EXAGGERATE")),
    ("They don't constantly mention achievements.", "list", dict(items=["EXAGGERATING", "LISTING ACHIEVEMENTS"], mode="strike", acc="ACHIEVEMENTS")),
    ("They don't turn every story into proof that they're important.", "list", dict(items=["EXAGGERATING", "LISTING ACHIEVEMENTS", "PROVING IMPORTANCE"], mode="strike", acc="PROOF IMPORTANT")),
    ("They simply talk.", "bubbles", dict(texts=["HONESTLY, SAME."], acc="TALK")),
    ("Listen.", "bubbles", dict(texts=["I'M LISTENING."], acc="LISTEN")),
    ("Ask questions.", "question", dict(a_lbl="AND THEN", b_lbl="WHAT HAPPENED?", acc="QUESTIONS")),
    ("And somehow…", "pulse", dict(acc="SOMEHOW")),
    ("You feel more comfortable around them.", "hud", dict(lbl="COMFORT", start=30, end=95, icons="heart", crowd=2, acc="COMFORTABLE")),
    ("Why?", "big", dict(text="WHY?", acc="WHY")),
    ("Because confidence doesn't always need an audience.", "stage", dict(lbl="NO AUDIENCE NEEDED", empty=True, drop=True, acc="CONFIDENCE AUDIENCE")),
    ("Sometimes the most secure people aren't constantly trying to demonstrate their value.", "shield", dict(front="SECURE", back="CALM", acc="SECURE DEMONSTRATE")),
    ("They don't need every conversation to become a performance.", "stage", dict(lbl="NOT A PERFORMANCE", empty=True, acc="PERFORMANCE")),
    ("They can admit they don't know something.", "quote", dict(text="I DON'T KNOW.", acc="ADMIT KNOW")),
    ("They can laugh at themselves.", "bubbles", dict(texts=["HAHA, THAT WAS ME."], acc="LAUGH")),
    ("They can allow someone else to have the spotlight.", "stage", dict(lbl="YOUR TURN", acc="SPOTLIGHT")),
    ("Being impressive can attract attention.", "crowd", dict(n=7, highlight=3, highlight_label="IMPRESSIVE", acc="IMPRESSIVE ATTENTION")),
    ("Being genuine can create connection.", "network", dict(nodes=["TRUST", "WARMTH", "HONESTY"], tangled=False, acc="GENUINE CONNECTION")),
    ("And connection is usually more valuable than winning every interaction.", "scale", dict(left="CONNECTION", right="WINNING", tip=-1, acc="CONNECTION VALUABLE WINNING")),
    ("What makes someone genuinely confident in your opinion?", "brain", dict(says="REAL CONFIDENCE IS...", acc="GENUINELY CONFIDENT")),
    ("Not appearance or achievements. What behavior?", "cta", dict(kind="comment", lbl="WHAT BEHAVIOR?", acc="BEHAVIOR")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="TRYING TO IMPRESS", start=95, end=5, lbl2="CONFIDENCE", start2=20, end2=97, icons="thumb", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
