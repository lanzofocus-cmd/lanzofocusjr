from kit import build, follow_sub

TITLE = ("THE MOMENT YOU REALIZE YOU'VE", "BEEN WAITING FOR YOURSELF")
OUTPUT = "130_Youve_Been_Waiting_For_Yourself_16x9.mp4"
SPEC = [
    ("You keep waiting for someone to encourage you.", "crowd", dict(n=7, dim=True, acc="WAITING ENCOURAGE")),
    ("Someone to recognize your potential.", "iceberg", dict(top="WHAT THEY SEE", bottom="YOUR POTENTIAL", acc="RECOGNIZE POTENTIAL.")),
    ("Someone to tell you that you can do it.", "bubbles", dict(texts=["YOU CAN DO IT."], inverted=True, acc="CAN")),
    ("Someone to make you feel ready.", "progress", dict(lbl="READY", value=0.3, acc="READY.")),
    ("But what if…", "pulse", dict()),
    ("You've been waiting for a voice that you could become?", "mirror", dict(reflect="solid", lbl="THE VOICE", acc="VOICE BECOME?")),
    ("The voice that says…", "pulse", dict(acc="VOICE")),
    ("\"Let's try.\"", "quote", dict(text="LET'S TRY.", acc="TRY.\"")),
    ("\"Let's learn.\"", "quote", dict(text="LET'S LEARN.", acc="LEARN.\"")),
    ("\"Let's see what happens.\"", "quote", dict(text="LET'S SEE WHAT HAPPENS.", acc="SEE")),
    ("Not because success is guaranteed.", "doc", dict(title="GUARANTEE", empty=True, stamp="NONE", acc="NOT GUARANTEED.")),
    ("But because your curiosity deserves an opportunity.", "door", dict(open_=True, lbl="CURIOSITY", acc="CURIOSITY DESERVES OPPORTUNITY.")),
    ("You don't always need someone else to believe in you before you begin believing that you're worth the effort.", "crown", dict(lbl="WORTH IT", acc="BELIEVE WORTH EFFORT.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
