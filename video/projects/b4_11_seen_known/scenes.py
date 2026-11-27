from kit import build, follow_sub

TITLE = ("THE DIFFERENCE BETWEEN", "BEING SEEN AND BEING KNOWN")
OUTPUT = "101_Being_Seen_Vs_Being_Known_16x9.mp4"
SPEC = [
    ("You can have thousands of people watching you…", "stage", dict(acc="THOUSANDS WATCHING")),
    ("And still feel like nobody truly knows you.", "mirror", dict(reflect="dashed", lbl="WHO KNOWS YOU?", acc="NOBODY TRULY KNOWS")),
    ("Because being seen isn't the same as being understood.", "scale", dict(left="SEEN", right="UNDERSTOOD", tip=0, acc="SEEN ISN'T UNDERSTOOD.")),
    ("People can know your achievements.", "list", dict(items=["ACHIEVEMENTS"], mode="check", acc="ACHIEVEMENTS.")),
    ("Your appearance.", "list", dict(items=["ACHIEVEMENTS", "APPEARANCE"], mode="check", acc="APPEARANCE.")),
    ("Your posts.", "list", dict(items=["ACHIEVEMENTS", "APPEARANCE", "POSTS"], mode="check", acc="POSTS.")),
    ("Your personality in public.", "list", dict(items=["ACHIEVEMENTS", "APPEARANCE", "POSTS", "PUBLIC YOU"], mode="check", acc="PUBLIC.")),
    ("But knowing someone requires something deeper.", "iceberg", dict(top="SEEN", bottom="KNOWN", acc="DEEPER.")),
    ("Conversations.", "list", dict(items=["CONVERSATIONS"], mode="empty", acc="CONVERSATIONS.")),
    ("Honesty.", "list", dict(items=["CONVERSATIONS", "HONESTY"], mode="empty", acc="HONESTY.")),
    ("Trust.", "list", dict(items=["CONVERSATIONS", "HONESTY", "TRUST"], mode="empty", acc="TRUST.")),
    ("Time.", "list", dict(items=["CONVERSATIONS", "HONESTY", "TRUST", "TIME"], mode="empty", acc="TIME.")),
    ("The parts of yourself that don't fit into a photograph.", "frame", dict(who="THE PHOTO", dashed_fig=True, acc="DON'T PHOTOGRAPH.")),
    ("Don't confuse attention with connection.", "scale", dict(left="ATTENTION", right="CONNECTION", tip=0, acc="ATTENTION CONNECTION.")),
    ("You can be visible to everyone…", "crowd", dict(n=9, highlight=4, highlight_label="VISIBLE", acc="VISIBLE EVERYONE…")),
    ("And still need someone who actually knows you.", "crowd", dict(n=2, highlight=0, highlight_label="KNOWN", acc="ACTUALLY KNOWS")),
    ("Share this with someone who makes you feel understood.", "cta", dict(kind="share", acc="SHARE UNDERSTOOD.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
