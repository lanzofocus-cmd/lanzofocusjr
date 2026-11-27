from kit import build, follow_sub

TITLE = ("THE THINGS YOU", "NOTICE ABOUT OTHERS")
OUTPUT = "86_The_Things_You_Notice_About_Others_16x9.mp4"
SPEC = [
    ("The things you admire in someone else…", "crowd", dict(n=3, highlight=1, highlight_label="ADMIRED", acc="ADMIRE")),
    ("May reveal something about yourself.", "mirror", dict(reflect="solid", lbl="YOU", acc="REVEAL YOURSELF.")),
    ("When you admire someone's courage…", "sticker", dict(tags=["COURAGE"], acc="COURAGE…")),
    ("Perhaps courage matters to you.", "key", dict(lbl="COURAGE", acc="COURAGE")),
    ("When you admire someone's kindness…", "sticker", dict(tags=["KINDNESS"], acc="KINDNESS…")),
    ("Perhaps kindness is something you value.", "key", dict(lbl="KINDNESS", acc="KINDNESS VALUE.")),
    ("When you admire someone's creativity…", "sticker", dict(tags=["CREATIVITY"], acc="CREATIVITY…")),
    ("Perhaps you have a desire to create.", "plant", dict(height=0.5, roots=False, acc="DESIRE CREATE.")),
    ("Admiration isn't always about wanting to become that person.", "shed", dict(old="YOU", new="THEM?", acc="ISN'T BECOME")),
    ("Sometimes it's a mirror.", "mirror", dict(reflect="solid", lbl="A MIRROR", acc="MIRROR.")),
    ("It shows you values…", "list", dict(items=["COURAGE", "KINDNESS", "CREATIVITY"], mode="empty", acc="VALUES…")),
    ("You haven't fully expressed in your own life yet.", "iceberg", dict(top="WHAT YOU SHOW", bottom="WHAT YOU VALUE", acc="HAVEN'T EXPRESSED YET.")),
    ("So the next time you admire someone…", "crowd", dict(n=5, highlight=2, highlight_label="ADMIRED", acc="ADMIRE")),
    ("Ask yourself:", "pulse", dict(acc="ASK")),
    ("What exactly am I admiring?", "question", dict(acc="EXACTLY ADMIRING?")),
    ("And how can I bring more of that into my own life?", "door", dict(open_=True, lbl="INTO YOUR LIFE", acc="BRING OWN")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
