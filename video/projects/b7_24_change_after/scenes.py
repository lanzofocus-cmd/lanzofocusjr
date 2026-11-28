from kit import build, follow_sub, hook

TITLE = ("WHY PEOPLE CHANGE AFTER", "THEY GET WHAT THEY WANT")
OUTPUT = "224_Why_People_Change_After_They_Get_What_They_Want_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever noticed that sometimes people behave differently after achieving something?", "shed", dict(old="BEFORE", new="AFTER", acc="BEHAVE DIFFERENTLY")),
    ("Before the opportunity…", "timeline", dict(n=8, progress=0.3, tag="BEFORE", acc="BEFORE")),
    ("They were patient.", "list", dict(items=["PATIENT"], mode="check", acc="PATIENT")),
    ("Respectful.", "list", dict(items=["PATIENT", "RESPECTFUL"], mode="check", acc="RESPECTFUL")),
    ("Interested.", "list", dict(items=["PATIENT", "RESPECTFUL", "INTERESTED"], mode="check", acc="INTERESTED")),
    ("After they got what they wanted…", "crown", dict(lbl="GOT IT", acc="AFTER WANTED")),
    ("The behavior changed.", "list", dict(items=["PATIENT", "RESPECTFUL", "INTERESTED"], mode="strike", acc="CHANGED")),
    ("This can happen because some people are more interested in the outcome than the relationship.", "scale", dict(left="OUTCOME", right="RELATIONSHIP", tip=-1, acc="OUTCOME RELATIONSHIP")),
    ("They were never truly invested in the connection.", "network", dict(nodes=["YOU", "THEM"], tangled=False, acc="NEVER INVESTED")),
    ("They were invested in what the connection could provide.", "receipt", dict(items=[("FAVOR", "TAKEN"), ("ACCESS", "TAKEN"), ("HELP", "TAKEN")], total="WHAT YOU PROVIDED", acc="PROVIDE")),
    ("That's why it's important to pay attention to consistency.", "chart", dict(kind="flat", lbl="CONSISTENCY", acc="CONSISTENCY")),
    ("Not just how someone treats you when they need something.", "hud", dict(lbl="KINDNESS", start=20, end=95, icons=None, crowd=0, tag="WHEN THEY NEED YOU", acc="NEED")),
    ("Not just how they behave when everything is convenient.", "list", dict(items=["WHEN IT'S CONVENIENT"], mode="empty", acc="CONVENIENT")),
    ("But how they treat people when there's nothing to gain.", "crowd", dict(n=5, highlight=2, highlight_label="NOTHING TO GAIN", acc="NOTHING GAIN")),
    ("Character becomes easier to observe when the reward disappears.", "hud", dict(lbl="REWARD", start=100, end=0, lbl2="TRUE CHARACTER", start2=0, end2=100, icons=None, crowd=0, drop=True, acc="CHARACTER REWARD DISAPPEARS")),
    ("What behavior reveals someone's character more clearly than their words?", "scale", dict(left="WORDS", right="BEHAVIOR", tip=1, acc="REVEALS CHARACTER WORDS")),
    ("Comment your answer.", "cta", dict(kind="comment", lbl="THE REAL TELL", acc="COMMENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="KINDNESS (BEFORE)", start=10, end=95, lbl2="KINDNESS (AFTER)", start2=90, end2=8, icons="thumb", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
