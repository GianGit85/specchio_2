import qrcode, random, math, sys
from qrcode.constants import ERROR_CORRECT_H
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = sys.argv[1]; OUT = "/home/user/specchio_2/stampa"
URL = "https://giangit85.github.io/specchio_2/"
for nome in ["luckiest-guy", "special-elite"]:
    f = TTFont(f"{S}/fonts/fontsource-{nome}-5.3.0/files/{nome}-latin-400-normal.woff"); f.flavor = None; f.save(f"{S}/{nome}.ttf")
LG = lambda px: ImageFont.truetype(f"{S}/luckiest-guy.ttf", px)
SE = lambda px: ImageFont.truetype(f"{S}/special-elite.ttf", px)
logo = Image.open("/home/user/specchio_2/assets/logo-copia-incolla.jpg").convert("RGB")
random.seed(7)

# ---------- QR con logo al centro ----------
def crea_qr(lato, scuro=(20, 14, 10), chiaro=(255, 255, 255)):
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=4)
    q.add_data(URL); q.make(fit=True)
    img = q.make_image(fill_color=scuro, back_color=chiaro).convert("RGB").resize((lato, lato), Image.NEAREST)
    lw = int(lato * .24); lh = int(lw * logo.height / logo.width)
    pad = int(lato * .018)
    box = Image.new("RGB", (lw + 2 * pad, lh + 2 * pad), chiaro)
    box.paste(logo.resize((lw, lh), Image.LANCZOS), (pad, pad))
    img.paste(box, ((lato - box.width) // 2, (lato - box.height) // 2))
    return img

qr = crea_qr(1800); qr.save(f"{OUT}/qr-code.png", dpi=(300, 300))

# ---------- Biglietto (300 dpi, 17 x 6.5 cm) ----------
W, H = 2000, 770
STUB = 600; XP = W - STUB
t = Image.new("RGB", (W, H), (18, 12, 8))
px = t.load()
# sfondo scuro con fumo rosa/azzurro (solo parte principale)
fumo = Image.new("RGB", (W, H), (0, 0, 0)); fd = ImageDraw.Draw(fumo)
for (cx, cy, r, col) in [(260, 700, 520, (255, 90, 200)), (1150, 650, 520, (79, 216, 255)), (700, 0, 480, (122, 92, 255))]:
    fd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
fumo = fumo.filter(ImageFilter.GaussianBlur(170))
base = Image.new("RGB", (W, H), (30, 20, 14))
t = Image.blend(base, fumo, .28)
d = ImageDraw.Draw(t)
# matrice cartoncino a destra
kraft = Image.new("RGB", (STUB, H), (236, 222, 192)); kd = ImageDraw.Draw(kraft)
for _ in range(9000):
    x, y = random.randrange(STUB), random.randrange(H); c = random.randint(-18, 12)
    kd.point((x, y), fill=(236 + c, 222 + c, 192 + c))
t.paste(kraft, (XP, 0))

# testo 3D come il titolo della locandina
def titolo3D(img, testo, xc, y, px_):
    f = LG(px_); dd = ImageDraw.Draw(img)
    w = dd.textlength(testo, font=f); x = xc - w / 2
    strati = [(101, 74, 38), (122, 90, 48), (143, 108, 60), (165, 128, 75), (184, 146, 90), (201, 164, 106)]
    passo = max(1, px_ // 22)
    for i, c in enumerate(strati): dd.text((x, y + passo * (6 - i)), testo, font=f, fill=c)
    dd.text((x, y), testo, font=f, fill=(244, 233, 208), stroke_width=max(1, px_ // 40), stroke_fill=(107, 74, 34))
def centrato(dd, testo, xc, y, f, col):
    dd.text((xc - dd.textlength(testo, font=f) / 2, y), testo, font=f, fill=col)

xc = XP / 2
centrato(d, "UNA COMMEDIA TEATRALE DI", xc - 100, 62, SE(30), (244, 233, 208))
lg = logo.resize((118, int(118 * logo.height / logo.width)), Image.LANCZOS).rotate(-3, expand=True, fillcolor=(30, 20, 14))
t.paste(lg, (int(xc + 195 - lg.width / 2), 22))
titolo3D(t, "COME FECERO I GRECI", xc, 188, 108)
d = ImageDraw.Draw(t)
centrato(d, "Sai qual è la cosa più importante", xc, 352, SE(42), (244, 233, 208))
centrato(d, "di questo spettacolo?", xc, 405, SE(42), (244, 233, 208))
centrato(d, "20 NOVEMBRE 2026 · ORE 21:00", xc, 520, LG(64), (107, 74, 16))
centrato(d, "20 NOVEMBRE 2026 · ORE 21:00", xc, 515, LG(64), (242, 194, 48))
centrato(d, "TEATRO SANT'ANNA · VIA BRIONE 40, TORINO", xc, 610, LG(44), (90, 20, 14))
centrato(d, "TEATRO SANT'ANNA · VIA BRIONE 40, TORINO", xc, 606, LG(44), (224, 74, 58))
centrato(d, "@copia.in.colla", xc, 690, SE(30), (244, 233, 208))

# perforazione e tacche a semicerchio
for y in range(20, H - 20, 26): d.ellipse([XP - 5, y, XP + 5, y + 10], fill=(18, 12, 8))
for yy in (-34, H - 34): d.ellipse([XP - 34, yy, XP + 34, yy + 68], fill=(255, 255, 255))

# matrice: lettere ritagliate "INQUADRAMI" non entrano: titolo breve + QR
carte = [((242, 194, 48), (29, 29, 29)), ((216, 53, 42), (246, 236, 214)), ((47, 95, 168), (246, 236, 214)), ((29, 29, 29), (242, 194, 48)),
         ((58, 143, 74), (246, 236, 214)), ((232, 130, 42), (29, 29, 29)), ((241, 228, 200), (194, 47, 38)), ((246, 236, 214), (47, 95, 168))]
def collage(img, parola, xc, y, lw):
    gap = 6; tot = len(parola) * lw + (len(parola) - 1) * gap; x = xc - tot / 2
    fonts = [LG, SE]
    for i, ch in enumerate(parola):
        bg, fg = carte[i % len(carte)]
        tile = Image.new("RGBA", (lw, int(lw * 1.3)), bg + (255,)); td = ImageDraw.Draw(tile)
        f = fonts[i % 2](int(lw * .82)); w = td.textlength(ch, font=f)
        td.text(((lw - w) / 2, lw * .12), ch, font=f, fill=fg)
        tile = tile.rotate(random.uniform(-8, 8), expand=True, resample=Image.BICUBIC)
        ombra = Image.new("RGBA", tile.size, (0, 0, 0, 0)); ombra.paste((0, 0, 0, 110), mask=tile.split()[3])
        img.paste(ombra, (int(x) + 4, int(y + random.uniform(-6, 6)) + 5), ombra)
        img.paste(tile, (int(x), int(y + random.uniform(-6, 6))), tile)
        x += lw + gap
tR = t.convert("RGBA")
collage(tR, "INQUADRAMI", XP + STUB / 2, 34, 50)
t = tR.convert("RGB"); d = ImageDraw.Draw(t)
QL = 470
qrb = crea_qr(QL, chiaro=(255, 255, 255))
t.paste(qrb, (int(XP + (STUB - QL) / 2), 128))
centrato(d, "la risposta è qui dentro", XP + STUB / 2, 618, SE(30), (60, 40, 20))
centrato(d, "apri la fotocamera e inquadra", XP + STUB / 2, 660, SE(24), (110, 85, 55))

# bordo arrotondato (trasparente fuori)
mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, H - 1], 36, fill=255)
for yy in (-34, H - 34): ImageDraw.Draw(mask).ellipse([XP - 34, yy, XP + 34, yy + 68], fill=0)
out = Image.new("RGBA", (W, H)); out.paste(t, (0, 0), mask)
out.save(f"{OUT}/biglietto.png", dpi=(300, 300))
white = Image.new("RGB", (W, H), (255, 255, 255)); white.paste(t, (0, 0), mask)
# PDF A4 con 4 biglietti, linee di taglio
A4 = Image.new("RGB", (2480, 3508), (255, 255, 255)); ad = ImageDraw.Draw(A4)
for i in range(4):
    x0, y0 = 240, 200 + i * (H + 80)
    A4.paste(white, (x0, y0))
    for (x, y) in [(x0, y0), (x0 + W, y0), (x0, y0 + H), (x0 + W, y0 + H)]:
        ad.line([x - 40, y, x - 10, y], fill=(160, 160, 160), width=2); ad.line([x + 10, y, x + 40, y], fill=(160, 160, 160), width=2)
        ad.line([x, y - 40, x, y - 10], fill=(160, 160, 160), width=2); ad.line([x, y + 10, x, y + 40], fill=(160, 160, 160), width=2)
A4.save(f"{OUT}/biglietti-A4.pdf", resolution=300)
print("fatto")
