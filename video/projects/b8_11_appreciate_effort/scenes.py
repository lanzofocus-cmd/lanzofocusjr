from kit import build, follow_sub, hook

TITLE = ("APPRECIATE OTHER", "PEOPLE'S EFFORT")
OUTPUT = "261_Why_You_Should_Learn_To_Appreciate_Other_Peoples_Effort_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine working hard on something.", "bricks", dict(rows=5, lbl="HARD WORK", uneven=False, acc="WORKING HARD")),
    ("Nobody notices.", "crowd", dict(n=7, dim=True, acc="NOBODY NOTICES")),
    ("Nobody mentions it.", "bubbles", dict(texts=["..."], acc="MENTIONS")),
    ("Nobody appreciates the effort.", "hud", dict(lbl="APPRECIATION", start=0, end=0, icons=None, crowd=4, acc="APPRECIATES EFFORT")),
    ("Then imagine someone simply saying:", "crowd", dict(n=3, highlight=1, highlight_label="SOMEONE", acc="SIMPLY")),
    ("\"I noticed how much effort you put into that.\"", "bubbles", dict(texts=["I NOTICED HOW MUCH", "EFFORT YOU PUT IN."], acc="NOTICED EFFORT")),
    ("That sentence might mean more than they realize.", "hud", dict(lbl="HOW MUCH IT MEANT", start=5, end=100, icons="heart", crowd=2, drop=True, acc="SENTENCE MORE REALIZE")),
    ("Because people often notice results…", "crown", dict(lbl="THE RESULT", acc="RESULTS")),
    ("But forget the effort that created them.", "iceberg", dict(top="THE RESULT", bottom="THE EFFORT", acc="FORGET EFFORT")),
    ("The person who prepared.", "list", dict(items=["PREPARED"], mode="check", acc="PREPARED")),
    ("The person who practiced.", "list", dict(items=["PREPARED", "PRACTICED"], mode="check", acc="PRACTICED")),
    ("The person who helped.", "list", dict(items=["PREPARED", "PRACTICED", "HELPED"], mode="check", acc="HELPED")),
    ("The person who stayed patient.", "list", dict(items=["PREPARED", "PRACTICED", "HELPED", "STAYED PATIENT"], mode="check", acc="PATIENT")),
    ("The person who tried again.", "list", dict(items=["PREPARED", "PRACTICED", "HELPED", "STAYED PATIENT", "TRIED AGAIN"], mode="check", acc="AGAIN")),
    ("Appreciation doesn't need to be dramatic.", "list", dict(items=["DRAMATIC"], mode="strike", acc="APPRECIATION DRAMATIC")),
    ("It doesn't need to cost money.", "price", dict(text="$0", sub="COSTS NOTHING", acc="MONEY")),
    ("It doesn't need to be a huge speech.", "stage", dict(lbl="NO SPEECH NEEDED", empty=True, acc="SPEECH")),
    ("Sometimes recognizing someone's effort is enough to make them feel seen.", "crowd", dict(n=5, highlight=2, highlight_label="SEEN", acc="RECOGNIZING SEEN")),
    ("And the interesting thing is…", "pulse", dict(acc="INTERESTING")),
    ("You probably have opportunities to do this every day.", "timeline", dict(n=7, progress=1.0, tag="EVERY DAY", acc="OPPORTUNITIES EVERY")),
    ("You can notice someone's effort.", "list", dict(items=["NOTICE"], mode="check", acc="NOTICE")),
    ("You can thank them.", "list", dict(items=["NOTICE", "THANK THEM"], mode="check", acc="THANK")),
    ("You can acknowledge what they did.", "list", dict(items=["NOTICE", "THANK THEM", "ACKNOWLEDGE"], mode="check", acc="ACKNOWLEDGE")),
    ("You can make appreciation a habit instead of waiting for a special occasion.", "loop", dict(items=["NOTICE", "THANK", "NOTICE", "THANK"], lbl="A HABIT", acc="HABIT OCCASION")),
    ("Think of someone whose effort you appreciate but haven't told recently.", "brain", dict(says="I SHOULD TELL THEM.", acc="EFFORT APPRECIATE TOLD")),
    ("Send them this video, or tell them directly.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND DIRECTLY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="EFFORT", start=10, end=100, lbl2="NOTICED", start2=0, end2=2, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
