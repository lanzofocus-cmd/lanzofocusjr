from kit import build, follow_sub

TITLE = ("THE PRICE OF BEING", "EASY TO LIKE")
OUTPUT = "79_The_Price_Of_Being_Easy_To_Like_16x9.mp4"
SPEC = [
    ("Being liked feels good.", "bubbles", dict(texts=["LOVE YOU!", "SO NICE!"], inverted=True, acc="LIKED GOOD.")),
    ("But if being liked becomes your highest priority…", "network", dict(nodes=["BE LIKED", "YOUR VIEWS", "YOUR NEEDS", "YOUR TRUTH", "YOUR GOALS"], focus=0, tangled=False, acc="HIGHEST PRIORITY…")),
    ("You may begin making decisions that don't belong to you.", "ring", dict(tags=["DO THIS", "SAY THAT", "LIKE THIS", "BE THAT"], acc="DON'T BELONG")),
    ("You agree when you disagree.", "quote", dict(text="YEAH, TOTALLY.", acc="AGREE DISAGREE.")),
    ("You laugh when something isn't funny.", "bubbles", dict(texts=["HAHA", "HAHAHA"], acc="LAUGH ISN'T FUNNY.")),
    ("You hide what you actually think.", "iceberg", dict(top="WHAT YOU SAY", bottom="WHAT YOU THINK", acc="HIDE ACTUALLY")),
    ("You become whatever the situation seems to require.", "sticker", dict(tags=["AGREEABLE", "FUNNY", "EASY"], acc="WHATEVER REQUIRE.")),
    ("And eventually…", "pulse", dict()),
    ("You may become incredibly easy to like…", "crowd", dict(n=7, highlight=3, highlight_label="LIKED", acc="EASY LIKE…")),
    ("But difficult to truly know.", "mirror", dict(reflect="dashed", lbl="WHO ARE YOU?", acc="DIFFICULT TRULY KNOW.")),
    ("Because people are connecting with the version you created for them.", "stage", dict(lbl="THE VERSION", acc="VERSION CREATED")),
    ("Not the person underneath.", "iceberg", dict(top="THE PERFORMANCE", bottom="THE REAL YOU", acc="UNDERNEATH.")),
    ("Being accepted for a performance isn't the same as being accepted for who you are.", "scale", dict(left="PERFORMANCE", right="WHO YOU ARE", tip=0, acc="PERFORMANCE ISN'T WHO")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
