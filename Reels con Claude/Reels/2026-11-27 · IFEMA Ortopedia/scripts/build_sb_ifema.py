"""Storyboard IFEMA · 5 versiones. Genera un HTML autocontenido (fotogramas y demo de música incrustados)."""
import base64, html, os, subprocess
O = "/tmp/claude-0/-home-user-editor-videos/d01835c0-842d-5f46-b60e-65aa20332005/scratchpad/ifema"
D = "/home/user/editor-videos/Reels con Claude/Tomas/2026-11-27 · IFEMA Ortopedia"

# clave: (archivo, duración, papel, qué se ve, segundo del fotograma)
C = {
 "9703": ("IMG_9703.MOV", 4.1, "Aparcamiento", "Primer plano del maletero cerrándose", 2.0),
 "9762": ("IMG_9762.MOV", 12.8, "Aparcamiento · VOZ", "Actor con el exo cierra el maletero y habla a cámara", 8.0),
 "9757": ("IMG_9757.MOV", 4.8, "Primer plano", "Se abrocha la hebilla del cinturón", 2.0),
 "9758": ("IMG_9758.MOV", 4.6, "Primer plano", "Ajuste de la cincha del muslo", 2.0),
 "9759": ("IMG_9759.MOV", 6.9, "Primer plano", "Correa y cincha del muslo", 3.0),
 "9766": ("IMG_9766.MOV", 12.5, "Movimiento", "Dos personas con el exo andando hacia el pabellón", 4.0),
 "9767": ("IMG_9767.MOV", 8.8, "Aparcamiento", "Los dos mirando a cámara (se oye al director)", 3.0),
 "9709": ("IMG_9709.mov", 1.0, "Interior", "Cartel «Orto Medical Care · PAB-12»", 0.8),
 "9713": ("IMG_9713.MOV", 5.9, "Movimiento", "Cámara en marcha por el pabellón", 2.0),
 "9714": ("IMG_9714.MOV", 2.7, "Movimiento", "Maniquíes con el exo en un stand", 1.0),
 "9715": ("IMG_9715.mov", 4.2, "Movimiento", "Cámara en marcha, el movimiento más rápido", 1.8),
 "9716": ("IMG_9716.mov", 2.7, "Prueba · VOZ", "Le ponen el exo a un visitante («como el Play…»)", 1.2),
 "9719": ("IMG_9719.mov", 3.0, "Prueba · VOZ", "Primer plano de la cadera y la app", 1.2),
 "9734": ("IMG_9734.MOV", 12.8, "Prueba · VOZ", "Se lo pone y explica el modo estándar", 5.0),
 "9735": ("IMG_9735.MOV", 13.9, "Prueba · VOZ", "Camina y el exo copia su ritmo", 6.0),
 "9737": ("IMG_9737.MOV", 2.1, "Primer plano", "Manos ajustando la cincha de la rodilla", 1.0),
 "9743": ("IMG_9743.mov", 3.9, "Prueba · VOZ", "Visitante: «como si fuese un títere»", 2.0),
 "9744": ("IMG_9744.MOV", 4.4, "Prueba · VOZ", "Grupo con exos: «como una persona sana»", 2.6),
}
def thumb(k):
    f = f"{O}/t_{k}.jpg"
    if not os.path.exists(f):
        src = os.path.join(D, C[k][0])
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(C[k][4]), "-i", src, "-frames:v", "1",
                        "-vf", "scale=180:320:force_original_aspect_ratio=increase,crop=180:320", "-q:v", "7", f], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode()
T = {k: thumb(k) for k in C}
audio = "data:audio/mpeg;base64," + base64.b64encode(open(f"{O}/demo_rock_152bpm.mp3", "rb").read()).decode()

