from kit import build, follow_sub

TITLE = ("THE COST OF", "ALWAYS SAYING YES")
OUTPUT = "21_The_Cost_Of_Always_Saying_Yes_16x9.mp4"
SPEC = [
    ("Every time you say yes to something you don't actually want…", "quote", dict(text="SURE, NO PROBLEM.", acc="YES DON'T")),
    ("You might be saying no to something that matters more.", "scale", dict(left="THEIR ASK", right="WHAT MATTERS", tip=-1, acc="NO MATTERS")),
    ("Yes to another distraction.", "list", dict(items=["YES: DISTRACTION"], mode="check", acc="DISTRACTION.")),
    ("Yes to another unnecessary obligation.", "list", dict(items=["YES: DISTRACTION", "YES: OBLIGATION"], mode="check", acc="UNNECESSARY OBLIGATION.")),
    ("Yes to someone else's priorities.", "list", dict(items=["YES: DISTRACTION", "YES: OBLIGATION", "YES: THEIR PRIORITY"], mode="check", acc="ELSE'S PRIORITIES.")),
    ("And eventually…", "pulse", dict()),
    ("Your own priorities disappear beneath everyone else's.", "iceberg", dict(top="THEIR PRIORITIES", bottom="YOURS, BURIED", acc="DISAPPEAR BENEATH")),
    ("Being helpful is valuable.", "crowd", dict(n=5, highlight=2, highlight_label="HELPFUL", acc="HELPFUL VALUABLE.")),
    ("But constantly abandoning yourself to please others isn't kindness.", "ring", dict(tags=["CAN YOU?", "ONE MORE?", "QUICK FAVOR?", "PLEASE?"], center_tag="EMPTY", acc="ABANDONING ISN'T KINDNESS.")),
    ("You can care about people…", "bubbles", dict(texts=["I CARE.", "I'M HERE."], inverted=True, acc="CARE")),
    ("Without giving away every hour of your life.", "timeline", dict(n=10, progress=1.0, tag="YOUR HOURS", acc="EVERY HOUR")),
    ("Learn to protect the things that matter to you.", "shield", dict(front="BOUNDARY", back="WHAT MATTERS", acc="PROTECT MATTER")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
