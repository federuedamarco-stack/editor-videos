"""Storyboard A2 · Remix de la A (reel de IFEMA). Tiempos calculados a 118 bpm."""
import base64, html, re, subprocess
O = "/tmp/claude-0/-home-user-editor-videos/d01835c0-842d-5f46-b60e-65aa20332005/scratchpad/ifema"
D = "/home/user/editor-videos/Reels con Claude/Tomas/2026-11-27 · IFEMA Ortopedia"
css = re.search(r"<style>.*?</style>", open(f"{O}/storyboard-ifema.html", encoding="utf-8").read(), re.S).group(0)
BEAT = 60 / 118


def thumb(name, clip, t):
    f = f"{O}/c_{name}.jpg"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", f"{D}/{clip}", "-frames:v", "1",
                    "-vf", "scale=180:320:force_original_aspect_ratio=increase,crop=180:320", "-q:v", "7", f], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode()


Q = lambda n, c, t: (n, thumb(n, c, t))
TH = dict([Q("ifema", "IMG_9755.mov", 0.5), Q("maleta", "IMG_9701.mov", 1.5), Q("cierra", "IMG_9703.MOV", 1.9),
           Q("h1", "IMG_9757.MOV", 1.5), Q("h2", "IMG_9758.MOV", 1.5), Q("h3", "IMG_9759.MOV", 3.5),
           Q("cartel", "IMG_9709.mov", 0.3), Q("mani", "IMG_9714.MOV", 1.0), Q("visit", "IMG_9726.MOV", 3.0),
           Q("t43", "IMG_9743.mov", 2.0), Q("t34", "IMG_9734.MOV", 9.0), Q("t44", "IMG_9744.MOV", 2.6),
           Q("corre", "IMG_9763.MOV", 3.4), Q("camina", "IMG_9767.MOV", 5.8), Q("espalda", "IMG_9766.MOV", 1.5)])
# (beats, nombre, clip, miniaturas, qué se ve, texto, sonido, [voz?])
S = [
 (4, "El edificio de IFEMA", "IMG_9755 · cámara lenta", ["ifema"],
  "Abrimos con la fachada de IFEMA Madrid, con el nombre a la vista. Va a cámara lenta para que dure 2 s.",
  "«LLEGAMOS A IFEMA» en dos líneas, grande.",
  "Suena la voz del actor, solo audio: «hemos venido a IFEMA para…». Golpe en el primer fotograma y entra la música.", True),
 (5, "El maletero lleno de equipos", "IMG_9701", ["maleta"],
  "El maletero abierto, lleno de exoesqueletos. Coincide con lo que dice: «…dar a conocer nuestros equipos y nuestra tecnología».",
  "Subtítulos de la voz, con EQUIPOS y TECNOLOGÍA en lima.", "Sigue la voz del actor. La música baja sola.", True),
 (4, "Se cierra el maletero", "IMG_9703", ["cierra"],
  "El maletero se cierra en primer plano. El golpe real de la tapa cae en el primer tiempo del compás.",
  "PROFESIONALES en lima: «…a los profesionales del sector».", "Golpe de la tapa + zoom rápido. La voz termina aquí.", True),
 (8, "Cómo se pone", "IMG_9757 · 9758 · 9759", ["h1", "h2", "h3"],
  "Pantalla dividida con una toma arriba (la hebilla) y dos abajo (las piernas), como en la A.",
  "«1 CINTURA», «2 PIERNA», «3 PIERNA».", "Whoosh y un clic por rótulo.", False),
 (4, "El cartel de la feria", "IMG_9709 · cámara lenta", ["cartel"],
  "El cartel con la persona que pasa, a cámara lenta.", "«ORTO MEDICAL CARE 2026».", "Whoosh.", False),
 (4, "Maniquíes", "IMG_9714", ["mani"], "Los maniquíes con el exoesqueleto, para dar paso a las pruebas.", "—", "Whoosh.", False),
 (4, "Un visitante con el exo", "IMG_9726 · nuevo", ["visit"],
  "Un visitante con el exoesqueleto en la cintura, con alguien de ExoMov explicándole. Es el único clip nuevo que enseña a un profesional con el equipo puesto.",
  "Entra el cuadro «REACCIONES DE LOS PROFESIONALES» y se queda durante las tres pruebas.", "Whoosh. Sin voz: su audio habla de otra cosa.", False),
 (8, "Prueba 1 · el títere", "IMG_9743", ["t43"], "La visitante probándolo.", "«como si fuese un TÍTERE que te están manejando desde arriba».", "Su voz. La música baja.", True),
 (7, "Prueba 2 · el ritmo", "IMG_9734", ["t34"], "El asistente anda con el exoesqueleto: «…te va a copiar al RITMO al que andas».", "RITMO en lima.", "Su voz.", True),
 (7, "Prueba 3 · persona sana", "IMG_9744", ["t44"], "El grupo con exoesqueletos en el pasillo.", "«ese es el modo como una persona SANA como lo llevaría».", "Su voz. Aquí termina el cuadro de reacciones.", True),
 (5, "Corriendo con el exo", "IMG_9763 · nuevo", ["corre"],
  "Una persona de ExoMov con el exoesqueleto puesto cruza el aparcamiento corriendo. Es el plano con más energía del material y no estaba en la A.",
  "—", "La música vuelve a subir y un riser lo lleva hasta el siguiente corte.", False),
 (6, "Los dos, hacia la cámara", "IMG_9767", ["camina"], "Las dos personas andando hacia la cámara, desde que echan a andar.", "Entra la tarjeta lima «DESCUBRE CÓMO PROBARLO · Consúltanos por WhatsApp».", "Música a tope.", False),
 (5, "Los dos, de espaldas", "IMG_9766", ["espalda"], "Se alejan andando. Sigue la tarjeta de WhatsApp.", "—", "Última subida de la música.", False),
 (5, "Cierre", "", [], "Logo de ExoMov, «Libertad de movimiento» y exomov.com.", "—", "Golpe final y acorde de guitarra.", False),
]


