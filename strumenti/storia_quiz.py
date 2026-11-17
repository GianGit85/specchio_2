import sys, random, numpy as np
from PIL import Image, ImageDraw, ImageFont
F, OUT = sys.argv[1], sys.argv[2]
LG = lambda px: ImageFont.truetype(f"{F}/luckiest-guy.ttf", px)
SE = lambda px: ImageFont.truetype(f"{F}/special-elite.ttf", px)
W, H = 1080, 1920
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
def nube(cx, cy, r, col, a):
    return np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)))[..., None] * np.array(col, np.float32) * a
g = np.zeros((H, W, 3), np.float32); g[:] = (20, 13, 9)
g += nube(60, 1500, 620, (255, 90, 200), .32) + nube(1050, 1150, 600, (79, 216, 255), .25) + nube(540, 120, 640, (122, 92, 255), .2)
im = Image.fromarray(np.clip(g, 0, 255).astype(np.uint8)).convert("RGBA"); d = ImageDraw.Draw(im)
STRATI = [(101,74,38),(122,90,48),(143,108,60),(165,128,75),(184,146,90),(201,164,106)]
def t3d(t, y, px, col=(244,233,208)):
    f = LG(px); x = W / 2 - d.textlength(t, font=f) / 2
    for i, c in enumerate(STRATI): d.text((x, y + max(1, px // 22) * (6 - i)), t, font=f, fill=c)
    d.text((x, y), t, font=f, fill=col, stroke_width=max(2, px // 32), stroke_fill=(107, 74, 34))
def cen(t, y, f, col): d.text((W / 2 - d.textlength(t, font=f) / 2, y), t, font=f, fill=col)

# intestazione (sotto la zona coperta da Instagram)
logo = Image.open("/home/user/come-fecero-i-greci/assets/logo-copia-incolla.jpg").convert("RGB")
lw = 150; lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS).rotate(-3, expand=True, fillcolor=(30, 20, 26))
im.paste(lg, (W // 2 - lg.width // 2, 215)); d = ImageDraw.Draw(im)
cen("UN GIOCO DI", 380, SE(30), (244, 233, 208))
t3d("COME FECERO I GRECI", 420, 64)

# domanda grande
cen("GLI SPIRITI SANNO TUTTO", 580, SE(38), (242, 194, 48))
t3d("CHI ERI", 640, 150); t3d("NELLA VITA", 800, 120); t3d("PRECEDENTE?", 935, 120)

# foglietti con esempi
random.seed(5)
def foglietto(testo, cx, cy, ang, larg=760):
    f = SE(34); righe, riga = [], ""
    for p in testo.split():
        pr = (riga + " " + p).strip()
        if d.textlength(pr, font=f) > larg - 70 and riga: righe.append(riga); riga = p
        else: riga = pr
    righe.append(riga)
    h = 40 + len(righe) * 46
    t = Image.new("RGBA", (larg, int(h)), (0, 0, 0, 0)); td = ImageDraw.Draw(t)
    pts = [(0, 3)] + [(x, random.uniform(0, 6)) for x in range(20, larg, 20)] + [(larg, 3), (larg, h - 3)] + [(x, h - random.uniform(0, 6)) for x in range(larg - 20, 0, -20)] + [(0, h - 3)]
    td.polygon(pts, fill=(241, 228, 200, 255))
    for i, r in enumerate(righe): td.text((larg / 2 - td.textlength(r, font=f) / 2, 22 + i * 46), r, font=f, fill=(42, 28, 16))
    t = t.rotate(ang, expand=True, resample=Image.BICUBIC)
    om = Image.new("RGBA", t.size, (0, 0, 0, 0)); om.paste((0, 0, 0, 120), mask=t.split()[3])
    im.alpha_composite(om, (int(cx - t.width / 2) + 7, int(cy - t.height / 2) + 9)); im.alpha_composite(t, (int(cx - t.width / 2), int(cy - t.height / 2)))
foglietto("…una spia francese che non sapeva il francese?", W / 2 - 40, 1140, 2.5)
foglietto("…un fantasma che non pagava l'affitto?", W / 2 + 40, 1250, -2)
foglietto("…un generale con una collezione di cucchiaini?", W / 2 - 20, 1360, 1.5)
d = ImageDraw.Draw(im)
cen("3 domande, 20 secondi", 1445, SE(40), (244, 233, 208))

# spazio per lo sticker Link + freccia
cen("Tocca il link e scoprilo", 1510, LG(52), (242, 194, 48))
ax, ay = W // 2, 1582
d.polygon([(ax - 26, ay), (ax + 26, ay), (ax + 26, ay + 40), (ax + 52, ay + 40), (ax, ay + 92), (ax - 52, ay + 40), (ax - 26, ay + 40)], fill=(242, 194, 48))
# (zona 1740-1800 lasciata libera per lo sticker)
im.convert("RGB").save(OUT, quality=92)
print("ok")
