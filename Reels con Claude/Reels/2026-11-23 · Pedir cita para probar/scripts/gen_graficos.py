"""Pasada 3-4 · Genera el proyecto HyperFrames (1080x1920) del reel «Pedir cita para probar».
Estilo: Mi estilo/Reglas-de-estilo.md (ExoMov). Selectores literales, todo dentro de <template> en las subcomposiciones."""
import json, re, html

P = "/home/user/editor-videos/Reels con Claude/Reels/2026-11-23 · Pedir cita para probar"
G, T = f"{P}/graficos", f"{P}/trabajo"
DUR = 32.2
END_AT = 29.70            # empieza el cierre
caps = json.load(open(f"{T}/captions.json", encoding="utf-8"))

INK, LIME, PAPER, MUTED, S2, BORDER = "#121311", "#BEBD39", "#F6F6F1", "#A9A99E", "#262723", "#3A3B35"
FONTS = """
@font-face { font-family: "Bebas Neue"; src: url("assets/fonts/bebas-neue-400.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-700.woff2") format("woff2"); font-weight: 700; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-800.woff2") format("woff2"); font-weight: 800; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-500.woff2") format("woff2"); font-weight: 500; }
"""
ENTER = 'ease: "power3.out"'          # «asistir, no empujar»: sin rebote
EXIT = 'ease: "power2.in"'
clean = lambda s: re.sub(r"[¿?¡!,.;:]", "", s)
f3 = lambda x: f"{x:.3f}"

# ---------------------------------------------------------------- subtítulos
cap_html, cap_js = [], []
for i, c in enumerate(caps):
    start, end = c["start"], min(c["end"], END_AT - 0.02)
    if start >= END_AT:
        continue
    words = [clean(w["w"]) for w in c["words"]]
    cls = "cap clip key" if c["key"] else "cap clip"
    spans = "".join(f'<span id="w{i}-{k}" class="w">{html.escape(w)}</span>' for k, w in enumerate(words))
    cap_html.append(f'<div id="cap-{i}" class="{cls}" data-start="{f3(start)}" data-duration="{f3(end - start)}" data-track-index="1"><div class="line">{spans}</div></div>')
    if c["key"]:
        cap_js.append(f'ctl.fromTo("#cap-{i} .line", {{ opacity: 0, y: 26, scale: .94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.38, {ENTER} }}, {f3(start)});')
    else:
        for k, w in enumerate(c["words"]):
            t = max(start, w["t"])
            style = ("{ opacity: 0, y: 18 }", "{ opacity: 1, y: 0, duration: 0.3, ") if i % 3 else ("{ opacity: 0, y: 14, filter: \"blur(6px)\" }", "{ opacity: 1, y: 0, filter: \"blur(0px)\", duration: 0.34, ")
            cap_js.append(f'ctl.fromTo("#w{i}-{k}", {style[0]}, {style[1]}{ENTER} }}, {f3(t)});')

captions = f"""<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{FONTS}
        #captions-root {{ position: absolute; inset: 0; }}
        #captions-root .cap {{ position: absolute; left: 80px; right: 150px; top: 1260px; height: 260px; display: flex; align-items: center; justify-content: center; text-align: center; }}
        #captions-root .line {{ display: flex; flex-wrap: wrap; justify-content: center; align-items: baseline; gap: 0 16px; max-width: 100%; }}
        #captions-root .w {{ display: inline-block; font-family: "Figtree", sans-serif; font-weight: 700; font-size: 62px; line-height: 1.1; color: {PAPER};
              text-shadow: 0 4px 18px rgba(18,19,17,.6), 0 1px 3px rgba(18,19,17,.7); }}
        #captions-root .key .w {{ font-family: "Bebas Neue", sans-serif; font-weight: 400; font-size: 168px; line-height: .92; letter-spacing: .01em; text-transform: uppercase; color: {LIME};
              text-shadow: 0 6px 24px rgba(18,19,17,.65), 0 2px 4px rgba(18,19,17,.6); }}
      </style>
      <div id="captions-root" data-composition-id="captions" data-width="1080" data-height="1920" data-duration="{DUR}">
        {chr(10).join(cap_html)}
      </div>
      <script>
        const ctl = gsap.timeline({{ paused: true }});
        {chr(10).join(cap_js)}
        window.__timelines["captions"] = ctl;
      </script>
    </template>
  </body>
</html>
"""

