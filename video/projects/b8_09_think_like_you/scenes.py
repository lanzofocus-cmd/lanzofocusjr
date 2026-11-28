from kit import build, follow_sub, hook

TITLE = ("STOP EXPECTING EVERYONE", "TO THINK LIKE YOU")
OUTPUT = "259_Why_You_Should_Stop_Expecting_Everyone_To_Think_Like_You_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("One of the biggest sources of frustration in life…", "gauge", dict(lbl="FRUSTRATION", start=0.1, end=0.8, acc="FRUSTRATION")),
    ("Is expecting other people to think the way you do.", "mirror", dict(reflect="solid", lbl="LIKE ME?", acc="EXPECTING THINK")),
    ("You assume they understand your intentions.", "list", dict(items=["THEY GET MY INTENTIONS"], mode="tag", tag="ASSUMED", acc="INTENTIONS")),
    ("You assume they value the same things.", "list", dict(items=["THEY GET MY INTENTIONS", "SAME VALUES"], mode="tag", tag="ASSUMED", acc="VALUE SAME")),
    ("You assume they would make the same decision.", "list", dict(items=["THEY GET MY INTENTIONS", "SAME VALUES", "SAME DECISION"], mode="tag", tag="ASSUMED", acc="DECISION")),
    ("You assume they see the situation the way you see it.", "list", dict(items=["THEY GET MY INTENTIONS", "SAME VALUES", "SAME DECISION", "SAME VIEW"], mode="tag", tag="ASSUMED", acc="SITUATION")),
    ("Then they behave differently.", "path", dict(kind="fork", labels=("YOU", "THEM"), walker=False, acc="DIFFERENTLY")),
    ("And you're confused.", "question", dict(a_lbl="WHY WOULD", b_lbl="THEY DO THAT?", acc="CONFUSED")),
    ("But people have different experiences.", "list", dict(items=["EXPERIENCES"], mode="tag", tag="DIFFERENT", acc="EXPERIENCES")),
    ("Different priorities.", "list", dict(items=["EXPERIENCES", "PRIORITIES"], mode="tag", tag="DIFFERENT", acc="PRIORITIES")),
    ("Different personalities.", "list", dict(items=["EXPERIENCES", "PRIORITIES", "PERSONALITIES"], mode="tag", tag="DIFFERENT", acc="PERSONALITIES")),
    ("Different fears.", "list", dict(items=["EXPERIENCES", "PRIORITIES", "PERSONALITIES", "FEARS"], mode="tag", tag="DIFFERENT", acc="FEARS")),
    ("Different ways of interpreting information.", "list", dict(items=["EXPERIENCES", "PRIORITIES", "PERSONALITIES", "FEARS", "INTERPRETATIONS"], mode="tag", tag="DIFFERENT", acc="INTERPRETING")),
    ("Two people can look at the same situation…", "iceberg", dict(top="SAME SITUATION", bottom="TWO DIFFERENT STORIES", acc="SAME SITUATION")),
    ("And genuinely reach different conclusions.", "path", dict(kind="fork", labels=("CONCLUSION A", "CONCLUSION B"), acc="GENUINELY CONCLUSIONS")),
    ("This doesn't mean every opinion is equally correct.", "list", dict(items=["ALL EQUALLY CORRECT"], mode="strike", acc="EQUALLY CORRECT")),
    ("It doesn't mean you should accept harmful behavior.", "shield", dict(front="BOUNDARIES", back="YOU", acc="HARMFUL")),
    ("It means you should stop assuming your perspective is the only perspective someone could reasonably have.", "network", dict(nodes=["YOUR VIEW", "THEIR VIEW", "ANOTHER VIEW", "AND ANOTHER"], tangled=False, drop=True, acc="ASSUMING ONLY PERSPECTIVE")),
    ("Understanding another person's reasoning doesn't require agreeing with it.", "scale", dict(left="UNDERSTAND", right="AGREE", tip=0, acc="UNDERSTANDING AGREEING")),
    ("Sometimes the best conversations begin when you stop trying to force someone to see the world exactly as you do.", "bubbles", dict(texts=["HELP ME SEE IT YOUR WAY."], acc="BEST CONVERSATIONS FORCE")),
    ("What's something you've learned from someone whose perspective was completely different from yours?", "cta", dict(kind="comment", lbl="WHAT THEY TAUGHT YOU", acc="LEARNED PERSPECTIVE DIFFERENT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PEOPLE WHO THINK LIKE YOU", start=100, end=4, icons="q", tag="REALITY CHECK", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
