from kit import build, follow_sub, hook

TITLE = ("THE PROBLEM WITH CONSTANTLY", "SEEKING VALIDATION")
OUTPUT = "212_The_Problem_With_Constantly_Seeking_Validation_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine doing something you're genuinely proud of.", "crown", dict(lbl="PROUD", acc="PROUD")),
    ("You finish a project.", "doc", dict(title="PROJECT", empty=False, stamp="DONE", acc="PROJECT")),
    ("You learn a skill.", "book", dict(chapter="NEW SKILL", acc="SKILL")),
    ("You accomplish a goal.", "stairs", dict(n=6, climb=6, acc="GOAL")),
    ("Then you immediately look around.", "ring", dict(acc="LOOK AROUND")),
    ("Did anyone notice?", "crowd", dict(n=7, dim=True, acc="NOTICE")),
    ("Did anyone compliment it?", "bubbles", dict(texts=["..."], acc="COMPLIMENT")),
    ("Did anyone react?", "phone", dict(lbl="0 REACTIONS", acc="REACT")),
    ("And if nobody does…", "pulse", dict(acc="NOBODY")),
    ("Suddenly, the achievement feels smaller.", "hud", dict(lbl="FEELS LIKE", start=95, end=20, icons=None, crowd=0, acc="ACHIEVEMENT SMALLER")),
    ("This is what happens when you allow external recognition to become the measurement of internal satisfaction.", "progress", dict(lbl="SATISFACTION = LIKES?", value=0.15, acc="EXTERNAL RECOGNITION INTERNAL SATISFACTION")),
    ("Recognition isn't bad.", "list", dict(items=["RECOGNITION"], mode="check", acc="RECOGNITION")),
    ("It's normal to enjoy appreciation.", "hud", dict(lbl="APPRECIATION", start=30, end=80, icons="heart", acc="NORMAL APPRECIATION")),
    ("But if you need other people to confirm every accomplishment before you believe it matters…", "doc", dict(title="ACHIEVEMENT", empty=False, stamp="PENDING APPROVAL", acc="CONFIRM BELIEVE MATTERS")),
    ("You may never develop the ability to recognize your own progress.", "mirror", dict(reflect="dashed", lbl="YOUR PROGRESS?", acc="RECOGNIZE OWN PROGRESS")),
    ("Not everything meaningful will be publicly acknowledged.", "chairs", dict(n=6, lbl="NOBODY WATCHING", acc="MEANINGFUL PUBLICLY")),
    ("Some of your best decisions will happen privately.", "alone", dict(tag="A GOOD DECISION", acc="BEST PRIVATELY")),
    ("Some of your biggest improvements will be invisible.", "progress", dict(lbl="IMPROVEMENT", value=0.7, invisible=True, acc="BIGGEST INVISIBLE")),
    ("Some achievements will only matter to you.", "mirror", dict(reflect="solid", lbl="IT MATTERS", acc="ONLY YOU")),
    ("Learn to recognize those too.", "crown", dict(lbl="SELF-RECOGNIZED", drop=True, acc="RECOGNIZE TOO")),
    ("What is something you've accomplished that nobody really noticed?", "frame", dict(who="UNNOTICED WIN", acc="ACCOMPLISHED NOBODY")),
    ("Share it. It deserves recognition too.", "cta", dict(kind="comment", lbl="YOUR QUIET WIN", acc="SHARE DESERVES")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PRIDE IN YOUR WORK", start=95, end=12, icons="q", tag="0 LIKES", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
