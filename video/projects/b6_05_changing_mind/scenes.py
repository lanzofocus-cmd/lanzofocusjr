from kit import build, follow_sub, hook

TITLE = ("THE POWER OF", "CHANGING YOUR MIND")
OUTPUT = "195_The_Power_Of_Changing_Your_Mind_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Most people say they want to become smarter.", "brain", dict(says="I WANT TO", says2="BE SMARTER.", acc="SMARTER")),
    ("But there's a hidden requirement.", "lock", dict(lbl="HIDDEN", acc="HIDDEN REQUIREMENT")),
    ("You have to be willing to discover that you were wrong.", "quote", dict(text="I WAS WRONG.", acc="WILLING WRONG")),
    ("And that's harder than it sounds.", "gauge", dict(lbl="DIFFICULTY", start=0.2, end=0.85, acc="HARDER")),
    ("Because opinions aren't always just opinions.", "bubbles", dict(texts=["I THINK..."], acc="OPINIONS")),
    ("Sometimes they're connected to your identity.", "sticker", dict(tags=["MY OPINION", "WHO I AM"], acc="CONNECTED IDENTITY")),
    ("You believe something.", "sticker", dict(tags=["I BELIEVE"], acc="BELIEVE")),
    ("You defend it.", "shield", dict(front="MY BELIEF", back="ME", acc="DEFEND")),
    ("You tell people about it.", "crowd", dict(n=7, highlight=3, highlight_label="I'M SURE", acc="TELL")),
    ("You build your reputation around it.", "bricks", dict(rows=4, lbl="REPUTATION", uneven=False, acc="REPUTATION")),
    ("Then new information appears.", "doc", dict(title="NEW INFO", empty=False, acc="NEW INFORMATION")),
    ("And instead of examining it…", "question", dict(a_lbl="EXAMINE", b_lbl="IT?", acc="EXAMINING")),
    ("You immediately look for reasons to reject it.", "doc", dict(title="NEW INFO", empty=False, stamp="REJECTED", acc="IMMEDIATELY REJECT")),
    ("Not because the information is incorrect.", "list", dict(items=["INCORRECT"], mode="strike", acc="INCORRECT")),
    ("But because accepting it would mean admitting that your previous understanding was incomplete.", "puzzle", dict(missing=True, lbl="INCOMPLETE", acc="ADMITTING INCOMPLETE")),
    ("But think about the smartest people you've ever met.", "crowd", dict(n=5, highlight=2, highlight_label="THE SMARTEST", acc="SMARTEST")),
    ("Are they the people who never change their minds?", "lock", dict(lbl="NEVER CHANGE", acc="NEVER CHANGE")),
    ("Or the people who can listen carefully, examine evidence, and adjust their beliefs when necessary?", "list", dict(items=["LISTEN", "EXAMINE", "ADJUST"], mode="check", acc="LISTEN EXAMINE ADJUST")),
    ("Changing your mind doesn't automatically mean you were weak.", "list", dict(items=["WEAK"], mode="strike", acc="CHANGING WEAK")),
    ("It may mean you're finally strong enough to prioritize truth over your ego.", "hud", dict(lbl="TRUTH", start=30, end=95, lbl2="EGO", start2=90, end2=15, icons=None, crowd=0, acc="STRONG TRUTH EGO")),
    ("You don't have to defend every opinion you have.", "shield", dict(front="EVERY OPINION", back="?", acc="DEFEND EVERY")),
    ("You don't have to protect every old version of your thinking.", "shed", dict(old="OLD THINKING", new="NEW THINKING", acc="PROTECT OLD")),
    ("You are allowed to say:", "pulse", dict(acc="ALLOWED")),
    ("\"I didn't understand that before.\"", "quote", dict(text="I DIDN'T UNDERSTAND THAT BEFORE.", acc="UNDERSTAND")),
    ("\"I was wrong.\"", "quote", dict(text="I WAS WRONG.", acc="WRONG")),
    ("\"I see it differently now.\"", "quote", dict(text="I SEE IT DIFFERENTLY NOW.", acc="DIFFERENTLY")),
    ("Those sentences aren't signs of weakness.", "list", dict(items=["WEAKNESS"], mode="strike", acc="WEAKNESS")),
    ("They're signs that your mind is still working.", "brain", dict(says="STILL LEARNING.", acc="MIND WORKING")),
    ("What's an opinion you completely changed as you got older?", "shed", dict(old="THEN", new="NOW", acc="OPINION CHANGED OLDER")),
    ("Comment it.", "cta", dict(kind="comment", lbl="AN OPINION YOU CHANGED", acc="COMMENT")),
    ("Those conversations can be more valuable than arguments.", "scale", dict(left="CONVERSATION", right="ARGUMENT", tip=-1, acc="CONVERSATIONS VALUABLE ARGUMENTS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="BEING RIGHT", start=100, end=20, lbl2="LEARNING", start2=10, end2=96, icons="q", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
