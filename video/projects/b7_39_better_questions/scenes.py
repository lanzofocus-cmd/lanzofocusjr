from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO ASK", "BETTER QUESTIONS")
OUTPUT = "239_The_People_Who_Ask_Better_Questions_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Some people are always searching for answers.", "compass", dict(lbl="ANSWERS?", settle=False, acc="ANSWERS")),
    ("But the quality of an answer often depends on the quality of the question.", "scale", dict(left="QUESTION", right="ANSWER", tip=0, acc="QUALITY ANSWER QUESTION")),
    ("Instead of asking:", "arrows", dict(items=["INSTEAD OF"], acc="INSTEAD")),
    ("\"Why am I bad at this?\"", "quote", dict(text="WHY AM I BAD AT THIS?", acc="BAD")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What part of this haven't I learned yet?\"", "puzzle", dict(missing=True, lbl="NOT LEARNED YET", acc="PART LEARNED")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"Why does everything go wrong?\"", "quote", dict(text="WHY DOES EVERYTHING GO WRONG?", acc="EVERYTHING")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What is actually happening, and what can I influence?\"", "key", dict(lbl="WHAT I CAN INFLUENCE", acc="ACTUALLY INFLUENCE")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"How do I become successful?\"", "quote", dict(text="HOW DO I BECOME SUCCESSFUL?", acc="SUCCESSFUL")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What skills, decisions, and habits would make success more likely?\"", "list", dict(items=["SKILLS", "DECISIONS", "HABITS"], mode="check", acc="SKILLS DECISIONS HABITS")),
    ("Better questions change the direction of your thinking.", "path", dict(kind="fork", labels=("WHY ME?", "WHAT NOW?"), drop=True, acc="BETTER DIRECTION THINKING")),
    ("They move you from vague frustration…", "fog", dict(lbl="VAGUE", acc="VAGUE FRUSTRATION")),
    ("Toward specific understanding.", "puzzle", dict(missing=False, lbl="SPECIFIC", acc="SPECIFIC UNDERSTANDING")),
    ("You may not immediately find the answer.", "hourglass", dict(acc="IMMEDIATELY ANSWER")),
    ("But you can stop asking questions that keep you stuck in the same place.", "cage", dict(words=["WHY ME?", "WHY ALWAYS?"], acc="STUCK SAME")),
    ("What's a question you think everyone should ask themselves more often?", "cta", dict(kind="comment", lbl="ASK YOURSELF...", acc="QUESTION EVERYONE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="\"WHY ME?\"", start=90, end=10, lbl2="\"WHAT CAN I CHANGE?\"", start2=10, end2=92, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
