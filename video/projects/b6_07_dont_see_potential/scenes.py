from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO DON'T", "SEE YOUR POTENTIAL")
OUTPUT = "197_The_People_Who_Dont_See_Your_Potential_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("One of the strangest experiences in life is realizing that someone else's opinion of you…", "bubbles", dict(texts=["OH, I KNOW HIM."], acc="STRANGEST OPINION")),
    ("Can be completely outdated.", "doc", dict(title="YOU, 2019", empty=False, stamp="OUTDATED", acc="OUTDATED")),
    ("Maybe they met you years ago.", "timeline", dict(n=8, progress=0.15, tag="YEARS AGO", acc="YEARS AGO")),
    ("Maybe they remember a mistake you made.", "frame", dict(who="ONE MISTAKE", acc="MISTAKE")),
    ("Maybe they know the version of you that was inexperienced, insecure, or struggling.", "sticker", dict(tags=["INEXPERIENCED", "INSECURE", "STRUGGLING"], acc="INEXPERIENCED INSECURE STRUGGLING")),
    ("And every time you try to become something different…", "shed", dict(old="THEN", new="BECOMING", acc="DIFFERENT")),
    ("They still see the old version.", "frame", dict(who="THE OLD YOU", new="THE REAL YOU", acc="STILL OLD")),
    ("You start improving.", "chart", dict(kind="up", lbl="YOU", acc="IMPROVING")),
    ("You learn.", "book", dict(chapter="LEARNING", acc="LEARN")),
    ("You change your habits.", "list", dict(items=["NEW HABIT", "NEW HABIT", "NEW HABIT"], mode="check", acc="HABITS")),
    ("You develop new interests.", "network", dict(nodes=["MUSIC", "BOOKS", "TRAINING", "BUILDING"], tangled=False, acc="INTERESTS")),
    ("But their perception doesn't move.", "hud", dict(lbl="YOUR GROWTH", start=20, end=90, lbl2="THEIR VIEW OF YOU", start2=12, end2=12, icons=None, crowd=0, acc="PERCEPTION MOVE")),
    ("And if you're not careful…", "pulse", dict(acc="CAREFUL")),
    ("You begin trying to convince them.", "bubbles", dict(texts=["BUT I'VE CHANGED!"], acc="CONVINCE")),
    ("You explain every improvement.", "bubbles", dict(texts=["BUT I'VE CHANGED!", "LET ME EXPLAIN..."], acc="EXPLAIN IMPROVEMENT")),
    ("You prove every achievement.", "stage", dict(lbl="PROOF", acc="PROVE ACHIEVEMENT")),
    ("You desperately want them to notice that you're different now.", "crowd", dict(n=5, dim=True, acc="DESPERATELY NOTICE DIFFERENT")),
    ("But here's something you need to understand.", "key", dict(lbl="UNDERSTAND", acc="UNDERSTAND")),
    ("You cannot force someone to update their opinion of you.", "lock", dict(lbl="THEIR OPINION", acc="CANNOT FORCE UPDATE")),
    ("You can only continue becoming the person you want to become.", "stairs", dict(n=7, climb=5, acc="CONTINUE BECOMING")),
    ("Some people will notice eventually.", "crowd", dict(n=5, highlight=1, highlight_label="NOTICED", acc="NOTICE EVENTUALLY")),
    ("Some won't.", "crowd", dict(n=5, dim=True, acc="WON'T")),
    ("And your growth cannot depend on whether everyone recognizes it.", "plant", dict(height=0.7, roots=True, lbl="YOUR GROWTH", acc="GROWTH CANNOT DEPEND")),
    ("Imagine spending years building a house…", "house", dict(progress=0.5, watchers=False, lbl="YOUR HOUSE", acc="YEARS BUILDING HOUSE")),
    ("But constantly stopping construction to ask people who never visit whether they believe you're building one.", "house", dict(progress=0.5, watchers=True, lbl="ARE YOU SURE?", acc="STOPPING NEVER VISIT")),
    ("At some point, you have to keep working.", "house", dict(progress=0.9, watchers=True, acc="KEEP WORKING")),
    ("Not to prove that they were wrong.", "list", dict(items=["PROVE THEM WRONG"], mode="strike", acc="PROVE WRONG")),
    ("But because the house is yours.", "house", dict(drop=True, progress=1.0, watchers=False, lbl="YOURS", acc="HOUSE YOURS")),
    ("Your future is yours.", "key", dict(lbl="YOUR FUTURE", acc="FUTURE YOURS")),
    ("And you don't need every person from your past to approve of the person you're becoming.", "beam", dict(lbl="WHO YOU'RE BECOMING", tags=("OLD YOU", "SAME AS ALWAYS"), acc="APPROVE BECOMING")),
    ("Have you ever felt like someone still sees an old version of you?", "frame", dict(who="THE OLD YOU", fade=True, acc="OLD VERSION")),
    ("Share your thoughts.", "cta", dict(kind="comment", lbl="SHARE YOUR THOUGHTS", acc="SHARE")),
    ("And follow LanzoFocus for more videos that challenge how you see yourself and your life.", "follow"),
]
_HOOK = ("hud", dict(lbl="YOUR GROWTH", start=10, end=95, lbl2="THEIR OPINION", start2=10, end2=10, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