# ---------------------------------------------------------------- gráficos
def card(id_, t0, t1, top, inner, cls="card"):
    return (f'<div id="{id_}" class="{cls} clip" data-start="{f3(t0)}" data-duration="{f3(t1 - t0)}" data-track-index="1" style="top:{top}px">{inner}</div>',
            [f'gtl.fromTo("#{id_}", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.42, {ENTER} }}, {f3(t0)});',
             f'gtl.to("#{id_}", {{ opacity: 0, y: -24, duration: 0.2, {EXIT} }}, {f3(t1 - 0.2)});'])

g_html, g_js = [], []
def add(h, js):
    g_html.append(h); g_js.extend(js)

# gancho · etiqueta «4 pasos»
add(f'<div id="tag-hook" class="tagrow clip" data-start="5.250" data-duration="1.730" data-track-index="1" style="top:1452px"><span class="tag"><i class="dot"></i>4 pasos para probarlo</span></div>',
    ['gtl.fromTo("#tag-hook .tag", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.32, ease: "power3.out" }, 5.250);',
     'gtl.to("#tag-hook .tag", { opacity: 0, duration: 0.18, ease: "power2.in" }, 6.780);'])

# paso 1 · llámanos
pills = ["Caminar", "Trabajo", "Senderismo", "Rehabilitación"]
h, js = card("c1", 7.02, 12.40, 230,
             '<div class="step">Paso 1</div><div class="title">Llámanos o escríbenos</div>'
             '<div class="pills">' + "".join(f'<span id="p{k}" class="pill">{p}</span>' for k, p in enumerate(pills)) + "</div>")
add(h, js + [f'gtl.fromTo("#p{k}", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {f3(9.90 + 0.14 * k)});' for k in range(4)])

# paso 2 · en la clínica (checks en su palabra)
checks = [("Ponértelo", 14.48), ("Ajustarlo", 15.32), ("Probarlo", 16.62)]
h, js = card("c2", 13.62, 17.16, 230,
             '<div class="step">Paso 2</div><div class="title">En la clínica</div><div class="checks">' +
             "".join(f'<div id="k{k}" class="chk"><i class="box"></i><i id="kf{k}" class="fill"></i><span>{t}</span></div>' for k, (t, _) in enumerate(checks)) + "</div>")
add(h, js + sum([[f'gtl.fromTo("#kf{k}", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.24, ease: "power3.out" }}, {f3(t - 0.03)});',
                  f'gtl.fromTo("#k{k} span", {{ opacity: .45 }}, {{ opacity: 1, duration: 0.2, ease: "power2.out" }}, {f3(t - 0.03)});'] for k, (_, t) in enumerate(checks)], []))

# paso 3 · la prueba (barra en «se adapta a ti»)
h, js = card("c3", 17.22, 22.06, 260,
             '<div class="step">Paso 3</div><div class="title">La prueba</div><div class="bar"><i id="barfill"></i></div>')
add(h, js + ['gtl.fromTo("#barfill", { scaleX: 0 }, { scaleX: 1, duration: 0.48, ease: "power3.out" }, 21.420);'])

# paso 4 · tú decides → tarjeta lima
h, js = card("c4", 22.20, 26.06, 230, '<div class="step">Paso 4</div><div class="title">Tú decides</div>')
add(h, js)
h, js = card("c4b", 26.16, 28.00, 930, '<div class="step">Paso 4</div><div class="title">Pruébalo antes<br>de comprarlo</div>', cls="card lime")
add(h, js)

