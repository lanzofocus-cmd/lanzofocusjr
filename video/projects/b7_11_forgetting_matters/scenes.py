from kit import build, follow_sub, hook

TITLE = ("WHY YOU KEEP FORGETTING", "WHAT MATTERS")
OUTPUT = "211_Why_You_Keep_Forgetting_What_Matters_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("You wake up knowing what matters.", "sunrise", dict(acc="WAKE MATTERS")),
    ("You have goals.", "list", dict(items=["GOALS"], mode="empty", acc="GOALS")),
    ("Plans.", "list", dict(items=["GOALS", "PLANS"], mode="empty", acc="PLANS")),
    ("Things you promised yourself you'd do.", "list", dict(items=["GOALS", "PLANS", "PROMISES"], mode="empty", acc="PROMISED")),
    ("Then the day begins.", "hourglass", dict(acc="DAY BEGINS")),
    ("Messages.", "notifs", dict(items=["NEW MESSAGE"], acc="MESSAGES")),
    ("Notifications.", "notifs", dict(items=["NEW MESSAGE", "12 NOTIFICATIONS"], acc="NOTIFICATIONS")),
    ("Random tasks.", "notifs", dict(items=["NEW MESSAGE", "12 NOTIFICATIONS", "CAN YOU QUICKLY..."], acc="RANDOM TASKS")),
    ("Unexpected problems.", "tangle", dict(lbl="UNEXPECTED", acc="UNEXPECTED PROBLEMS")),
    ("And by nighttime…", "pulse", dict(acc="NIGHTTIME")),
    ("You realize the entire day was spent reacting.", "receipt", dict(items=[("MESSAGES", "3 HRS"), ("SCROLLING", "2 HRS"), ("REACTING", "4 HRS"), ("YOUR GOALS", "0")], total="A REACTIVE DAY", acc="ENTIRE REACTING")),
    ("This doesn't always happen because you don't care.", "list", dict(items=["YOU DON'T CARE"], mode="strike", acc="CARE")),
    ("Sometimes the important things simply don't demand attention as loudly as everything else.", "scale", dict(left="LOUD", right="IMPORTANT", tip=-1, acc="IMPORTANT LOUDLY")),
    ("A notification appears immediately.", "notifs", dict(items=["NEW NOTIFICATION"], acc="NOTIFICATION IMMEDIATELY")),
    ("A goal doesn't.", "compass", dict(lbl="YOUR GOAL", settle=False, acc="GOAL")),
    ("A message demands a response.", "bubbles", dict(texts=["???", "HELLO??"], acc="DEMANDS")),
    ("Your future doesn't send you reminders every five minutes.", "phone", dict(lbl="NO MESSAGES FROM YOUR FUTURE", drop=True, acc="FUTURE REMINDERS")),
    ("That's why you need to deliberately create reminders of what matters.", "key", dict(lbl="REMINDERS", acc="DELIBERATELY REMINDERS")),
    ("Write down your priorities.", "doc", dict(title="PRIORITIES", empty=False, acc="PRIORITIES")),
    ("Keep them visible.", "list", dict(items=["1. HEALTH", "2. THE PROJECT", "3. FAMILY"], mode="check", acc="VISIBLE")),
    ("Decide what deserves your attention before the day begins.", "timeline", dict(n=8, progress=0.05, tag="BEFORE IT BEGINS", acc="DECIDE BEFORE")),
    ("Otherwise, your attention will be controlled by whatever happens to demand it.", "cage", dict(words=["URGENT", "NEW", "PING"], acc="CONTROLLED DEMAND")),
    ("Your life doesn't need to be perfectly organized.", "list", dict(items=["PERFECTLY ORGANIZED"], mode="strike", acc="PERFECTLY ORGANIZED")),
    ("But your priorities should not be accidental.", "compass", dict(lbl="ON PURPOSE", acc="PRIORITIES ACCIDENTAL")),
    ("What is one priority you don't want to keep forgetting?", "list", dict(items=["MY PRIORITY: ..."], mode="empty", acc="PRIORITY FORGETTING")),
    ("Comment it so you can put it into words.", "cta", dict(kind="comment", lbl="PUT IT INTO WORDS", acc="COMMENT WORDS")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="DAY SPENT REACTING", start=5, end=94, lbl2="ON WHAT MATTERS", start2=60, end2=4, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
