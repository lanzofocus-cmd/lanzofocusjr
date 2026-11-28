from kit import build, follow_sub, hook

TITLE = ("LEARN TO BE PATIENT", "WITH PEOPLE")
OUTPUT = "279_Why_You_Should_Learn_To_Be_Patient_With_People_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People don't always understand things at the same speed.", "timeline", dict(compare=True, acc="UNDERSTAND SPEED")),
    ("Some learn quickly.", "chart", dict(kind="up", lbl="FAST", acc="QUICKLY")),
    ("Some need more explanation.", "book", dict(chapter="ONE MORE TIME", acc="EXPLANATION")),
    ("Some need time to process.", "hourglass", dict(acc="PROCESS")),
    ("Some are experiencing something for the first time.", "startline", dict(behind=False, acc="FIRST TIME")),
    ("And sometimes we become impatient because we expect others to understand immediately.", "gauge", dict(lbl="IMPATIENCE", start=0.2, end=0.85, acc="IMPATIENT IMMEDIATELY")),
    ("But think about the things you struggled with before you learned them.", "frame", dict(who="YOU, LEARNING", acc="STRUGGLED LEARNED")),
    ("Think about the questions you once asked.", "question", dict(a_lbl="HOW DOES", b_lbl="THIS WORK?", acc="QUESTIONS")),
    ("The mistakes you once made.", "list", dict(items=["MISTAKE", "MISTAKE", "MISTAKE"], mode="strike", acc="MISTAKES")),
    ("The concepts that eventually became obvious.", "puzzle", dict(missing=False, lbl="OBVIOUS NOW", acc="CONCEPTS OBVIOUS")),
    ("They weren't always obvious.", "puzzle", dict(missing=True, lbl="NOT ALWAYS", drop=True, acc="WEREN'T OBVIOUS")),
    ("Patience doesn't mean allowing everything.", "list", dict(items=["ALLOW EVERYTHING"], mode="strike", acc="PATIENCE ALLOWING")),
    ("It doesn't mean ignoring responsibility.", "list", dict(items=["ALLOW EVERYTHING", "IGNORE RESPONSIBILITY"], mode="strike", acc="RESPONSIBILITY")),
    ("It means recognizing that people are still learning.", "plant", dict(height=0.5, roots=True, lbl="STILL LEARNING", acc="STILL LEARNING")),
    ("And sometimes the most helpful response isn't criticism.", "list", dict(items=["CRITICISM"], mode="strike", acc="HELPFUL CRITICISM")),
    ("It's explanation.", "bubbles", dict(texts=["HERE, LET ME SHOW YOU."], acc="EXPLANATION")),
    ("What is something you struggled to understand before that now seems simple?", "shed", dict(old="CONFUSING", new="SIMPLE", acc="STRUGGLED SIMPLE")),
    ("Share it to remind someone learning takes time.", "cta", dict(kind="comment", lbl="LEARNING TAKES TIME", acc="SHARE LEARNING TIME")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="YOUR PATIENCE", start=90, end=8, lbl2="THEIR LEARNING", start2=10, end2=40, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
