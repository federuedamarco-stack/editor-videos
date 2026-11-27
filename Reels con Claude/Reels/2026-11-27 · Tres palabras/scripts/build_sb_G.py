"""Storyboard G · «Tres palabras para un exoesqueleto» (Instagram: hook, retención y CTA)."""
import base64, html, re, subprocess
O = "/tmp/claude-0/-home-user-editor-videos/d01835c0-842d-5f46-b60e-65aa20332005/scratchpad/ifema"
D = "/home/user/editor-videos/Reels con Claude/Tomas/2026-11-27 · IFEMA Ortopedia"
V1 = "/home/user/editor-videos/Reels con Claude/Tomas"
css = re.search(r"<style>.*?</style>", open(f"{O}/storyboard-ifema.html", encoding="utf-8").read(), re.S).group(0)


def thumb(name, base, clip, t):
    f = f"{O}/g_{name}.jpg"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", f"{base}/{clip}", "-frames:v", "1",
                    "-vf", "scale=180:320:force_original_aspect_ratio=increase,crop=180:320", "-q:v", "7", f], check=True)
    return "data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode()


TH = {
 "run": thumb("run", D, "IMG_9763.MOV", 3.4), "stairs2": thumb("stairs2", V1, "IMG_9632.MOV", 5.5), "steps": thumb("steps", V1, "IMG_9629.MOV", 2.6),
 "sen1": thumb("sen1", D, "IMG_9738_comprimido.mp4", 4.5), "sen2": thumb("sen2", D, "IMG_9738_comprimido.mp4", 22.0),
 "b1": thumb("b1", D, "IMG_9755.mov", 0.5), "b2": thumb("b2", D, "IMG_9726.MOV", 3.0),
 "tit": thumb("tit", D, "IMG_9743.mov", 2.0), "t34": thumb("t34", D, "IMG_9734.MOV", 7.0),
 "walk": thumb("walk", D, "IMG_9767.MOV", 5.8), "back": thumb("back", D, "IMG_9766.MOV", 1.5),
}
ROLE = {"hook": "HOOK", "ctx": "CONTEXTO", "ret": "RETENCIÓN", "body": "CUERPO", "cta": "CTA"}
# (inicio, fin, rol, nombre, clip, miniaturas, qué se ve, texto en pantalla, sonido)
S = [
 (0.0, 3.0, "hook", "Hook · la pregunta y la primera palabra", "IMG_9738 · 9743 · 9763", ["run", "sen1", "tit"],
  "Tres destellos de 0,4 s con gente caminando con el exoesqueleto (el corredor, la visitante, la otra visitante) y aterrizamos en la visitante, ya en movimiento desde el primer fotograma.",
  "«¿QUÉ SIENTE UN PROFESIONAL AL PROBAR UN EXOESQUELETO?» en tres líneas, grande, en el primer fotograma. Aparece la primera palabra: «RARA».",
  "Su voz desde el segundo 1: «…una sensación muy RARA». Golpe en el primer fotograma y entra la música."),
 (3.0, 7.0, "ctx", "Dónde estamos", "IMG_9755 · 9726", ["b1", "b2"],
  "La fachada de IFEMA Madrid, a cámara lenta (2 s), y un visitante con el exoesqueleto puesto (2 s).",
  "«IFEMA · ORTO MEDICAL CARE 2026 · LA FERIA PROFESIONAL DE LA ORTOPEDIA». Barra de progreso fina arriba que se va llenando hasta el final.",
  "Música sola. Whoosh en el corte."),
 (7.0, 14.0, "body", "Palabra 1 · RARA", "IMG_9738 · 0:02 – 0:08", ["sen1"],
  "Un solo plano de 7 s: la visitante camina y lo cuenta. Sin cortes para que se note que es real.",
  "Etiqueta «1/3 · RARA». «RARA» y «CURIOSA» en lima, grandes. Subtítulos de lo que dice.",
  "Su voz, con la música muy baja. Cortamos la palabrota del inicio, como en el A2."),
 (14.0, 19.0, "body", "Palabra 2 · TÍTERE", "IMG_9743 · 0:00 – 0:04", ["tit"],
  "La otra visitante probándolo mientras alguien de ExoMov le ajusta.",
  "Etiqueta «2/3 · TÍTERE». TÍTERE en lima: «como si fuese un TÍTERE que te están manejando desde arriba». A los 2 s, un aviso pequeño: «la tercera palabra lo resume».",
  "Su voz. Whoosh en el corte. Aquí está la apertura de bucle: promete algo que llega en 10 s."),
 (19.0, 24.0, "ret", "Giro · cómo funciona", "IMG_9734 · 0:05 – 0:09", ["t34"],
  "Cambiamos de ritmo en medio del vídeo: el asistente anda con el exoesqueleto. Es el único tramo explicativo y rompe el patrón de las reacciones.",
  "«ANDAS… Y ÉL TE COPIA». RITMO en lima: «te va a copiar al RITMO al que andas».",
  "Su voz. Un riser que sube durante los últimos 2 s y se corta justo antes de la palabra 3."),
 (24.0, 31.0, "body", "Palabra 3 · REPOTENCIADO (el pago del hook)", "IMG_9738 · 0:20 – 0:25", ["sen2"],
  "La visitante vuelve: «te sientes ridículo andando porque te sientes raro, te sientes como repotenciado, ¿verdad?». En el vídeo original, justo en esa frase, la cámara enfoca un brazo; por eso pasa a un plano de ella caminando de espaldas mientras sigue su voz. Silencio de música un segundo antes de la palabra, y vuelve a golpe.",
  "Etiqueta «3/3 · REPOTENCIADO». REPOTENCIADO enorme, en lima, ocupa casi todo el ancho.",
  "Su voz. Corte de música y golpe justo en «repotenciado»."),
 (31.0, 35.0, "ret", "Energía · lo que se ve", "IMG_9763 · 9632 · 9629", ["run", "stairs2", "steps"],
  "Tres planos de 1,3 s con el exoesqueleto en movimiento: la persona corriendo, subir escaleras acompañado y los primeros pasos en la clínica. Es lo más visual del material y sube la energía justo antes del CTA.",
  "Sin texto, o solo «RARA · TÍTERE · REPOTENCIADO» apareciendo palabra a palabra.",
  "Música a tope. Whoosh en cada corte."),
 (35.0, 38.5, "cta", "CTA · colabora con nosotros", "IMG_9767 · 9766 · voz de 9646", ["walk", "back"],
  "Sin la imagen del banco. Encima de su voz ponemos a las dos personas de ExoMov con la camiseta andando hacia la cámara (2 s) y de espaldas (1,5 s), para que parezca la misma historia.",
  "Tarjeta lima: «¿ERES PROFESIONAL DE LA ORTOPEDIA? · ORTOPEDIAS Y CLÍNICAS · Comenta COLABORADORES y te enviamos el enlace al WhatsApp». Entra en el segundo 0,2, con la voz.",
  "Su voz sola, sin cara: «Escríbenos y te contamos». La música baja un momento y vuelve. El ambiente del banco queda tapado por la música."),
 (38.5, 41.0, "cta", "Cierre y bucle", "Gráfico", [],
  "Logo, «Libertad de movimiento» y exomov.com. Termina en un corte limpio para que al reiniciarse enlace con la pregunta del principio.",
  "Debajo de la web: «Ortopedias y clínicas · comenta COLABORADORES».",
  "Golpe final y la música se corta en seco, sin fundido, para que el bucle no suene a final."),
]
dur = S[-1][1]
esc = html.escape
rows, track = "", ""
for a, b, role, name, clip, ths, what, txt, snd in S:
    th = "".join(f'<img src="{TH[k]}" alt="">' for k in ths) or '<div class="logo">EXOMOV</div>'
    tag = ' accent' if role in ("hook", "cta") else ''
    rows += f'''<article class="sc"><div class="th">{th}<small>{esc(clip)}</small></div>
      <div class="tx"><div class="hd"><span class="mono">0:{int(a):02d} – 0:{int(b):02d}</span><h4>{esc(name)}</h4><span class="tag{tag}">{ROLE[role]}</span></div><p>{esc(what)}</p>
      <dl><dt>Texto</dt><dd>{esc(txt)}</dd><dt>Sonido</dt><dd>{esc(snd)}</dd></dl></div></article>'''
    k = "v" if role in ("hook", "cta") else ("x" if role == "ctx" else "c")
    lab = {"hook": "Hook", "ctx": "Dónde", "body": "Palabra", "ret": "Giro", "cta": "CTA"}[role]
    track += f'<div class="seg k{k}" style="flex:{b - a}"><span>{lab}</span></div>'

