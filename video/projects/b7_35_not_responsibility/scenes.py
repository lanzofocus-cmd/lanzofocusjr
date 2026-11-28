from kit import build, follow_sub, hook

TITLE = ("SOME THINGS ARE NOT", "YOUR RESPONSIBILITY")
OUTPUT = "235_The_Moment_You_Realize_Some_Things_Are_Not_Your_Responsibility_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You can care about someone…", "crowd", dict(n=3, highlight=1, highlight_label="SOMEONE", acc="CARE")),
    ("Without solving every problem they have.", "list", dict(items=["SOLVE EVERYTHING"], mode="strike", acc="SOLVING EVERY")),
    ("You can support someone…", "bubbles", dict(texts=["I'M HERE FOR YOU."], acc="SUPPORT")),
    ("Without controlling their decisions.", "list", dict(items=["CONTROL THEIR CHOICES"], mode="strike", acc="CONTROLLING")),
    ("You can listen…", "bubbles", dict(texts=["I'M LISTENING."], acc="LISTEN")),
    ("Without becoming responsible for every emotion they experience.", "list", dict(items=["OWN THEIR EMOTIONS"], mode="strike", acc="RESPONSIBLE EMOTION")),
    ("Sometimes people take responsibility for things that were never entirely theirs.", "bricks", dict(rows=6, lbl="NOT ALL YOURS", uneven=True, acc="RESPONSIBILITY NEVER")),
    ("They feel guilty for someone else's reaction.", "gauge", dict(lbl="GUILT", start=0.2, end=0.8, acc="GUILTY REACTION")),
    ("They try to prevent every disappointment.", "shield", dict(front="NO DISAPPOINTMENT", back="EVERYONE", acc="PREVENT DISAPPOINTMENT")),
    ("They constantly adjust themselves to keep everyone comfortable.", "battery", dict(lbl="YOU", start=0.9, end=0.1, drains=5, acc="ADJUST COMFORTABLE")),
    ("But you are not responsible for controlling every outcome in every relationship.", "fog", dict(lbl="EVERY OUTCOME", drop=True, acc="NOT RESPONSIBLE EVERY OUTCOME")),
    ("You are responsible for your behavior.", "list", dict(items=["YOUR BEHAVIOR"], mode="check", acc="BEHAVIOR")),
    ("Your communication.", "list", dict(items=["YOUR BEHAVIOR", "YOUR COMMUNICATION"], mode="check", acc="COMMUNICATION")),
    ("Your choices.", "list", dict(items=["YOUR BEHAVIOR", "YOUR COMMUNICATION", "YOUR CHOICES"], mode="check", acc="CHOICES")),
    ("Your boundaries.", "list", dict(items=["YOUR BEHAVIOR", "YOUR COMMUNICATION", "YOUR CHOICES", "YOUR BOUNDARIES"], mode="check", acc="BOUNDARIES")),
    ("You can be compassionate without carrying everything.", "scale", dict(left="COMPASSION", right="CARRYING IT ALL", tip=-1, acc="COMPASSIONATE CARRYING")),
    ("Helping someone doesn't mean abandoning yourself.", "mirror", dict(reflect="solid", lbl="STILL HERE", acc="HELPING ABANDONING")),
    ("What is something people need to learn they cannot control?", "brain", dict(says="I CAN'T CONTROL...", acc="LEARN CONTROL")),
    ("Share your perspective.", "cta", dict(kind="comment", lbl="YOUR PERSPECTIVE", acc="PERSPECTIVE")),
    ("", "follow"),
]
_HOOK = ("battery", dict(lbl="YOUR ENERGY", start=1.0, end=0.05, drains=5))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
