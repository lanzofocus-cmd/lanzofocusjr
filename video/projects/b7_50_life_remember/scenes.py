from kit import build, follow_sub, hook

TITLE = ("THE LIFE YOU", "WILL REMEMBER")
OUTPUT = "250_The_Life_You_Will_Remember_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine looking back on your life years from now.", "timeline", dict(n=12, progress=0.9, tag="YEARS FROM NOW", acc="LOOKING BACK")),
    ("What do you think you'll remember?", "brain", dict(says="WHAT STAYED?", acc="REMEMBER")),
    ("Will it be every notification?", "notifs", dict(acc="NOTIFICATION")),
    ("Every argument online?", "bubbles", dict(texts=["YOU'RE WRONG!", "NO, YOU ARE!"], acc="ARGUMENT")),
    ("Every time you compared yourself to someone?", "timeline", dict(compare=True, acc="COMPARED")),
    ("Every day you spent worrying about what people thought?", "crowd", dict(n=7, dim=True, acc="WORRYING THOUGHT")),
    ("Probably not.", "list", dict(items=["NOTIFICATIONS", "ARGUMENTS", "COMPARISONS", "WORRIES"], mode="strike", acc="NOT")),
    ("You'll remember certain people.", "crowd", dict(n=5, highlight=2, highlight_label="THEM", acc="PEOPLE")),
    ("Certain conversations.", "bubbles", dict(texts=["REMEMBER THAT NIGHT?"], acc="CONVERSATIONS")),
    ("Certain experiences.", "frame", dict(who="THAT SUMMER", acc="EXPERIENCES")),
    ("Certain moments that seemed ordinary when they happened.", "frame", dict(who="AN ORDINARY DAY", new="YOU, LATER", acc="ORDINARY")),
    ("The laughter.", "list", dict(items=["THE LAUGHTER"], mode="check", acc="LAUGHTER")),
    ("The things you learned.", "list", dict(items=["THE LAUGHTER", "WHAT YOU LEARNED"], mode="check", acc="LEARNED")),
    ("The times you tried something new.", "list", dict(items=["THE LAUGHTER", "WHAT YOU LEARNED", "TRYING NEW THINGS"], mode="check", acc="TRIED NEW")),
    ("The times you were there for someone.", "list", dict(items=["THE LAUGHTER", "WHAT YOU LEARNED", "TRYING NEW THINGS", "BEING THERE"], mode="check", acc="THERE")),
    ("The moments you finally understood something important.", "list", dict(items=["THE LAUGHTER", "WHAT YOU LEARNED", "TRYING NEW THINGS", "BEING THERE", "UNDERSTANDING"], mode="check", acc="UNDERSTOOD IMPORTANT")),
    ("And that should make you think about how you're spending your attention today.", "hourglass", dict(acc="ATTENTION TODAY")),
    ("Because the future memories of your life are being created in moments you're currently living.", "pulse", dict(drop=True, acc="MEMORIES CREATED CURRENTLY LIVING")),
    ("Don't spend all your time preparing to live.", "list", dict(items=["PREPARING TO LIVE"], mode="strike", acc="PREPARING LIVE")),
    ("Don't spend all your attention watching someone else's life.", "phone", dict(lbl="SOMEONE ELSE'S LIFE", acc="WATCHING SOMEONE ELSE'S")),
    ("Don't wait for every condition to become perfect.", "hourglass", dict(acc="WAIT PERFECT")),
    ("Make plans.", "list", dict(items=["MAKE PLANS"], mode="check", acc="PLANS")),
    ("Work toward goals.", "list", dict(items=["MAKE PLANS", "WORK TOWARD GOALS"], mode="check", acc="GOALS")),
    ("Learn.", "list", dict(items=["MAKE PLANS", "WORK TOWARD GOALS", "LEARN"], mode="check", acc="LEARN")),
    ("Improve.", "list", dict(items=["MAKE PLANS", "WORK TOWARD GOALS", "LEARN", "IMPROVE"], mode="check", acc="IMPROVE")),
    ("But also participate in the life that's already happening around you.", "ring", dict(tags=["FRIENDS", "FAMILY", "TODAY", "THIS MOMENT"], acc="PARTICIPATE ALREADY HAPPENING")),
    ("Because one day…", "sunrise", dict(acc="ONE DAY")),
    ("These ordinary moments will become memories.", "frame", dict(who="THIS MOMENT", fade=True, acc="ORDINARY MEMORIES")),
    ("And you won't be able to return to them.", "door", dict(closing=True, lbl="NO RETURN", acc="RETURN")),
    ("What is one thing you want to make more memories doing?", "cta", dict(kind="comment", lbl="MORE MEMORIES DOING...", acc="MEMORIES")),
    ("Share it below, and follow LanzoFocus for ideas, lessons, and perspectives that remind you to live deliberately, think deeply, and keep growing.", "follow"),
]
_HOOK = ("hud", dict(lbl="TIME ON YOUR PHONE", start=10, end=92, lbl2="MEMORIES MADE", start2=60, end2=8, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
