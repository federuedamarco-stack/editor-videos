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
           Q("cartel", "IMG_9709.mov", 0.3), Q("visit", "IMG_9726.MOV", 3.0),
           Q("t34", "IMG_9734.MOV", 9.0), Q("t44", "IMG_9744.MOV", 2.6),
           Q("corre", "IMG_9763.MOV", 3.4), Q("sen1", "IMG_9738_comprimido.mp4", 4.5), Q("sen2", "IMG_9738_comprimido.mp4", 20.2)])
# (beats, nombre, clip, miniaturas, qué se ve, texto, sonido, [voz?])
S = [
 (4, "El edificio de IFEMA", "IMG_9755 · cámara lenta", ["ifema"],
  "Abrimos con la fachada de IFEMA Madrid, con el nombre a la vista, a cámara lenta para que dure 2 s.",
  "«LLEGAMOS A IFEMA» en dos líneas, grande.",
  "Suena la voz del actor, solo audio: «hemos venido a IFEMA para…». Golpe en el primer fotograma y entra la música.", True),
 (5, "El maletero lleno de equipos", "IMG_9701", ["maleta"],
  "El maletero abierto, lleno de exoesqueletos, justo cuando dice «…dar a conocer nuestros equipos y nuestra tecnología».",
  "Subtítulos de la voz, con EQUIPOS y TECNOLOGÍA en lima.", "Sigue la voz del actor. La música baja sola.", True),
 (4, "Se cierra el maletero", "IMG_9703", ["cierra"],
  "El maletero se cierra en primer plano. El golpe real de la tapa cae en el primer tiempo del compás.",
  "PROFESIONALES en lima: «…a los profesionales del sector».", "Golpe de la tapa + zoom rápido. La voz termina aquí.", True),
 (4, "El cartel de la feria", "IMG_9709 · cámara lenta", ["cartel"], "El cartel con la persona que pasa, a cámara lenta.", "«ORTO MEDICAL CARE 2026».", "Whoosh.", False),
 (4, "Un visitante con el exo", "IMG_9726", ["visit"],
  "Un visitante con el exoesqueleto en la cintura, con alguien de ExoMov explicándole. Uso solo los 2 s finales.", "—", "Whoosh. Sin voz: su audio habla de otra cosa.", False),
 (7, "Prueba · el ritmo", "IMG_9734", ["t34"], "El asistente anda con el exoesqueleto: «…te va a copiar al RITMO al que andas».", "RITMO en lima.", "Su voz. La música baja.", True),
 (7, "Prueba · persona sana", "IMG_9744", ["t44"], "El grupo con exoesqueletos en el pasillo.", "«ese es el modo como una persona SANA como lo llevaría».", "Su voz.", True),
 (5, "Corriendo con el exo", "IMG_9763", ["corre"],
  "Una persona de ExoMov con el exoesqueleto puesto cruza el aparcamiento corriendo. Es el plano con más energía y sube la música antes de la reacción.",
  "—", "La música vuelve a subir y un riser lo lleva a la siguiente escena.", False),
 (16, "Reacción de un profesional · 1", "IMG_9738 · 0:00 – 0:08", ["sen1"],
  "La visitante camina con el exoesqueleto por la feria y cuenta qué siente. Un solo plano, sin cortes, durante 8 s.",
  "Cuadro «REACCIÓN DE UN PROFESIONAL» arriba, fijo durante toda la escena. Subtítulos de lo que dice: «*****, una sensación muy rara, una sensación muy curiosa, ¿verdad?».",
  "Su voz, con la música muy baja. La primera palabra, la palabrota, se silencia y se tapa con un pitido corto de 0,5 s. En el subtítulo sale con asteriscos.", True),
 (22, "Reacción de un profesional · 2", "IMG_9738 · 0:14 – 0:25", ["sen2"],
  "Seguimos con ella andando. Quito el tramo del medio (8 a 14 s), que casi no tiene voz, y la dejo hablar hasta el final de su idea.",
  "Sigue el cuadro. «te sientes ridículo andando… te sientes como REPOTENCIADO, ¿verdad?», con REPOTENCIADO en lima.",
  "Su voz. Al terminar su frase corto la escena y entra la tarjeta lima de WhatsApp en los últimos 2 s.", True),
 (6, "Cierre", "", [], "Cuando acaba ella, cerramos con el logo de ExoMov, «Libertad de movimiento» y exomov.com.", "«DESCUBRE CÓMO PROBARLO · Consúltanos por WhatsApp» en una tarjeta lima encima del último plano.", "Golpe final y acorde de guitarra.", False),
]


def tm(s):
    m, x = divmod(s, 60); return f"{int(m)}:{x:04.1f}".replace(".", ",")