# cierre
add(f'<div id="endcard" class="clip" data-start="{f3(END_AT - 0.08)}" data-duration="{f3(DUR - END_AT + 0.08)}" data-track-index="2">'
    '<img id="end-logo" src="assets/logos/exomov-logo-blanco.png" alt="ExoMov" />'
    '<div id="end-claim">Libertad de movimiento</div><div id="end-web">exomov.com</div></div>',
    [f'gtl.fromTo("#endcard", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "power2.out" }}, {f3(END_AT - 0.08)});',
     f'gtl.fromTo("#end-logo", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.48, {ENTER} }}, {f3(END_AT + 0.05)});',
     f'gtl.fromTo("#end-claim", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.42, {ENTER} }}, {f3(END_AT + 0.35)});',
     f'gtl.fromTo("#end-web", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.4, {ENTER} }}, {f3(END_AT + 0.4)});'])

graphics = f"""<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{FONTS}
        #gfx-root {{ position: absolute; inset: 0; font-family: "Figtree", sans-serif; }}
        #gfx-root .card {{ position: absolute; left: 80px; right: 150px; padding: 36px 40px; border-radius: 28px; background: rgba(18,19,17,.88); border: 2px solid {BORDER}; color: {PAPER}; }}
        #gfx-root #c1 {{ padding: 28px 36px; }}
        #gfx-root #c1 .title {{ font-size: 84px; }}
        #gfx-root #c1 .pills {{ margin-top: 14px; gap: 10px; }}
        #gfx-root .card.lime {{ background: {LIME}; border-color: #828120; color: {INK}; }}
        #gfx-root .step {{ font-weight: 700; font-size: 28px; line-height: 1; letter-spacing: .06em; text-transform: uppercase; color: {LIME}; }}
        #gfx-root .lime .step {{ color: #2C2B0E; }}
        #gfx-root .title {{ font-family: "Bebas Neue", sans-serif; font-size: 96px; line-height: .92; letter-spacing: .01em; text-transform: uppercase; margin-top: 10px; }}
        #gfx-root .sub {{ font-weight: 700; font-size: 34px; line-height: 1.2; margin-top: 10px; color: {PAPER}; }}
        #gfx-root .pills {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }}
        #gfx-root .pill {{ display: inline-block; height: 52px; line-height: 52px; padding: 0 22px; border-radius: 999px; background: {S2}; color: {PAPER}; font-weight: 700; font-size: 28px; letter-spacing: .06em; text-transform: uppercase; }}
        #gfx-root .checks {{ display: grid; gap: 8px; margin-top: 16px; }}
        #gfx-root .chk {{ position: relative; display: flex; align-items: center; height: 46px; padding-left: 62px; font-weight: 700; font-size: 38px; }}
        #gfx-root .chk .box {{ position: absolute; left: 0; top: 4px; width: 40px; height: 40px; border-radius: 999px; border: 3px solid {BORDER}; }}
        #gfx-root .chk .fill {{ position: absolute; left: 0; top: 4px; width: 40px; height: 40px; border-radius: 999px; background: {LIME}; }}
        #gfx-root .chk .fill::after {{ content: ""; position: absolute; left: 13px; top: 7px; width: 10px; height: 19px; border: solid {INK}; border-width: 0 5px 5px 0; transform: rotate(45deg); }}
        #gfx-root .bar {{ height: 22px; border-radius: 999px; background: {S2}; margin-top: 22px; overflow: hidden; }}
        #gfx-root .bar i {{ display: block; width: 100%; height: 100%; background: {LIME}; transform-origin: 0 50%; }}
        #gfx-root .tagrow {{ position: absolute; left: 80px; right: 150px; display: flex; justify-content: center; }}
        #gfx-root .tag {{ display: inline-flex; align-items: center; gap: 14px; height: 56px; padding: 0 26px; border-radius: 999px; background: rgba(18,19,17,.88); border: 2px solid {BORDER};
              color: {PAPER}; font-weight: 700; font-size: 28px; letter-spacing: .06em; text-transform: uppercase; }}
        #gfx-root .tag .dot {{ width: 14px; height: 14px; border-radius: 999px; background: {LIME}; }}
        #endcard {{ position: absolute; inset: 0; background: {INK}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; padding-bottom: 120px; }}
        #end-logo {{ width: 640px; height: auto; }}
        #end-claim {{ max-width: 700px; font-family: "Bebas Neue", sans-serif; font-size: 112px; line-height: .95; letter-spacing: .01em; text-transform: uppercase; color: {PAPER}; text-align: center; }}
        #end-web {{ font-weight: 700; font-size: 44px; color: {LIME}; letter-spacing: .01em; }}
      </style>
      <div id="gfx-root" data-composition-id="graphics" data-width="1080" data-height="1920" data-duration="{DUR}">
        {chr(10).join(g_html)}
      </div>
      <script>
        const gtl = gsap.timeline({{ paused: true }});
        {chr(10).join(g_js)}
        window.__timelines["graphics"] = gtl;
      </script>
    </template>
  </body>
</html>
"""

