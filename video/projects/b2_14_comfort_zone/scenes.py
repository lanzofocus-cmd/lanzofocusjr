from kit import build, follow_sub

TITLE = ("YOUR COMFORT ZONE ISN'T", "ALWAYS COMFORTABLE")
OUTPUT = "24_Your_Comfort_Zone_Isnt_Always_Comfortable_16x9.mp4"
SPEC = [
    ("You think staying where you are is the safe choice.", "alone", dict(tag="SAFE ZONE", acc="SAFE")),
    ("But what if it isn't?", "question", dict(a_lbl="SAFE?", acc="ISN'T?")),
    ("What if staying in a situation you hate…", "cage", dict(words=["STUCK", "UNHAPPY"], acc="HATE…")),
    ("Avoiding conversations…", "bubbles", dict(texts=["WE NEED TO TALK.", "LATER."], acc="AVOIDING")),
    ("Never attempting something new…", "door", dict(lbl="SOMETHING NEW", acc="NEVER NEW…")),
    ("Is slowly creating a different kind of discomfort?", "gauge", dict(lbl="DISCOMFORT", start=0.1, end=0.75, acc="DIFFERENT DISCOMFORT?")),
    ("The discomfort of wondering.", "brain", dict(says="WHAT IF?", acc="WONDERING.")),
    ("Of regret.", "price", dict(text="REGRET", acc="REGRET.")),
    ("Of imagining what might have happened.", "path", dict(kind="fork", labels=("WHAT HAPPENED", "WHAT MIGHT HAVE"), walker=False, acc="IMAGINING MIGHT")),
    ("Growth isn't always comfortable.", "plant", dict(height=0.6, lbl="GROWING PAINS", acc="GROWTH")),
    ("But neither is remaining exactly where you are.", "chart", dict(kind="flat", lbl="STAYING PUT", acc="NEITHER REMAINING")),
    ("Sometimes the unfamiliar path is frightening…", "path", dict(kind="dashed", fog=True, acc="UNFAMILIAR FRIGHTENING…")),
    ("Because it's unfamiliar.", "fog", dict(lbl="UNKNOWN", acc="UNFAMILIAR.")),
    ("Not because it's wrong.", "compass", dict(lbl="NOT WRONG", acc="NOT WRONG.")),
    ("Follow LanzoFocus for perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