def tm(s):
    m, x = divmod(s, 60); return f"{int(m)}:{x:04.1f}".replace(".", ",")


SHORT = ["IFEMA", "Maletero", "Cierre", "Cómo se pone", "Cartel", "Manik.", "Visitante", "Títere", "Ritmo", "Sana", "Corre", "Andan", "Espaldas", "Cierre"]
rows, track, t, tot = "", "", 0.0, sum(b for b, *_ in S)
for si, (beats, name, clip, ths, what, txt, snd, voice) in enumerate(S):
    d = beats * BEAT; a, b = t, t + d; t = b
    th = "".join(f'<img src="{TH[k]}" alt="">' for k in ths) or '<div class="logo">EXOMOV</div>'
    rows += f'''<article class="sc"><div class="th">{th}<small>{html.escape(clip) if clip else "gráfico"}</small></div>
      <div class="tx"><div class="hd"><span class="mono">{tm(a)} – {tm(b)}</span><h4>{html.escape(name)}</h4>{'<span class="tag accent">con voz</span>' if voice else ''}</div><p>{html.escape(what)}</p>
      <dl><dt>Texto</dt><dd>{html.escape(txt)}</dd><dt>Sonido</dt><dd>{html.escape(snd)}</dd></dl></div></article>'''
    track += f'<div class="seg k{"v" if voice else ("x" if not clip else "c")}" style="flex:{beats}"><span>{html.escape(SHORT[si])}</span></div>'
dur = tot * BEAT + 0.8
audio = "data:audio/mpeg;base64," + base64.b64encode(open(f"{O}/demo_rock_118bpm.mp3", "rb").read()).decode()

