from kit import build, follow_sub

TITLE = ("THE ROOM YOU", "WALK INTO")
OUTPUT = "154_The_Room_You_Walk_Into_16x9.mp4"
SPEC = [
    ("Pay attention to who you become in different rooms.", "door", dict(open_=True, lbl="NEXT ROOM", acc="BECOME ROOMS")),
    ("Some rooms make you think bigger.", "stairs", dict(n=6, climb=5, acc="BIGGER")),
    ("Others make you shrink.", "alone", dict(tag="SMALLER", others=4, acc="SHRINK")),
    ("Some conversations make you curious.", "bubbles", dict(texts=["WHAT IF WE TRIED...?", "TELL ME MORE."], acc="CURIOUS")),
    ("Others make you feel like you need to prove your existence.", "stage", dict(lbl="PROVE IT", acc="PROVE EXISTENCE")),
    ("Your environment doesn't just surround you.", "ring", dict(acc="ENVIRONMENT SURROUND")),
    ("It influences the person you practice being.", "mirror", dict(reflect="solid", lbl="WHO YOU PRACTICE", acc="INFLUENCES PRACTICE")),
    ("Tag someone whose presence makes you a better version of yourself.", "cta", dict(kind="share", lbl="TAG THEM", acc="TAG BETTER")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
