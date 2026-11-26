from kit import build, follow_sub

TITLE = ("YOUR MISTAKES", "AREN'T YOUR NAME")
OUTPUT = "22_Your_Mistakes_Arent_Your_Name_16x9.mp4"
SPEC = [
    ("You've made mistakes.", "list", dict(items=["THAT ONE", "AND THAT ONE"], mode="strike", acc="MISTAKES.")),
    ("Maybe some of them still bother you.", "brain", dict(says="REMEMBER THAT?", acc="BOTHER")),
    ("Maybe you replay them.", "dots", dict(connect=True, acc="REPLAY")),
    ("Maybe you wish you could go back and make a different decision.", "path", dict(kind="fork", labels=("WHAT YOU DID", "WHAT YOU WISH"), acc="BACK DIFFERENT")),
    ("But a mistake is something you did.", "big", dict(text="DID", sub="A MISTAKE IS AN ACTION", acc="DID.")),
    ("It isn't automatically who you are.", "sticker", dict(tags=["MISTAKE"], strike=True, acc="ISN'T WHO")),
    ("You can acknowledge what happened.", "mirror", dict(reflect="solid", lbl="IT HAPPENED", acc="ACKNOWLEDGE")),
    ("Learn from it.", "book", dict(chapter="WHAT HAPPENED", text="LESSON", acc="LEARN")),
    ("Take responsibility.", "alone", dict(tag="MY RESPONSIBILITY", acc="RESPONSIBILITY.")),
    ("And still refuse to let one chapter define the entire book.", "book", dict(chapter="ONE CHAPTER", text="NOT THE WHOLE BOOK", acc="ONE CHAPTER ENTIRE BOOK.")),
    ("You don't erase your past by pretending it didn't happen.", "frame", dict(who="YOUR PAST", acc="ERASE PRETENDING")),
    ("You move forward by refusing to repeat it.", "shed", dict(old="THEN", new="FORWARD", acc="FORWARD REFUSING REPEAT")),
    ("Follow LanzoFocus for ideas that help you see life differently.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