SHORT = ["IFEMA", "Maletero", "Cierre", "Cartel", "Visitante", "Ritmo", "Sana", "Corre", "Reacción 1", "Reacción 2", "Cierre"]
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
  <p class="lede">Misma historia que la A, pero con otro arranque y mucha menos edición. La primera frase del actor se mantiene solo como voz, sin verlo, y encima van la fachada de IFEMA, el maletero lleno y su cierre. Después de las pruebas rápidas, el reel se detiene en la reacción de una visitante: un plano largo, con un texto de «Reacción de un profesional», y se cierra cuando ella acaba. La música es otra: rock más tranquilo.</p>
  <div class="facts"><span class="tag accent">≈ {dur:.0f} s</span><span class="tag">Rock indie · 118 bpm</span><span class="tag">Texto: LLEGAMOS A IFEMA · REACCIÓN DE UN PROFESIONAL</span><span class="tag">Voz: actor (solo audio) + 2 pruebas + la visitante</span><span class="tag">1080×1920 · 30 fps</span></div>
 </header>
 <section class="timeline" aria-label="Línea de tiempo"><div class="label">Línea de tiempo · {len(S)-1} planos y un cierre</div>
  <div class="track">{track}</div><div class="ticks mono"><span>0:00</span><span>0:25</span><span>{tm(dur)}</span></div>
  <div class="legend"><span><i></i>Tramos con voz</span></div></section>
 <section class="cmp2">
  <div class="box"><h3 class="label">Qué cambia en esta versión</h3><ul>
   <li><b>Quito:</b> la prueba del títere (9743), los maniquíes (9714), la pantalla dividida de cómo se pone, el final con las dos personas andando (9767 y 9766) y todo lo que ya había quitado antes (pasillo, camiseta, «Play», app y «cadencia»).</li>
   <li><b>Pongo:</b> la reacción de la visitante (9738), larga y casi sin cortes, con el texto «Reacción de un profesional».</li>
   <li><b>Cierre:</b> cuando ella termina, entra la tarjeta de WhatsApp y el logo, sin más planos de por medio.</li>
   <li><b>La palabrota:</b> se silencia y se tapa con un pitido, y en el subtítulo sale con asteriscos.</li></ul></div>
  <div class="box"><h3 class="label">El clip nuevo (9738)</h3><ul>
   <li><b>Es vertical y dura 27 s.</b> Uso dos tramos: de 0 a 8 s (su primera impresión) y de 14 a 25 s (lo de sentirse «repotenciado»). Cortaría 6 s sin voz en el medio.</li>
   <li><b>Dónde está el «ostia»:</b> el audio tiene mucho ruido y el programa no lo reconoce con claridad. Lo más probable es que sea la primera palabra (entre 0,4 y 1,1 s). <b>Dime el segundo exacto para ponerle el pitido justo encima.</b></li>
   <li><b>Los subtítulos de esta parte no son fiables.</b> Los saca el programa y tiene frases mal entendidas. Te los pasaré antes de renderizar para que los revises.</li>
   <li><b>No hay cambios en el resto de clips</b> respecto al storyboard anterior.</li></ul></div>
 </section>
 <section class="box"><h3 class="label">La música</h3>
  <p>Otra pista de rock original generada en código, sin derechos. Es más lenta que la de la A: <b>118 bpm</b> en lugar de 152, con la guitarra más limpia, menos distorsión y menos charles. Yo no puedo escucharla: dime si el estilo te vale. Si prefieres una canción tuya, súbela y corto a su ritmo.</p>
  <audio controls preload="none" src="{audio}"></audio></section>
 {rows}
 <section class="box"><h2>Antes de renderizar</h2><ul>
  <li><b>¿En qué segundo dice «ostia»?</b> Sin eso no puedo poner el pitido en el sitio exacto.</li>
  <li><b>¿Lo del cierre es así?</b> He entendido que la reacción de la visitante es lo último del reel, antes del logo. Si prefieres que vuelva el final con las dos personas andando, lo pongo después.</li>
  <li><b>¿Dejo las dos pruebas rápidas (ritmo y persona sana) y la del visitante (9726) antes de ella?</b> Si prefieres menos aún, puedo dejar solo la reacción.</li>
  <li><b>Permisos.</b> La visitante sale con la cara a cámara y se la oye. Confirma que tienes su permiso.</li></ul></section>
 <footer>Tiempos exactos al compás de 118 bpm. Se ajustan al fotograma al montar.</footer>
</div>
'''
open(f"{O}/storyboard-ifema-A2.html", "w", encoding="utf-8").write(page)
print(len(page) // 1024, "KB ·", f"{dur:.1f} s ·", tot, "pulsos")
