import sys
S = sys.argv[1]; OUT = "/home/user/specchio_2/stampa"
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
URL = "https://giangit85.github.io/specchio_2/"
LG = lambda px: ImageFont.truetype(f"{S}/luckiest-guy.ttf", px)
NERO, BIANCO = (0, 0, 0), (255, 255, 255)
logo = ImageEnhance.Contrast(ImageOps.grayscale(Image.open("/home/user/specchio_2/assets/logo-copia-incolla.jpg"))).enhance(1.6).convert("RGB")
q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0); q.add_data(URL); q.make(fit=True)
M = q.get_matrix(); N = len(M)

def biglietto(W):
    quiet = 3                                   # margine bianco attorno al QR (in moduli)
    cell = W / (N + 2 * quiet)
    tpx = int(W * .105)                         # titolo su una riga
    f = LG(tpx)
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    while tmp.textlength("COME FECERO I GRECI", font=f) > W * .9: tpx -= 2; f = LG(tpx)
    top = int(W * .035); hT = int(tpx * 1.15)
    qy = top + hT                                # il QR inizia subito sotto il titolo
    H = int(qy + W)
    img = Image.new("RGB", (W, H), BIANCO); d = ImageDraw.Draw(img)
    w = d.textlength("COME FECERO I GRECI", font=f); x = (W - w) / 2
    d.text((x + tpx // 14, top + tpx // 14), "COME FECERO I GRECI", font=f, fill=NERO)
    d.text((x, top), "COME FECERO I GRECI", font=f, fill=BIANCO, stroke_width=max(2, tpx // 22), stroke_fill=NERO)
    occhio = lambda x, y: (x < 7 and y < 7) or (x >= N - 7 and y < 7) or (x < 7 and y >= N - 7)
    lw = int(W * .23); lh = int(lw * logo.height / logo.width)
    cx0 = (W - lw) / 2 - cell * .6; cx1 = (W + lw) / 2 + cell * .6
    cy0 = qy + (W - lh) / 2 - cell * .6; cy1 = qy + (W + lh) / 2 + cell * .6
    for yy in range(N):
        for xx in range(N):
            if not M[yy][xx] or occhio(xx, yy): continue
            X = (xx + quiet) * cell; Y = qy + (yy + quiet) * cell
            if cx0 < X + cell / 2 < cx1 and cy0 < Y + cell / 2 < cy1: continue
            p = cell * .08; d.ellipse([X + p, Y + p, X + cell - p, Y + cell - p], fill=NERO)
    for ox, oy in [(0, 0), (N - 7, 0), (0, N - 7)]:
        X = (ox + quiet) * cell; Y = qy + (oy + quiet) * cell
        d.rounded_rectangle([X, Y, X + 7 * cell, Y + 7 * cell], radius=cell * 2, fill=NERO)
        d.rounded_rectangle([X + cell, Y + cell, X + 6 * cell, Y + 6 * cell], radius=cell * 1.3, fill=BIANCO)
        d.rounded_rectangle([X + 2 * cell, Y + 2 * cell, X + 5 * cell, Y + 5 * cell], radius=cell * .9, fill=NERO)
    img.paste(logo.resize((lw, lh), Image.LANCZOS), ((W - lw) // 2, int(qy + (W - lh) / 2)))
    return img

# file singolo ad alta risoluzione
big = biglietto(1200); big.save(f"{OUT}/qr-biglietto.png", dpi=(300, 300))

# A4 a 300 dpi: biglietti larghi 4 cm, griglia con linee di taglio
DPI = 300; cm = DPI / 2.54
card = biglietto(int(4 * cm))
cw, ch = card.size
A4w, A4h = int(21 * cm), int(29.7 * cm)
cols, rows = int((A4w - 1.6 * cm) // cw), int((A4h - 1.6 * cm) // ch)
x0 = (A4w - cols * cw) // 2; y0 = (A4h - rows * ch) // 2
pag = Image.new("RGB", (A4w, A4h), BIANCO); d = ImageDraw.Draw(pag)
for r in range(rows):
    for c in range(cols): pag.paste(card, (x0 + c * cw, y0 + r * ch))
grigio = (170, 170, 170)
for c in range(cols + 1):
    x = x0 + c * cw; d.line([x, y0 - 40, x, y0 + rows * ch + 40], fill=grigio, width=2)
for r in range(rows + 1):
    y = y0 + r * ch; d.line([x0 - 40, y, x0 + cols * cw + 40, y], fill=grigio, width=2)
pag.save(f"{OUT}/biglietti-A4.pdf", resolution=DPI)
pag.save(f"{S}/anteprima-A4.png")
print(f"biglietto {cw/cm:.1f} x {ch/cm:.1f} cm, {cols} x {rows} = {cols*rows} per foglio")
card.save(f"{S}/card-stampa.png")
