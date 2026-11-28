from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO CHANGE YOUR", "LIFE WITHOUT KNOWING IT")
OUTPUT = "276_The_People_Who_Change_Your_Life_Without_Knowing_It_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes someone says something to you…", "bubbles", dict(texts=["YOU'RE GOOD AT THIS."], acc="SAYS")),
    ("And forgets about it immediately.", "frame", dict(who="THEM", fade=True, acc="FORGETS")),
    ("But you remember.", "frame", dict(who="THAT MOMENT", new="YOU, YEARS LATER", acc="REMEMBER")),
    ("Maybe they encouraged you.", "bubbles", dict(texts=["KEEP GOING."], acc="ENCOURAGED")),
    ("Maybe they explained something.", "book", dict(chapter="THEY EXPLAINED", acc="EXPLAINED")),
    ("Maybe they treated you kindly during a difficult moment.", "shield", dict(front="KINDNESS", back="YOU", acc="KINDLY DIFFICULT")),
    ("Maybe they gave you an opportunity.", "door", dict(open_=True, lbl="A CHANCE", acc="OPPORTUNITY")),
    ("Maybe they simply made you feel like you belonged.", "ring", dict(center_tag="YOU BELONG", acc="BELONGED")),
    ("They may never realize how much that moment mattered.", "hud", dict(lbl="WHAT THEY THINK IT MEANT", start=0, end=5, lbl2="WHAT IT MEANT TO YOU", start2=0, end2=100, icons=None, crowd=0, acc="NEVER MATTERED")),
    ("This is one of the interesting things about human connection.", "network", dict(nodes=["YOU", "THEM", "SOMEONE", "ANYONE"], tangled=False, acc="HUMAN CONNECTION")),
    ("We don't always know the impact we're having.", "fog", dict(lbl="YOUR IMPACT", acc="IMPACT")),
    ("A small action can become a significant memory for someone else.", "frame", dict(who="A SMALL KINDNESS", acc="SMALL SIGNIFICANT MEMORY")),
    ("That's why you shouldn't underestimate ordinary kindness.", "crown", dict(lbl="ORDINARY KINDNESS", acc="UNDERESTIMATE ORDINARY KINDNESS")),
    ("You don't need to know exactly how much impact you're having.", "question", dict(acc="EXACTLY IMPACT")),
    ("You simply need to recognize that your behavior can matter more than you realize.", "dots", dict(connect=True, drop=True, acc="BEHAVIOR MATTER REALIZE")),
    ("Share a story about someone who influenced you without knowing how much their actions mattered.", "cta", dict(kind="comment", lbl="WHO CHANGED YOUR LIFE?", acc="STORY INFLUENCED MATTERED")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="WHAT THEY SAID", start=0, end=4, lbl2="WHAT YOU REMEMBER", start2=0, end2=100, icons="heart", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
