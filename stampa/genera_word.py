"""Genera stampa/biglietti.docx: un A4 con 30 biglietti QR (5 x 6) da 3,9 cm, bordo a bordo.
Uso: python3 stampa/genera_word.py  (dalla cartella della repo)"""
import os, tempfile
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

URL = "https://giangit85.github.io/specchio_2/"
QUI = os.path.dirname(os.path.abspath(__file__)); RADICE = os.path.dirname(QUI)
TMP = tempfile.mkdtemp()
COLONNE, RIGHE, LARGHEZZA_CM = 5, 6, 3.9
DPI = 600                                            # immagini nitide in stampa

ttf = os.path.join(TMP, "lg.ttf")
f = TTFont(os.path.join(RADICE, "assets", "luckiest-guy.woff2")); f.flavor = None; f.save(ttf)
LG = lambda px: ImageFont.truetype(ttf, px)
NERO, BIANCO = (0, 0, 0), (255, 255, 255)
logo = ImageEnhance.Contrast(ImageOps.grayscale(Image.open(os.path.join(RADICE, "assets", "logo-copia-incolla.jpg")))).enhance(1.6).convert("RGB")
q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0); q.add_data(URL); q.make(fit=True)
M = q.get_matrix(); N = len(M)

def biglietto(W):
    quiet = 3
    cell = W / (N + 2 * quiet)
    tpx = int(W * .105); fnt = LG(tpx)
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    while tmp.textlength("COME FECERO I GRECI", font=fnt) > W * .9: tpx -= 2; fnt = LG(tpx)
    top = int(W * .035); qy = top + int(tpx * 1.15); H = int(qy + W)
    img = Image.new("RGB", (W, H), BIANCO); d = ImageDraw.Draw(img)
    x = (W - d.textlength("COME FECERO I GRECI", font=fnt)) / 2
    d.text((x + tpx // 14, top + tpx // 14), "COME FECERO I GRECI", font=fnt, fill=NERO)
    d.text((x, top), "COME FECERO I GRECI", font=fnt, fill=BIANCO, stroke_width=max(2, tpx // 22), stroke_fill=NERO)
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

card = biglietto(round(LARGHEZZA_CM / 2.54 * DPI))
px = lambda cm: round(cm / 2.54 * DPI)
w_cm = LARGHEZZA_CM; h_cm = w_cm * card.height / card.width
MARGINE = .5                                            # margine pagina (la stampante non arriva al bordo)
AREA_W, AREA_H = 21 - 2 * MARGINE, 29.6 - 2 * MARGINE  # 1 mm di riserva per non creare una seconda pagina

# Una sola immagine a tutta pagina: impaginazione identica in Word, LibreOffice e in stampa
pag = Image.new("L", (px(AREA_W), px(AREA_H)), 255); d = ImageDraw.Draw(pag)
cw, ch = card.size
x0 = (pag.width - COLONNE * cw) // 2; y0 = (pag.height - RIGHE * ch) // 2
for r in range(RIGHE):
    for c in range(COLONNE): pag.paste(card.convert("L"), (x0 + c * cw, y0 + r * ch))
# linee di taglio da bordo a bordo: si taglia sempre per tutta la larghezza/altezza del foglio
for c in range(COLONNE + 1):
    x = x0 + c * cw; d.line([x, 0, x, pag.height], fill=165, width=3)
for r in range(RIGHE + 1):
    y = y0 + r * ch; d.line([0, y, pag.width, y], fill=165, width=3)
png = os.path.join(TMP, "pagina.png"); pag.save(png, dpi=(DPI, DPI), optimize=True)

doc = Document()
sez = doc.sections[0]
sez.page_width, sez.page_height = Cm(21), Cm(29.7)
sez.left_margin = sez.right_margin = sez.top_margin = sez.bottom_margin = Cm(MARGINE)
sez.header_distance = sez.footer_distance = Cm(0)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
pf = p.paragraph_format; pf.space_before = pf.space_after = Pt(0); pf.line_spacing = 1
p.add_run().add_picture(png, width=Cm(AREA_W), height=Cm(AREA_H))
out = os.path.join(QUI, "biglietti.docx"); doc.save(out)
print(f"{out}: {COLONNE * RIGHE} biglietti da {w_cm:.1f} x {h_cm:.2f} cm")
