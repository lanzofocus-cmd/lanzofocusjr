from kit import build, follow_sub, hook

TITLE = ("THE LIFE YOU", "DIDN'T PLAN")
OUTPUT = "200_The_Life_You_Didnt_Plan_16x9.mp4"
MUSIC = "vyzee"
SPEC = [
    ("Nobody can plan their entire life accurately.", "doc", dict(title="LIFE PLAN", empty=False, stamp="APPROXIMATE", acc="NOBODY ENTIRE ACCURATELY")),
    ("You can create goals.", "list", dict(items=["GOALS"], mode="check", acc="GOALS")),
    ("Make schedules.", "list", dict(items=["GOALS", "SCHEDULES"], mode="check", acc="SCHEDULES")),
    ("Build expectations.", "list", dict(items=["GOALS", "SCHEDULES", "EXPECTATIONS"], mode="check", acc="EXPECTATIONS")),
    ("Imagine exactly where you'll be in five years.", "map", dict(a_lbl="NOW", b_lbl="5 YEARS", acc="EXACTLY FIVE YEARS")),
    ("But life has a way of introducing things you never considered.", "path", dict(kind="winding", acc="NEVER CONSIDERED")),
    ("People you never expected to meet.", "crowd", dict(n=5, highlight=2, highlight_label="UNEXPECTED", acc="PEOPLE MEET")),
    ("Opportunities you didn't know existed.", "door", dict(open_=True, lbl="UNKNOWN DOOR", acc="OPPORTUNITIES EXISTED")),
    ("Problems you couldn't have predicted.", "chart", dict(kind="wave", lbl="THE PLOT", acc="PROBLEMS PREDICTED")),
    ("Interests you didn't have before.", "network", dict(nodes=["NEW", "SURPRISING", "YOURS NOW"], tangled=False, acc="INTERESTS BEFORE")),
    ("And sometimes…", "pulse", dict(acc="")),
    ("The life you eventually love looks completely different from the one you originally planned.", "scale", dict(left="PLANNED", right="LOVED", tip=1, acc="LOVE DIFFERENT PLANNED")),
    ("That's why your plan should give you direction…", "compass", dict(lbl="DIRECTION", acc="PLAN DIRECTION")),
    ("Not imprison you.", "cage", dict(words=["THE PLAN"], acc="IMPRISON")),
    ("You can take your goals seriously without pretending you can predict every step.", "path", dict(kind="winding", fog=True, acc="SERIOUSLY PREDICT EVERY STEP")),
    ("You can work toward something while remaining open to discovering something better.", "door", dict(open_=True, lbl="SOMETHING BETTER", acc="OPEN BETTER")),
    ("You can change your mind.", "shed", dict(old="OLD PLAN", new="NEW PLAN", acc="CHANGE MIND")),
    ("You can learn new things about yourself.", "mirror", dict(reflect="solid", lbl="NEW", acc="LEARN YOURSELF")),
    ("You can recognize that your definition of success has changed.", "hud", dict(lbl="SUCCESS = MONEY", start=80, end=30, lbl2="SUCCESS = MEANING", start2=20, end2=85, icons=None, crowd=0, acc="DEFINITION SUCCESS CHANGED")),
    ("The future isn't a finished picture waiting for you to follow the instructions.", "frame", dict(who="FINISHED PICTURE?", dashed_fig=True, acc="FINISHED PICTURE INSTRUCTIONS")),
    ("It's something you participate in creating.", "bricks", dict(rows=4, lbl="YOU BUILD IT", uneven=True, acc="PARTICIPATE CREATING")),
    ("So make plans.", "doc", dict(title="PLAN", empty=False, acc="PLANS")),
    ("Take your goals seriously.", "list", dict(items=["GOALS"], mode="check", acc="SERIOUSLY")),
    ("Build something.", "house", dict(progress=0.8, watchers=False, lbl="SOMETHING", acc="BUILD")),
    ("But leave enough room for the unexpected.", "puzzle", dict(missing=True, lbl="ROOM FOR SURPRISES", acc="ROOM UNEXPECTED")),
    ("Because sometimes the most meaningful parts of your life…", "dots", dict(connect=True, acc="MEANINGFUL")),
    ("Will be the things you never knew to plan for.", "sunrise", dict(acc="NEVER PLAN")),
    ("What's one unexpected thing that changed your direction or perspective?", "path", dict(kind="fork", labels=("THE PLAN", "WHAT HAPPENED"), acc="UNEXPECTED DIRECTION PERSPECTIVE")),
    ("Share it in the comments.", "cta", dict(kind="comment", lbl="YOUR UNEXPECTED TURN", acc="SHARE COMMENTS")),
    ("And follow LanzoFocus for meaningful ideas, lessons, and perspectives that help you become better every day.", "follow"),
]
_HOOK = ("path", dict(kind="winding", labels=("PLAN", "LIFE")))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
