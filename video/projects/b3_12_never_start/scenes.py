from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO", "NEVER START")
OUTPUT = "52_The_People_Who_Never_Start_16x9.mp4"
SPEC = [
    ("There are two kinds of people who want to do something.", "crowd", dict(n=2, acc="TWO KINDS")),
    ("The ones who try…", "stairs", dict(n=6, climb=2, acc="TRY…")),
    ("And the ones who keep imagining what trying would look like.", "brain", dict(says="WHAT IF I TRIED...", acc="IMAGINING")),
    ("The second group can become incredibly knowledgeable.", "book", dict(chapter="EXPERT IN THEORY", acc="KNOWLEDGEABLE.")),
    ("They research.", "list", dict(items=["RESEARCH"], mode="check", acc="RESEARCH.")),
    ("They plan.", "list", dict(items=["RESEARCH", "PLAN"], mode="check", acc="PLAN.")),
    ("They watch tutorials.", "list", dict(items=["RESEARCH", "PLAN", "TUTORIALS"], mode="check", acc="TUTORIALS.")),
    ("They discuss ideas.", "list", dict(items=["RESEARCH", "PLAN", "TUTORIALS", "DISCUSS"], mode="check", acc="DISCUSS")),
    ("They know exactly what they would do…", "doc", dict(title="THE PLAN", empty=False, acc="EXACTLY")),
    ("If they ever started.", "list", dict(items=["START"], mode="empty", acc="EVER STARTED.")),
    ("But there is a problem.", "big", dict(text="PROBLEM", acc="PROBLEM.")),
    ("Imagining progress can feel so satisfying that it replaces progress.", "progress", dict(lbl="FEELS LIKE PROGRESS", value=0.9, invisible=True, acc="IMAGINING REPLACES")),
    ("Your brain gets a taste of the excitement…", "brain", dict(says="THIS FEELS GREAT!", acc="EXCITEMENT…")),
    ("Without the discomfort of doing the work.", "list", dict(items=["THE ACTUAL WORK"], mode="empty", acc="WITHOUT WORK.")),
    ("And that's why planning can become a trap.", "cage", dict(words=["PLANNING"], acc="TRAP.")),
    ("At some point…", "pulse", dict()),
    ("You have to stop imagining the finished version.", "frame", dict(who="THE FINISHED VERSION", dashed_fig=True, acc="STOP FINISHED")),
    ("And become the unfinished beginner.", "stairs", dict(n=6, climb=1, highlight=0, acc="UNFINISHED BEGINNER.")),
    ("What have you been planning to start?", "question", dict(acc="PLANNING START?")),
    ("Comment it.", "cta", dict(kind="comment", lbl="WHAT WILL YOU START?", acc="COMMENT")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