# ---------------------------------------------------------------- raíz + zooms (origen en la cara)
Z = [(0.00, 1.06, 1.00, 0.80, "power3.out"),      # el gancho entra cerca y se asienta
     (3.04, 1.00, 1.06, 0.45, "power3.out"),      # «probarlo»
     (3.82, 1.06, 1.00, 0.70, "power2.inOut"),
     (8.60, 1.00, 1.04, 3.60, "sine.inOut"),      # empuje lento mientras explica
     (12.40, 1.04, 1.00, 0.30, "power2.out"),
     (13.66, 1.00, 1.04, 3.50, "sine.inOut"),     # plano A
     (17.18, 1.00, 1.00, 0.01, "none"),
     (18.18, 1.00, 1.04, 3.10, "sine.inOut"),     # plano B
     (21.28, 1.00, 1.00, 0.01, "none"),
     (21.40, 1.00, 1.05, 0.45, "power3.out"),     # «se adapta a ti»
     (22.08, 1.00, 1.00, 0.01, "none"),
     (23.00, 1.00, 1.04, 2.60, "sine.inOut"),     # plano C
     (25.62, 1.00, 1.00, 0.01, "none"),
     (26.80, 1.00, 1.05, 0.50, "power3.out"),     # «antes de adquirirlo» (la tarjeta lima ya está desde «decidirte»)
     (28.03, 1.08, 1.03, 0.60, "power3.out")]     # salto al banco tapado con zoom
zjs = "\n      ".join(f'tl.fromTo("#zoom", {{ scale: {a} }}, {{ scale: {b}, duration: {d}, ease: "{e}", immediateRender: {"true" if i == 0 else "false"} }}, {t});' for i, (t, a, b, d, e) in enumerate(Z))
index = f"""<!doctype html>
<html lang="es" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {INK}; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; }}
      #zoom {{ position: absolute; inset: 0; transform-origin: 50% 35%; }}
      #base {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
      .layer {{ position: absolute; inset: 0; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <div id="zoom"><video id="base" class="clip" src="assets/base.mp4" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="0"></video></div>
      <div id="captions-host" class="layer" data-composition-id="captions" data-composition-src="compositions/captions.html" data-track-kind="captions" data-start="0" data-duration="{DUR}" data-track-index="2" data-width="1080" data-height="1920"></div>
      <div id="graphics-host" class="layer" data-composition-id="graphics" data-composition-src="compositions/graphics.html" data-start="0" data-duration="{DUR}" data-track-index="3" data-width="1080" data-height="1920"></div>
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {zjs}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
open(f"{G}/index.html", "w", encoding="utf-8").write(index)
open(f"{G}/compositions/captions.html", "w", encoding="utf-8").write(captions)
open(f"{G}/compositions/graphics.html", "w", encoding="utf-8").write(graphics)
print("ok · index + captions (%d) + graphics (%d)" % (len(cap_html), len(g_html)))
