from kit import build, follow_sub, hook

TITLE = ("WHY SOME PEOPLE", "NEVER FEEL SATISFIED")
OUTPUT = "198_Why_Some_People_Never_Feel_Satisfied_16x9.mp4"
MUSIC = "vyzee"
SPEC = [
    ("Imagine reaching a goal you've spent months working toward.", "stairs", dict(n=6, climb=6, acc="GOAL MONTHS")),
    ("You finally achieve it.", "crown", dict(lbl="ACHIEVED", acc="ACHIEVE")),
    ("You feel proud.", "hud", dict(lbl="SATISFACTION", start=20, end=100, icons="heart", crowd=4, acc="PROUD")),
    ("You celebrate.", "stage", dict(lbl="CELEBRATE", acc="CELEBRATE")),
    ("And then…", "pulse", dict(acc="")),
    ("A few days later, your mind moves to the next thing.", "hud", dict(lbl="SATISFACTION", start=100, end=30, icons=None, crowd=0, tag="3 DAYS LATER", acc="NEXT THING")),
    ("The next goal.", "list", dict(items=["NEXT GOAL"], mode="empty", acc="GOAL")),
    ("The next achievement.", "list", dict(items=["NEXT GOAL", "NEXT ACHIEVEMENT"], mode="empty", acc="ACHIEVEMENT")),
    ("The next level.", "list", dict(items=["NEXT GOAL", "NEXT ACHIEVEMENT", "NEXT LEVEL"], mode="empty", acc="LEVEL")),
    ("And suddenly, the thing you once desperately wanted becomes normal.", "frame", dict(who="ONCE A DREAM", fade=True, acc="DESPERATELY NORMAL")),
    ("This happens because humans are remarkably good at adapting.", "brain", dict(says="THIS IS NORMAL NOW.", acc="ADAPTING")),
    ("The exciting thing becomes familiar.", "gauge", dict(lbl="EXCITEMENT", start=0.9, end=0.25, acc="EXCITING FAMILIAR")),
    ("The new achievement becomes part of your everyday life.", "bricks", dict(rows=3, lbl="EVERYDAY", uneven=False, acc="EVERYDAY")),
    ("And your mind begins searching for something else to chase.", "compass", dict(lbl="SOMETHING ELSE", settle=False, acc="SEARCHING CHASE")),
    ("There's nothing wrong with having ambition.", "list", dict(items=["AMBITION"], mode="check", acc="AMBITION")),
    ("Wanting to improve is a good thing.", "chart", dict(kind="up", lbl="IMPROVE", acc="IMPROVE GOOD")),
    ("But if you never pause to appreciate what you've accomplished…", "hourglass", dict(acc="PAUSE APPRECIATE")),
    ("You create a life where the finish line is constantly moving.", "stairs", dict(n=9, climb=6, highlight=8, acc="FINISH CONSTANTLY MOVING")),
    ("You reach something.", "crown", dict(lbl="REACHED", acc="REACH")),
    ("Then immediately decide it isn't enough.", "progress", dict(lbl="ENOUGH?", value=0.3, acc="ENOUGH")),
    ("You improve.", "chart", dict(kind="up", lbl="YOU", acc="IMPROVE")),
    ("Then immediately focus on what's missing.", "puzzle", dict(missing=True, lbl="WHAT'S MISSING", acc="MISSING")),
    ("And eventually, you can become so focused on your next achievement…", "arrows", dict(items=["NEXT", "NEXT", "NEXT"], acc="FOCUSED NEXT")),
    ("That you forget to experience the one you just earned.", "frame", dict(who="WHAT YOU EARNED", dashed_fig=True, acc="FORGET EARNED")),
    ("Ambition should help you move forward.", "path", dict(kind="straight", acc="AMBITION FORWARD")),
    ("It shouldn't make you incapable of appreciating the present.", "sunrise", dict(acc="APPRECIATING PRESENT")),
    ("You can want more…", "stairs", dict(drop=True, n=7, climb=4, acc="MORE")),
    ("Without treating what you already have as worthless.", "receipt", dict(items=[("WHAT YOU HAVE", "PRICELESS")], total="NOT WORTHLESS", acc="ALREADY WORTHLESS")),
    ("What's something you worked hard for that you didn't appreciate enough after achieving it?", "frame", dict(who="IT", new="YOU, LATER", acc="WORKED APPRECIATE")),
    ("Share it.", "cta", dict(kind="comment", lbl="SHARE IT", acc="SHARE")),
    ("Maybe someone else is currently living the moment you once dreamed of.", "crowd", dict(n=7, highlight=5, highlight_label="DREAMING OF IT", acc="LIVING DREAMED")),
    ("", "follow"),
]
_HOOK = ("stairs", dict(n=9, climb=6, highlight=8))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
