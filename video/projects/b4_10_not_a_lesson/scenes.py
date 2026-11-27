from kit import build, follow_sub

TITLE = ("YOU DON'T NEED TO TURN", "EVERYTHING INTO A LESSON")
OUTPUT = "100_You_Dont_Need_To_Turn_Everything_Into_A_Lesson_16x9.mp4"
SPEC = [
    ("Not every bad experience needs to become a motivational quote.", "quote", dict(text="EVERYTHING HAPPENS FOR...", acc="NOT QUOTE.")),
    ("Sometimes things are disappointing.", "chart", dict(kind="down", lbl="DISAPPOINTING", acc="DISAPPOINTING.")),
    ("Sometimes people make mistakes.", "list", dict(items=["A MISTAKE"], mode="strike", acc="MISTAKES.")),
    ("Sometimes something hurts.", "pulse", dict(acc="HURTS.")),
    ("Sometimes you simply have a bad day.", "big", dict(text="BAD DAY", acc="BAD DAY.")),
    ("You don't need to immediately find the hidden meaning.", "puzzle", dict(missing=True, lbl="NO HIDDEN PIECE", acc="IMMEDIATELY HIDDEN MEANING.")),
    ("You don't need to pretend you're grateful for every difficult experience.", "mirror", dict(reflect="dashed", lbl="FAKE GRATEFUL?", acc="PRETEND GRATEFUL")),
    ("You can acknowledge that something was unpleasant…", "mirror", dict(reflect="solid", lbl="IT WAS BAD", acc="ACKNOWLEDGE UNPLEASANT…")),
    ("And still move forward.", "path", dict(kind="straight", acc="FORWARD.")),
    ("Growth doesn't require you to romanticize every problem.", "plant", dict(height=0.5, roots=False, acc="DOESN'T ROMANTICIZE")),
    ("You can learn from something without pretending you enjoyed going through it.", "book", dict(chapter="LEARNED, NOT ENJOYED", acc="LEARN WITHOUT ENJOYED")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
