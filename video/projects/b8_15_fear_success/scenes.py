from kit import build, follow_sub, hook

TITLE = ("WHY PEOPLE SOMETIMES", "FEAR SUCCESS")
OUTPUT = "265_Why_People_Sometimes_Fear_Success_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("People often talk about fear of failure.", "chart", dict(kind="down", lbl="FAILURE", acc="FEAR FAILURE")),
    ("But there's another fear that can be just as powerful.", "gauge", dict(lbl="FEAR", start=0.2, end=0.8, acc="ANOTHER POWERFUL")),
    ("Fear of what happens if you actually succeed.", "crown", dict(lbl="SUCCESS?", acc="SUCCEED")),
    ("What if people expect more from you?", "crowd", dict(n=7, highlight=3, highlight_label="MORE, PLEASE", acc="EXPECT MORE")),
    ("What if you can't maintain the result?", "progress", dict(lbl="KEEPING IT UP", value=0.9, acc="MAINTAIN")),
    ("What if your success changes your relationships?", "network", dict(nodes=["FRIENDS", "FAMILY", "OLD CREW"], tangled=True, acc="CHANGES RELATIONSHIPS")),
    ("What if you become responsible for something bigger?", "bricks", dict(rows=6, lbl="BIGGER", uneven=False, acc="RESPONSIBLE BIGGER")),
    ("What if people start paying attention?", "stage", dict(lbl="SPOTLIGHT", acc="ATTENTION")),
    ("Sometimes people don't avoid opportunities because they believe they'll fail.", "list", dict(items=["FEAR OF FAILING"], mode="strike", acc="AVOID FAIL")),
    ("They avoid them because success would change something familiar.", "door", dict(open_=True, lbl="UNFAMILIAR", drop=True, acc="SUCCESS CHANGE FAMILIAR")),
    ("And change can be uncomfortable even when it's positive.", "gauge", dict(lbl="DISCOMFORT", start=0.2, end=0.6, acc="UNCOMFORTABLE POSITIVE")),
    ("This doesn't mean every hesitation is fear of success.", "list", dict(items=["EVERY HESITATION"], mode="strike", acc="HESITATION")),
    ("Sometimes an opportunity genuinely isn't right.", "puzzle", dict(missing=True, lbl="NOT A FIT", acc="GENUINELY RIGHT")),
    ("But when you repeatedly avoid something you want…", "loop", dict(items=["WANT IT", "GET CLOSE", "BACK AWAY", "WANT IT"], acc="REPEATEDLY AVOID WANT")),
    ("It's worth asking whether you're afraid of the failure…", "scale", dict(left="FAILURE", right="SUCCESS", tip=-1, acc="AFRAID FAILURE")),
    ("Or of what success might require from you.", "scale", dict(left="FAILURE", right="SUCCESS", tip=1, acc="SUCCESS REQUIRE")),
    ("What do you think is more frightening for people: failing at something or succeeding and having to maintain it?", "cta", dict(kind="comment", lbl="FAILING OR SUCCEEDING?", acc="FRIGHTENING FAILING SUCCEEDING")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="FEAR OF FAILURE", start=10, end=40, lbl2="FEAR OF SUCCESS", start2=10, end2=92, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