# ------------------------------------------------------------------ variantes
V = [
 dict(n="A", nombre="Crónica al ritmo", dur="≈ 45 s", musica="Rock garaje · 152 bpm", texto="NOS VAMOS A IFEMA", voz="Actor + 5 pruebas",
      idea="La versión de referencia: sigue el orden que me has contado. Cortes a golpe de música y cámara que se escapa de un plano al siguiente.",
      seg=[("Maletero", 3, "c"), ("Actor", 6, "v"), ("Cómo se pone", 6, "c"), ("Pabellón", 7, "c"), ("Pruebas", 17, "v"), ("Remate", 4, "c"), ("Cierre", 2, "x")],
      esc=[
       ("0:00–0:03", "Golpe de maletero", ["9703"], "El maletero se cierra en primer plano. La puerta golpea en el tiempo 1 y entra la batería. Zoom rápido del 8 % sobre el golpe.", "«NOS VAMOS A IFEMA» entra a golpe en el tiempo 3.", "Golpe de la puerta + bombo."),
       ("0:03–0:09", "Hemos venido a IFEMA", ["9762"], "El actor ya con el exo, mirando a cámara. Recorto lo que dice el director antes y me quedo desde que cierra el maletero.", "Subtítulos de 1-3 palabras. IFEMA, EQUIPOS y TECNOLOGÍA en lima.", "Voz del actor. La música baja sola mientras habla."),
       ("0:09–0:15", "Cómo se pone", ["9757", "9758", "9759", "9737"], "Cuatro primeros planos de ≈1,5 s. El cierre del maletero enlaza con el cierre de la hebilla (corte por acción).", "«1 CINTURA · 2 MUSLO · 3 CORREA · 4 RODILLA», un rótulo por golpe.", "Un clic seco de hebilla en cada corte, a tempo. Sin voz."),
       ("0:15–0:22", "Entramos al pabellón", ["9766", "9709", "9713", "9715", "9714"], "Cada corte se esconde en el giro brusco de la cámara: el plano sale en el barrido y el siguiente entra por el mismo lado.", "Sin texto: el cartel PAB-12 ya habla.", "Whoosh en cada corte."),
       ("0:22–0:39", "Las pruebas", ["9716", "9743", "9734", "9735", "9744"], "Cinco tomas de otras personas probándolo. Solo uso su audio.", "Subtítulos con una palabra clave por frase: PLAY, TÍTERE, RITMO, CADENCIA, SANA.", "Voz de las pruebas. La música baja a un hilo y vuelve a subir en cada corte."),
       ("0:39–0:43", "Remate", ["9719", "9743", "9744", "9714"], "Cuatro cortes de 1 s, sin voz. La música vuelve a subir.", "Tarjeta lima: «Descubre cómo probarlo · Consúltanos por WhatsApp».", "Riser y golpe final."),
       ("0:43–0:45", "Cierre", [], "Logo, «Libertad de movimiento» y exomov.com.", "—", "Acorde final de guitarra."),
      ]),
 dict(n="B", nombre="Relámpago", dur="≈ 30 s", musica="Rock garaje · 168 bpm (más rápido)", texto="EXOESQUELETOS EN IFEMA", voz="Actor + 2 pruebas",
      idea="Todo más corto y más rápido: pensado para que casi nadie se vaya antes del final. Se queda con lo más visual y con las dos frases más curiosas.",
      seg=[("Maletero", 2, "c"), ("Actor", 3, "v"), ("Cómo se pone", 6, "c"), ("Pabellón", 5, "c"), ("Pruebas", 10, "v"), ("Cierre", 4, "x")],
      esc=[
       ("0:00–0:02", "Golpe de maletero", ["9703"], "Maletero cerrándose y zoom rápido al golpe.", "«EXOESQUELETOS EN IFEMA» en dos líneas.", "Golpe + bombo."),
       ("0:02–0:05", "Hemos venido a IFEMA", ["9762"], "Solo la primera mitad de la frase: «hemos venido a IFEMA para dar a conocer nuestros equipos».", "IFEMA y EQUIPOS en lima.", "Voz del actor."),
       ("0:05–0:11", "Cómo se pone, a ráfagas", ["9757", "9758", "9759", "9737", "9719"], "Cortes de medio segundo, dos por cada plano, para que el ojo no pueda descansar.", "Rótulos: CINTURA · MUSLO · RODILLA · APP.", "Un clic por corte."),
       ("0:11–0:16", "Barrido por el pabellón", ["9766", "9715", "9713", "9714", "9709"], "Cinco planos de 1 s unidos por el movimiento de cámara.", "—", "Whoosh en cada corte."),
       ("0:16–0:26", "Las dos pruebas", ["9743", "9744", "9734", "9735"], "Solo dos frases con voz: «como si fuese un títere que te están manejando desde arriba» y «ese es el modo como una persona sana». Entre medias, 1,5 s de cada uno andando.", "TÍTERE y SANA en lima.", "Voz y música baja; sube en los planos sin voz."),
       ("0:26–0:30", "Cierre", [], "Tarjeta lima de WhatsApp (2,5 s) y logo (1,5 s).", "«Descubre cómo probarlo».", "Golpe final."),
      ]),
 dict(n="C", nombre="Empieza por la prueba", dur="≈ 40 s", musica="Indie · 128 bpm (más abierto)", texto="¿COMO UN TÍTERE?", voz="Actor + 4 pruebas",
      idea="El gancho es la frase más rara de todo el material, en silencio y sin música. Después «rebobinamos» al aparcamiento y contamos el día.",
      seg=[("Gancho", 5, "v"), ("Rebobinado", 5, "v"), ("Cómo se pone", 6, "c"), ("Pabellón", 5, "c"), ("Pruebas", 15, "v"), ("Cierre", 4, "x")],
      esc=[
       ("0:00–0:05", "La frase", ["9743"], "Empieza directamente con la visitante: «como si fuese un títere que te están manejando desde arriba». Sin música.", "«¿COMO UN TÍTERE?» grande, en lima y blanco.", "Solo la voz, un segundo de silencio."),
       ("0:05–0:10", "Rebobinamos", ["9703", "9762"], "Efecto de cinta hacia atrás hasta el maletero y el actor: «hemos venido a IFEMA para dar a conocer nuestros equipos».", "«NOS VAMOS A IFEMA».", "Sonido de cinta rebobinando y entra la música indie."),
       ("0:10–0:16", "Cómo se pone", ["9757", "9758", "9759"], "Tres primeros planos de 2 s, algo más sosegados que en la versión A.", "«1 CINTURA · 2 MUSLO · 3 CORREA».", "Un clic por plano."),
       ("0:16–0:21", "Pabellón", ["9709", "9713", "9715", "9714"], "Barridos de cámara.", "—", "Whoosh."),
       ("0:21–0:36", "Las pruebas", ["9716", "9734", "9735", "9744"], "Cuatro tomas con voz, con la música muy baja.", "Palabras clave en lima.", "Voz de las pruebas."),
       ("0:36–0:40", "Cierre", ["9743"], "Vuelve la visitante, ahora sin voz, y cae la tarjeta de WhatsApp y el logo.", "«Descubre cómo probarlo».", "Golpe final."),
      ]),
 dict(n="D", nombre="Un día en IFEMA", dur="≈ 60 s", musica="Rock garaje · 140 bpm (más pesado)", texto="UN DÍA EN IFEMA", voz="Actor + 6 pruebas",
      idea="La versión larga, con todo el material. Para ver si la gente aguanta un minuto cuando el ritmo no se detiene.",
      seg=[("Maletero", 4, "c"), ("Actor", 7, "v"), ("Cómo se pone", 8, "c"), ("Camino", 6, "c"), ("Pabellón", 6, "c"), ("Pruebas", 25, "v"), ("Cierre", 4, "x")],
      esc=[
       ("0:00–0:04", "Golpe de maletero", ["9703"], "Maletero y zoom al golpe.", "«UN DÍA EN IFEMA».", "Golpe + bombo."),
       ("0:04–0:11", "Hemos venido a IFEMA", ["9762"], "La frase completa del actor, hasta «a los profesionales del sector».", "IFEMA, EQUIPOS, TECNOLOGÍA y PROFESIONALES en lima.", "Voz del actor."),
       ("0:11–0:19", "Cómo se pone", ["9757", "9758", "9759", "9737"], "Cuatro primeros planos de 2 s.", "«1 CINTURA · 2 MUSLO · 3 CORREA · 4 RODILLA».", "Un clic por corte."),
       ("0:19–0:25", "Camino al pabellón", ["9766", "9767"], "Los dos andando con el exo por el aparcamiento y, al final, mirando a cámara. Silencio el audio de 9767, que se oye al director.", "—", "Música a tope."),
       ("0:25–0:31", "Entramos", ["9709", "9713", "9715", "9714"], "Cortes sobre los barridos de cámara.", "—", "Whoosh."),
       ("0:31–0:56", "Las pruebas, completas", ["9716", "9719", "9734", "9735", "9743", "9744"], "Seis tomas con voz: el Play, la app, el modo estándar, la cadencia, el títere y el modo de persona sana.", "Una palabra clave por frase.", "Voz de las pruebas, con la música casi apagada."),
       ("0:56–1:00", "Cierre", [], "Tarjeta de WhatsApp y logo.", "«Descubre cómo probarlo».", "Acorde final."),
      ]),
 dict(n="E", nombre="Cómo se pone, en 30 s", dur="≈ 30 s", musica="Indie · 128 bpm (otra pista)", texto="CÓMO SE PONE UN EXOESQUELETO", voz="Solo 1 frase",
      idea="La versión de utilidad: casi sin voz, con rótulos grandes que enseñan el orden. Es la que mejor se guarda y se comparte.",
      seg=[("Título", 3, "c"), ("Paso 1", 3, "c"), ("Paso 2", 3, "c"), ("Paso 3", 3, "c"), ("Paso 4", 3, "c"), ("Encender", 7, "v"), ("A andar", 5, "c"), ("Cierre", 3, "x")],
      esc=[
       ("0:00–0:03", "Título", ["9757"], "Abrir con la hebilla en primer plano: clic y zoom rápido.", "«CÓMO SE PONE UN EXOESQUELETO».", "Clic de hebilla + entra la música."),
       ("0:03–0:15", "Cuatro pasos", ["9757", "9758", "9759", "9737"], "Un primer plano de 3 s por paso. El número entra a golpe y la cámara hace un empujón corto.", "«1 CINTURA», «2 MUSLO», «3 CORREA», «4 RODILLA» con el número muy grande.", "Un clic por paso."),
       ("0:15–0:22", "Encender y ajustar", ["9716", "9719"], "La única voz del vídeo: «como el Play, entonces a partir de ahora puedes…», y la app en la cadera.", "«5 ENCENDER» y «6 AJUSTAR».", "Voz y música baja."),
       ("0:22–0:27", "Y a andar", ["9735", "9743"], "Los dos andando, sin voz y con la música a tope.", "«Y A ANDAR».", "Riser y golpe."),
       ("0:27–0:30", "Cierre", [], "Tarjeta de WhatsApp y logo.", "«Descubre cómo probarlo».", "Acorde final."),
      ]),
]

