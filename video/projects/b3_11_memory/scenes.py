from kit import build, follow_sub

TITLE = ("YOUR MEMORY ISN'T ALWAYS", "TELLING THE TRUTH")
OUTPUT = "51_Your_Memory_Isnt_Always_Telling_The_Truth_16x9.mp4"
SPEC = [
    ("You remember the past…", "frame", dict(who="THE PAST", acc="REMEMBER PAST…")),
    ("But that doesn't mean you're remembering it accurately.", "frame", dict(who="ACCURATE?", dashed_fig=True, acc="DOESN'T ACCURATELY.")),
    ("Your mind can make embarrassing moments feel bigger.", "stage", dict(lbl="EMBARRASSING", performing=False, acc="EMBARRASSING BIGGER.")),
    ("Make old failures feel more permanent.", "sticker", dict(tags=["FAILURE"], acc="PERMANENT.")),
    ("Make difficult periods feel like they lasted forever.", "hourglass", dict(acc="FOREVER.")),
    ("And sometimes…", "pulse", dict()),
    ("It can make the past seem better than it actually was.", "frame", dict(who="THE GOOD OLD DAYS?", acc="BETTER ACTUALLY")),
    ("You might be remembering a person…", "frame", dict(who="A PERSON", acc="PERSON…")),
    ("A place…", "map", dict(a_lbl="THAT PLACE", b_lbl="", acc="PLACE…")),
    ("Or a time in your life…", "timeline", dict(n=10, progress=0.4, tag="THAT TIME", acc="TIME")),
    ("Through the feelings you have today.", "brain", dict(says="HOW I FEEL NOW", acc="FEELINGS TODAY.")),
    ("Your memories are real experiences.", "list", dict(items=["IT HAPPENED"], mode="check", acc="REAL")),
    ("But the interpretation you attach to them can change.", "arrows", dict(items=["THE MEANING"], acc="INTERPRETATION CHANGE.")),
    ("So when your mind says…", "brain", dict(acc="MIND")),
    ("\"Everything used to be better.\"", "quote", dict(text="IT USED TO BE BETTER.", acc="BETTER.\"")),
    ("\"Everyone remembers that mistake.\"", "quote", dict(text="EVERYONE REMEMBERS.", acc="EVERYONE REMEMBERS")),
    ("\"I've always been like this.\"", "quote", dict(text="I'VE ALWAYS BEEN LIKE THIS.", acc="ALWAYS")),
    ("Pause.", "pulse", dict(acc="PAUSE.")),
    ("Your memory is a story about your past.", "book", dict(chapter="THE PAST", acc="STORY PAST.")),
    ("It is not a prediction of your future.", "doc", dict(title="FUTURE", empty=True, stamp="NOT PREDICTED", acc="NOT PREDICTION FUTURE.")),
    ("Save this for the next time your past starts defining your present.", "cta", dict(kind="save", acc="SAVE DEFINING")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
