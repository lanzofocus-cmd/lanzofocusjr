from kit import build, follow_sub

TITLE = ("YOU'RE NOT ALWAYS", "THE MAIN CHARACTER")
OUTPUT = "61_Youre_Not_Always_The_Main_Character_16x9.mp4"
SPEC = [
    ("It's uncomfortable to realize…", "pulse", dict(acc="UNCOMFORTABLE")),
    ("That most people aren't thinking about you nearly as much as you think.", "stage", dict(empty=True, acc="AREN'T THINKING")),
    ("They have their own worries.", "crowd", dict(n=5, acc="OWN WORRIES.")),
    ("Their own problems.", "bubbles", dict(texts=["MY RENT...", "MY EXAM..."], acc="PROBLEMS.")),
    ("Their own embarrassing moments.", "stage", dict(lbl="THEIR MOMENT", performing=False, acc="EMBARRASSING")),
    ("Their own lives.", "ring", dict(acc="LIVES.")),
    ("The thing you said yesterday…", "quote", dict(text="THAT THING I SAID...", acc="YESTERDAY…")),
    ("The outfit you wore…", "alone", dict(tag="THAT OUTFIT", acc="OUTFIT")),
    ("The mistake you made…", "list", dict(items=["THAT MISTAKE"], mode="strike", acc="MISTAKE")),
    ("They may have forgotten it already.", "frame", dict(who="FORGOTTEN", fade=True, acc="FORGOTTEN ALREADY.")),
    ("And that realization can be freeing.", "key", dict(lbl="FREEDOM", acc="FREEING.")),
    ("Because you've been carrying the weight of an imaginary audience.", "chairs", dict(lbl="IMAGINARY AUDIENCE", acc="IMAGINARY AUDIENCE.")),
    ("Trying to look perfect.", "mirror", dict(reflect="dashed", lbl="PERFECT?", acc="PERFECT.")),
    ("Trying to avoid mistakes.", "shield", dict(front="NO MISTAKES", back="", acc="AVOID MISTAKES.")),
    ("Trying to control what people think.", "brain", dict(says="WHAT WILL THEY THINK?", acc="CONTROL THINK.")),
    ("But everyone is busy living their own story.", "book", dict(chapter="THEIR STORY", acc="OWN STORY.")),
    ("You can stop performing for an audience that probably isn't watching.", "stage", dict(empty=True, performing=False, acc="STOP PERFORMING ISN'T")),
    ("Live a little more honestly.", "sunrise", dict(acc="HONESTLY.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
