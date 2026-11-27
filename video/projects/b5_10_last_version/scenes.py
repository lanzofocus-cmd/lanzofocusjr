from kit import build, follow_sub

TITLE = ("THE LAST", "VERSION OF YOU")
OUTPUT = "150_The_Last_Version_Of_You_16x9.mp4"
SPEC = [
    ("You are not required to remain loyal to the version of yourself that made your life harder.", "frame", dict(who="OLD YOU", acc="LOYAL VERSION HARDER")),
    ("The person who made those decisions had a different understanding.", "brain", dict(says="I THOUGHT...", acc="DIFFERENT UNDERSTANDING")),
    ("A different mindset.", "list", dict(items=["MINDSET"], mode="tag", tag="THEN", acc="MINDSET")),
    ("Different experiences.", "list", dict(items=["MINDSET", "EXPERIENCES"], mode="tag", tag="THEN", acc="EXPERIENCES")),
    ("Different information.", "list", dict(items=["MINDSET", "EXPERIENCES", "INFORMATION"], mode="tag", tag="THEN", acc="INFORMATION")),
    ("You can acknowledge your past without continuing to live inside it.", "door", dict(open_=True, lbl="THE PAST", acc="ACKNOWLEDGE WITHOUT INSIDE")),
    ("Growth sometimes means disagreeing with who you used to be.", "shed", dict(old="USED TO BE", new="BECOMING", acc="GROWTH DISAGREEING")),
    ("What's one old version of yourself you're ready to leave behind?", "frame", dict(who="OLD VERSION", fade=True, new="YOU NOW", acc="LEAVE BEHIND")),
    ("You don't need to explain everything. Just name it.", "cta", dict(kind="comment", lbl="JUST NAME IT", acc="NAME")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
