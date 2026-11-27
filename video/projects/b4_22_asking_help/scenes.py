from kit import build, follow_sub

TITLE = ("THE COST OF NEVER", "ASKING FOR HELP")
OUTPUT = "112_The_Cost_Of_Never_Asking_For_Help_16x9.mp4"
SPEC = [
    ("You keep trying to figure everything out alone.", "alone", dict(tag="ALONE", others=4, acc="EVERYTHING ALONE.")),
    ("Because asking for help feels uncomfortable.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.8, acc="HELP UNCOMFORTABLE.")),
    ("Maybe you don't want to bother someone.", "brain", dict(says="I'LL BE A BOTHER.", acc="BOTHER")),
    ("Maybe you think you should already know.", "brain", dict(says="I SHOULD KNOW.", acc="ALREADY KNOW.")),
    ("Maybe you're afraid of looking incapable.", "sticker", dict(tags=["INCAPABLE?"], acc="AFRAID INCAPABLE.")),
    ("But learning often requires other people.", "ring", dict(acc="LEARNING OTHER PEOPLE.")),
    ("Teachers.", "ring", dict(tags=["TEACHERS"], acc="TEACHERS.")),
    ("Friends.", "ring", dict(tags=["TEACHERS", "FRIENDS"], acc="FRIENDS.")),
    ("Mentors.", "ring", dict(tags=["TEACHERS", "FRIENDS", "MENTORS"], acc="MENTORS.")),
    ("Family.", "ring", dict(tags=["TEACHERS", "FRIENDS", "MENTORS", "FAMILY"], acc="FAMILY.")),
    ("Someone who has experience you don't.", "ring", dict(tags=["TEACHERS", "FRIENDS", "MENTORS", "FAMILY", "EXPERIENCE"], acc="EXPERIENCE DON'T.")),
    ("You don't lose independence by asking a question.", "quote", dict(text="CAN YOU SHOW ME?", acc="DON'T INDEPENDENCE QUESTION.")),
    ("You gain information.", "doc", dict(title="INFORMATION", empty=False, acc="GAIN INFORMATION.")),
    ("Being capable doesn't mean doing everything alone.", "list", dict(items=["DO EVERYTHING ALONE"], mode="strike", acc="CAPABLE DOESN'T ALONE.")),
    ("Sometimes capability means knowing when to ask.", "key", dict(lbl="KNOW WHEN TO ASK", acc="CAPABILITY ASK.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
