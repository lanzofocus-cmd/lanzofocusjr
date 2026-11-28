from kit import build, follow_sub, hook

TITLE = ("DON'T MAKE YOUR WORST MOMENT", "YOUR ENTIRE STORY")
OUTPUT = "226_Why_You_Should_Not_Make_Your_Worst_Moment_Your_Entire_Story_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine someone meeting you during the worst moment of your life.", "frame", dict(who="YOUR WORST DAY", acc="WORST MOMENT")),
    ("They see the mistake.", "list", dict(items=["THE MISTAKE"], mode="tag", tag="SEEN", acc="MISTAKE")),
    ("The failure.", "list", dict(items=["THE MISTAKE", "THE FAILURE"], mode="tag", tag="SEEN", acc="FAILURE")),
    ("The emotional reaction.", "list", dict(items=["THE MISTAKE", "THE FAILURE", "THE REACTION"], mode="tag", tag="SEEN", acc="EMOTIONAL REACTION")),
    ("The bad decision.", "list", dict(items=["THE MISTAKE", "THE FAILURE", "THE REACTION", "THE BAD CALL"], mode="tag", tag="SEEN", acc="BAD DECISION")),
    ("And they decide that's who you are.", "sticker", dict(tags=["THAT'S WHO THEY ARE"], acc="WHO")),
    ("Would that be fair?", "scale", dict(left="ONE MOMENT", right="A WHOLE PERSON", tip=1, acc="FAIR")),
    ("Probably not.", "big", dict(text="NO.", acc="NOT")),
    ("Because people are more complicated than one moment.", "network", dict(nodes=["PAST", "LESSONS", "INTENTIONS", "GROWTH", "ONE MOMENT"], tangled=False, acc="COMPLICATED ONE")),
    ("You have experiences.", "book", dict(chapter="EXPERIENCES", acc="EXPERIENCES")),
    ("Intentions.", "brain", dict(says="I MEANT WELL.", acc="INTENTIONS")),
    ("Lessons.", "list", dict(items=["LESSONS"], mode="check", acc="LESSONS")),
    ("Decisions you've made before.", "timeline", dict(n=10, progress=0.4, tag="BEFORE", acc="BEFORE")),
    ("Decisions you'll make afterward.", "timeline", dict(n=10, progress=0.8, tag="AFTER", acc="AFTERWARD")),
    ("One moment can reveal something important.", "pulse", dict(acc="REVEAL IMPORTANT")),
    ("But it doesn't automatically describe your entire identity.", "book", dict(chapter="ONE PAGE", text="NOT THE WHOLE BOOK", drop=True, acc="DESCRIBE ENTIRE IDENTITY")),
    ("This applies to how you judge other people…", "crowd", dict(n=5, highlight=2, highlight_label="THEM", acc="JUDGE OTHER")),
    ("And how you judge yourself.", "mirror", dict(reflect="solid", lbl="YOU", acc="YOURSELF")),
    ("Take mistakes seriously.", "list", dict(items=["TAKE IT SERIOUSLY"], mode="check", acc="SERIOUSLY")),
    ("Learn from them.", "list", dict(items=["TAKE IT SERIOUSLY", "LEARN"], mode="check", acc="LEARN")),
    ("Repair what you can.", "list", dict(items=["TAKE IT SERIOUSLY", "LEARN", "REPAIR"], mode="check", acc="REPAIR")),
    ("But don't pretend a single moment contains the entire story of a human being.", "timeline", dict(n=12, progress=0.5, tag="ONE MOMENT", acc="SINGLE ENTIRE HUMAN")),
    ("Share this with someone who deserves to be seen as more than one mistake.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE MORE MISTAKE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="ONE BAD MOMENT", start=0, end=100, lbl2="YOUR WHOLE STORY", start2=100, end2=3, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
