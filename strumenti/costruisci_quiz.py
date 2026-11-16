src = open("/home/user/specchio_2/index.html").read()
i = src.index("  // ---------- Suoni (generati al momento, nessun file) ----------"); j = src.index("  // ---------- Sfera 3D", i)
suoni = src[i:j]
SITO = "https://giangit85.github.io/Come-fecero-i-greci/"
pagina = r'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no">
<meta name="theme-color" content="#0b0705">
<title>Chi eri nella vita precedente? 🔮</title>
<meta name="description" content="5 domande, 30 secondi. Gli spiriti sanno tutto. Come fecero i Greci, una commedia di Copia Incolla.">
<meta property="og:type" content="website">
<meta property="og:url" content="__SITO__">
<meta property="og:title" content="Chi eri nella vita precedente? 🔮">
<meta property="og:description" content="5 domande, 30 secondi. Gli spiriti sanno tutto.">
<meta property="og:image" content="__SITO__assets/anteprima.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="it_IT">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/luckiest-guy.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/special-elite.woff2" as="font" type="font/woff2" crossorigin>
<style>
  @font-face { font-family: "Luckiest Guy"; src: url("assets/luckiest-guy.woff2") format("woff2"); font-display: swap; }
  @font-face { font-family: "Special Elite"; src: url("assets/special-elite.woff2") format("woff2"); font-display: swap; }
  :root { --crema: #f4e9d0; --giallo: #f2c230; --rosso: #e04a3a; --carta: #f1e4c8; --inchiostro: #2a1c10;
          --titolo: "Luckiest Guy", "Arial Black", Impact, sans-serif; --macchina: "Special Elite", "Courier New", monospace; }
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body { margin: 0; height: 100%; color: var(--crema); }
  body { font-family: var(--macchina); overflow: hidden; -webkit-user-select: none; user-select: none;
         background: radial-gradient(ellipse at 50% 40%, #2a1c13 0%, #120c08 55%, #070504 100%); }
  .fumo { position: fixed; inset: -20%; pointer-events: none; z-index: 0; }
  .fumo i { position: absolute; width: 70vmax; height: 70vmax; border-radius: 50%; opacity: .22; }
  .fumo i:nth-child(1) { background: radial-gradient(circle, #ff5ac8 0%, transparent 62%); left: -10%; bottom: 0; animation: deriva1 18s ease-in-out infinite alternate; }
  .fumo i:nth-child(2) { background: radial-gradient(circle, #4fd8ff 0%, transparent 62%); right: -15%; bottom: 10%; animation: deriva2 22s ease-in-out infinite alternate; }
  .fumo i:nth-child(3) { background: radial-gradient(circle, #7a5cff 0%, transparent 62%); left: 20%; top: -10%; opacity: .16; animation: deriva1 26s ease-in-out infinite alternate-reverse; }
  .schermata { position: fixed; inset: 0; z-index: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 14px; text-align: center; padding: max(16px, env(safe-area-inset-top)) 20px max(16px, env(safe-area-inset-bottom));
    opacity: 0; pointer-events: none; transition: opacity .5s ease; }
  .schermata.attiva { opacity: 1; pointer-events: auto; }
  .piccolo { font-size: .78rem; letter-spacing: .25em; opacity: .85; }
  .logo { width: 96px; transform: rotate(-3deg); box-shadow: 0 6px 18px rgba(0,0,0,.6); border-radius: 2px; }
  .titolo { font-family: var(--titolo); font-weight: normal; margin: 0; font-size: clamp(2.1rem, 11vw, 3.3rem); line-height: .98; color: var(--crema);
    -webkit-text-stroke: 1px #6b4a22;
    text-shadow: 0 1px 0 #c9a46a, 0 2px 0 #b8925a, 0 3px 0 #a5804b, 0 4px 0 #8f6c3c, 0 5px 0 #7a5a30, 0 6px 0 #654a26, 0 10px 18px rgba(0,0,0,.7); }
  .titolo.mini { font-size: clamp(1.3rem, 6.5vw, 1.8rem); }
  .domanda-grande { font-family: var(--titolo); color: var(--giallo); font-size: clamp(1.5rem, 7.5vw, 2.1rem); line-height: 1.1; text-shadow: 0 3px 0 #6b4a10; margin: 6px 0 0; }
  .sotto { font-size: 1rem; opacity: .85; max-width: 20em; line-height: 1.45; }
  .amico { background: var(--carta); color: var(--inchiostro); padding: 12px 16px; max-width: 22em; transform: rotate(-1.5deg);
    box-shadow: 4px 6px 0 rgba(0,0,0,.45); font-size: .95rem; line-height: 1.4; }
  .amico b { color: #c22f26; }
  .bottone { font-family: var(--titolo); font-size: 1.15rem; letter-spacing: .05em; color: #1d1d1d; background: var(--giallo);
    border: none; border-radius: 14px; padding: 15px 30px; cursor: pointer; text-decoration: none; display: inline-block;
    box-shadow: 0 5px 0 #8a6a10, 0 9px 18px rgba(0,0,0,.6); transition: transform .1s ease, box-shadow .1s ease; }
  .bottone:active { transform: translateY(4px); box-shadow: 0 1px 0 #8a6a10, 0 4px 10px rgba(0,0,0,.6); }
  .bottone.whatsapp { background: #25d366; color: #fff; box-shadow: 0 5px 0 #128c4a, 0 9px 18px rgba(0,0,0,.6); text-shadow: 0 1px 2px rgba(0,0,0,.25); }
  .bottone.whatsapp:active { box-shadow: 0 1px 0 #128c4a, 0 4px 10px rgba(0,0,0,.6); }
  .bottone.prenota { background: var(--rosso); color: #fff; box-shadow: 0 5px 0 #7a1d14, 0 9px 18px rgba(0,0,0,.6); }
  .bottone.prenota:active { box-shadow: 0 1px 0 #7a1d14, 0 4px 10px rgba(0,0,0,.6); }
  .link { background: none; border: none; color: #bbb; font-family: var(--macchina); font-size: .9rem; text-decoration: underline; cursor: pointer; padding: 8px; }
  .nascosto { opacity: 0 !important; pointer-events: none !important; }
  .audio { position: fixed; z-index: 10; top: max(10px, env(safe-area-inset-top)); right: 12px; width: 40px; height: 40px; border-radius: 50%;
    border: 1px solid rgba(244,233,208,.35); background: rgba(0,0,0,.35); color: var(--crema); font-size: 18px; cursor: pointer; padding: 0; }

  /* Domande */
  .avanzamento { display: flex; gap: 8px; }
  .avanzamento i { width: 10px; height: 10px; border-radius: 50%; background: rgba(244,233,208,.25); }
  .avanzamento i.fatto { background: var(--giallo); }
  .testo-domanda { font-family: var(--titolo); font-size: clamp(1.45rem, 7vw, 2rem); line-height: 1.15; max-width: 14em; min-height: 2.4em;
    display: flex; align-items: center; justify-content: center; color: var(--crema); text-shadow: 0 3px 0 #654a26; }
  .risposte { display: flex; flex-direction: column; gap: 14px; width: min(100%, 360px); }
  .risposta { font-family: var(--macchina); font-size: 1.08rem; color: var(--inchiostro); background: var(--carta); border: none; padding: 16px 14px;
    cursor: pointer; box-shadow: 4px 5px 0 rgba(0,0,0,.45); transition: transform .12s ease; animation: entra .45s ease both; }
  .risposta:nth-child(1) { transform: rotate(-1.2deg); animation-delay: .05s; }
  .risposta:nth-child(2) { transform: rotate(.8deg); animation-delay: .15s; }
  .risposta:nth-child(3) { transform: rotate(-.6deg); animation-delay: .25s; }
  .risposta:active, .risposta.scelta { transform: scale(.96) rotate(0); background: var(--giallo); }

  /* Attesa */
  .attesa { font-size: 1.15rem; line-height: 1.6; max-width: 18em; }
  .puntini::after { content: ""; animation: puntini 1.2s steps(4) infinite; }

  /* Risultato */
  .intro-ris { font-size: 1.1rem; min-height: 1.5em; }
  .risultato { font-family: var(--titolo); font-weight: normal; margin: 0; max-width: 13em; font-size: clamp(1.7rem, 8.2vw, 2.5rem); line-height: 1.08; color: var(--crema);
    -webkit-text-stroke: 1px #6b4a22; text-shadow: 0 1px 0 #c9a46a, 0 2px 0 #b8925a, 0 3px 0 #a5804b, 0 4px 0 #8f6c3c, 0 8px 14px rgba(0,0,0,.7); }
  .risultato.appare { animation: appare .7s cubic-bezier(.3,1.5,.5,1) both; }
  .gancio { font-size: .98rem; max-width: 21em; line-height: 1.45; font-style: italic; opacity: .9; }
  .azioni { display: flex; flex-direction: column; align-items: center; gap: 12px; }

  /* Pagina iniziale: prima il gioco */
  .firma { display: flex; align-items: center; gap: 10px; margin-top: 18px; font-size: .78rem; opacity: .8; text-align: left; line-height: 1.35; }
  .firma img { width: 46px; transform: rotate(-3deg); box-shadow: 0 3px 8px rgba(0,0,0,.6); }
  /* Esito: pagina che scorre */
  #esito { justify-content: flex-start; overflow-y: auto; -webkit-overflow-scrolling: touch; padding-top: max(28px, env(safe-area-inset-top)); padding-bottom: 40px; }
  .ponte { font-family: var(--titolo); color: var(--giallo); font-size: clamp(1.15rem, 5.6vw, 1.5rem); line-height: 1.15; text-shadow: 0 2px 0 #6b4a10; max-width: 16em; margin: 10px 0 0; }
  .confronto { background: var(--carta); color: var(--inchiostro); padding: 10px 14px; max-width: 22em; transform: rotate(1deg); box-shadow: 4px 6px 0 rgba(0,0,0,.45); font-size: .9rem; line-height: 1.45; text-align: left; }
  .confronto b { color: #c22f26; }
  .legame-intro { display: block; margin-top: 10px; font-size: .85rem; opacity: .85; }
  .legame { display: block; margin-top: 4px; font-family: var(--titolo); font-size: 1.15rem; line-height: 1.2; color: #2a1c10; text-transform: uppercase; }
  .confronto { text-align: center; }
  .scheda { width: min(100%, 380px); background: rgba(0,0,0,.35); border: 1px solid rgba(244,233,208,.2); border-radius: 14px; padding: 12px 12px 18px;
    display: flex; flex-direction: column; align-items: center; gap: 9px; }
  .locandina { width: 100%; margin-top: 8px; border-radius: 8px; box-shadow: 0 8px 22px rgba(0,0,0,.6); }
  .sinossi { font-size: .95rem; line-height: 1.5; max-width: 22em; }
  .quando { font-family: var(--titolo); color: var(--giallo); font-size: 1.15rem; text-shadow: 0 2px 0 #6b4a10; line-height: 1.2; }
  .dove { font-family: var(--titolo); color: var(--rosso); font-size: 1rem; text-shadow: 0 2px 0 #5a140e; }
  .sfida { font-size: .95rem; opacity: .9; margin: 10px 0 0; }
  .toast { position: fixed; z-index: 20; left: 12px; right: 12px; bottom: max(14px, env(safe-area-inset-bottom)); background: var(--carta); color: var(--inchiostro);
    border-radius: 14px; padding: 14px; box-shadow: 0 10px 30px rgba(0,0,0,.6); display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center;
    transform: translateY(140%); transition: transform .45s cubic-bezier(.3,1.3,.5,1); }
  .toast.su { transform: none; }
  .toast p { margin: 0; font-size: 1rem; line-height: 1.4; }
  .toast .chiudi { position: absolute; top: 4px; right: 10px; background: none; border: none; font-size: 1.3rem; color: var(--inchiostro); cursor: pointer; }
  @keyframes deriva1 { to { transform: translate(18vw, -12vh) scale(1.15); } }
  @keyframes deriva2 { to { transform: translate(-20vw, -18vh) scale(1.2); } }
  @keyframes entra { from { opacity: 0; translate: 0 18px; } to { opacity: 1; translate: 0 0; } }
  @keyframes appare { from { opacity: 0; transform: scale(.6) rotate(-4deg); } to { opacity: 1; transform: none; } }
  @keyframes puntini { 0% { content: ""; } 25% { content: "."; } 50% { content: ".."; } 75% { content: "..."; } }
</style>
</head>
<body>
<div class="fumo"><i></i><i></i><i></i></div>
<button id="btnAudio" class="audio" aria-label="Suoni">🔊</button>
<script src="quiz.js"></script>

<!-- 1. INIZIO -->
<section id="inizio" class="schermata attiva">
  <div id="amico" class="amico" style="display:none"></div>
  <h1 class="titolo">CHI ERI NELLA<br>VITA PRECEDENTE?</h1>
  <p class="sotto">5 domande. Gli spiriti sanno tutto.</p>
  <button id="btnInizia" class="bottone">Scoprilo in 30 secondi 🔮</button>
  <div class="firma"><img src="assets/logo-copia-incolla.jpg" alt=""><span>Un gioco di <b>Come fecero i Greci</b><br>commedia teatrale di Copia Incolla</span></div>
</section>

<!-- 2. DOMANDE -->
<section id="quiz" class="schermata">
  <h2 class="titolo mini">COME FECERO I GRECI</h2>
  <div class="avanzamento" id="avanzamento"></div>
  <div class="testo-domanda" id="testoDomanda"></div>
  <div class="risposte" id="risposte"></div>
</section>

<!-- 3. ATTESA -->
<section id="consulto" class="schermata">
  <p class="attesa">Gli spiriti stanno consultando<br>l'archivio delle vite passate<span class="puntini"></span></p>
</section>

<!-- 4. RISULTATO -->
<section id="esito" class="schermata">
  <h2 class="titolo mini">COME FECERO I GRECI</h2>
  <p class="intro-ris" id="introRis"></p>
  <h3 class="risultato nascosto" id="risultato"></h3>
  <div class="azioni nascosto" id="azioni">
    <div id="confronto" class="confronto" style="display:none"></div>
    <p class="ponte">Non sei l'unico tornato da una vita precedente…</p>
    <div class="scheda">
      <div class="quando" id="quando"></div>
      <div class="dove" id="dove"></div>
      <a id="btnPrenota" class="bottone prenota" target="_blank" rel="noopener">🎟️ Prenota il tuo posto</a>
      <img class="locandina" src="assets/locandina.jpg" alt="Locandina di Come fecero i Greci">
      <p class="sinossi"><b>Come fecero i Greci</b>, una commedia di Copia Incolla.<br>Spie italiane degli anni '40, tutte reincarnate, in una missione impossibile tra sedute spiritiche, travestimenti e gelati.</p>
    </div>
    <p class="sfida">Scopri chi erano i tuoi amici:</p>
    <a id="btnWhatsapp" class="bottone whatsapp" target="_blank" rel="noopener">Sfida un amico su WhatsApp</a>
    <button id="btnRifai" class="link">Rifai il quiz</button>
  </div>
</section>

<!-- Invito a condividere quando si torna dal modulo di prenotazione -->
<div id="toast" class="toast">
  <button class="chiudi" id="chiudiToast" aria-label="Chiudi">×</button>
  <p><b>Posto prenotato?</b> 🎉<br>Ora scopri chi erano i tuoi amici!</p>
  <a id="btnWhatsapp2" class="bottone whatsapp" target="_blank" rel="noopener">Sfida un amico su WhatsApp</a>
</div>

<script>
(() => {
  // ====== DATI: per una replica basta cambiare queste righe ======
  const SITO = "__SITO__";
  const PRENOTA = "https://forms.gle/PsdN4vKsmonuJ4nEA";
  const QUANDO = "20 NOVEMBRE 2026 · ORE 21:00";
  const DOVE = "TEATRO SANT'ANNA · VIA BRIONE 40, TORINO";
  // ===============================================================
  const DOMANDE = window.DOMANDE, RISULTATI = window.RISULTATI;
  const $ = id => document.getElementById(id);
  const attesa = ms => new Promise(ok => setTimeout(ok, ms));
  let risposte = [], occupato = false;

  function mostra(id) { document.querySelectorAll(".schermata").forEach(s => s.classList.toggle("attiva", s.id === id)); }
  async function scrivi(el, testo, vel = 38) {
    el.textContent = "";
    for (let i = 1; i <= testo.length; i++) {
      el.textContent = testo.slice(0, i);
      const ch = testo[i - 1];
      if (ch !== "…") try { suono.tasto(ch); } catch (_) {}
      await attesa(ch === "…" ? 350 : ch === " " ? 45 : vel);
    }
  }

  // Arrivo dal link di un amico: ?r=numero
  const r = parseInt(new URLSearchParams(location.search).get("r"), 10);
  const amico = (r >= 1 && r <= RISULTATI.length) ? RISULTATI[r - 1] : null;
  if (amico) {
    const a = $("amico"); a.style.display = "";
    a.innerHTML = `Un tuo amico nella vita precedente era <b>${amico}</b>…<br>e gli spiriti hanno detto qualcosa anche su di te 🔒<br>Rispondi alle 5 domande per scoprirlo.`;
  }
  $("btnPrenota").href = PRENOTA;
  $("quando").textContent = QUANDO; $("dove").textContent = DOVE;
  // Chi va a prenotare e poi torna sulla pagina riceve l'invito a sfidare gli amici
  let haPrenotato = false;
  $("btnPrenota").addEventListener("click", () => { haPrenotato = true; });
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible" && haPrenotato) { haPrenotato = false; setTimeout(() => $("toast").classList.add("su"), 500); }
  });
  $("chiudiToast").addEventListener("click", () => $("toast").classList.remove("su"));
  $("btnWhatsapp2").addEventListener("click", () => $("toast").classList.remove("su"));

  $("btnInizia").addEventListener("click", () => { suono.avvia(); suono.carta(); risposte = []; domanda(); });
  $("btnRifai").addEventListener("click", () => { suono.carta(); risposte = []; domanda(); });

  function domanda() {
    const n = risposte.length, d = DOMANDE[n];
    $("avanzamento").innerHTML = DOMANDE.map((_, i) => `<i class="${i <= n ? "fatto" : ""}"></i>`).join("");
    $("testoDomanda").textContent = d.testo;
    $("risposte").innerHTML = d.risposte.map((t, i) => `<button class="risposta" data-i="${i}">${t}</button>`).join("");
    $("risposte").querySelectorAll(".risposta").forEach(b => b.addEventListener("click", () => scegli(b)));
    mostra("quiz"); occupato = false;
  }

  async function scegli(b) {
    if (occupato) return; occupato = true;
    b.classList.add("scelta"); suono.carta();
    risposte.push(+b.dataset.i);
    await attesa(280);
    if (risposte.length < DOMANDE.length) domanda(); else esito();
  }

  async function esito() {
    mostra("consulto");
    await attesa(1900);
    const n = window.calcolaRisultato(risposte), testo = RISULTATI[n - 1];
    $("risultato").classList.add("nascosto"); $("risultato").classList.remove("appare");
    $("azioni").classList.add("nascosto"); $("introRis").textContent = "";
    mostra("esito");
    await attesa(400);
    await scrivi($("introRis"), "Nella vita precedente eri…");
    await attesa(250);
    $("risultato").textContent = testo.charAt(0).toUpperCase() + testo.slice(1);
    $("risultato").classList.remove("nascosto"); $("risultato").classList.add("appare");
    suono.rivela(); if (navigator.vibrate) navigator.vibrate([40, 60, 90]);
    const messaggio = `Ho scoperto chi ero nella vita precedente: ${testo} 😂\n…e gli spiriti hanno detto qualcosa anche su di te 👀 Scopri cosa 👉 ${SITO}r/${n}.html\n(è il gioco di Come fecero i Greci, spettacolo teatrale)`;
    $("btnWhatsapp").href = $("btnWhatsapp2").href = "https://wa.me/?text=" + encodeURIComponent(messaggio);
    if (amico) {
      $("confronto").style.display = "";
      $("confronto").innerHTML = `Tu: <b>${testo}</b><br>Il tuo amico: <b>${amico}</b>
        <span class="legame-intro">E gli spiriti dicono che nella vita precedente voi due eravate…</span>
        <span class="legame">${window.calcolaLegame(n, r)}</span>`;
    }
    $("esito").scrollTop = 0;
    await attesa(900);
    $("azioni").classList.remove("nascosto");
  }

SUONI
})();
</script>
</body>
</html>
'''
pagina = pagina.replace("__SITO__", SITO).replace("SUONI", suoni)
open("/home/user/come-fecero-i-greci/index.html", "w").write(pagina)

# Una pagina per ogni risultato: serve solo a dare l'anteprima giusta su WhatsApp, poi porta al quiz
import os, html, json, subprocess
ris = json.loads(subprocess.check_output(["node", "-e",
    "global.window={};require('/home/user/come-fecero-i-greci/quiz.js');console.log(JSON.stringify(window.RISULTATI))"]))
os.makedirs("/home/user/come-fecero-i-greci/r", exist_ok=True)
for n, t in enumerate(ris, 1):
    tit = html.escape(f"Nella vita precedente ero {t} 😂", quote=True)
    open(f"/home/user/come-fecero-i-greci/r/{n}.html", "w").write(f'''<!DOCTYPE html>
<html lang="it"><head><meta charset="UTF-8">
<title>{tit}</title>
<meta property="og:type" content="website">
<meta property="og:url" content="{SITO}r/{n}.html">
<meta property="og:title" content="{tit}">
<meta property="og:description" content="…e gli spiriti hanno detto qualcosa anche su di te 👀">
<meta property="og:image" content="{SITO}assets/r/{n}.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0; url=../?r={n}">
<script>location.replace("../?r={n}");</script>
</head><body></body></html>
''')
print(len(ris), "risultati")
