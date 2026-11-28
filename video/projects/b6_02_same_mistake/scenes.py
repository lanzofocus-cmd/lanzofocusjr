from kit import build, follow_sub, hook

TITLE = ("WHY YOU KEEP MAKING", "THE SAME MISTAKE")
OUTPUT = "192_Why_You_Keep_Making_The_Same_Mistake_16x9.mp4"
MUSIC = "vyzee"
SPEC = [
    ("Have you ever made a mistake…", "list", dict(items=["MISTAKE"], mode="strike", acc="MISTAKE")),
    ("Promised yourself you wouldn't do it again…", "doc", dict(title="NEVER AGAIN", empty=False, acc="PROMISED AGAIN")),
    ("And then somehow found yourself doing the exact same thing?", "loop", dict(items=["MISTAKE", "PROMISE", "SAME MISTAKE", "REGRET"], acc="EXACT SAME")),
    ("Maybe you reacted emotionally.", "gauge", dict(lbl="EMOTION", start=0.3, end=0.95, acc="EMOTIONALLY")),
    ("Maybe you procrastinated.", "phone", dict(lbl="JUST 5 MORE MINUTES", acc="PROCRASTINATED")),
    ("Maybe you made a decision you knew wasn't good for you.", "path", dict(kind="fork", labels=("GOOD FOR YOU", "EASY"), acc="DECISION KNEW")),
    ("And afterward, you asked yourself:", "mirror", dict(reflect="solid", acc="AFTERWARD")),
    ("\"Why did I do that again?\"", "quote", dict(text="WHY DID I DO THAT AGAIN?", acc="AGAIN")),
    ("Here's something important.", "pulse", dict(acc="IMPORTANT")),
    ("Understanding that something is wrong and understanding why you keep doing it are two completely different things.", "scale", dict(left="WHAT'S WRONG", right="WHY I DO IT", tip=0, acc="WRONG WHY DIFFERENT")),
    ("Imagine someone who always procrastinates.", "alone", dict(tag="ALWAYS LATER", acc="PROCRASTINATES")),
    ("They tell themselves they need to be more disciplined.", "quote", dict(text="I JUST NEED MORE DISCIPLINE.", acc="DISCIPLINED")),
    ("But every time they sit down to work, the task feels overwhelming.", "bricks", dict(rows=6, lbl="THE TASK", uneven=False, acc="OVERWHELMING")),
    ("So they avoid it.", "door", dict(open_=True, lbl="AVOID", acc="AVOID")),
    ("Avoiding it gives them temporary relief.", "hud", dict(lbl="RELIEF", start=10, end=85, icons=None, crowd=0, tag="TEMPORARY", acc="TEMPORARY RELIEF")),
    ("That relief teaches their brain that avoiding the task is a solution.", "brain", dict(says="AVOIDING WORKS!", acc="TEACHES SOLUTION")),
    ("And suddenly, procrastination isn't just laziness.", "list", dict(items=["JUST LAZINESS"], mode="strike", acc="PROCRASTINATION LAZINESS")),
    ("It's a pattern reinforced by temporary comfort.", "loop", dict(items=["TASK", "OVERWHELM", "AVOID", "RELIEF"], lbl="THE PATTERN", acc="PATTERN COMFORT")),
    ("If you only attack the behavior…", "shield", dict(front="TRY HARDER", back="THE BEHAVIOR", acc="ATTACK BEHAVIOR")),
    ("You might never understand the reason behind it.", "iceberg", dict(top="THE BEHAVIOR", bottom="THE REASON", acc="REASON BEHIND")),
    ("Maybe the task is too vague.", "fog", dict(lbl="TOO VAGUE", acc="VAGUE")),
    ("Maybe you don't know where to begin.", "map", dict(a_lbl="YOU", b_lbl="WHERE?", acc="BEGIN")),
    ("Maybe you're afraid of doing it badly.", "gauge", dict(lbl="FEAR", start=0.2, end=0.7, acc="AFRAID BADLY")),
    ("Maybe you're overwhelmed.", "tangle", dict(lbl="OVERWHELMED", acc="OVERWHELMED")),
    ("The solution isn't always to tell yourself to try harder.", "list", dict(items=["TRY HARDER"], mode="strike", acc="SOLUTION HARDER")),
    ("Sometimes the solution is to understand the system that keeps producing the same result.", "loop", dict(items=["SITUATION", "FEELING", "DECISION", "RESULT"], lbl="THE SYSTEM", acc="UNDERSTAND SYSTEM RESULT")),
    ("Don't just ask:", "arrows", dict(items=["THE QUESTION"], acc="ASK")),
    ("\"Why did I fail?\"", "quote", dict(text="WHY DID I FAIL?", acc="FAIL")),
    ("Ask:", "pulse", dict(acc="")),
    ("\"What happened immediately before I made that decision?\"", "timeline", dict(n=8, progress=0.6, tag="JUST BEFORE", acc="IMMEDIATELY BEFORE")),
    ("\"What was I feeling?\"", "brain", dict(says="WHAT WAS I FEELING?", acc="FEELING")),
    ("\"What was I trying to avoid?\"", "door", dict(closing=True, lbl="AVOIDING WHAT?", acc="AVOID")),
    ("\"What could I change so the same situation becomes easier to handle next time?\"", "key", dict(lbl="NEXT TIME", acc="CHANGE EASIER NEXT")),
    ("Because if you keep repeating the same pattern…", "loop", dict(items=["TASK", "OVERWHELM", "AVOID", "RELIEF"], acc="REPEATING PATTERN")),
    ("The answer may not be another promise.", "doc", dict(title="NEVER AGAIN", empty=False, stamp="AGAIN?", acc="ANOTHER PROMISE")),
    ("It may be a better understanding of yourself.", "loop", dict(items=["TASK", "OVERWHELM", "AVOID", "RELIEF"], broken=True, lbl="UNDERSTOOD", acc="UNDERSTANDING YOURSELF")),
    ("Comment one pattern you've noticed in yourself that you're trying to understand, not just fight.", "cta", dict(kind="comment", lbl="ONE PATTERN YOU NOTICED", acc="PATTERN UNDERSTAND FIGHT")),
    ("And save this if you want to remember to investigate your habits instead of blindly blaming yourself.", "cta", dict(kind="save", lbl="INVESTIGATE, DON'T BLAME", acc="SAVE INVESTIGATE BLAMING")),
    ("", "follow"),
]
_HOOK = ("loop", dict(items=["MISTAKE", "PROMISE", "SAME MISTAKE", "REGRET"]))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
