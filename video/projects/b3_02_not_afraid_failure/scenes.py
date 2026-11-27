from kit import build, follow_sub

TITLE = ("YOU'RE NOT AFRAID", "OF FAILURE")
OUTPUT = "42_Youre_Not_Afraid_Of_Failure_16x9.mp4"
SPEC = [
    ("You're probably not afraid of failing.", "big", dict(text="FAILURE?", acc="NOT FAILING.")),
    ("You're afraid of what failure would make you believe about yourself.", "mirror", dict(reflect="dashed", lbl="WHAT IT MEANS", acc="BELIEVE YOURSELF.")),
    ("Because failing at something is one thing.", "list", dict(items=["ONE ATTEMPT"], mode="strike", acc="ONE")),
    ("But what if you fail…", "chart", dict(kind="down", lbl="IT DIDN'T WORK", acc="FAIL…")),
    ("And suddenly your mind says:", "brain", dict(acc="MIND")),
    ("\"Maybe I'm not talented.\"", "brain", dict(says="MAYBE I'M NOT TALENTED.", acc="TALENTED.\"")),
    ("\"Maybe I was never capable.\"", "brain", dict(says="MAYBE I'M NOT TALENTED.", says2="NEVER CAPABLE.", acc="NEVER CAPABLE.\"")),
    ("\"Maybe everyone was right.\"", "bubbles", dict(texts=["NOT TALENTED", "NEVER CAPABLE", "THEY WERE RIGHT"], center="brain", acc="EVERYONE RIGHT.\"")),
    ("That's the real fear.", "big", dict(text="THE REAL FEAR", acc="REAL FEAR.")),
    ("Not the mistake.", "list", dict(items=["THE MISTAKE"], mode="strike", acc="NOT MISTAKE.")),
    ("The identity you might attach to it.", "sticker", dict(tags=["FAILURE"], acc="IDENTITY ATTACH")),
    ("But failure doesn't reveal your permanent potential.", "iceberg", dict(top="ONE RESULT", bottom="YOUR POTENTIAL", acc="DOESN'T PERMANENT")),
    ("It reveals what happened under a particular set of circumstances…", "doc", dict(title="REPORT", empty=False, acc="CIRCUMSTANCES…")),
    ("With your current knowledge…", "progress", dict(lbl="CURRENT KNOWLEDGE", value=0.3, acc="CURRENT KNOWLEDGE…")),
    ("At one particular moment.", "timeline", dict(n=10, progress=0.3, tag="ONE MOMENT", acc="ONE MOMENT.")),
    ("That's not a final verdict.", "doc", dict(title="VERDICT", empty=True, stamp="NOT FINAL", acc="NOT VERDICT.")),
    ("It's information.", "doc", dict(title="DATA", empty=False, stamp="INFORMATION", acc="INFORMATION.")),
    ("Stop treating every failure like a courtroom where your entire future is being judged.", "scale", dict(left="ONE FAILURE", right="YOUR FUTURE", tip=0, acc="COURTROOM JUDGED.")),
    ("You're allowed to be inexperienced without being incapable.", "scale", dict(left="INEXPERIENCED", right="INCAPABLE", tip=-1, acc="INEXPERIENCED INCAPABLE.")),
    ("Save this for the next time a mistake makes you question yourself.", "cta", dict(kind="save", acc="SAVE")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
