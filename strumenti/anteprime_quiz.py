import sys, os, json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
S = sys.argv[1]; R = "/home/user/come-fecero-i-greci"
LG = lambda px: ImageFont.truetype(f"{S}/luckiest-guy.ttf", px)
SE = lambda px: ImageFont.truetype(f"{S}/special-elite.ttf", px)
W, H = 1200, 630
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
def nube(cx, cy, r, col, a):
    return np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)))[..., None] * np.array(col, np.float32) * a
fondo = np.zeros((H, W, 3), np.float32); fondo[:] = (22, 15, 10)
fondo += nube(80, 620, 420, (255, 90, 200), .33) + nube(1150, 560, 420, (79, 216, 255), .26) + nube(600, -40, 460, (122, 92, 255), .2)
FONDO = Image.fromarray(np.clip(fondo, 0, 255).astype(np.uint8))
logo = Image.open(f"{R}/assets/logo-copia-incolla.jpg").convert("RGB")
lg = logo.resize((92, int(92 * logo.height / logo.width)), Image.LANCZOS).rotate(-3, expand=True, fillcolor=(26, 18, 22))
STRATI = [(101,74,38),(122,90,48),(143,108,60),(165,128,75),(184,146,90),(201,164,106)]
def testo3D(d, t, x, y, px, centro=True):
    f = LG(px); w = d.textlength(t, font=f); x0 = x - w / 2 if centro else x
    for i, c in enumerate(STRATI): d.text((x0, y + max(1, px // 22) * (6 - i)), t, font=f, fill=c)
    d.text((x0, y), t, font=f, fill=(244, 233, 208), stroke_width=max(2, px // 32), stroke_fill=(107, 74, 34))
def a_capo(d, testo, f, larg):
    righe, riga = [], ""
    for p in testo.split():
        prova = (riga + " " + p).strip()
        if d.textlength(prova, font=f) > larg and riga: righe.append(riga); riga = p
        else: riga = prova
    return righe + [riga]
def anteprima(sopra, grande, sotto, out):
    im = FONDO.copy(); d = ImageDraw.Draw(im)
    im.paste(lg, (46, 30)); testo3D(d, "COME FECERO I GRECI", 160, 58, 46, centro=False)
    d.text((162, 112), "un gioco della commedia teatrale di Copia Incolla", font=SE(22), fill=(244, 233, 208))
    d.text((W / 2 - d.textlength(sopra, font=SE(36)) / 2, 178), sopra, font=SE(36), fill=(244, 233, 208))
    px = 78
    while True:
        righe = a_capo(d, grande.upper(), LG(px), W - 140)
        if len(righe) <= 3 or px <= 46: break
        px -= 4
    alt = len(righe) * px * 1.12; y = 225 + (300 - alt) / 2
    for r in righe: testo3D(d, r, W / 2, y, px); y += px * 1.12
    d.text((W / 2 - d.textlength(sotto, font=SE(34)) / 2, 556), sotto, font=SE(34), fill=(242, 194, 48))
    im.save(out, quality=84)
os.makedirs(f"{R}/assets/r", exist_ok=True)
ris = json.loads(subprocess.check_output(["node", "-e", f"global.window={{}};require('{R}/quiz.js');console.log(JSON.stringify(window.RISULTATI))"]))
for n, t in enumerate(ris, 1):
    anteprima("NELLA VITA PRECEDENTE ERO…", t, "…e gli spiriti hanno detto qualcosa anche su di te", f"{R}/assets/r/{n}.jpg")
anteprima("IL MEDIUM HA UNA DOMANDA PER TE", "Chi eri nella vita precedente?", "5 domande, 30 secondi. Gli spiriti sanno tutto.", f"{R}/assets/anteprima.jpg")
print("ok", len(ris))
