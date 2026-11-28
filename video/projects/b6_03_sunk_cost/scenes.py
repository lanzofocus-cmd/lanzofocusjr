from kit import build, follow_sub, hook

TITLE = ("THE SUNK", "COST TRAP")
OUTPUT = "193_The_Sunk_Cost_Trap_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine spending three years building something.", "bricks", dict(rows=5, lbl="3 YEARS", uneven=False, acc="THREE YEARS BUILDING")),
    ("Time.", "receipt", dict(items=[("TIME", "3 YRS")], acc="TIME")),
    ("Energy.", "receipt", dict(items=[("TIME", "3 YRS"), ("ENERGY", "ALL OF IT")], acc="ENERGY")),
    ("Money.", "receipt", dict(items=[("TIME", "3 YRS"), ("ENERGY", "ALL OF IT"), ("MONEY", "$$$")], acc="MONEY")),
    ("Effort.", "receipt", dict(items=[("TIME", "3 YRS"), ("ENERGY", "ALL OF IT"), ("MONEY", "$$$"), ("EFFORT", "MAX")], total="INVESTED", acc="EFFORT")),
    ("And then realizing…", "pulse", dict(acc="REALIZING")),
    ("It's no longer what you want.", "compass", dict(lbl="WHAT YOU WANT", settle=False, acc="NO LONGER WANT")),
    ("Or maybe it isn't working.", "chart", dict(kind="down", lbl="RESULTS", acc="ISN'T WORKING")),
    ("But you keep going.", "path", dict(kind="straight", acc="KEEP GOING")),
    ("Not because the future looks promising.", "fog", dict(lbl="THE FUTURE", acc="FUTURE PROMISING")),
    ("But because stopping feels like admitting that everything you invested was wasted.", "coins", dict(stacks=5, lbl="WASTED?", acc="STOPPING INVESTED WASTED")),
    ("This is one of the most dangerous ways people make decisions.", "gauge", dict(lbl="DANGER", start=0.2, end=0.9, acc="DANGEROUS DECISIONS")),
    ("They allow the past to control the future.", "map", dict(a_lbl="THE PAST", b_lbl="THE FUTURE", acc="PAST CONTROL FUTURE")),
    ("They stay in situations because they've already spent so much time there.", "chairs", dict(n=5, lbl="STILL HERE", acc="STAY ALREADY SPENT")),
    ("They continue projects that no longer make sense.", "doc", dict(title="PROJECT", empty=False, stamp="NO SENSE", acc="CONTINUE PROJECTS SENSE")),
    ("They defend decisions simply because they made them.", "shield", dict(front="MY DECISION", back="EGO", acc="DEFEND MADE")),
    ("But here's the truth.", "key", dict(lbl="THE TRUTH", acc="TRUTH")),
    ("The time you've already spent is gone whether you continue or stop.", "hourglass", dict(acc="SPENT GONE CONTINUE STOP")),
    ("Continuing doesn't magically recover the past.", "receipt", dict(items=[("3 YEARS", "SPENT"), ("REFUND", "NONE")], total="GONE", acc="CONTINUING RECOVER PAST")),
    ("The real question isn't:", "question", dict(acc="REAL QUESTION")),
    ("\"How much have I already invested?\"", "quote", dict(text="HOW MUCH HAVE I INVESTED?", acc="INVESTED")),
    ("The real question is:", "question", dict(acc="REAL QUESTION")),
    ("\"Knowing what I know now, is this still worth investing in?\"", "scale", dict(left="THE PAST", right="WORTH IT NOW?", tip=1, acc="NOW WORTH")),
    ("Imagine buying a ticket to a movie you don't enjoy.", "ticket", dict(lbl="ADMIT ONE", sub="NON-REFUNDABLE", acc="TICKET MOVIE ENJOY")),
    ("You can sit through the entire thing because you paid for it…", "chairs", dict(n=7, lbl="2 MORE HOURS", acc="SIT ENTIRE PAID")),
    ("Or you can recognize that your remaining time is more valuable than proving the original purchase was worth it.", "ticket", dict(lbl="ADMIT ONE", sub="ALREADY SPENT", tear=True, walk=True, acc="REMAINING VALUABLE PROVING")),
    ("Life works the same way.", "timeline", dict(n=10, progress=0.4, tag="YOUR LIFE", acc="LIFE SAME")),
    ("Sometimes continuing is courage.", "stairs", dict(n=6, climb=4, acc="CONTINUING COURAGE")),
    ("Sometimes stopping is wisdom.", "door", dict(open_=True, lbl="WALK AWAY", acc="STOPPING WISDOM")),
    ("The difference is whether you're moving forward because the future is worth it…", "compass", dict(lbl="THE FUTURE", acc="FORWARD FUTURE WORTH")),
    ("Or because you refuse to let go of the past.", "cage", dict(words=["ALREADY INVESTED", "TOO LATE NOW"], acc="REFUSE PAST")),
    ("Don't let yesterday's investment decide tomorrow's direction.", "beam", dict(drop=True, lbl="TOMORROW", tags=("3 YEARS", "THE MONEY", "THE EFFORT"), acc="YESTERDAY'S TOMORROW'S DIRECTION")),
    ("Have you ever continued something simply because you had already invested so much in it?", "coins", dict(stacks=4, lbl="INVESTED", acc="CONTINUED INVESTED")),
    ("Share your experience.", "cta", dict(kind="comment", lbl="YOUR STORY", acc="SHARE EXPERIENCE")),
    ("Someone might recognize the same trap in their own life.", "crowd", dict(n=7, highlight=4, highlight_label="SAME TRAP", acc="RECOGNIZE TRAP")),
    ("", "follow"),
]
_HOOK = ("receipt", dict(items=[("TIME", "3 YRS"), ("ENERGY", "ALL OF IT"), ("MONEY", "$$$")], total="WASTED?"))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
