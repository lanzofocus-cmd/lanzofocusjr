from kit import build, follow_sub

TITLE = ("THIS IS THE PART YOU'LL", "NEVER GET TO REWATCH")
OUTPUT = "90_This_Is_The_Part_Youll_Never_Get_To_Rewatch_16x9.mp4"
SPEC = [
    ("One day…", "sunrise", dict(acc="ONE DAY…")),
    ("You'll wish you could return to an ordinary moment.", "frame", dict(who="AN ORDINARY MOMENT", acc="RETURN ORDINARY")),
    ("A conversation.", "bubbles", dict(texts=["HOW WAS YOUR DAY?"], acc="CONVERSATION.")),
    ("A day with your family.", "crowd", dict(n=4, acc="FAMILY.")),
    ("A walk.", "path", dict(kind="winding", acc="WALK.")),
    ("A laugh that seemed unimportant.", "bubbles", dict(texts=["HAHA"], inverted=True, acc="LAUGH UNIMPORTANT.")),
    ("A moment when everything wasn't perfect…", "puzzle", dict(missing=True, lbl="NOT PERFECT", acc="WASN'T PERFECT…")),
    ("But life was happening.", "pulse", dict(acc="HAPPENING.")),
    ("And you didn't know it was a memory yet.", "frame", dict(who="A MEMORY, LATER", new="YOU, THEN", acc="MEMORY YET.")),
    ("You were probably thinking about the future.", "map", dict(a_lbl="NOW", b_lbl="THE FUTURE", acc="FUTURE.")),
    ("Waiting for something bigger.", "hourglass", dict(acc="BIGGER.")),
    ("Something more exciting.", "gauge", dict(lbl="EXCITEMENT", start=0.3, end=0.35, acc="EXCITING.")),
    ("Something that would finally make life feel important.", "big", dict(text="SOMEDAY", acc="FINALLY IMPORTANT.")),
    ("But maybe…", "pulse", dict()),
    ("Life was already happening in the moments you kept overlooking.", "dots", dict(connect=True, n=12, acc="ALREADY OVERLOOKING.")),
    ("Not every meaningful moment announces itself.", "chairs", dict(lbl="NO ANNOUNCEMENT", acc="MEANINGFUL ANNOUNCES")),
    ("Some are quiet.", "pulse", dict(acc="QUIET.")),
    ("Some are ordinary.", "big", dict(text="TUESDAY", sub="JUST ANOTHER DAY", acc="ORDINARY.")),
    ("Some disappear before you realize how much they mattered.", "frame", dict(who="GONE", fade=True, acc="DISAPPEAR MATTERED.")),
    ("So don't spend your entire life waiting for the extraordinary…", "hourglass", dict(acc="WAITING EXTRAORDINARY…")),
    ("And miss the life happening around you.", "ring", dict(center_tag="RIGHT NOW", acc="MISS AROUND")),
    ("If someone came to mind while watching this, send them this video.", "cta", dict(kind="share", lbl="SEND IT TO THEM", acc="SEND")),
    ("And if this reminded you to pay attention to your own life…", "compass", dict(lbl="PAY ATTENTION", acc="ATTENTION")),
    ("Save it. You may need to hear it again.", "cta", dict(kind="save", acc="SAVE AGAIN.")),
    ("Follow LanzoFocus for ideas, lessons, and perspectives that challenge the way you think.", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
