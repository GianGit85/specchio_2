import sys, numpy as np, qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
F, OUTDIR = sys.argv[1], sys.argv[2]
URL = "https://giangit85.github.io/Come-fecero-i-greci/?sala=1"
LG = lambda px: ImageFont.truetype(f"{F}/luckiest-guy.ttf", px)
SE = lambda px: ImageFont.truetype(f"{F}/special-elite.ttf", px)
W, H = 2480, 3508            # A4 a 300 dpi
logo_c = Image.open("/home/user/come-fecero-i-greci/assets/logo-copia-incolla.jpg").convert("RGB")

def qr_tondo(lato, logo):
    q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0); q.add_data(URL); q.make(fit=True)
    M = q.get_matrix(); N = len(M); quiet = 3; cell = lato / (N + 2 * quiet)
    img = Image.new("RGB", (lato, lato), "white"); d = ImageDraw.Draw(img)
    occhio = lambda x, y: (x < 7 and y < 7) or (x >= N - 7 and y < 7) or (x < 7 and y >= N - 7)
    lw = int(lato * .23); lh = int(lw * logo.height / logo.width)
    c0, c1 = (lato - lw) / 2 - cell * .6, (lato + lw) / 2 + cell * .6
    r0, r1 = (lato - lh) / 2 - cell * .6, (lato + lh) / 2 + cell * .6
    for y in range(N):
        for x in range(N):
            if not M[y][x] or occhio(x, y): continue
            X, Y = (x + quiet) * cell, (y + quiet) * cell
            if c0 < X + cell / 2 < c1 and r0 < Y + cell / 2 < r1: continue
            p = cell * .08; d.ellipse([X + p, Y + p, X + cell - p, Y + cell - p], fill="black")
    for ox, oy in [(0, 0), (N - 7, 0), (0, N - 7)]:
        X, Y = (ox + quiet) * cell, (oy + quiet) * cell
        d.rounded_rectangle([X, Y, X + 7 * cell, Y + 7 * cell], radius=cell * 2, fill="black")
        d.rounded_rectangle([X + cell, Y + cell, X + 6 * cell, Y + 6 * cell], radius=cell * 1.3, fill="white")
        d.rounded_rectangle([X + 2 * cell, Y + 2 * cell, X + 5 * cell, Y + 5 * cell], radius=cell * .9, fill="black")
    img.paste(logo.resize((lw, lh), Image.LANCZOS), ((lato - lw) // 2, (lato - lh) // 2))
    return img

def cartello(colori):
    if colori:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        nube = lambda cx, cy, r, c, a: np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (r * r)))[..., None] * np.array(c, np.float32) * a
        g = np.zeros((H, W, 3), np.float32); g[:] = (20, 13, 9)
        g += nube(150, 3000, 1400, (255, 90, 200), .3) + nube(2400, 2300, 1300, (79, 216, 255), .24) + nube(1240, 200, 1500, (122, 92, 255), .2)
        im = Image.fromarray(np.clip(g, 0, 255).astype(np.uint8))
        crema, giallo, testo, strati, bordo = (244, 233, 208), (242, 194, 48), (244, 233, 208), [(101,74,38),(122,90,48),(143,108,60),(165,128,75),(184,146,90),(201,164,106)], (107, 74, 34)
        logo = logo_c
    else:
        im = Image.new("RGB", (W, H), "white")
        crema, giallo, testo, strati, bordo = (255, 255, 255), (0, 0, 0), (0, 0, 0), [(0, 0, 0)] * 6, (0, 0, 0)
        logo = ImageEnhance.Contrast(ImageOps.grayscale(logo_c)).enhance(1.6).convert("RGB")
    d = ImageDraw.Draw(im)
    def cen(t, y, f, c): d.text((W / 2 - d.textlength(t, font=f) / 2, y), t, font=f, fill=c)
    def t3d(t, y, px):
        f = LG(px); x = W / 2 - d.textlength(t, font=f) / 2; passo = max(2, px // 22)
        if colori:
            for i, c in enumerate(strati): d.text((x, y + passo * (6 - i)), t, font=f, fill=c)
            d.text((x, y), t, font=f, fill=crema, stroke_width=max(3, px // 32), stroke_fill=bordo)
        else:                                   # lettere vuote con ombra piena, come il biglietto
            d.text((x + px // 14, y + px // 14), t, font=f, fill="black")
            d.text((x, y), t, font=f, fill="white", stroke_width=max(4, px // 22), stroke_fill="black")
    lw = 300; lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS).rotate(-3, expand=True, fillcolor=im.getpixel((10, 10)))
    im.paste(lg, (W // 2 - lg.width // 2, 150)); d = ImageDraw.Draw(im)
    cen("UN GIOCO DI", 470, SE(64), testo)
    t3d("COME FECERO I GRECI", 560, 150)
    cen("Mentre aspetti che si apra il sipario…", 810, SE(78), giallo)
    t3d("CHI ERI NELLA", 930, 230)
    t3d("VITA PRECEDENTE?", 1170, 230)
    # QR su pannello bianco
    Q = 1400; pad = 70
    x0, y0 = (W - Q) // 2, 1500
    d.rounded_rectangle([x0 - pad, y0 - pad, x0 + Q + pad, y0 + Q + pad], radius=60, fill="white", outline=None if colori else "black", width=0 if colori else 8)
    im.paste(qr_tondo(Q, logo), (x0, y0)); d = ImageDraw.Draw(im)
    t3d("INQUADRA E SCOPRILO", y0 + Q + pad + 80, 150)
    cen("3 domande · 20 secondi · gli spiriti sanno tutto", y0 + Q + pad + 290, SE(70), testo)
    cen("e se ti piace, seguici: @copia.in.colla", y0 + Q + pad + 400, SE(66), giallo)
    return im

for colori, nome in [(True, "cartello-sala-quiz-colori"), (False, "cartello-sala-quiz-bn")]:
    im = cartello(colori)
    im.save(f"{OUTDIR}/{nome}.pdf", resolution=300)
    im.resize((W // 4, H // 4)).save(f"{OUTDIR}/../{nome}-anteprima.jpg".replace("/stampa/../", "/"), quality=85) if False else None
    im.save(f"/tmp/claude-0/-home-user/5bdb26ee-678b-59a9-8d32-841d63617df9/scratchpad/{nome}.png")
print("ok")
