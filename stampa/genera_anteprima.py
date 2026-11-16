import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S = sys.argv[1]
LG = lambda px: ImageFont.truetype(f"{S}/luckiest-guy.ttf", px)
SE = lambda px: ImageFont.truetype(f"{S}/special-elite.ttf", px)
W, H = 1200, 630
# sfondo con fumo
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
img = np.zeros((H, W, 3), np.float32)
img[:] = (22, 15, 10)
def nube(cx, cy, r, col, a):
    g = np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)))[..., None]
    return g * np.array(col, np.float32) * a
img += nube(150, 600, 380, (255, 90, 200), .33) + nube(560, 560, 360, (79, 216, 255), .25) + nube(1050, 80, 420, (122, 92, 255), .2)
# sfera 3D (stessa logica dello shader della pagina)
cx, cy, R = 300, 285, 205
px, py = (xx - cx) / R, (yy - cy) / R
r2 = px * px + py * py; r = np.sqrt(r2); dentro = r <= 1
z = np.sqrt(np.clip(1 - r2, 0, 1))
n = np.stack([px, -py, z], -1)
L = np.array([-.55, .62, .6]); L /= np.linalg.norm(L)
# interno: nebbia viola con macchie rosa/azzurre
col = np.zeros((H, W, 3), np.float32); col[:] = (70, 42, 110)
rng = np.random.default_rng(4)
for _ in range(22):
    bx, by = rng.uniform(-.8, .8, 2); br = rng.uniform(.2, .5)
    c = [(255, 90, 200), (79, 216, 255), (122, 92, 255), (255, 255, 255)][rng.integers(4)]
    g = np.exp(-(((px - bx) ** 2 + (py - by) ** 2) / (br * br)))[..., None]
    col += g * np.array(c, np.float32) * (.06 if c == (255, 255, 255) else .16)
col = np.clip(col, 0, 255)
col *= (.78 + .3 * np.clip(n @ L, 0, None))[..., None]
cau = np.exp(-(((px - .32) ** 2 + (py - .52) ** 2) * 10))[..., None]; col += cau * np.array([255, 210, 240]) * .3
fres = ((1 - z) ** 2.4)[..., None]
tb = np.clip((px + .9) / 1.8, 0, 1)[..., None]; tb = tb * tb * (3 - 2 * tb)
bordo = np.array([255, 90, 205], np.float32) * (1 - tb) + np.array([77, 216, 255], np.float32) * tb
col = col * (1 - fres * .55) + bordo * fres * .55
Rf = n * (2 * n[..., 2:3]) - np.array([0, 0, 1])   # riflesso della vista
sp = np.clip(Rf @ L, 0, None)
col += (sp ** 28 * .55 + sp ** 420 * 1.1)[..., None] * 255
col = np.clip(col, 0, 255)
alpha = np.clip((1 - r) * R / 1.5, 0, 1)[..., None]
# alone e piedistallo
img += nube(cx, cy, R * 1.5, (255, 90, 200), .25) + nube(cx + 40, cy, R * 1.4, (79, 216, 255), .18)
img = np.clip(img, 0, 255)
base = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(base)
bw = R * 1.3; by = cy + R * .74; bh = bw * .36
def oro(x0, x1):
    t = np.clip((xx - x0) / (x1 - x0), 0, 1)
    stop = np.array([0, .3, .43, .68, 1]); cols = np.array([(46,26,10),(201,162,74),(246,227,161),(168,122,44),(46,26,10)], np.float32)
    return np.stack([np.interp(t, stop, cols[:, k]) for k in range(3)], -1)
def maschera(fn):
    m = Image.new("L", (W, H), 0); fn(ImageDraw.Draw(m)); return (np.asarray(m, np.float32) / 255)[..., None]
arr = np.asarray(base).astype(np.float32)
om = maschera(lambda m: m.ellipse([cx - bw * .7, by + bh * .85, cx + bw * .7, by + bh * 1.1], fill=255))
arr = arr * (1 - om * .55)
for forma, (a, b) in [(lambda m: m.ellipse([cx - bw * .5, by + bh * .68, cx + bw * .5, by + bh * .96], fill=255), (cx - bw * .5, cx + bw * .5)),
                      (lambda m: m.polygon([(cx - bw * .27, by + bh * .14), (cx + bw * .27, by + bh * .14), (cx + bw * .4, by + bh * .8), (cx - bw * .4, by + bh * .8)], fill=255), (cx - bw * .4, cx + bw * .4)),
                      (lambda m: m.ellipse([cx - bw * .3, by + bh * .02, cx + bw * .3, by + bh * .26], fill=255), (cx - bw * .3, cx + bw * .3))]:
    mk = maschera(forma); arr = arr * (1 - mk) + oro(a, b) * mk
base = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(base)
img = np.asarray(base).astype(np.float32)
img = img * (1 - alpha) + col * alpha
base = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)); d = ImageDraw.Draw(base)
# testi a destra
xc = 860
def centrato(t, y, f, c):
    d.text((xc - d.textlength(t, font=f) / 2, y), t, font=f, fill=c)
centrato("UNA COMMEDIA TEATRALE DI", 70, SE(24), (244, 233, 208))
logo = Image.open("/home/user/specchio_2/assets/logo-copia-incolla.jpg").convert("RGB")
lw = 120; lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS).rotate(-3, expand=True, fillcolor=(30, 20, 30))
base.paste(lg, (xc - lg.width // 2, 105))
def titolo3D(t, y, px_):
    f = LG(px_); x = xc - d.textlength(t, font=f) / 2
    for i, c in enumerate([(101,74,38),(122,90,48),(143,108,60),(165,128,75),(184,146,90),(201,164,106)]):
        d.text((x, y + px_ // 22 * (6 - i)), t, font=f, fill=c)
    d.text((x, y), t, font=f, fill=(244, 233, 208), stroke_width=max(2, px_ // 30), stroke_fill=(107, 74, 34))
titolo3D("COME FECERO", 240, 84); titolo3D("I GRECI", 330, 84)
centrato("Sai qual è la cosa più importante", 470, SE(30), (244, 233, 208))
centrato("di questo spettacolo?", 508, SE(30), (244, 233, 208))
centrato("Il medium ha la risposta 🔮".replace(" 🔮", "…"), 565, SE(24), (242, 194, 48))
base.convert("RGB").save("/home/user/specchio_2/assets/anteprima.jpg", quality=88)
print("ok")
