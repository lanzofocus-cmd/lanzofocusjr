from kit import build, follow_sub

TITLE = ("THE PROBLEM WITH TRYING", "TO BE “NORMAL”")
OUTPUT = "94_The_Problem_With_Trying_To_Be_Normal_16x9.mp4"
SPEC = [
    ("You spend so much time trying not to be weird…", "crowd", dict(n=7, highlight=3, highlight_label="TOO WEIRD?", acc="WEIRD…")),
    ("That you forget what makes you interesting.", "iceberg", dict(top="WHAT YOU SHOW", bottom="WHAT'S INTERESTING", acc="INTERESTING.")),
    ("You hide your opinions.", "list", dict(items=["OPINIONS"], mode="strike", acc="OPINIONS.")),
    ("Your hobbies.", "list", dict(items=["OPINIONS", "HOBBIES"], mode="strike", acc="HOBBIES.")),
    ("Your personality.", "list", dict(items=["OPINIONS", "HOBBIES", "PERSONALITY"], mode="strike", acc="PERSONALITY.")),
    ("Your interests.", "list", dict(items=["OPINIONS", "HOBBIES", "PERSONALITY", "INTERESTS"], mode="strike", acc="INTERESTS.")),
    ("You choose the safer answer.", "path", dict(kind="fork", labels=("SAFE", "YOU"), acc="SAFER")),
    ("The more acceptable version of yourself.", "mirror", dict(reflect="dashed", lbl="ACCEPTABLE YOU", acc="ACCEPTABLE")),
    ("But here's the irony.", "big", dict(text="IRONY", acc="IRONY.")),
    ("If you spend your entire life trying to be like everyone else…", "crowd", dict(n=9, dim=True, acc="EVERYONE ELSE…")),
    ("You may eventually become someone you don't even recognize.", "mirror", dict(reflect="dashed", lbl="WHO IS THAT?", acc="DON'T RECOGNIZE.")),
    ("You don't have to be different for attention.", "stage", dict(lbl="FOR ATTENTION?", acc="DIFFERENT ATTENTION.")),
    ("You just don't have to erase yourself for acceptance.", "frame", dict(who="ERASED", dashed_fig=True, fade=True, acc="ERASE ACCEPTANCE.")),
    ("Being yourself isn't about standing out.", "crowd", dict(n=7, highlight=3, acc="YOURSELF ISN'T STANDING")),
    ("It's about not disappearing.", "alone", dict(tag="STILL HERE", acc="NOT DISAPPEARING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
