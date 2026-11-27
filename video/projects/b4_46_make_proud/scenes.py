from kit import build, follow_sub

TITLE = ("YOU DON'T NEED TO MAKE", "EVERYONE PROUD")
OUTPUT = "136_You_Dont_Need_To_Make_Everyone_Proud_16x9.mp4"
SPEC = [
    ("You want people to be proud of you.", "crowd", dict(n=7, highlight=3, highlight_label="YOU", acc="PROUD")),
    ("Your family.", "ring", dict(tags=["FAMILY"], acc="FAMILY.")),
    ("Your friends.", "ring", dict(tags=["FAMILY", "FRIENDS"], acc="FRIENDS.")),
    ("The people who supported you.", "ring", dict(tags=["FAMILY", "FRIENDS", "SUPPORTERS"], acc="SUPPORTED")),
    ("And that's understandable.", "list", dict(items=["UNDERSTANDABLE"], mode="check", acc="UNDERSTANDABLE.")),
    ("But what happens when their expectations conflict?", "ring", dict(tags=["BE A DOCTOR", "TRAVEL!", "STAY CLOSE", "START A BUSINESS"], acc="EXPECTATIONS CONFLICT?")),
    ("What happens when everyone wants something different?", "network", dict(nodes=["THIS", "THAT", "THE OTHER", "SOMETHING ELSE", "ANYTHING BUT"], tangled=True, acc="EVERYONE DIFFERENT?")),
    ("You cannot build a life that satisfies every person.", "bricks", dict(rows=3, lbl="FOR EVERYONE?", uneven=True, acc="CANNOT EVERY")),
    ("At some point…", "pulse", dict()),
    ("You must make decisions based on your own values.", "compass", dict(lbl="YOUR VALUES", acc="OWN VALUES.")),
    ("Listen to people.", "bubbles", dict(texts=["HERE'S MY ADVICE."], acc="LISTEN")),
    ("Respect their perspectives.", "list", dict(items=["THEIR VIEW"], mode="check", acc="RESPECT")),
    ("But remember…", "pulse", dict(acc="REMEMBER…")),
    ("You are the person who has to live the life you're choosing.", "alone", dict(tag="YOUR LIFE", acc="LIVE CHOOSING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
