from kit import build, follow_sub, hook

TITLE = ("THE PEOPLE WHO ONLY", "REMEMBER YOUR MISTAKES")
OUTPUT = "254_The_People_Who_Only_Remember_Your_Mistakes_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("Imagine making one mistake.", "list", dict(items=["ONE MISTAKE"], mode="strike", acc="ONE MISTAKE")),
    ("Then spending years trying to become better.", "timeline", dict(n=10, progress=0.8, tag="YEARS OF WORK", acc="YEARS BETTER")),
    ("You learn.", "list", dict(items=["LEARN"], mode="check", acc="LEARN")),
    ("You change.", "list", dict(items=["LEARN", "CHANGE"], mode="check", acc="CHANGE")),
    ("You develop new habits.", "list", dict(items=["LEARN", "CHANGE", "NEW HABITS"], mode="check", acc="HABITS")),
    ("You make better decisions.", "list", dict(items=["LEARN", "CHANGE", "NEW HABITS", "BETTER DECISIONS"], mode="check", acc="DECISIONS")),
    ("But whenever someone talks about you…", "bubbles", dict(texts=["OH, REMEMBER WHEN THEY..."], acc="TALKS")),
    ("They bring up the same old mistake.", "frame", dict(who="THAT ONE MISTAKE", acc="SAME OLD MISTAKE")),
    ("It's as if everything you've done since then doesn't exist.", "progress", dict(lbl="YOUR GROWTH", value=0.8, invisible=True, acc="EVERYTHING EXIST")),
    ("This can be frustrating.", "gauge", dict(lbl="FRUSTRATION", start=0.2, end=0.8, acc="FRUSTRATING")),
    ("But it also teaches you something important.", "key", dict(lbl="THE LESSON", acc="TEACHES IMPORTANT")),
    ("You cannot force everyone to update their understanding of you.", "lock", dict(lbl="THEIR VIEW", acc="FORCE UPDATE")),
    ("Some people remember the past because that's the only version of you they've paid attention to.", "frame", dict(who="THE ONLY VERSION THEY SAW", acc="PAST ONLY VERSION")),
    ("Some people don't know how much you've changed.", "iceberg", dict(top="WHAT THEY KNOW", bottom="HOW MUCH YOU CHANGED", acc="CHANGED")),
    ("And some people simply aren't interested in recognizing it.", "crowd", dict(n=5, dim=True, acc="INTERESTED RECOGNIZING")),
    ("You can explain.", "list", dict(items=["EXPLAIN"], mode="check", acc="EXPLAIN")),
    ("You can demonstrate.", "list", dict(items=["EXPLAIN", "DEMONSTRATE"], mode="check", acc="DEMONSTRATE")),
    ("You can continue improving.", "list", dict(items=["EXPLAIN", "DEMONSTRATE", "KEEP IMPROVING"], mode="check", acc="IMPROVING")),
    ("But eventually, you need to stop making your growth dependent on whether someone from your past acknowledges it.", "beam", dict(lbl="YOUR GROWTH", tags=("REMEMBER WHEN?", "SAME OLD YOU"), acc="GROWTH DEPENDENT ACKNOWLEDGES")),
    ("Your improvement is still real.", "hud", dict(lbl="YOUR IMPROVEMENT", start=90, end=90, icons=None, crowd=0, tag="REAL", acc="IMPROVEMENT REAL")),
    ("Your lessons still matter.", "book", dict(chapter="LESSONS", acc="LESSONS MATTER")),
    ("Your decisions still count.", "doc", dict(title="DECISIONS", empty=False, stamp="COUNTED", acc="DECISIONS COUNT")),
    ("You don't need to convince every person who remembers your worst moment that you're different now.", "list", dict(items=["CONVINCE EVERYONE"], mode="strike", acc="CONVINCE WORST DIFFERENT")),
    ("Sometimes the best response is to continue living differently.", "path", dict(kind="straight", drop=True, acc="BEST CONTINUE DIFFERENTLY")),
    ("Have you ever felt like people kept judging you based on an old version of yourself?", "frame", dict(who="THE OLD YOU", fade=True, acc="JUDGING OLD")),
    ("Share your perspective.", "cta", dict(kind="comment", lbl="YOUR PERSPECTIVE", acc="PERSPECTIVE")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="YEARS OF GROWTH", start=0, end=95, lbl2="WHAT THEY REMEMBER", start2=5, end2=5, icons="q", tag="ONE MISTAKE", count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
