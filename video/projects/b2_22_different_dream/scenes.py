from kit import build, follow_sub

TITLE = ("YOU'RE ALLOWED TO HAVE", "A DIFFERENT DREAM")
OUTPUT = "32_Youre_Allowed_To_Have_A_Different_Dream_16x9.mp4"
SPEC = [
    ("Maybe the dream you had years ago…", "frame", dict(who="THE OLD DREAM", acc="DREAM YEARS")),
    ("Doesn't excite you anymore.", "gauge", dict(lbl="EXCITEMENT", start=0.8, end=0.15, acc="DOESN'T ANYMORE.")),
    ("Maybe you've changed.", "shed", dict(old="THEN", new="NOW", acc="CHANGED.")),
    ("Maybe you learned more about yourself.", "book", dict(chapter="ABOUT YOU", acc="LEARNED YOURSELF.")),
    ("Maybe the life you once imagined…", "house" if False else "map", dict(a_lbl="YOU", b_lbl="THE OLD PLAN", acc="IMAGINED…")),
    ("Isn't the life you actually want.", "path", dict(kind="fork", labels=("THE OLD PLAN", "WHAT YOU WANT"), acc="ACTUALLY WANT.")),
    ("And that's okay.", "big", dict(text="OKAY", acc="OKAY.")),
    ("Changing direction doesn't automatically mean you failed.", "compass", dict(lbl="NEW DIRECTION", acc="DIRECTION DOESN'T FAILED.")),
    ("Sometimes it means you're finally paying attention.", "brain", dict(says="THIS ISN'T ME.", acc="FINALLY ATTENTION.")),
    ("You don't have to spend your entire life chasing a version of yourself…", "timeline", dict(n=10, progress=0.8, tag="CHASING", acc="CHASING VERSION")),
    ("That no longer exists.", "frame", dict(who="WHO YOU WERE", dashed_fig=True, fade=True, acc="NO LONGER EXISTS.")),
    ("You are allowed to reconsider.", "question", dict(a_lbl="THEN", b_lbl="NOW", acc="ALLOWED RECONSIDER.")),
    ("You are allowed to choose differently.", "arrows", dict(items=["YOUR DREAM"], acc="CHOOSE DIFFERENTLY.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
