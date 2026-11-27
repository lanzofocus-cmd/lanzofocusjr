from kit import build, follow_sub

TITLE = ("THE THINGS YOU WILL", "NEVER REGRET LEARNING")
OUTPUT = "138_The_Things_You_Will_Never_Regret_Learning_16x9.mp4"
SPEC = [
    ("You may forget certain facts.", "frame", dict(who="FACTS", fade=True, acc="FORGET FACTS.")),
    ("You may change careers.", "arrows", dict(items=["CAREER"], acc="CAREERS.")),
    ("You may stop using a particular skill.", "list", dict(items=["THAT SKILL"], mode="strike", acc="STOP SKILL.")),
    ("But some lessons remain useful.", "key", dict(lbl="FOR LIFE", acc="REMAIN USEFUL.")),
    ("How to communicate.", "list", dict(items=["COMMUNICATE"], mode="check", acc="COMMUNICATE.")),
    ("How to think critically.", "list", dict(items=["COMMUNICATE", "THINK CRITICALLY"], mode="check", acc="CRITICALLY.")),
    ("How to manage your time.", "list", dict(items=["COMMUNICATE", "THINK CRITICALLY", "MANAGE TIME"], mode="check", acc="TIME.")),
    ("How to treat people.", "list", dict(items=["COMMUNICATE", "THINK CRITICALLY", "MANAGE TIME", "TREAT PEOPLE WELL"], mode="check", acc="PEOPLE.")),
    ("How to learn.", "list", dict(items=["COMMUNICATE", "THINK CRITICALLY", "MANAGE TIME", "TREAT PEOPLE WELL", "LEARN"], mode="check", acc="LEARN.")),
    ("How to admit mistakes.", "quote", dict(text="I WAS WRONG.", acc="ADMIT MISTAKES.")),
    ("How to make decisions.", "path", dict(kind="fork", labels=("THIS", "THAT"), acc="DECISIONS.")),
    ("These skills travel with you.", "receipt", dict(items=[("COMMUNICATION", "PACKED"), ("THINKING", "PACKED"), ("KINDNESS", "PACKED")], acc="TRAVEL")),
    ("Across environments.", "map", dict(a_lbl="HERE", b_lbl="ANYWHERE", acc="ENVIRONMENTS.")),
    ("Across opportunities.", "door", dict(open_=True, lbl="ANY DOOR", acc="OPPORTUNITIES.")),
    ("Across different versions of your life.", "shed", dict(old="THEN", new="NEXT", acc="VERSIONS")),
    ("Don't only learn things for where you are now.", "alone", dict(tag="NOW", acc="ONLY NOW.")),
    ("Learn things that will help wherever you go next.", "compass", dict(lbl="WHEREVER NEXT", acc="WHEREVER NEXT.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
