"""Contact sheet of every scene in a project: python3 tools_preview.py projects/<name> out.jpg [t]"""
import sys, importlib.util, math
import render as R
from PIL import Image, ImageDraw
spec = importlib.util.spec_from_file_location("scenes", sys.argv[1] + "/scenes.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
R.TITLE = m.TITLE; R.FOLLOW_SUB = getattr(m, "FOLLOW_SUB", R.FOLLOW_SUB)
t = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
HOOK = getattr(m, "HOOK", None)
fns = [HOOK or R.s_title] + m.SCENES
tiles = []
for fn in fns:
    layer = Image.new("RGBA", (R.W, R.H)); d = ImageDraw.Draw(layer)
    fn(d, 1.5 if fn in (R.s_title, HOOK) else t, 4.0)
    bg = R.make_background().convert("RGBA"); bg.alpha_composite(layer)
    tiles.append(bg.convert("RGB").resize((480, 270)))
rows = math.ceil(len(tiles) / 4)
sheet = Image.new("RGB", (480 * 4, 270 * rows), (40, 40, 40))
for i, tl in enumerate(tiles):
    sheet.paste(tl, ((i % 4) * 480, (i // 4) * 270))
sheet.save(sys.argv[2], quality=85)
