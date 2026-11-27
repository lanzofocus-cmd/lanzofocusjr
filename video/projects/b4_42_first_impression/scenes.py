from kit import build, follow_sub

TITLE = ("WHY YOUR FIRST IMPRESSION", "ISN'T ALWAYS THE TRUTH")
OUTPUT = "132_Why_Your_First_Impression_Isnt_Always_The_Truth_16x9.mp4"
SPEC = [
    ("You meet someone.", "crowd", dict(n=2, acc="MEET")),
    ("They seem confident.", "sticker", dict(tags=["CONFIDENT"], acc="CONFIDENT.")),
    ("Quiet.", "sticker", dict(tags=["CONFIDENT", "QUIET"], acc="QUIET.")),
    ("Funny.", "sticker", dict(tags=["CONFIDENT", "QUIET", "FUNNY"], acc="FUNNY.")),
    ("Serious.", "sticker", dict(tags=["CONFIDENT", "QUIET", "FUNNY", "SERIOUS"], acc="SERIOUS.")),
    ("And your mind immediately creates a story.", "book", dict(chapter="YOUR STORY ABOUT THEM", acc="IMMEDIATELY STORY.")),
    ("But first impressions are guesses.", "question", dict(acc="GUESSES.")),
    ("They are based on limited information.", "doc", dict(title="INFORMATION", empty=True, acc="LIMITED")),
    ("A person's personality is more complicated than their first interaction.", "iceberg", dict(top="FIRST IMPRESSION", bottom="THE WHOLE PERSON", acc="COMPLICATED FIRST")),
    ("Someone quiet may be thoughtful.", "sticker", dict(tags=["QUIET → THOUGHTFUL"], acc="QUIET THOUGHTFUL.")),
    ("Someone confident may be uncertain.", "sticker", dict(tags=["CONFIDENT → UNCERTAIN"], acc="CONFIDENT UNCERTAIN.")),
    ("Someone who seems distant may simply be tired.", "sticker", dict(tags=["DISTANT → TIRED"], acc="DISTANT TIRED.")),
    ("Don't confuse the first chapter you see…", "book", dict(chapter="CHAPTER 1", acc="FIRST CHAPTER")),
    ("With the entire story.", "book", dict(chapter="THE WHOLE STORY", acc="ENTIRE STORY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
