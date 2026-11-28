from kit import build, follow_sub, hook

TITLE = ("BECOMING SOMEONE YOU", "DON'T RECOGNIZE")
OUTPUT = "201_The_Danger_Of_Becoming_Someone_You_Dont_Recognize_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Have you ever looked at someone else's life and thought, \"I want that\"?", "phone", dict(lbl="I WANT THAT", acc="SOMEONE ELSE'S WANT")),
    ("Their confidence.", "list", dict(items=["CONFIDENCE"], mode="tag", tag="THEIRS", acc="CONFIDENCE")),
    ("Their lifestyle.", "list", dict(items=["CONFIDENCE", "LIFESTYLE"], mode="tag", tag="THEIRS", acc="LIFESTYLE")),
    ("Their success.", "list", dict(items=["CONFIDENCE", "LIFESTYLE", "SUCCESS"], mode="tag", tag="THEIRS", acc="SUCCESS")),
    ("Their personality.", "list", dict(items=["CONFIDENCE", "LIFESTYLE", "SUCCESS", "PERSONALITY"], mode="tag", tag="THEIRS", acc="PERSONALITY")),
    ("Their reputation.", "list", dict(items=["CONFIDENCE", "LIFESTYLE", "SUCCESS", "PERSONALITY", "REPUTATION"], mode="tag", tag="THEIRS", acc="REPUTATION")),
    ("You begin copying the things you admire.", "mirror", dict(reflect="dashed", lbl="COPY", acc="COPYING ADMIRE")),
    ("At first, it seems harmless.", "gauge", dict(lbl="HARMLESS?", start=0.1, end=0.2, acc="HARMLESS")),
    ("You adopt their habits. Their way of speaking. Their opinions. Their goals.", "sticker", dict(tags=["THEIR HABITS", "THEIR WORDS", "THEIR OPINIONS", "THEIR GOALS"], acc="HABITS SPEAKING OPINIONS GOALS")),
    ("But eventually, you might become so focused on becoming someone impressive…", "stage", dict(lbl="IMPRESSIVE", acc="IMPRESSIVE")),
    ("That you forget to ask whether you're becoming someone you actually like.", "mirror", dict(reflect="dashed", lbl="DO YOU LIKE THEM?", drop=True, acc="BECOMING ACTUALLY LIKE")),
    ("There's a difference between being inspired by someone and trying to replace yourself with them.", "scale", dict(left="INSPIRED", right="REPLACED", tip=0, acc="INSPIRED REPLACE")),
    ("Inspiration gives you ideas.", "brain", dict(says="NEW IDEA!", acc="INSPIRATION IDEAS")),
    ("Imitation can make you abandon your own.", "frame", dict(who="YOUR OWN IDEAS", fade=True, acc="IMITATION ABANDON")),
    ("Maybe you don't enjoy the things you're pretending to enjoy.", "stage", dict(lbl="PRETENDING", acc="PRETENDING ENJOY")),
    ("Maybe the goal you're chasing only looks attractive because someone else achieved it.", "crown", dict(lbl="THEIR GOAL", acc="CHASING SOMEONE ELSE")),
    ("Maybe you're trying to build a life that would impress people who don't even know what makes you happy.", "crowd", dict(n=7, dim=True, acc="IMPRESS HAPPY")),
    ("Take inspiration from others.", "network", dict(nodes=["MENTOR", "FRIEND", "AUTHOR", "COACH"], tangled=False, acc="INSPIRATION")),
    ("Learn from them.", "book", dict(chapter="LESSONS", acc="LEARN")),
    ("Study what they do well.", "list", dict(items=["WHAT THEY DO WELL"], mode="check", acc="STUDY WELL")),
    ("But don't disappear inside someone else's identity.", "frame", dict(who="YOU?", dashed_fig=True, acc="DISAPPEAR IDENTITY")),
    ("You don't have to become a copy to become better.", "shed", dict(old="A COPY", new="A BETTER YOU", acc="COPY BETTER")),
    ("You can improve your own life without abandoning who you are.", "plant", dict(height=0.6, roots=True, lbl="STILL YOU", acc="IMPROVE WHO")),
    ("Have you ever realized you were trying to become someone else instead of improving yourself?", "mirror", dict(reflect="solid", lbl="YOURSELF", acc="SOMEONE ELSE IMPROVING")),
    ("Share what made you notice.", "cta", dict(kind="comment", lbl="WHAT MADE YOU NOTICE", acc="NOTICE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="LIKE THEM", start=10, end=96, lbl2="LIKE YOURSELF", start2=90, end2=8, icons="heart", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
