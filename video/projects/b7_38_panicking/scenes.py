from kit import build, follow_sub, hook

TITLE = ("DON'T DECIDE", "WHILE PANICKING")
OUTPUT = "238_Why_You_Should_Not_Make_Decisions_While_Panicking_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("When you're panicking…", "gauge", dict(lbl="PANIC", start=0.3, end=0.98, acc="PANICKING")),
    ("Everything feels urgent.", "notifs", dict(items=["URGENT", "URGENT!", "URGENT!!"], acc="URGENT")),
    ("Your mind wants an immediate solution.", "brain", dict(says="FIX IT NOW!", acc="IMMEDIATE SOLUTION")),
    ("An immediate response.", "list", dict(items=["RESPOND NOW"], mode="empty", acc="RESPONSE")),
    ("An immediate decision.", "list", dict(items=["RESPOND NOW", "DECIDE NOW"], mode="empty", acc="DECISION")),
    ("An immediate escape from the uncertainty.", "door", dict(open_=True, lbl="ESCAPE", acc="ESCAPE UNCERTAINTY")),
    ("But urgency can make you overlook important information.", "fog", dict(lbl="IMPORTANT INFO", acc="URGENCY OVERLOOK")),
    ("You may send a message you regret.", "phone", dict(lbl="SENT. OOPS.", acc="MESSAGE REGRET")),
    ("Make a decision you didn't properly consider.", "path", dict(kind="fork", labels=("FIRST OPTION", "BETTER OPTION"), acc="PROPERLY CONSIDER")),
    ("Or choose the first option simply because it makes the discomfort stop.", "list", dict(items=["FIRST OPTION"], mode="check", acc="FIRST DISCOMFORT")),
    ("Sometimes the most useful thing you can do is create a little space.", "hourglass", dict(drop=True, acc="USEFUL SPACE")),
    ("Pause.", "list", dict(items=["PAUSE"], mode="check", acc="PAUSE")),
    ("Breathe.", "list", dict(items=["PAUSE", "BREATHE"], mode="check", acc="BREATHE")),
    ("Gather information.", "list", dict(items=["PAUSE", "BREATHE", "GATHER INFO"], mode="check", acc="INFORMATION")),
    ("Think through the consequences.", "list", dict(items=["PAUSE", "BREATHE", "GATHER INFO", "THINK IT THROUGH"], mode="check", acc="CONSEQUENCES")),
    ("Not every problem needs to be solved in the exact moment you feel it.", "timeline", dict(n=8, progress=0.2, tag="NOT RIGHT NOW", acc="EXACT MOMENT")),
    ("You can take something seriously without reacting immediately.", "scale", dict(left="SERIOUS", right="IMMEDIATE", tip=-1, acc="SERIOUSLY IMMEDIATELY")),
    ("A calm decision is often more useful than a fast decision made under pressure.", "hud", dict(lbl="CALM", start=20, end=90, lbl2="PANIC", start2=95, end2=15, icons=None, crowd=0, acc="CALM FAST PRESSURE")),
    ("Save this reminder for moments when everything feels urgent and you need to slow down before deciding.", "cta", dict(kind="save", lbl="SLOW DOWN FIRST", acc="SAVE URGENT SLOW")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PANIC", start=10, end=99, lbl2="CLEAR THINKING", start2=80, end2=5, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
