from kit import build, follow_sub, hook

TITLE = ("THE LIFE YOU ARE BUILDING", "IS ALSO HAPPENING TODAY")
OUTPUT = "280_The_Life_You_Are_Building_Is_Also_Happening_Today_16x9.mp4"
MUSIC = "twofaced"
SPEC = [
    ("It's easy to become obsessed with the future.", "map", dict(a_lbl="NOW", b_lbl="THE FUTURE", acc="OBSESSED FUTURE")),
    ("The future version of yourself.", "frame", dict(who="FUTURE YOU", acc="VERSION")),
    ("The future achievement.", "crown", dict(lbl="SOMEDAY", acc="ACHIEVEMENT")),
    ("The future opportunity.", "door", dict(open_=True, lbl="SOMEDAY", acc="OPPORTUNITY")),
    ("The future lifestyle.", "house", dict(progress=1.0, watchers=False, lbl="SOMEDAY", acc="LIFESTYLE")),
    ("You imagine everything that will happen after you finally reach your goal.", "brain", dict(says="AFTER I MAKE IT...", acc="IMAGINE AFTER GOAL")),
    ("And suddenly, the present becomes something you're simply trying to get through.", "hourglass", dict(acc="PRESENT THROUGH")),
    ("But your future life isn't separate from your current life.", "timeline", dict(n=10, progress=0.4, tag="ONE LINE", acc="SEPARATE CURRENT")),
    ("It's being built from it.", "bricks", dict(rows=5, lbl="BUILT FROM TODAY", uneven=False, drop=True, acc="BUILT")),
    ("The people you spend time with today.", "list", dict(items=["THE PEOPLE"], mode="check", acc="PEOPLE")),
    ("The skills you're learning today.", "list", dict(items=["THE PEOPLE", "THE SKILLS"], mode="check", acc="SKILLS")),
    ("The decisions you're making today.", "list", dict(items=["THE PEOPLE", "THE SKILLS", "THE DECISIONS"], mode="check", acc="DECISIONS")),
    ("The moments you're experiencing today.", "list", dict(items=["THE PEOPLE", "THE SKILLS", "THE DECISIONS", "THE MOMENTS"], mode="check", acc="MOMENTS")),
    ("These aren't merely obstacles between you and your future.", "list", dict(items=["OBSTACLES"], mode="strike", acc="OBSTACLES")),
    ("They're part of your life.", "pulse", dict(acc="PART LIFE")),
    ("You should absolutely have goals.", "list", dict(items=["GOALS"], mode="check", acc="GOALS")),
    ("You should work toward them.", "list", dict(items=["GOALS", "WORK"], mode="check", acc="WORK")),
    ("You should prepare.", "list", dict(items=["GOALS", "WORK", "PREPARE"], mode="check", acc="PREPARE")),
    ("You should improve.", "list", dict(items=["GOALS", "WORK", "PREPARE", "IMPROVE"], mode="check", acc="IMPROVE")),
    ("But don't treat your current life as if it has no value until you achieve something.", "hud", dict(lbl="VALUE OF TODAY", start=5, end=100, icons=None, crowd=0, tag="NOT ZERO", acc="CURRENT VALUE ACHIEVE")),
    ("You are not only building the future.", "house", dict(progress=0.6, watchers=False, lbl="THE FUTURE", acc="BUILDING FUTURE")),
    ("You are living the present.", "sunrise", dict(acc="LIVING PRESENT")),
    ("And both deserve your attention.", "scale", dict(left="FUTURE", right="PRESENT", tip=0, acc="BOTH ATTENTION")),
    ("What's one thing you're working toward, and one thing in your current life you don't want to forget to appreciate?", "list", dict(items=["WORKING TOWARD: ...", "APPRECIATING: ..."], mode="empty", acc="WORKING APPRECIATE")),
    ("Share both.", "cta", dict(kind="comment", lbl="SHARE BOTH", acc="BOTH")),
    ("", "follow"),
]
_HOOK = ("hud", dict(lbl="FOCUS ON SOMEDAY", start=20, end=100, lbl2="FOCUS ON TODAY", start2=70, end2=4, icons=None, count=2.4))
LINES, SCENES = build(SPEC)
FOLLOW_SUB = follow_sub(SPEC[-1][0])
HOOK = hook(TITLE, *_HOOK)
