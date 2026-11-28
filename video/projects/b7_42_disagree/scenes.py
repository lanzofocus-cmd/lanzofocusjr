from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO DON'T", "NEED TO AGREE WITH YOU")
OUTPUT = "242_The_People_Who_Dont_Need_To_Agree_With_You_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("A healthy conversation doesn't always end with agreement.", "bubbles", dict(texts=["I SEE IT DIFFERENTLY.", "FAIR ENOUGH."], acc="HEALTHY AGREEMENT")),
    ("Two people can understand each other…", "network", dict(nodes=["YOU", "THEM"], tangled=False, acc="UNDERSTAND")),
    ("And still have different opinions.", "scale", dict(left="YOUR VIEW", right="THEIR VIEW", tip=0, acc="DIFFERENT OPINIONS")),
    ("Different experiences.", "list", dict(items=["EXPERIENCES"], mode="tag", tag="DIFFERENT", acc="EXPERIENCES")),
    ("Different values.", "list", dict(items=["EXPERIENCES", "VALUES"], mode="tag", tag="DIFFERENT", acc="VALUES")),
    ("Different interpretations.", "list", dict(items=["EXPERIENCES", "VALUES", "INTERPRETATIONS"], mode="tag", tag="DIFFERENT", acc="INTERPRETATIONS")),
    ("The problem begins when disagreement becomes personal.", "gauge", dict(lbl="PERSONAL", start=0.1, end=0.85, acc="DISAGREEMENT PERSONAL")),
    ("When you assume someone is stupid because they think differently.", "sticker", dict(tags=["STUPID?"], acc="STUPID DIFFERENTLY")),
    ("When you stop listening because you already decided they're wrong.", "shield", dict(front="ALREADY DECIDED", back="YOU", acc="LISTENING WRONG")),
    ("When every conversation becomes a battle for superiority.", "stage", dict(lbl="WHO WINS?", acc="BATTLE SUPERIORITY")),
    ("You don't need to agree with everyone.", "list", dict(items=["AGREE WITH EVERYONE"], mode="strike", acc="AGREE")),
    ("But learning to disagree respectfully can make you better at understanding the world.", "compass", dict(lbl="UNDERSTANDING", drop=True, acc="DISAGREE RESPECTFULLY UNDERSTANDING")),
    ("Sometimes you leave a conversation without changing your opinion…", "hud", dict(lbl="YOUR OPINION", start=70, end=70, icons=None, crowd=0, acc="WITHOUT OPINION")),
    ("But with a better understanding of why someone else holds theirs.", "hud", dict(lbl="YOUR OPINION", start=70, end=70, lbl2="UNDERSTANDING THEM", start2=10, end2=85, icons=None, crowd=0, acc="BETTER WHY")),
    ("That still has value.", "list", dict(items=["STILL VALUABLE"], mode="check", acc="VALUE")),
    ("What do you think is the most important rule for disagreeing respectfully?", "cta", dict(kind="comment", lbl="THE ONE RULE", acc="RULE DISAGREEING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="AGREEMENT", start=50, end=12, lbl2="RESPECT", start2=50, end2=95, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
