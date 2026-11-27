from kit import build, follow_sub

TITLE = ("THE STRANGERS WHO", "CONTROL YOUR LIFE")
OUTPUT = "41_The_Strangers_Who_Control_Your_Life_16x9.mp4"
SPEC = [
    ("Imagine making a decision…", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="DECISION…")),
    ("Then realizing you made it because of people who don't even know you.", "crowd", dict(n=9, dim=True, acc="DON'T KNOW")),
    ("You chose that outfit because strangers might judge it.", "stage", dict(lbl="JUDGED?", acc="OUTFIT JUDGE")),
    ("You stayed quiet because strangers might laugh.", "bubbles", dict(texts=["HAHA", "LOL"], acc="QUIET LAUGH.")),
    ("You abandoned an idea because strangers might think it was stupid.", "list", dict(items=["YOUR IDEA"], mode="strike", acc="ABANDONED STUPID.")),
    ("And somehow…", "pulse", dict()),
    ("People who have never spoken to you are influencing how you live your life.", "ring", dict(tags=["STRANGER", "STRANGER", "STRANGER", "STRANGER"], acc="NEVER INFLUENCING")),
    ("Think about how strange that is.", "big", dict(text="STRANGE", acc="STRANGE")),
    ("You're giving people who don't know your story…", "book", dict(chapter="YOUR STORY", acc="STORY…")),
    ("A vote on how your story should end.", "doc", dict(title="BALLOT", empty=False, stamp="THEIR VOTE?", acc="VOTE END.")),
    ("Not everyone deserves that power.", "key", dict(lbl="YOUR POWER", acc="DESERVES POWER.")),
    ("The next time you're about to change something about yourself just to avoid judgment…", "mirror", dict(reflect="dashed", lbl="FOR THEM?", acc="CHANGE JUDGMENT…")),
    ("Ask yourself:", "pulse", dict(acc="ASK")),
    ("Would I still make this decision if nobody could see it?", "chairs", dict(lbl="NOBODY WATCHING", acc="NOBODY SEE")),
    ("If the answer is yes, you probably have your answer.", "list", dict(items=["YES"], mode="check", acc="YES ANSWER.")),
    ("Comment: What's one thing you've stopped caring about people's opinions on?", "cta", dict(kind="comment", lbl="WHAT DID YOU STOP CARING ABOUT?", acc="COMMENT: OPINIONS")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
