from kit import build, follow_sub

TITLE = ("THE COMPLIMENT", "YOU DON'T BELIEVE")
OUTPUT = "164_The_Compliment_You_Dont_Believe_16x9.mp4"
SPEC = [
    ("Sometimes people compliment you…", "bubbles", dict(texts=["YOU DID GREAT!"], acc="COMPLIMENT")),
    ("And your mind immediately finds a reason they're wrong.", "brain", dict(says="NO, I DIDN'T.", acc="REASON WRONG")),
    ("\"They're just being nice.\"", "quote", dict(text="THEY'RE JUST BEING NICE.", acc="NICE")),
    ("\"They don't really mean it.\"", "quote", dict(text="THEY DON'T REALLY MEAN IT.", acc="MEAN")),
    ("\"I could be better.\"", "quote", dict(text="I COULD BE BETTER.", acc="BETTER")),
    ("But constantly dismissing every positive thing about yourself isn't humility.", "shield", dict(front="DEFLECTING", back="HUMILITY?", acc="DISMISSING HUMILITY")),
    ("It's refusing to consider evidence.", "doc", dict(title="EVIDENCE", empty=False, stamp="IGNORED", acc="REFUSING EVIDENCE")),
    ("You don't have to believe you're perfect.", "list", dict(items=["PERFECT"], mode="strike", acc="PERFECT")),
    ("Just stop assuming every good thing people notice is false.", "mirror", dict(reflect="solid", lbl="THEY SEE IT TOO", acc="GOOD NOTICE FALSE")),
    ("Save this if accepting a compliment is harder for you than giving one.", "cta", dict(kind="save", lbl="JUST SAY THANK YOU", acc="SAVE ACCEPTING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