# ------------------------------------------------------------------ HTML
esc = html.escape
cl_html = "".join(
    f'<figure class="clip"><img src="{T[k]}" alt="{esc(v[3])}"><figcaption><b>{v[0].split(".")[0].replace("IMG_", "")}</b> · {v[1]:.1f} s<span>{esc(v[2])}</span></figcaption></figure>'
    for k, v in C.items())
rows = "".join(f'<tr><td><b>{v["n"]}</b> · {esc(v["nombre"])}</td><td>{v["dur"]}</td><td>{esc(v["musica"])}</td><td>{esc(v["texto"])}</td><td>{esc(v["voz"])}</td></tr>' for v in V)
cmp_card = "".join(f'<div class="vc"><h3>{v["n"]} · {esc(v["nombre"])}</h3><dl><dt>Duración</dt><dd>{v["dur"]}</dd><dt>Música</dt><dd>{esc(v["musica"])}</dd><dt>Texto</dt><dd>{esc(v["texto"])}</dd><dt>Voz</dt><dd>{esc(v["voz"])}</dd></dl></div>' for v in V)

def variant(v):
    tot = sum(s for _, s, _ in v["seg"])
    track = "".join(f'<div class="seg k{k}" style="flex:{s}" title="{esc(n)} · {s} s"><span>{esc(n)}</span></div>' for n, s, k in v["seg"])
    sc = ""
    for tm, name, ks, what, txt, snd in v["esc"]:
        th = "".join(f'<img src="{T[k]}" alt="{esc(C[k][3])}" title="IMG_{k}">' for k in ks) or '<div class="logo">EXOMOV</div>'
        lab = " · ".join(ks) if ks else "gráfico"
        sc += f'''<article class="sc"><div class="th">{th}<small>{lab}</small></div>
          <div class="tx"><div class="hd"><span class="mono">{tm}</span><h4>{esc(name)}</h4></div><p>{esc(what)}</p>
          <dl><dt>Texto</dt><dd>{esc(txt)}</dd><dt>Sonido</dt><dd>{esc(snd)}</dd></dl></div></article>'''
    return f'''<section class="var" id="v{v["n"]}"><div class="vh"><span class="vl">{v["n"]}</span><div><h2>{esc(v["nombre"])}</h2>
      <div class="facts"><span class="tag accent">{v["dur"]}</span><span class="tag">{esc(v["musica"])}</span><span class="tag">Texto: {esc(v["texto"])}</span><span class="tag">{esc(v["voz"])}</span></div></div></div>
      <p class="idea">{esc(v["idea"])}</p>
      <div class="track">{track}</div><div class="ticks mono"><span>0:00</span><span>{tot // 2}</span><span>{tot} s</span></div>
      {sc}</section>'''

