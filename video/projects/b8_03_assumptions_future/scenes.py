from kit import build, follow_sub, hook

TITLE = ("ASSUMPTIONS ABOUT", "YOUR FUTURE")
OUTPUT = "253_The_Problem_With_Making_Assumptions_About_Your_Future_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever decided you probably wouldn't succeed at something…", "doc", dict(title="PREDICTION", empty=False, stamp="FAIL", acc="DECIDED SUCCEED")),
    ("Before you even tried?", "startline", dict(behind=True, acc="BEFORE TRIED")),
    ("Maybe you thought you weren't talented enough.", "sticker", dict(tags=["NOT TALENTED"], acc="TALENTED")),
    ("Maybe you believed someone else would be better.", "crowd", dict(n=5, highlight=1, highlight_label="BETTER?", acc="BETTER")),
    ("Maybe you assumed the opportunity was impossible.", "lock", dict(lbl="IMPOSSIBLE?", acc="IMPOSSIBLE")),
    ("Maybe you told yourself you would probably fail.", "quote", dict(text="I'LL PROBABLY FAIL.", acc="FAIL")),
    ("And because you believed that prediction…", "brain", dict(says="I KNOW HOW", says2="THIS ENDS.", acc="PREDICTION")),
    ("You never gave yourself enough evidence to prove whether it was true.", "doc", dict(title="EVIDENCE", empty=True, acc="NEVER EVIDENCE TRUE")),
    ("This is a dangerous habit.", "gauge", dict(lbl="DANGER", start=0.2, end=0.8, acc="DANGEROUS")),
    ("Because your brain is capable of predicting failure based on incomplete information.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="PREDICTING INCOMPLETE")),
    ("You haven't learned the skill.", "progress", dict(lbl="SKILL", value=0.05, acc="LEARNED")),
    ("Therefore, you assume you can't learn it.", "lock", dict(lbl="CAN'T LEARN?", acc="ASSUME CAN'T")),
    ("You haven't experienced the opportunity.", "door", dict(open_=False, lbl="UNOPENED", acc="EXPERIENCED")),
    ("Therefore, you assume it isn't for you.", "sticker", dict(tags=["NOT FOR ME"], acc="ISN'T")),
    ("You haven't tried the challenge.", "stairs", dict(n=6, climb=0, acc="TRIED")),
    ("Therefore, you assume it's beyond your ability.", "hud", dict(lbl="YOUR ABILITY", start=20, end=20, icons=None, crowd=0, tag="ASSUMED", acc="BEYOND ABILITY")),
    ("But predictions aren't facts.", "doc", dict(title="PREDICTION", empty=False, stamp="NOT A FACT", acc="PREDICTIONS FACTS")),
    ("Your current ability is not a complete measurement of your future ability.", "chart", dict(kind="up", lbl="YOUR ABILITY", drop=True, acc="CURRENT COMPLETE FUTURE")),
    ("Your current circumstances are not a permanent forecast.", "fog", dict(lbl="FORECAST", acc="CIRCUMSTANCES PERMANENT")),
    ("And your lack of experience isn't evidence that you're incapable.", "list", dict(items=["NO EXPERIENCE = INCAPABLE"], mode="strike", acc="EXPERIENCE INCAPABLE")),
    ("You don't need to guarantee success before trying something.", "list", dict(items=["GUARANTEE FIRST"], mode="strike", acc="GUARANTEE TRYING")),
    ("You simply need to stop pretending that you already know the outcome.", "question", dict(a_lbl="THE", b_lbl="OUTCOME", acc="PRETENDING OUTCOME")),
    ("Sometimes the future is uncertain because you haven't created enough evidence yet.", "bricks", dict(rows=3, lbl="EVIDENCE, BRICK BY BRICK", uneven=True, acc="UNCERTAIN CREATED EVIDENCE")),
    ("What's something you used to believe you couldn't do, but later discovered was possible?", "shed", dict(old="COULDN'T", new="DID IT", acc="BELIEVE POSSIBLE")),
    ("Tell us your story.", "cta", dict(kind="comment", lbl="YOUR STORY", acc="STORY")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="PREDICTED FAILURE", start=10, end=95, lbl2="ATTEMPTS MADE", start2=0, end2=0, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
