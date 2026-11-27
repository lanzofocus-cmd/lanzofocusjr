from kit import build, follow_sub

TITLE = ("THE MOMENT YOU STOP EXPECTING", "LIFE TO BE FAIR")
OUTPUT = "134_When_You_Stop_Expecting_Life_To_Be_Fair_16x9.mp4"
SPEC = [
    ("Life isn't always fair.", "scale", dict(left="EFFORT", right="RESULT", tip=-1, acc="ISN'T FAIR.")),
    ("Effort doesn't always produce immediate results.", "progress", dict(lbl="RESULTS", value=0.1, acc="DOESN'T IMMEDIATE")),
    ("Good people can experience difficult circumstances.", "chart", dict(kind="down", lbl="CIRCUMSTANCES", acc="GOOD DIFFICULT")),
    ("Opportunities aren't distributed equally.", "startline", dict(behind=True, acc="AREN'T EQUALLY.")),
    ("And pretending otherwise doesn't help.", "mirror", dict(reflect="solid", lbl="HONEST", acc="PRETENDING")),
    ("But recognizing unfairness…", "doc", dict(title="UNFAIR", empty=False, acc="RECOGNIZING UNFAIRNESS…")),
    ("Doesn't mean you have to surrender.", "shield", dict(front="NO SURRENDER", back="", acc="DOESN'T SURRENDER.")),
    ("You can acknowledge what isn't fair…", "list", dict(items=["IT'S NOT FAIR"], mode="check", acc="ACKNOWLEDGE ISN'T")),
    ("And still make decisions that improve your situation.", "stairs", dict(n=6, climb=2, acc="IMPROVE SITUATION.")),
    ("You can recognize your disadvantages…", "list", dict(items=["DISADVANTAGES"], mode="check", acc="DISADVANTAGES…")),
    ("Without letting them become your entire identity.", "sticker", dict(tags=["DISADVANTAGED"], strike=True, acc="ENTIRE IDENTITY.")),
    ("You don't have to pretend the game is fair to keep playing your part in it.", "path", dict(kind="winding", acc="PRETEND FAIR PLAYING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
