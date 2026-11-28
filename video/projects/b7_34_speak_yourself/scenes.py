from kit import build, follow_sub, hook

TITLE = ("THE WAY YOU SPEAK", "TO YOURSELF")
OUTPUT = "234_Why_The_Way_You_Speak_To_Yourself_Matters_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine someone following you around all day…", "path", dict(kind="straight", acc="FOLLOWING")),
    ("And constantly saying:", "bubbles", dict(texts=["..."], acc="CONSTANTLY")),
    ("\"You're stupid.\"", "quote", dict(text="YOU'RE STUPID.", acc="STUPID")),
    ("\"You can't do this.\"", "quote", dict(text="YOU CAN'T DO THIS.", acc="CAN'T")),
    ("\"You always fail.\"", "quote", dict(text="YOU ALWAYS FAIL.", acc="FAIL")),
    ("\"You're not good enough.\"", "quote", dict(text="YOU'RE NOT GOOD ENOUGH.", acc="ENOUGH")),
    ("\"Why even try?\"", "quote", dict(text="WHY EVEN TRY?", acc="TRY")),
    ("How long would you want to spend around that person?", "hourglass", dict(acc="HOW LONG")),
    ("Now imagine that voice is your own.", "mirror", dict(reflect="solid", lbl="THE VOICE", drop=True, acc="VOICE OWN")),
    ("You might think you're motivating yourself through criticism.", "gauge", dict(lbl="CRITICISM", start=0.3, end=0.9, acc="MOTIVATING CRITICISM")),
    ("But constantly attacking yourself doesn't automatically create improvement.", "chart", dict(kind="flat", lbl="IMPROVEMENT", acc="ATTACKING IMPROVEMENT")),
    ("It can make mistakes feel dangerous.", "gauge", dict(lbl="FEAR OF MISTAKES", start=0.2, end=0.85, acc="DANGEROUS")),
    ("It can make learning uncomfortable.", "book", dict(chapter="LEARNING", text="DREAD", acc="LEARNING UNCOMFORTABLE")),
    ("It can make you afraid to attempt something new.", "door", dict(closing=True, lbl="SOMETHING NEW", acc="AFRAID ATTEMPT")),
    ("You can hold yourself accountable without insulting yourself.", "scale", dict(left="ACCOUNTABLE", right="INSULTING", tip=-1, acc="ACCOUNTABLE INSULTING")),
    ("You can recognize mistakes without turning them into personal attacks.", "shield", dict(front="IT WAS A MISTAKE", back="YOU", acc="RECOGNIZE PERSONAL ATTACKS")),
    ("You can say:", "pulse", dict(acc="")),
    ("\"I made a mistake.\"", "quote", dict(text="I MADE A MISTAKE.", acc="MADE")),
    ("Instead of:", "arrows", dict(items=["INSTEAD OF"], acc="")),
    ("\"I'm a mistake.\"", "list", dict(items=["I'M A MISTAKE."], mode="strike", acc="I'M")),
    ("The difference isn't about pretending everything is fine.", "list", dict(items=["PRETEND IT'S FINE"], mode="strike", acc="PRETENDING FINE")),
    ("It's about creating a mindset where improvement is possible.", "plant", dict(height=0.6, roots=True, lbl="ROOM TO GROW", acc="MINDSET IMPROVEMENT POSSIBLE")),
    ("Save this if you need a reminder that accountability doesn't require self-insult.", "cta", dict(kind="save", lbl="BE ACCOUNTABLE, NOT CRUEL", acc="SAVE ACCOUNTABILITY SELF-INSULT")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="SELF-CRITICISM", start=10, end=97, lbl2="SELF-BELIEF", start2=80, end2=6, icons="thumbdown", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
