from kit import build, follow_sub, hook

TITLE = ("YOU'RE NOT THE CENTER", "OF EVERYONE'S WORLD")
OUTPUT = "229_The_Moment_You_Realize_Youre_Not_The_Center_Of_Everyones_World_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You make a mistake.", "list", dict(items=["OOPS"], mode="strike", acc="MISTAKE")),
    ("You say something awkward.", "bubbles", dict(texts=["YOU TOO! ...WAIT."], acc="AWKWARD")),
    ("You walk into a room.", "door", dict(open_=True, lbl="THE ROOM", acc="ROOM")),
    ("You feel embarrassed.", "gauge", dict(lbl="EMBARRASSMENT", start=0.2, end=0.9, acc="EMBARRASSED")),
    ("And your mind tells you everyone noticed.", "crowd", dict(n=9, highlight=4, highlight_label="EVERYONE SAW?", acc="EVERYONE NOTICED")),
    ("Everyone is thinking about it.", "brain", dict(says="THEY'RE ALL", says2="THINKING ABOUT IT", acc="THINKING")),
    ("Everyone remembers.", "doc", dict(title="FOREVER", empty=False, acc="REMEMBERS")),
    ("But think about how much time you spend thinking about other people's small mistakes.", "hourglass", dict(acc="OTHER SMALL MISTAKES")),
    ("Probably very little.", "hud", dict(lbl="TIME SPENT", start=40, end=2, icons=None, crowd=0, acc="LITTLE")),
    ("You have your own problems.", "list", dict(items=["YOUR PROBLEMS"], mode="check", acc="PROBLEMS")),
    ("Your own plans.", "list", dict(items=["YOUR PROBLEMS", "YOUR PLANS"], mode="check", acc="PLANS")),
    ("Your own worries.", "list", dict(items=["YOUR PROBLEMS", "YOUR PLANS", "YOUR WORRIES"], mode="check", acc="WORRIES")),
    ("Other people are usually doing the same.", "ring", dict(tags=["THEIR PLANS", "THEIR WORRIES", "THEIR DAY", "THEIR PROBLEMS"], acc="SAME")),
    ("They may notice something briefly…", "pulse", dict(acc="BRIEFLY")),
    ("Then move on.", "path", dict(kind="straight", acc="MOVE")),
    ("Understanding this can make life much less intimidating.", "gauge", dict(lbl="INTIMIDATION", start=0.8, end=0.15, acc="LESS INTIMIDATING")),
    ("You don't need to perform perfectly.", "list", dict(items=["PERFORM PERFECTLY"], mode="strike", acc="PERFORM")),
    ("You don't need to eliminate every awkward moment.", "list", dict(items=["PERFORM PERFECTLY", "ZERO AWKWARDNESS"], mode="strike", acc="AWKWARD")),
    ("You don't need to control everyone's impression of you.", "list", dict(items=["PERFORM PERFECTLY", "ZERO AWKWARDNESS", "CONTROL IMPRESSIONS"], mode="strike", acc="CONTROL IMPRESSION")),
    ("People are busy living their own lives.", "crowd", dict(n=9, dim=True, acc="BUSY OWN")),
    ("And that means you have more freedom than you think.", "beam", dict(lbl="FREEDOM", tags=("WHAT WILL THEY THINK?",), drop=True, acc="FREEDOM")),
    ("Save this for the next time embarrassment makes something feel much bigger than it actually is.", "cta", dict(kind="save", lbl="NOBODY'S WATCHING THAT CLOSELY", acc="SAVE EMBARRASSMENT BIGGER")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PEOPLE WHO NOTICED", start=0, end=100, icons="q", tag="REALLY?", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
