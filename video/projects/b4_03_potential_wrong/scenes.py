from kit import build, follow_sub

TITLE = ("THE PEOPLE WHO KNOW YOUR", "POTENTIAL CAN STILL BE WRONG")
OUTPUT = "93_The_People_Who_Know_Your_Potential_Can_Still_Be_Wrong_16x9.mp4"
SPEC = [
    ("Someone once told you what you couldn't become.", "quote", dict(text="YOU'LL NEVER BE THAT.", acc="COULDN'T BECOME.")),
    ("Maybe they said it confidently.", "gauge", dict(lbl="THEIR CONFIDENCE", start=0.8, end=0.95, acc="CONFIDENTLY.")),
    ("Maybe they had a reason.", "doc", dict(title="THEIR REASON", empty=False, acc="REASON.")),
    ("Maybe you believed them.", "sticker", dict(tags=["CAN'T"], acc="BELIEVED")),
    ("But confidence doesn't make an opinion correct.", "scale", dict(left="CONFIDENT", right="CORRECT", tip=0, acc="DOESN'T CORRECT.")),
    ("People can know you…", "ring", dict(acc="KNOW")),
    ("And still misunderstand you.", "mirror", dict(reflect="dashed", lbl="THEIR VERSION", acc="MISUNDERSTAND")),
    ("They can recognize your current ability…", "progress", dict(lbl="CURRENT ABILITY", value=0.3, acc="CURRENT ABILITY…")),
    ("Without knowing what you're capable of developing.", "iceberg", dict(top="WHAT THEY SEE", bottom="WHAT YOU CAN DEVELOP", acc="CAPABLE DEVELOPING.")),
    ("They can judge your present…", "frame", dict(who="YOUR PRESENT", acc="PRESENT…")),
    ("Without seeing your future.", "path", dict(kind="dashed", fog=True, acc="FUTURE.")),
    ("Take advice seriously.", "book", dict(chapter="ADVICE", acc="ADVICE SERIOUSLY.")),
    ("But don't turn someone's opinion into a permanent ceiling.", "cage", dict(words=["THEIR OPINION"], acc="PERMANENT CEILING.")),
    ("The person who knows who you are today doesn't automatically know who you'll become tomorrow.", "shed", dict(old="TODAY", new="TOMORROW", acc="TODAY TOMORROW.")),
    ("Comment: Have you ever been underestimated?", "cta", dict(kind="comment", lbl="WHEN WERE YOU UNDERESTIMATED?", acc="COMMENT: UNDERESTIMATED?")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
