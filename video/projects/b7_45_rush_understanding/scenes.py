from kit import build, follow_sub, hook

TITLE = ("DON'T RUSH YOUR", "UNDERSTANDING")
OUTPUT = "245_Why_You_Should_Not_Rush_Your_Understanding_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Sometimes people hear one explanation…", "bubbles", dict(texts=["HERE'S HOW IT WORKS."], acc="ONE EXPLANATION")),
    ("And immediately believe they understand an entire subject.", "hud", dict(lbl="FEELS LIKE I KNOW", start=10, end=95, icons=None, crowd=0, acc="IMMEDIATELY ENTIRE")),
    ("One video.", "list", dict(items=["ONE VIDEO"], mode="check", acc="VIDEO")),
    ("One article.", "list", dict(items=["ONE VIDEO", "ONE ARTICLE"], mode="check", acc="ARTICLE")),
    ("One conversation.", "list", dict(items=["ONE VIDEO", "ONE ARTICLE", "ONE CONVERSATION"], mode="check", acc="CONVERSATION")),
    ("One experience.", "list", dict(items=["ONE VIDEO", "ONE ARTICLE", "ONE CONVERSATION", "ONE EXPERIENCE"], mode="check", acc="EXPERIENCE")),
    ("But understanding something deeply takes more than exposure.", "iceberg", dict(top="EXPOSURE", bottom="DEEP UNDERSTANDING", acc="DEEPLY EXPOSURE")),
    ("You need to question it.", "list", dict(items=["QUESTION IT"], mode="empty", acc="QUESTION")),
    ("Compare perspectives.", "list", dict(items=["QUESTION IT", "COMPARE VIEWS"], mode="empty", acc="PERSPECTIVES")),
    ("Look for examples.", "list", dict(items=["QUESTION IT", "COMPARE VIEWS", "FIND EXAMPLES"], mode="empty", acc="EXAMPLES")),
    ("Try applying it.", "list", dict(items=["QUESTION IT", "COMPARE VIEWS", "FIND EXAMPLES", "APPLY IT"], mode="empty", acc="APPLYING")),
    ("Discover where your understanding breaks down.", "puzzle", dict(missing=True, lbl="THE GAP", acc="BREAKS")),
    ("The first explanation may be useful.", "doc", dict(title="EXPLANATION #1", empty=False, acc="USEFUL")),
    ("But it may also be incomplete.", "doc", dict(title="EXPLANATION #1", empty=False, stamp="INCOMPLETE", acc="INCOMPLETE")),
    ("The more important something is…", "gauge", dict(lbl="IMPORTANCE", start=0.2, end=0.9, acc="IMPORTANT")),
    ("The more valuable it becomes to understand it properly rather than simply repeat what you heard.", "scale", dict(left="UNDERSTAND", right="REPEAT", tip=-1, acc="VALUABLE PROPERLY REPEAT")),
    ("Don't be afraid to say:", "pulse", dict(acc="AFRAID")),
    ("\"I know a little about this.\"", "quote", dict(text="I KNOW A LITTLE ABOUT THIS.", acc="LITTLE")),
    ("Instead of pretending:", "arrows", dict(items=["INSTEAD OF"], acc="PRETENDING")),
    ("\"I understand everything.\"", "list", dict(items=["I UNDERSTAND EVERYTHING."], mode="strike", acc="EVERYTHING")),
    ("Curiosity is more valuable than pretending to be an expert.", "key", dict(lbl="CURIOSITY", drop=True, acc="CURIOSITY VALUABLE EXPERT")),
    ("What's something you want to understand more deeply instead of just knowing the basics?", "cta", dict(kind="comment", lbl="GO DEEPER ON...", acc="DEEPLY BASICS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="CONFIDENCE", start=5, end=99, lbl2="UNDERSTANDING", start2=5, end2=9, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
