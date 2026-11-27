from kit import build, follow_sub

TITLE = ("THE THINGS THAT", "ARE STILL POSSIBLE")
OUTPUT = "188_The_Things_That_Are_Still_Possible_16x9.mp4"
SPEC = [
    ("Your current situation is not a complete prediction of your future.", "fog", dict(lbl="YOUR FUTURE", acc="CURRENT PREDICTION FUTURE")),
    ("Your current skills.", "list", dict(items=["SKILLS"], mode="tag", tag="FOR NOW", acc="SKILLS")),
    ("Your current confidence.", "list", dict(items=["SKILLS", "CONFIDENCE"], mode="tag", tag="FOR NOW", acc="CONFIDENCE")),
    ("Your current circumstances.", "list", dict(items=["SKILLS", "CONFIDENCE", "CIRCUMSTANCES"], mode="tag", tag="FOR NOW", acc="CIRCUMSTANCES")),
    ("They're information about where you are.", "map", dict(a_lbl="YOU ARE HERE", b_lbl="?", acc="INFORMATION WHERE")),
    ("Not proof of where you must remain.", "doc", dict(title="PROOF", empty=True, stamp="NOT PROOF", acc="PROOF REMAIN")),
    ("The future contains possibilities you haven't experienced yet.", "door", dict(open_=True, lbl="NOT YET SEEN", acc="POSSIBILITIES YET")),
    ("Don't confuse what is true today with what will always be true.", "timeline", dict(n=10, progress=0.2, tag="TODAY", acc="TODAY ALWAYS")),
    ("Share this with someone who needs to stop treating their current situation like a permanent sentence.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SHARE PERMANENT SENTENCE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
