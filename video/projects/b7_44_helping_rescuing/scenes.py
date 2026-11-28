from kit import build, follow_sub, hook

TITLE = ("HELPING VS", "RESCUING")
OUTPUT = "244_The_Difference_Between_Helping_And_Rescuing_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Helping someone can be meaningful.", "crowd", dict(n=3, highlight=1, highlight_label="HELPED", acc="HELPING MEANINGFUL")),
    ("But there's a difference between helping someone through a problem…", "path", dict(kind="straight", acc="HELPING THROUGH")),
    ("And taking responsibility for solving every problem they have.", "bricks", dict(rows=6, lbl="ALL THEIR PROBLEMS", uneven=True, acc="RESPONSIBILITY EVERY")),
    ("When you constantly rescue someone from every consequence…", "shield", dict(front="YOU", back="THEM", acc="RESCUE CONSEQUENCE")),
    ("They may never have the opportunity to learn how to handle things themselves.", "cage", dict(words=["PROTECTED"], acc="LEARN THEMSELVES")),
    ("You can support someone.", "list", dict(items=["SUPPORT"], mode="check", acc="SUPPORT")),
    ("Give advice.", "list", dict(items=["SUPPORT", "ADVICE"], mode="check", acc="ADVICE")),
    ("Offer assistance.", "list", dict(items=["SUPPORT", "ADVICE", "ASSISTANCE"], mode="check", acc="ASSISTANCE")),
    ("Listen.", "list", dict(items=["SUPPORT", "ADVICE", "ASSISTANCE", "LISTEN"], mode="check", acc="LISTEN")),
    ("But you cannot live their life for them.", "list", dict(items=["LIVE IT FOR THEM"], mode="strike", acc="CANNOT LIVE")),
    ("Sometimes the most helpful thing you can do is provide support…", "bubbles", dict(texts=["I'M RIGHT HERE."], acc="HELPFUL SUPPORT")),
    ("Without removing their responsibility.", "key", dict(lbl="THEIRS TO HOLD", acc="RESPONSIBILITY")),
    ("Helping should make someone stronger when possible.", "plant", dict(height=0.7, roots=True, lbl="STRONGER", drop=True, acc="HELPING STRONGER")),
    ("It shouldn't automatically make you responsible for everything they struggle with.", "battery", dict(lbl="YOU", start=0.9, end=0.15, drains=1, acc="RESPONSIBLE EVERYTHING")),
    ("What do you think is the difference between genuinely helping someone and enabling them?", "scale", dict(left="HELPING", right="ENABLING", tip=0, acc="HELPING ENABLING")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="HELPING VS ENABLING", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="YOUR HELP", start=20, end=100, lbl2="THEIR GROWTH", start2=60, end2=8, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
