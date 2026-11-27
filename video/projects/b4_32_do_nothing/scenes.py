from kit import build, follow_sub

TITLE = ("WHY YOU SHOULD", "SOMETIMES DO NOTHING")
OUTPUT = "122_Why_You_Should_Sometimes_Do_Nothing_16x9.mp4"
SPEC = [
    ("Your mind is constantly searching for something.", "brain", dict(says="WHAT NEXT?", acc="CONSTANTLY SEARCHING")),
    ("Something to watch.", "notifs", dict(items=["SOMETHING TO WATCH"], acc="WATCH.")),
    ("Something to read.", "notifs", dict(items=["SOMETHING TO WATCH", "SOMETHING TO READ"], acc="READ.")),
    ("Something to answer.", "notifs", dict(items=["SOMETHING TO WATCH", "SOMETHING TO READ", "SOMETHING TO ANSWER"], acc="ANSWER.")),
    ("Something to do.", "notifs", dict(items=["SOMETHING TO WATCH", "SOMETHING TO READ", "SOMETHING TO ANSWER", "SOMETHING TO DO"], acc="DO.")),
    ("But what happens when you allow yourself to sit quietly?", "alone", dict(acc="SIT QUIETLY?")),
    ("Without entertainment.", "list", dict(items=["ENTERTAINMENT"], mode="strike", acc="WITHOUT ENTERTAINMENT.")),
    ("Without notifications.", "list", dict(items=["ENTERTAINMENT", "NOTIFICATIONS"], mode="strike", acc="WITHOUT NOTIFICATIONS.")),
    ("Without immediately filling the silence.", "list", dict(items=["ENTERTAINMENT", "NOTIFICATIONS", "FILLING SILENCE"], mode="strike", acc="SILENCE.")),
    ("You may notice thoughts you've been avoiding.", "iceberg", dict(top="THE NOISE", bottom="AVOIDED THOUGHTS", acc="THOUGHTS AVOIDING.")),
    ("Ideas you haven't had time to develop.", "plant", dict(height=0.3, roots=False, acc="IDEAS DEVELOP.")),
    ("Feelings you haven't recognized.", "brain", dict(says="OH. I FEEL THAT.", acc="FEELINGS RECOGNIZED.")),
    ("Your mind needs stimulation.", "gauge", dict(lbl="STIMULATION", start=0.3, end=0.7, acc="STIMULATION.")),
    ("But it also needs space.", "sunrise", dict(acc="SPACE.")),
    ("Not every empty moment needs to be filled.", "chairs", dict(lbl="EMPTY IS OKAY", acc="EMPTY FILLED.")),
    ("Sometimes the quiet is where you finally hear yourself.", "pulse", dict(acc="QUIET HEAR YOURSELF.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
