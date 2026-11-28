from kit import build, follow_sub, hook

TITLE = ("THE VALUE OF A", "SECOND CHANCE")
OUTPUT = "237_The_Value_Of_A_Second_Chance_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often talk about second chances as if they're automatic.", "loop", dict(items=["MISTAKE", "SORRY", "RESET", "MISTAKE"], acc="SECOND AUTOMATIC")),
    ("But a second chance doesn't mean repeating the same behavior and expecting a different result.", "loop", dict(items=["SAME", "SAME", "SAME", "SAME"], lbl="SAME RESULT", acc="REPEATING DIFFERENT RESULT")),
    ("It means recognizing what happened.", "list", dict(items=["RECOGNIZE"], mode="check", acc="RECOGNIZING")),
    ("Understanding the mistake.", "list", dict(items=["RECOGNIZE", "UNDERSTAND"], mode="check", acc="UNDERSTANDING")),
    ("Taking responsibility.", "list", dict(items=["RECOGNIZE", "UNDERSTAND", "OWN IT"], mode="check", acc="RESPONSIBILITY")),
    ("Making adjustments.", "list", dict(items=["RECOGNIZE", "UNDERSTAND", "OWN IT", "ADJUST"], mode="check", acc="ADJUSTMENTS")),
    ("And demonstrating through your actions that something has changed.", "shed", dict(old="BEFORE", new="CHANGED", acc="DEMONSTRATING ACTIONS CHANGED")),
    ("A second chance can be meaningful.", "door", dict(open_=True, lbl="SECOND CHANCE", acc="MEANINGFUL")),
    ("But change cannot be proven by promises alone.", "doc", dict(title="PROMISE", empty=False, stamp="NOT PROOF", acc="PROVEN PROMISES")),
    ("It requires behavior.", "bricks", dict(rows=4, lbl="BEHAVIOR", uneven=False, acc="BEHAVIOR")),
    ("And this applies to yourself too.", "mirror", dict(reflect="solid", lbl="YOU TOO", acc="YOURSELF")),
    ("If you failed at something before…", "chart", dict(kind="down", lbl="ATTEMPT 1", acc="FAILED")),
    ("You don't have to repeat the same approach.", "list", dict(items=["SAME APPROACH"], mode="strike", acc="REPEAT SAME")),
    ("You can learn.", "list", dict(items=["LEARN"], mode="check", acc="LEARN")),
    ("Adjust.", "list", dict(items=["LEARN", "ADJUST"], mode="check", acc="ADJUST")),
    ("Try differently.", "list", dict(items=["LEARN", "ADJUST", "TRY DIFFERENTLY"], mode="check", acc="DIFFERENTLY")),
    ("A second chance isn't simply returning to the beginning.", "startline", dict(behind=True, acc="RETURNING BEGINNING")),
    ("It's beginning again with information you didn't have before.", "stairs", dict(n=6, climb=2, drop=True, acc="BEGINNING AGAIN INFORMATION")),
    ("What do you think someone needs to do to genuinely deserve another chance?", "scale", dict(left="WORDS", right="ACTIONS", tip=1, acc="GENUINELY DESERVE")),
    ("Let's discuss.", "cta", dict(kind="comment", lbl="WHAT EARNS IT?", acc="DISCUSS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="ATTEMPT #2", start=0, end=96, lbl2="NEW INFORMATION", start2=0, end2=90, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
