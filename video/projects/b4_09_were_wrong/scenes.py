from kit import build, follow_sub

TITLE = ("THE MOMENT YOU REALIZE", "YOU WERE WRONG")
OUTPUT = "99_The_Moment_You_Realize_You_Were_Wrong_16x9.mp4"
SPEC = [
    ("One of the most uncomfortable moments in life…", "pulse", dict(acc="UNCOMFORTABLE")),
    ("Is realizing you were wrong about something you strongly believed.", "doc", dict(title="BELIEF", empty=False, stamp="WRONG", acc="WRONG STRONGLY")),
    ("Maybe you judged someone unfairly.", "sticker", dict(tags=["JUDGED"], acc="UNFAIRLY.")),
    ("Maybe you misunderstood a situation.", "puzzle", dict(missing=True, lbl="MISREAD", acc="MISUNDERSTOOD")),
    ("Maybe you defended an idea that wasn't true.", "shield", dict(front="DEFENDED", back="NOT TRUE", acc="DEFENDED WASN'T TRUE.")),
    ("Your first instinct might be to protect your pride.", "shield", dict(front="PRIDE", back="", acc="PROTECT PRIDE.")),
    ("But what if being wrong isn't something you need to hide?", "iceberg", dict(top="SHOWN", bottom="HIDDEN", acc="WRONG ISN'T HIDE?")),
    ("What if it's an opportunity to become more accurate?", "compass", dict(lbl="MORE ACCURATE", acc="OPPORTUNITY ACCURATE?")),
    ("To understand something better?", "book", dict(chapter="UNDERSTANDING", acc="BETTER?")),
    ("To see a person differently?", "mirror", dict(reflect="solid", lbl="SEE AGAIN", acc="DIFFERENTLY?")),
    ("Your pride wants to protect your old opinion.", "frame", dict(who="OLD OPINION", acc="PRIDE OLD OPINION.")),
    ("Your growth requires you to be willing to replace it.", "frame", dict(who="OLD OPINION", new="NEW UNDERSTANDING", acc="GROWTH REPLACE")),
    ("Being wrong isn't the end of intelligence.", "brain", dict(says="I WAS WRONG.", acc="ISN'T END INTELLIGENCE.")),
    ("Refusing to reconsider might be.", "lock", dict(lbl="CLOSED MIND", acc="REFUSING RECONSIDER")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
