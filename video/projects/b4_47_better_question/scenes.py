from kit import build, follow_sub

TITLE = ("THE POWER OF ASKING", "A BETTER QUESTION")
OUTPUT = "137_The_Power_Of_Asking_A_Better_Question_16x9.mp4"
SPEC = [
    ("Sometimes…", "pulse", dict()),
    ("The question you're asking is keeping you stuck.", "cage", dict(words=["WHY ME?"], acc="QUESTION STUCK.")),
    ("\"Why am I so bad at this?\"", "quote", dict(text="WHY AM I SO BAD AT THIS?", acc="BAD")),
    ("\"Why does this always happen?\"", "quote", dict(text="WHY DOES THIS ALWAYS HAPPEN?", acc="ALWAYS")),
    ("\"Why can't I change?\"", "quote", dict(text="WHY CAN'T I CHANGE?", acc="CAN'T")),
    ("Those questions assume the problem is permanent.", "lock", dict(lbl="PERMANENT?", acc="ASSUME PERMANENT.")),
    ("Try asking something different.", "arrows", dict(items=["THE QUESTION"], acc="DIFFERENT.")),
    ("\"What could I learn?\"", "quote", dict(text="WHAT COULD I LEARN?", acc="LEARN?\"")),
    ("\"What is one thing I can change?\"", "quote", dict(text="WHAT'S ONE THING I CAN CHANGE?", acc="ONE CHANGE?\"")),
    ("\"What haven't I tried?\"", "quote", dict(text="WHAT HAVEN'T I TRIED?", acc="HAVEN'T TRIED?\"")),
    ("\"What would make this easier?\"", "quote", dict(text="WHAT WOULD MAKE THIS EASIER?", acc="EASIER?\"")),
    ("The question you ask influences the answers you search for.", "compass", dict(lbl="YOUR QUESTION", acc="QUESTION INFLUENCES ANSWERS")),
    ("A better question can create a better direction.", "path", dict(kind="fork", labels=("WHY ME?", "WHAT NOW?"), acc="BETTER QUESTION BETTER DIRECTION.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
