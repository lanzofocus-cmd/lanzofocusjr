from kit import build, follow_sub, hook

TITLE = ("THE MOMENT YOU REALIZE", "YOU WERE THE PROBLEM")
OUTPUT = "208_The_Moment_You_Realize_You_Were_The_Problem_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("It's uncomfortable to realize that sometimes…", "mirror", dict(reflect="solid", acc="UNCOMFORTABLE")),
    ("You were the person making the situation worse.", "mirror", dict(reflect="solid", lbl="IT WAS ME", acc="WORSE")),
    ("Maybe you misunderstood someone.", "question", dict(a_lbl="WHAT", b_lbl="THEY MEANT", acc="MISUNDERSTOOD")),
    ("Maybe you reacted too quickly.", "gauge", dict(lbl="REACTION", start=0.2, end=0.95, acc="QUICKLY")),
    ("Maybe you refused to listen.", "shield", dict(front="NOT LISTENING", back="YOU", acc="REFUSED LISTEN")),
    ("Maybe you were so focused on being right that you ignored how your behavior affected someone else.", "scale", dict(left="BEING RIGHT", right="THEIR FEELINGS", tip=-1, acc="RIGHT IGNORED")),
    ("It's easy to recognize mistakes when other people make them.", "crowd", dict(n=5, highlight=1, highlight_label="THEIR MISTAKE", acc="EASY OTHER")),
    ("It's much harder when the mistake belongs to you.", "mirror", dict(reflect="solid", lbl="MINE", acc="HARDER YOU")),
    ("But this realization can be one of the most important moments in your life.", "sunrise", dict(acc="REALIZATION IMPORTANT")),
    ("Because you can't improve a behavior you refuse to acknowledge.", "lock", dict(lbl="REFUSAL", acc="IMPROVE ACKNOWLEDGE")),
    ("You can't repair damage while pretending you did nothing wrong.", "bricks", dict(rows=4, lbl="DAMAGE", uneven=True, acc="REPAIR PRETENDING")),
    ("And you can't grow while treating every uncomfortable piece of feedback as an attack.", "shield", dict(front="FEEDBACK = ATTACK", back="GROWTH", acc="GROW FEEDBACK ATTACK")),
    ("Taking responsibility doesn't mean blaming yourself for everything.", "list", dict(items=["BLAME YOURSELF FOR EVERYTHING"], mode="strike", acc="RESPONSIBILITY BLAMING")),
    ("It means being honest about the parts you actually control.", "key", dict(lbl="YOUR PART", acc="HONEST CONTROL")),
    ("Your behavior.", "list", dict(items=["BEHAVIOR"], mode="check", acc="BEHAVIOR")),
    ("Your decisions.", "list", dict(items=["BEHAVIOR", "DECISIONS"], mode="check", acc="DECISIONS")),
    ("Your words.", "list", dict(items=["BEHAVIOR", "DECISIONS", "WORDS"], mode="check", acc="WORDS")),
    ("Your willingness to change.", "list", dict(items=["BEHAVIOR", "DECISIONS", "WORDS", "WILLINGNESS TO CHANGE"], mode="check", acc="WILLINGNESS CHANGE")),
    ("Sometimes the most important sentence you can say is:", "pulse", dict(acc="IMPORTANT SENTENCE")),
    ("\"I understand why I was wrong.\"", "quote", dict(text="I UNDERSTAND WHY I WAS WRONG.", drop=True, acc="UNDERSTAND WRONG")),
    ("And then prove it through what you do next.", "stairs", dict(n=6, climb=2, acc="PROVE NEXT")),
    ("What's one lesson you've learned about yourself from a mistake?", "book", dict(chapter="ONE LESSON", acc="LESSON MISTAKE")),
    ("Share the lesson, not necessarily the entire story.", "cta", dict(kind="comment", lbl="JUST THE LESSON", acc="SHARE LESSON")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="THEIR FAULT", start=95, end=30, lbl2="MY PART", start2=5, end2=70, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
