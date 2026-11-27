from kit import build, follow_sub

TITLE = ("THE THING YOU'RE GOOD AT MIGHT", "NOT BE THE THING YOU LOVE")
OUTPUT = "121_Good_At_It_Vs_Loving_It_16x9.mp4"
SPEC = [
    ("You're good at something.", "progress", dict(lbl="SKILL", value=0.85, acc="GOOD")),
    ("People praise you.", "bubbles", dict(texts=["YOU'RE SO GOOD!", "NATURAL TALENT!"], inverted=True, acc="PRAISE")),
    ("You get results.", "chart", dict(kind="up", lbl="RESULTS", acc="RESULTS.")),
    ("And naturally…", "pulse", dict()),
    ("You begin believing that this must be what you're supposed to do.", "sticker", dict(tags=["THIS IS YOUR THING"], acc="SUPPOSED")),
    ("But ability and passion aren't always the same.", "scale", dict(left="ABILITY", right="PASSION", tip=0, acc="ABILITY PASSION AREN'T")),
    ("You can be talented at something…", "progress", dict(lbl="TALENT", value=0.9, acc="TALENTED")),
    ("And not enjoy it.", "gauge", dict(lbl="ENJOYMENT", start=0.5, end=0.1, acc="NOT ENJOY")),
    ("You can love something…", "gauge", dict(lbl="LOVE", start=0.2, end=0.95, acc="LOVE")),
    ("And still be inexperienced.", "progress", dict(lbl="EXPERIENCE", value=0.1, acc="INEXPERIENCED.")),
    ("You can change your interests.", "arrows", dict(items=["INTERESTS"], acc="CHANGE INTERESTS.")),
    ("You can discover new strengths.", "door", dict(open_=True, lbl="NEW STRENGTH", acc="DISCOVER STRENGTHS.")),
    ("Don't let other people's expectations turn one ability into your entire identity.", "sticker", dict(tags=["THE TALENTED ONE"], acc="EXPECTATIONS ONE ENTIRE IDENTITY.")),
    ("Being good at something doesn't mean you're obligated to build your whole life around it.", "bricks", dict(rows=3, lbl="NOT OBLIGATED", uneven=True, acc="DOESN'T OBLIGATED WHOLE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
