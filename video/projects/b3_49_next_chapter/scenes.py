from kit import build, follow_sub

TITLE = ("YOUR NEXT CHAPTER DOESN'T", "NEED TO RESEMBLE YOUR LAST")
OUTPUT = "89_Your_Next_Chapter_Doesnt_Need_To_Resemble_Your_Last_16x9.mp4"
SPEC = [
    ("You've spent years becoming someone.", "timeline", dict(n=10, progress=0.8, tag="YEARS", acc="YEARS BECOMING")),
    ("Learning.", "book", dict(chapter="LEARNING", acc="LEARNING.")),
    ("Making mistakes.", "list", dict(items=["MISTAKES"], mode="strike", acc="MISTAKES.")),
    ("Developing habits.", "path", dict(kind="straight", acc="HABITS.")),
    ("Building relationships.", "ring", dict(acc="RELATIONSHIPS.")),
    ("But what if your next chapter requires something different?", "book", dict(chapter="NEXT CHAPTER", acc="NEXT DIFFERENT?")),
    ("Different priorities.", "arrows", dict(items=["PRIORITIES"], acc="PRIORITIES.")),
    ("Different routines.", "arrows", dict(items=["PRIORITIES", "ROUTINES"], acc="ROUTINES.")),
    ("Different people.", "arrows", dict(items=["PRIORITIES", "ROUTINES", "PEOPLE"], acc="PEOPLE.")),
    ("Different ambitions.", "arrows", dict(items=["PRIORITIES", "ROUTINES", "PEOPLE", "AMBITIONS"], acc="AMBITIONS.")),
    ("You don't have to carry every part of your previous life into your future.", "receipt", dict(items=[("OLD HABITS", "LEAVE"), ("OLD FEARS", "LEAVE"), ("LESSONS", "KEEP")], acc="CARRY EVERY")),
    ("Some things helped you survive a chapter…", "shield", dict(front="SURVIVAL", back="", acc="SURVIVE")),
    ("But may not help you build the next one.", "bricks", dict(rows=3, lbl="THE NEXT ONE", uneven=False, acc="BUILD NEXT")),
    ("And that's okay.", "big", dict(text="OKAY", acc="OKAY.")),
    ("You can appreciate where you've been…", "map", dict(a_lbl="WHERE YOU'VE BEEN", b_lbl="", acc="APPRECIATE BEEN…")),
    ("Without remaining there.", "map", dict(a_lbl="THERE", b_lbl="HERE", acc="WITHOUT REMAINING")),
    ("Growth sometimes means keeping the lesson…", "list", dict(items=["THE LESSON"], mode="check", acc="KEEPING LESSON…")),
    ("And leaving the old version behind.", "shed", dict(old="OLD VERSION", new="NEXT CHAPTER", acc="LEAVING OLD BEHIND.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