page = f'''<title>Storyboard IFEMA A2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Figtree:wght@400;500;700;800&family=JetBrains+Mono:wght@500&display=swap">
{css}
<style>.timeline{{min-width:0;overflow-x:auto}} .timeline .track,.timeline .ticks{{min-width:640px}} .cmp2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}} .box audio{{width:100%;margin-top:12px}}</style>
<div class="wrap">
 <header>
  <div class="label">ExoMov · Evento en IFEMA · Remix de la A · Storyboard para aprobar</div>
  <h1>A2<br>Remix de la A</h1>
  <p class="lede">Misma historia que la A, pero con otro arranque y otros planos. La primera frase del actor se mantiene solo como voz, sin verlo, y encima van la fachada de IFEMA, el maletero lleno de equipos y el cierre del maletero. Quito los clips que se repetían entre versiones y uso tres de los nuevos. La música es otra: rock más tranquilo.</p>
  <div class="facts"><span class="tag accent">≈ {dur:.0f} s</span><span class="tag">Rock indie · 118 bpm</span><span class="tag">Texto: LLEGAMOS A IFEMA</span><span class="tag">Voz: actor (solo audio) + 3 pruebas</span><span class="tag">1080×1920 · 30 fps</span></div>
 </header>
 <section class="timeline" aria-label="Línea de tiempo"><div class="label">Línea de tiempo · {len(S)-1} planos y un cierre</div>
  <div class="track">{track}</div><div class="ticks mono"><span>0:00</span><span>0:20</span><span>{tm(dur)}</span></div>
  <div class="legend"><span><i></i>Tramos con voz</span></div></section>
 <section class="cmp2">
  <div class="box"><h3 class="label">Qué cambia respecto a la A</h3><ul>
   <li><b>Arranque nuevo:</b> la fachada de IFEMA, el maletero lleno y el cierre, con la voz del actor encima y sin verlo.</li>
   <li><b>Quito:</b> el pasillo (9713), el clip de la camiseta de ExoMov (9715), la reacción del «Play» (9716), el primer plano de la app (9719) y la prueba de la «cadencia» (9735).</li>
   <li><b>Uso nuevos:</b> IFEMA (9755), el maletero (9701), el visitante (9726) y la persona corriendo (9763).</li>
   <li><b>Más aire en el montaje:</b> todos los planos duran entre 2 y 4 s, salvo los de voz.</li></ul></div>
  <div class="box"><h3 class="label">Los clips nuevos</h3><ul>
   <li><b>9755 · IFEMA:</b> solo dura 1 s. Lo ralentizo a la mitad para llegar a 2 s.</li>
   <li><b>9701 · maletero:</b> bueno. Su voz («Claro, es que la batería que tengo…») la silencio.</li>
   <li><b>9726 · visitante:</b> la primera mitad es suelo y los pies; uso solo los 2 s finales. Su voz («te voy a poner…») también la silencio.</li>
   <li><b>9763 · corriendo:</b> uso 2,5 s del tramo en que cruza el aparcamiento. <b>No lo he oído ni sé qué pasaba</b>: si no quieres que se vea a alguien corriendo, lo quito.</li>
   <li><b>No uso</b> la parte de «Suscríbete al canal», que es ruido de fondo.</li></ul></div>
 </section>
 <section class="box"><h3 class="label">La música</h3>
  <p>Otra pista de rock original generada en código, sin derechos. Es más lenta que la de la A: <b>118 bpm</b> en lugar de 152, con la guitarra más limpia, menos distorsión y menos charles. Yo no puedo escucharla: dime si el estilo te vale. Si prefieres una canción tuya, súbela y corto a su ritmo.</p>
  <audio controls preload="none" src="{audio}"></audio></section>
 {rows}
 <section class="box"><h2>Antes de renderizar</h2><ul>
  <li><b>La frase del actor con voz y sin cara.</b> Se mantiene entera, pero si quieres verlo un momento, por ejemplo en «del sector» cerrando el maletero, lo pongo.</li>
  <li><b>El texto del gancho.</b> «LLEGAMOS A IFEMA» es nuevo. Cámbialo como quieras.</li>
  <li><b>La persona corriendo (9763).</b> Confírmame que se la puede ver así en el vídeo.</li>
  <li><b>Los rótulos de las piernas</b> dicen «2 PIERNA» y «3 PIERNA». Dime cuál es la izquierda y cuál la derecha.</li>
  <li><b>Permisos.</b> Salen visitantes y personal de la feria con la cara visible.</li></ul></section>
 <footer>Tiempos exactos al compás de 118 bpm. Se ajustan al fotograma al montar.</footer>
</div>
'''
open(f"{O}/storyboard-ifema-A2.html", "w", encoding="utf-8").write(page)
print(len(page) // 1024, "KB ·", f"{dur:.1f} s ·", tot, "pulsos")