page = f'''<title>Storyboard Tres palabras</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Figtree:wght@400;500;700;800&family=JetBrains+Mono:wght@500&display=swap">
{css}
<style>.timeline{{min-width:0;overflow-x:auto}} .timeline .track,.timeline .ticks{{min-width:560px}} .two2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}}</style>
<div class="wrap">
 <header>
  <div class="label">ExoMov · Vídeo nuevo para Instagram · Storyboard para aprobar</div>
  <h1>Tres palabras<br>para un exoesqueleto</h1>
  <p class="lede">Un reel de reacciones pensado para retener y dirigido a profesionales de la ortopedia: una pregunta y la primera palabra en los 3 primeros segundos, tres palabras que forman una pequeña historia (RARA, TÍTERE, REPOTENCIADO), un giro a mitad que corta la monotonía y una invitación final a colaborar con ExoMov. Mezcla el material de IFEMA con el del primer vídeo.</p>
  <div class="facts"><span class="tag accent">≈ {dur:.0f} s</span><span class="tag">Rock indie · 118 bpm</span><span class="tag">Hook: ¿QUÉ SIENTE UN PROFESIONAL AL PROBAR UN EXOESQUELETO?</span><span class="tag">CTA: COLABORA CON EXOMOV</span><span class="tag">1080×1920 · 30 fps</span></div>
 </header>
 <section class="timeline" aria-label="Línea de tiempo"><div class="label">Línea de tiempo · hook, cuerpo, retención y CTA</div>
  <div class="track">{track}</div><div class="ticks mono"><span>0:00</span><span>0:20</span><span>0:{int(dur)}</span></div>
  <div class="legend"><span><i></i>Hook y CTA, los dos momentos que más pesan en Instagram</span></div></section>
 <section class="two2">
  <div class="box"><h3 class="label">Por qué debería retener</h3><ul>
   <li><b>Hook en 3 s:</b> una pregunta que se entiende sin sonido, movimiento desde el primer fotograma y una voz real diciendo «rara».</li>
   <li><b>Una historia en tres palabras.</b> Cada palabra aparece en lima y enorme. RARA y TÍTERE abren una duda («¿en qué acaba?») y REPOTENCIADO la cierra.</li>
   <li><b>Aviso de que llega algo:</b> a mitad, un texto pequeño promete la tercera palabra. Es el motivo para no irse.</li>
   <li><b>Un cambio de ritmo cada 5-7 s:</b> reacción, reacción, explicación, reacción, montaje de movimiento.</li>
   <li><b>CTA doble:</b> en texto (tarjeta lima, dirigida a profesionales) y dicho por una persona («escríbenos y te contamos»).</li>
   <li><b>Bucle:</b> el final repite la pregunta del principio y la música se corta en seco, para que se vea otra vez.</li></ul></div>
  <div class="box"><h3 class="label">Qué reutiliza y qué cambia</h3><ul>
   <li><b>Del vídeo de IFEMA (A2):</b> la visitante (9738), la otra visitante (9743), el asistente (9734), el corredor (9763), la fachada (9755) y el visitante (9726).</li>
   <li><b>Del primer vídeo:</b> solo la <b>voz</b> del hombre de ExoMov («escríbenos y te contamos»), sin su imagen del banco, y los planos de la clínica (9632 y 9629).</li>
   <li><b>Diferente de los demás:</b> empieza por la pregunta en vez de por IFEMA, estructura el vídeo en capítulos y cierra con una invitación a colaborar, no a probar.</li>
   <li><b>Sin la palabrota.</b> El inicio del 9738 se corta igual que en el A2.</li></ul></div>
 </section>
 {rows}
 <section class="box"><h2>Decisiones ya tomadas</h2><ul>
  <li><b>Público:</b> profesionales de la ortopedia. Las visitantes lo son, así que el hook habla de «un profesional».</li>
  <li><b>Colaboradores:</b> ortopedias y clínicas.</li>
  <li><b>CTA:</b> «Comenta COLABORADORES y te enviamos el enlace al WhatsApp», en la tarjeta y en el cierre. Sin número ni enlace en el vídeo.</li>
  <li><b>La voz del banco:</b> solo «escríbenos y te contamos», sin su imagen, sobre las dos personas de ExoMov.</li>
  <li><b>Pendiente de ti:</b> los permisos de las visitantes, que salen con la cara visible y se las oye.</li></ul></section>
 <footer>Tiempos aproximados: se ajustan al compás de la música al montar. Cada texto grande entra a golpe, no con fundido.</footer>
</div>
'''
open(f"{O}/storyboard-ifema-G.html", "w", encoding="utf-8").write(page)
print(len(page) // 1024, "KB ·", dur, "s")
