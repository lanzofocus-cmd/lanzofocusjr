from kit import build, follow_sub

TITLE = ("WHY THE BEGINNING", "FEELS SO EXCITING")
OUTPUT = "115_Why_The_Beginning_Feels_So_Exciting_16x9.mp4"
SPEC = [
    ("The beginning of something feels exciting…", "sunrise", dict(acc="BEGINNING EXCITING…")),
    ("Because everything is possible.", "network", dict(nodes=["POSSIBLE", "POSSIBLE", "POSSIBLE", "POSSIBLE", "POSSIBLE"], tangled=False, acc="EVERYTHING POSSIBLE.")),
    ("You haven't experienced the difficult parts yet.", "path", dict(kind="dashed", fog=True, acc="DIFFICULT YET.")),
    ("You haven't encountered the repetitive work.", "timeline", dict(n=10, progress=0.05, acc="REPETITIVE WORK.")),
    ("You haven't discovered all the obstacles.", "iceberg", dict(top="WHAT YOU SEE", bottom="THE OBSTACLES", acc="OBSTACLES.")),
    ("But eventually…", "pulse", dict()),
    ("The fantasy becomes reality.", "frame", dict(who="THE FANTASY", dashed_fig=True, fade=True, acc="FANTASY REALITY.")),
    ("And reality requires effort.", "stairs", dict(n=6, climb=2, acc="REALITY EFFORT.")),
    ("This is where your relationship with the goal becomes important.", "compass", dict(lbl="THE GOAL", acc="RELATIONSHIP GOAL")),
    ("Do you want the idea of achieving it…", "frame", dict(who="THE IDEA", acc="IDEA")),
    ("Or do you actually want the process required?", "bricks", dict(rows=4, lbl="THE PROCESS", uneven=False, acc="PROCESS")),
    ("Because those are two different things.", "scale", dict(left="THE IDEA", right="THE PROCESS", tip=0, acc="TWO DIFFERENT")),
    ("Before committing to a dream…", "doc", dict(title="COMMITMENT", empty=False, acc="COMMITTING DREAM…")),
    ("Make sure you want more than its exciting beginning.", "timeline", dict(n=10, progress=0.6, tag="THE MIDDLE", acc="MORE EXCITING BEGINNING.")),
    ("", "follow"),
]
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