page = f'''<title>Storyboard IFEMA</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Figtree:wght@400;500;700;800&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: cabecera, material disponible, técnicas y música, comparativa, y una sección larga por versión (línea de tiempo + escenas). Tokens ExoMov. */
:root{{--bg:#f6f6f1;--surface:#fff;--surface-2:#ecece4;--border:#dcdcd1;--border-strong:#a9a99e;--text:#121311;--muted:#5a5a51;--accent:#bebd39;--accent-text:#5c5b16;--accent-soft:#ecebc2;--on-accent-soft:#2c2b0e;--ink:#121311;--paper:#f6f6f1;
 --display:'Bebas Neue',Impact,'Arial Narrow',sans-serif;--body:'Figtree','Segoe UI',system-ui,sans-serif;--mono:'JetBrains Mono',ui-monospace,Menlo,monospace}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#121311;--surface:#1b1c19;--surface-2:#262723;--border:#3a3b35;--border-strong:#5a5a51;--text:#f6f6f1;--muted:#a9a99e;--accent-text:#cdcc5c;--accent-soft:#2c2b0e;--on-accent-soft:#ecebc2;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#121311;--surface:#1b1c19;--surface-2:#262723;--border:#3a3b35;--border-strong:#5a5a51;--text:#f6f6f1;--muted:#a9a99e;--accent-text:#cdcc5c;--accent-soft:#2c2b0e;--on-accent-soft:#ecebc2;color-scheme:dark}}
*{{box-sizing:border-box}}body{{background:var(--bg);color:var(--text);font:16px/1.5 var(--body)}}
.wrap{{max-width:1100px;margin:0 auto;padding-block:48px 96px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:56px}}
h1,h2{{font-family:var(--display);font-weight:400;text-transform:uppercase;letter-spacing:.01em;margin:0;text-wrap:balance}}
h1{{font-size:clamp(44px,8vw,96px);line-height:.92}}h2{{font-size:34px;line-height:1.05}}
h3,h4{{margin:0;font-weight:700}}
.label{{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.lede{{max-width:66ch;color:var(--muted);font-size:18px;margin:16px 0 0}}
.facts{{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}}
.tag{{display:inline-flex;align-items:center;min-height:28px;padding:2px 12px;border-radius:999px;background:var(--surface-2);font-size:12px;font-weight:500}}
.tag.accent{{background:var(--accent-soft);color:var(--on-accent-soft);font-weight:700}}
.mono{{font-family:var(--mono);font-size:13px;font-variant-numeric:tabular-nums}}
.clips{{display:grid;grid-template-columns:repeat(auto-fill,minmax(118px,1fr));gap:12px;margin-top:16px}}
.clip{{margin:0;min-width:0}}.clip img{{width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:8px;display:block;background:var(--surface-2);max-width:100%}}
.clip figcaption{{font-size:12px;line-height:1.35;margin-top:6px;color:var(--muted)}}.clip figcaption b{{color:var(--text)}}.clip figcaption span{{display:block}}
.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}}
.box{{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:24px;min-width:0}}
.box ul{{margin:12px 0 0;padding-left:20px;display:grid;gap:8px}}
.box audio{{width:100%;margin-top:12px}}
.vc{{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:16px;min-width:0}}
.vgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:16px}}
dl{{display:grid;grid-template-columns:max-content minmax(0,1fr);gap:6px 14px;margin:8px 0 0;font-size:14px}}
dt{{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:2px}}dd{{margin:0;min-width:0;overflow-wrap:anywhere}}
.var{{display:grid;gap:14px;padding-top:40px;border-top:2px solid var(--border-strong)}}
.vh{{display:flex;gap:20px;align-items:flex-start}}.vl{{font-family:var(--display);font-size:96px;line-height:.8;color:var(--accent-text)}}
.idea{{margin:0;max-width:70ch;font-size:17px}}
.track{{display:flex;height:40px;border-radius:8px;overflow:hidden;gap:2px}}
.seg{{display:flex;align-items:center;justify-content:center;min-width:0;overflow:hidden;font-size:11px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;background:var(--surface-2);padding:0 2px}}
.seg span{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.seg.kv{{background:var(--accent-soft);color:var(--on-accent-soft)}}.seg.kx{{background:var(--ink);color:var(--paper)}}
.ticks{{display:flex;justify-content:space-between;color:var(--muted)}}
.sc{{display:grid;grid-template-columns:minmax(0,312px) minmax(0,1fr);gap:20px;padding:16px;background:var(--surface);border:1px solid var(--border);border-radius:14px}}
.th{{display:flex;flex-wrap:wrap;gap:6px;align-content:flex-start}}.th img{{width:56px;aspect-ratio:9/16;object-fit:cover;border-radius:6px}}
.th small{{width:100%;font:500 11px/1.3 var(--mono);color:var(--muted)}}.logo{{width:100%;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;background:var(--ink);color:var(--paper);font-family:var(--display);font-size:32px;border-radius:8px}}
.hd{{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline}}.tx p{{margin:6px 0 0}}
@media (max-width:640px){{.sc{{grid-template-columns:1fr}}.vl{{font-size:64px}}}}
footer{{color:var(--muted);font-size:14px}}
</style>
<div class="wrap">
 <header>
  <div class="label">ExoMov · Evento en IFEMA · Storyboard para aprobar</div>
  <h1>IFEMA<br>en 5 versiones</h1>
  <p class="lede">He visto los 18 clips. Aquí tienes cinco montajes distintos con el mismo material. Cambian la duración, la música, el texto del gancho y cuánta voz llevan, para que puedas probar cuál retiene más. No he montado nada todavía.</p>
  <div class="facts"><span class="tag accent">18 clips · 1 min 51 s de material</span><span class="tag">1080×1920 · 30 fps</span><span class="tag">Estilo ExoMov</span></div>
 </header>

 <section><h2>El material</h2><p class="lede">«VOZ» marca los clips cuyo audio vale para el vídeo. El resto se silencia y suena con música y efectos, como pediste. Entre los de movimiento, 9715, 9713 y 9714 son los que mejor sirven para cortar sobre el barrido de cámara.</p>
  <div class="clips">{cl_html}</div></section>

 <section class="two">
  <div class="box"><h3 class="label">Cómo lo corto, al estilo Edgar Wright</h3><ul>
   <li><b>Cortes a golpe de música.</b> Cada corte cae en un tiempo del compás, no cuando el plano «termina».</li>
   <li><b>Barridos como transición.</b> Salgo del plano en pleno giro de cámara y entro en el siguiente por el mismo lado.</li>
   <li><b>Sonido sincronizado con la acción.</b> Clic de hebilla, golpe de maletero y whoosh, justo en el fotograma del gesto.</li>
   <li><b>Corte por acción.</b> El maletero que se cierra enlaza con la hebilla que se cierra.</li>
   <li><b>Zoom rápido en los golpes</b> y rótulos que entran como un latigazo, no como un fundido.</li></ul></div>
  <div class="box"><h3 class="label">La música</h3>
   <p>Desde aquí no puedo descargar canciones: las webs de música libre están bloqueadas. Por eso he compuesto una pista de rock <b>original, generada en código</b>. No tiene derechos y la puedo ajustar al compás de cada versión. Tiene batería, bajo, guitarras con distorsión y una melodía.</p>
   <p>Es una demo de 14 s a 152 bpm. <b>Yo no puedo oírla</b>: dime si el estilo te vale o si prefieres otro.</p>
   <audio controls preload="none" src="{audio}"></audio>
   <p class="mono" style="color:var(--muted)">Si prefieres una canción tuya, súbela y corto a su ritmo. Ojo: Instagram suele limitar la música comercial en cuentas de empresa.</p></div>
 </section>

 <section><h2>Las cinco, de un vistazo</h2><div class="vgrid">{cmp_card}</div></section>

 {"".join(variant(v) for v in V)}

 <section class="box"><h2>Antes de montar</h2><ul>
  <li><b>¿Qué versiones hago?</b> Si las cinco, las monto todas con el mismo sistema, cambiando solo lo que ves aquí.</li>
  <li><b>¿Te vale el sonido de la demo?</b> Es lo que más me preocupa, porque no lo puedo escuchar.</li>
  <li><b>El nombre del evento.</b> En el cartel pone «Orto Medical Care» y el pabellón «PAB-12». ¿Pongo ese nombre en algún rótulo o dejo solo «IFEMA»?</li>
  <li><b>Los textos de los ganchos.</b> Cámbialos como quieras.</li>
  <li><b>Permisos.</b> Salen visitantes y asistentes a la feria con la cara visible. Confirma que puedes publicarlos.</li></ul></section>
 <footer>Los tiempos son aproximados: se ajustan al compás de cada pista al montar. El 9767 no lo uso con sonido: se oye al director dando instrucciones.</footer>
</div>
'''
open(f"{O}/storyboard-ifema.html", "w", encoding="utf-8").write(page)
print(len(page) // 1024, "KB")
