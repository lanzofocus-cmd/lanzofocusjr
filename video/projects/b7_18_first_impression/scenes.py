from kit import build, follow_sub, hook

TITLE = ("YOUR FIRST IMPRESSION", "CAN BE WRONG")
OUTPUT = "218_Why_Your_First_Impression_Of_Something_Can_Be_Wrong_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("The first time you try something…", "startline", dict(behind=False, acc="FIRST TRY")),
    ("Your brain immediately forms an opinion.", "brain", dict(says="VERDICT:", acc="IMMEDIATELY OPINION")),
    ("\"This is difficult.\"", "quote", dict(text="THIS IS DIFFICULT.", acc="DIFFICULT")),
    ("\"I'm not good at this.\"", "quote", dict(text="I'M NOT GOOD AT THIS.", acc="GOOD")),
    ("\"I don't like this.\"", "quote", dict(text="I DON'T LIKE THIS.", acc="LIKE")),
    ("\"This isn't for me.\"", "quote", dict(text="THIS ISN'T FOR ME.", acc="ME")),
    ("But first impressions aren't always accurate.", "doc", dict(title="FIRST IMPRESSION", empty=False, stamp="INACCURATE", acc="FIRST IMPRESSIONS ACCURATE")),
    ("Sometimes you're judging a new experience using your lack of experience.", "scale", dict(left="JUDGMENT", right="EXPERIENCE", tip=-1, acc="JUDGING LACK EXPERIENCE")),
    ("The first time you exercise a skill, it feels awkward.", "gauge", dict(lbl="AWKWARD", start=0.2, end=0.85, acc="SKILL AWKWARD")),
    ("The first time you enter a new environment, you feel uncomfortable.", "door", dict(open_=True, lbl="NEW PLACE", acc="ENVIRONMENT UNCOMFORTABLE")),
    ("The first time you learn something complicated, it seems impossible.", "tangle", dict(lbl="COMPLICATED", acc="COMPLICATED IMPOSSIBLE")),
    ("But after repetition…", "loop", dict(items=["TRY", "FAIL", "ADJUST", "AGAIN"], acc="REPETITION")),
    ("Your perspective changes.", "shed", dict(old="DAY 1", new="DAY 30", acc="PERSPECTIVE CHANGES")),
    ("The thing that once felt confusing becomes familiar.", "hud", dict(lbl="FAMILIAR", start=10, end=80, icons=None, crowd=0, acc="CONFUSING FAMILIAR")),
    ("The thing that once felt difficult becomes manageable.", "stairs", dict(n=6, climb=4, acc="DIFFICULT MANAGEABLE")),
    ("The thing you thought you hated may become something you genuinely enjoy.", "hud", dict(lbl="ENJOYMENT", start=5, end=90, icons="heart", acc="HATED ENJOY")),
    ("Give new experiences enough time to become real experiences.", "hourglass", dict(drop=True, acc="TIME REAL EXPERIENCES")),
    ("Don't let your first five minutes decide your opinion of something you haven't properly explored.", "timeline", dict(n=10, progress=0.05, tag="FIRST 5 MINUTES", acc="FIVE MINUTES EXPLORED")),
    ("What is something you initially disliked but eventually grew to enjoy?", "shed", dict(old="DISLIKED", new="LOVE IT", acc="DISLIKED ENJOY")),
    ("Tell us the story.", "cta", dict(kind="comment", lbl="TELL US THE STORY", acc="STORY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="FIRST IMPRESSION", start=50, end=8, lbl2="AFTER 30 DAYS", start2=0, end2=0, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
