from kit import build, follow_sub

TITLE = ("THE MOST IMPORTANT CONVERSATION", "YOU NEVER HAVE")
OUTPUT = "45_The_Most_Important_Conversation_You_Never_Have_16x9.mp4"
SPEC = [
    ("There is a conversation you keep avoiding.", "bubbles", dict(texts=["WE NEED TO TALK."], acc="AVOIDING.")),
    ("Not with another person.", "crowd", dict(n=5, dim=True, acc="NOT")),
    ("With yourself.", "mirror", dict(reflect="solid", lbl="YOU", acc="YOURSELF.")),
    ("The one where you admit what isn't working.", "list", dict(items=["THIS ISN'T WORKING"], mode="strike", acc="ADMIT ISN'T")),
    ("Where you stop pretending you're satisfied.", "gauge", dict(lbl="SATISFIED?", start=0.8, end=0.3, acc="PRETENDING SATISFIED.")),
    ("Where you acknowledge the goal you keep abandoning…", "list", dict(items=["THE GOAL"], mode="tag", tag="ABANDONED", acc="ABANDONING…")),
    ("The habit you keep defending…", "shield", dict(front="DEFENDING", back="THE HABIT", acc="DEFENDING…")),
    ("The decision you know you need to make.", "path", dict(kind="fork", labels=("AVOID", "DECIDE"), acc="DECISION")),
    ("It's easy to keep moving through life without asking difficult questions.", "path", dict(kind="straight", acc="EASY DIFFICULT QUESTIONS.")),
    ("But eventually…", "pulse", dict()),
    ("The questions you avoid begin influencing the answers your life gives you.", "question", dict(a_lbl="AVOIDED", b_lbl="YOUR LIFE", acc="AVOID ANSWERS")),
    ("So ask yourself honestly:", "mirror", dict(reflect="solid", lbl="HONESTLY", acc="HONESTLY:")),
    ("If nothing changed for the next three years…", "timeline", dict(n=4, progress=1.0, tag="3 YEARS LATER", acc="NOTHING THREE YEARS…")),
    ("Would I be okay with where I was?", "question", dict(a_lbl="YES", b_lbl="NO", acc="OKAY")),
    ("Don't answer quickly.", "hourglass", dict(acc="DON'T QUICKLY.")),
    ("Sit with it.", "pulse", dict(acc="SIT")),
    ("And if the answer is no…", "list", dict(items=["NO"], mode="check", acc="NO…")),
    ("Maybe it's time to stop avoiding the conversation.", "door", dict(open_=True, lbl="THE CONVERSATION", acc="STOP AVOIDING")),
    ("Save this and revisit the question honestly.", "cta", dict(kind="save", lbl="REVISIT THE QUESTION", acc="SAVE REVISIT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
