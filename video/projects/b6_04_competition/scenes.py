from kit import build, follow_sub, hook

TITLE = ("NOT EVERYTHING IS", "A COMPETITION")
OUTPUT = "194_You_Dont_Have_To_Turn_Everything_Into_A_Competition_16x9.mp4"
MUSIC = "vyzee"
SPEC = [
    ("Somewhere along the way, people started treating life like a race where everyone is competing against everyone else.", "timeline", dict(compare=True, acc="RACE EVERYONE COMPETING")),
    ("Someone gets a better grade.", "doc", dict(title="A+", empty=False, acc="BETTER GRADE")),
    ("Someone earns more money.", "coins", dict(stacks=6, lbl="THEIRS", acc="MONEY")),
    ("Someone becomes more successful.", "crown", dict(lbl="THEM", acc="SUCCESSFUL")),
    ("Someone gets attention.", "stage", dict(lbl="THEM", acc="ATTENTION")),
    ("And suddenly, their achievement feels like your loss.", "scale", dict(left="THEIR WIN", right="YOUR LOSS?", tip=1, acc="ACHIEVEMENT LOSS")),
    ("But think about that for a moment.", "brain", dict(says="WAIT...", acc="THINK")),
    ("If someone learns a new skill…", "book", dict(chapter="NEW SKILL", acc="LEARNS SKILL")),
    ("Did your ability to learn disappear?", "hud", dict(lbl="YOUR ABILITY TO LEARN", start=100, end=100, icons=None, crowd=0, acc="ABILITY DISAPPEAR")),
    ("If someone succeeds…", "stairs", dict(n=6, climb=6, acc="SUCCEEDS")),
    ("Did your opportunity to succeed become smaller?", "door", dict(open_=True, lbl="STILL OPEN", acc="OPPORTUNITY SMALLER")),
    ("If someone improves…", "chart", dict(kind="up", lbl="THEM", acc="IMPROVES")),
    ("Did your potential suddenly decrease?", "hud", dict(lbl="YOUR POTENTIAL", start=100, end=100, icons=None, crowd=0, acc="POTENTIAL DECREASE")),
    ("Most of the time, no.", "big", dict(text="NO.", acc="NO")),
    ("But comparison makes it feel like the world has limited space for success.", "chairs", dict(n=3, lbl="ONLY 3 SEATS?", acc="COMPARISON LIMITED SPACE")),
    ("It convinces you that you must constantly prove you're ahead.", "stage", dict(lbl="PROVE IT", acc="CONSTANTLY PROVE AHEAD")),
    ("And that mindset can make you resent people you could have learned from.", "crowd", dict(n=5, highlight=3, highlight_label="A TEACHER", acc="RESENT LEARNED")),
    ("Instead of asking:", "arrows", dict(items=["THE QUESTION"], acc="INSTEAD")),
    ("\"Why are they better than me?\"", "quote", dict(text="WHY ARE THEY BETTER THAN ME?", acc="BETTER")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What can I learn from what they're doing?\"", "bubbles", dict(texts=["HOW DID YOU DO THAT?", "LET ME SHOW YOU."], acc="LEARN DOING")),
    ("Instead of seeing someone else's achievement as evidence against yourself…", "doc", dict(title="EVIDENCE", empty=False, stamp="AGAINST YOU?", acc="ACHIEVEMENT EVIDENCE AGAINST")),
    ("See it as evidence that something is possible.", "doc", dict(title="EVIDENCE", empty=False, stamp="POSSIBLE", acc="EVIDENCE POSSIBLE")),
    ("You don't need to be the best person in every room.", "door", dict(open_=True, lbl="ANY ROOM", acc="BEST EVERY ROOM")),
    ("You don't need to win every race.", "list", dict(items=["WIN EVERY RACE"], mode="strike", acc="WIN EVERY RACE")),
    ("You don't even need to be moving at the same speed as everyone else.", "path", dict(kind="winding", acc="SAME SPEED")),
    ("Your goal isn't to defeat every person you encounter.", "crowd", dict(n=9, acc="DEFEAT EVERY")),
    ("Your goal is to build a life you're proud of.", "house", dict(progress=0.85, lbl="A LIFE YOU'RE PROUD OF", watchers=False, acc="BUILD PROUD")),
    ("And that becomes much easier when you stop treating other people's progress like an attack on your own.", "network", dict(nodes=["THEIR WIN", "YOUR WIN", "THEIR SKILL", "YOUR SKILL"], tangled=False, acc="EASIER PROGRESS ATTACK")),
    ("Think of someone you admire, not someone you're jealous of.", "scale", dict(left="ADMIRE", right="JEALOUS", tip=-1, acc="ADMIRE JEALOUS")),
    ("What is one thing you could learn from them?", "book", dict(chapter="FROM THEM", text="ONE LESSON", acc="ONE LEARN")),
    ("Comment it below.", "cta", dict(kind="comment", lbl="WHAT YOU'D LEARN", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("timeline", dict(compare=True))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
