from kit import build, follow_sub

TITLE = ("THE QUIETEST FORM", "OF SELF-SABOTAGE")
OUTPUT = "62_The_Quietest_Form_Of_Self_Sabotage_16x9.mp4"
SPEC = [
    ("Self-sabotage doesn't always look destructive.", "big", dict(text="SABOTAGE?", acc="DOESN'T DESTRUCTIVE.")),
    ("Sometimes it looks reasonable.", "doc", dict(title="REASONS", empty=False, acc="REASONABLE.")),
    ("\"I'll wait until I have more information.\"", "quote", dict(text="I NEED MORE INFO.", acc="INFORMATION.\"")),
    ("\"I should probably prepare a little more.\"", "quote", dict(text="A BIT MORE PREP.", acc="PREPARE")),
    ("\"Maybe this isn't the right time.\"", "quote", dict(text="NOT THE RIGHT TIME.", acc="RIGHT TIME.\"")),
    ("\"I'll try when I'm less busy.\"", "quote", dict(text="WHEN I'M LESS BUSY.", acc="BUSY.\"")),
    ("And each decision sounds logical by itself.", "list", dict(items=["MORE INFO", "MORE PREP", "BETTER TIME", "LESS BUSY"], mode="check", acc="LOGICAL")),
    ("But repeated long enough…", "timeline", dict(n=10, progress=0.8, tag="STILL WAITING", acc="REPEATED")),
    ("They can become a pattern of avoiding anything that makes you uncomfortable.", "cage", dict(words=["MORE INFO", "NOT NOW", "LATER"], acc="PATTERN AVOIDING")),
    ("The danger isn't one delay.", "list", dict(items=["ONE DELAY"], mode="empty", acc="ISN'T ONE")),
    ("It's when delay becomes your default response to uncertainty.", "sticker", dict(tags=["DEFAULT: DELAY"], acc="DEFAULT UNCERTAINTY.")),
    ("Ask yourself:", "pulse", dict(acc="ASK")),
    ("Am I genuinely preparing…", "question", dict(a_lbl="PREPARING?", acc="GENUINELY PREPARING…")),
    ("Or am I using preparation to avoid the possibility of failure?", "shield", dict(front="PREPARATION", back="FAILURE", acc="AVOID FAILURE?")),
    ("Be honest.", "mirror", dict(reflect="solid", lbl="HONEST", acc="HONEST.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
