from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO MAKE", "YOU FEEL SMALL")
OUTPUT = "210_The_People_Who_Make_You_Feel_Small_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever left a conversation feeling worse about yourself…", "bubbles", dict(texts=["OH... THAT'S CUTE."], acc="CONVERSATION WORSE")),
    ("Without fully understanding why?", "question", dict(acc="WHY")),
    ("Maybe the person constantly jokes about your goals.", "bubbles", dict(texts=["YOU? HAHA."], acc="JOKES GOALS")),
    ("Maybe they interrupt you.", "bubbles", dict(texts=["ANYWAY, ME..."], acc="INTERRUPT")),
    ("Maybe every achievement becomes a competition.", "timeline", dict(compare=True, acc="ACHIEVEMENT COMPETITION")),
    ("Maybe they make you feel stupid for asking questions.", "question", dict(a_lbl="DUMB", b_lbl="QUESTION?", acc="STUPID QUESTIONS")),
    ("Or maybe they constantly remind you of your mistakes.", "frame", dict(who="YOUR OLD MISTAKE", acc="REMIND MISTAKES")),
    ("One conversation doesn't always reveal someone's character.", "list", dict(items=["ONE CONVERSATION"], mode="empty", acc="ONE CHARACTER")),
    ("But repeated patterns matter.", "loop", dict(items=["JOKE", "INTERRUPT", "COMPETE", "REMIND"], lbl="THE PATTERN", acc="REPEATED PATTERNS")),
    ("Pay attention to how people respond when you succeed.", "list", dict(items=["WHEN YOU SUCCEED"], mode="empty", acc="SUCCEED")),
    ("When you disagree.", "list", dict(items=["WHEN YOU SUCCEED", "WHEN YOU DISAGREE"], mode="empty", acc="DISAGREE")),
    ("When you make a mistake.", "list", dict(items=["WHEN YOU SUCCEED", "WHEN YOU DISAGREE", "WHEN YOU SLIP UP"], mode="empty", acc="MISTAKE")),
    ("When you need help.", "list", dict(items=["WHEN YOU SUCCEED", "WHEN YOU DISAGREE", "WHEN YOU SLIP UP", "WHEN YOU NEED HELP"], mode="empty", acc="HELP")),
    ("When you have nothing impressive to offer.", "list", dict(items=["WHEN YOU SUCCEED", "WHEN YOU DISAGREE", "WHEN YOU SLIP UP", "WHEN YOU NEED HELP", "WHEN YOU HAVE NOTHING"], mode="empty", acc="NOTHING IMPRESSIVE")),
    ("You don't have to immediately label everyone.", "sticker", dict(tags=["TOXIC?"], strike=True, acc="LABEL")),
    ("But you should be allowed to recognize how certain interactions affect you.", "battery", dict(lbl="AFTER TALKING TO THEM", start=0.9, end=0.25, drains=1, acc="RECOGNIZE AFFECT")),
    ("Healthy relationships shouldn't require you to constantly defend your right to be yourself.", "shield", dict(front="DEFENDING", back="YOURSELF", acc="HEALTHY DEFEND YOURSELF")),
    ("And you don't need to become smaller just to make someone else comfortable.", "hud", dict(lbl="YOUR SIZE", start=30, end=100, icons=None, crowd=4, tag="FULL SIZE", drop=True, acc="SMALLER COMFORTABLE")),
    ("What behavior do you think people should stop accepting in friendships?", "list", dict(items=["STOP ACCEPTING..."], mode="empty", acc="STOP ACCEPTING")),
    ("Let's talk about it.", "cta", dict(kind="comment", lbl="STOP ACCEPTING THIS", acc="TALK")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="YOUR CONFIDENCE", start=90, end=15, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
