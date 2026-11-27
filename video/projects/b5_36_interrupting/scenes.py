from kit import build, follow_sub

TITLE = ("THE LIFE YOU KEEP", "INTERRUPTING")
OUTPUT = "176_The_Life_You_Keep_Interrupting_16x9.mp4"
SPEC = [
    ("Imagine trying to enjoy a movie…", "chairs", dict(n=5, lbl="MOVIE NIGHT", acc="MOVIE")),
    ("But checking your phone every thirty seconds.", "phone", dict(lbl="EVERY 30 SECONDS", acc="PHONE THIRTY")),
    ("Trying to read…", "book", dict(chapter="CHAPTER 1", acc="READ")),
    ("But switching apps constantly.", "notifs", dict(acc="SWITCHING APPS")),
    ("Trying to have a conversation…", "bubbles", dict(texts=["SO, HOW ARE YOU?"], acc="CONVERSATION")),
    ("But mentally leaving every time something appears on your screen.", "notifs", dict(items=["NEW MESSAGE", "NEW POST"], acc="MENTALLY LEAVING SCREEN")),
    ("Your life is happening in the moments you're constantly interrupting.", "pulse", dict(acc="HAPPENING INTERRUPTING")),
    ("Attention isn't just productivity.", "progress", dict(lbl="PRODUCTIVITY", value=0.6, acc="ATTENTION PRODUCTIVITY")),
    ("It's presence.", "big", dict(text="PRESENCE", acc="PRESENCE")),
    ("Save this as a reminder to give at least one moment today your full attention.", "cta", dict(kind="save", lbl="ONE MOMENT, FULL ATTENTION", acc="SAVE FULL ATTENTION")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
