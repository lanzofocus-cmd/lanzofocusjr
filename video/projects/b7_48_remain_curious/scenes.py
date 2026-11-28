from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO REMAIN", "CURIOUS ABOUT YOU")
OUTPUT = "248_The_People_Who_Remain_Curious_About_You_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("One of the simplest ways to show someone you care…", "crowd", dict(n=3, highlight=1, highlight_label="SOMEONE", acc="SIMPLEST CARE")),
    ("Is to remain curious about them.", "question", dict(a_lbl="HOW ARE YOU", b_lbl="REALLY?", acc="CURIOUS")),
    ("Not just asking questions when you need something.", "list", dict(items=["ONLY WHEN YOU NEED"], mode="strike", acc="NEED")),
    ("Not just talking about yourself.", "list", dict(items=["ONLY WHEN YOU NEED", "ONLY ABOUT YOU"], mode="strike", acc="YOURSELF")),
    ("Not just assuming that because you know someone…", "list", dict(items=["ONLY WHEN YOU NEED", "ONLY ABOUT YOU", "ASSUMING"], mode="strike", acc="ASSUMING")),
    ("You know everything about them.", "doc", dict(title="WHAT YOU KNOW", empty=False, stamp="OUTDATED?", acc="EVERYTHING")),
    ("People change.", "shed", dict(old="LAST YEAR", new="TODAY", acc="CHANGE")),
    ("Their interests change.", "list", dict(items=["INTERESTS"], mode="tag", tag="NEW", acc="INTERESTS")),
    ("Their worries change.", "list", dict(items=["INTERESTS", "WORRIES"], mode="tag", tag="NEW", acc="WORRIES")),
    ("Their goals change.", "list", dict(items=["INTERESTS", "WORRIES", "GOALS"], mode="tag", tag="NEW", acc="GOALS")),
    ("The person you knew last year may be experiencing something completely different today.", "frame", dict(who="LAST YEAR", new="TODAY", acc="LAST YEAR DIFFERENT TODAY")),
    ("Relationships become stronger when people continue discovering each other.", "network", dict(nodes=["CURIOSITY", "QUESTIONS", "LISTENING", "MEMORY"], tangled=False, acc="STRONGER DISCOVERING")),
    ("Ask questions.", "list", dict(items=["ASK"], mode="check", acc="ASK")),
    ("Listen to the answers.", "list", dict(items=["ASK", "LISTEN"], mode="check", acc="LISTEN")),
    ("Remember details.", "list", dict(items=["ASK", "LISTEN", "REMEMBER"], mode="check", acc="REMEMBER")),
    ("Show interest without treating the conversation like an interview.", "bubbles", dict(texts=["WAIT, TELL ME MORE!"], acc="INTEREST INTERVIEW")),
    ("Sometimes people don't need you to solve their problems.", "list", dict(items=["SOLVE IT"], mode="strike", acc="SOLVE")),
    ("They simply want to feel that you're still interested in who they are.", "hud", dict(lbl="FEELING SEEN", start=20, end=100, icons="heart", crowd=2, drop=True, acc="STILL INTERESTED WHO")),
    ("Send this to someone who makes you feel genuinely listened to.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND LISTENED")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="HOW WELL YOU KNOW THEM", start=95, end=40, icons="q", tag="LAST UPDATED: 2023", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
