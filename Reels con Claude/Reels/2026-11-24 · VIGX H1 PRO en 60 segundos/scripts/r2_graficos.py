"""Pasada 3-4 · Genera el proyecto HyperFrames (1080x1920) del reel «VIGX H1 PRO en 60 segundos» (versión retención).
Estilo: Mi estilo/Reglas-de-estilo.md (ExoMov). Selectores literales, todo dentro de <template> en las subcomposiciones."""
import json, re, html

P = "/home/user/editor-videos/Reels con Claude/Reels/2026-11-24 · VIGX H1 PRO en 60 segundos"
G, T = f"{P}/graficos", f"{P}/trabajo"
DUR = 60.0
END_AT = 58.00            # empieza el cierre
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
    if start >= END_AT or start < 3.6:      # en el gancho el título ya lo dice
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

# gancho · título como la portada
add('<div id="hook" class="clip" data-start="0.150" data-duration="3.600" data-track-index="1"><div id="hook-a">VIGX H1 PRO</div><div id="hook-b">en 60 segundos</div></div>',
    ['gtl.fromTo("#hook-a", { opacity: 0, y: 40, scale: .94 }, { opacity: 1, y: 0, scale: 1, duration: 0.42, ease: "power3.out" }, 0.150);',
     'gtl.fromTo("#hook-b", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.36, ease: "power3.out" }, 1.640);',
     'gtl.to("#hook", { opacity: 0, y: -24, duration: 0.2, ease: "power2.in" }, 3.550);'])

# rodillas · altura de la cincha
h, js = card("c1", 17.40, 21.30, 230, '<div class="step">Altura de la cincha</div><div class="title">3-4 dedos</div><div class="sub">por encima de la rodilla</div>')
add(h, js)

def tag(id_, t0, t1, top, txt):
    add(f'<div id="{id_}" class="tagrow clip" data-start="{f3(t0)}" data-duration="{f3(t1 - t0)}" data-track-index="1" style="top:{top}px"><span class="tag"><i class="dot"></i>{txt}</span></div>',
        [f'gtl.fromTo("#{id_} .tag", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.32, ease: "power3.out" }}, {f3(t0)});',
         f'gtl.to("#{id_} .tag", {{ opacity: 0, duration: 0.18, ease: "power2.in" }}, {f3(t1 - 0.18)});'])
tag("t-accion", 31.75, 35.60, 260, "En acción")
tag("t-pot", 37.85, 39.95, 260, "Potencia")
tag("t-mod", 41.25, 43.60, 260, "Modos de uso")

# seis modos · número gigante al lado
add('<div id="six" class="clip" data-start="43.700" data-duration="3.950" data-track-index="1"><div id="six-n">6</div><div id="six-t">modos</div></div>',
    ['gtl.fromTo("#six-n", { opacity: 0, y: 60, scale: .9 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "power3.out" }, 43.700);',
     'gtl.fromTo("#six-t", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.36, ease: "power3.out" }, 43.950);',
     'gtl.to("#six", { opacity: 0, duration: 0.2, ease: "power2.in" }, 47.450);'])

# montaje · llamada a la acción
h, js = card("cta", 53.00, 57.92, 300, '<div class="step">ExoMov</div><div class="title">Pruébalo en ExoMov</div>', cls="card lime")
add(h, js)

# cierre (2 s)
add(f'<div id="endcard" class="clip" data-start="{f3(END_AT - 0.08)}" data-duration="{f3(DUR - END_AT + 0.08)}" data-track-index="2">'
    '<img id="end-logo" src="assets/logos/exomov-logo-blanco.png" alt="ExoMov" />'
    '<div id="end-claim">Libertad de movimiento</div><div id="end-web">exomov.com</div></div>',
    [f'gtl.fromTo("#endcard", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25, ease: "power2.out" }}, {f3(END_AT - 0.08)});',
     f'gtl.fromTo("#end-logo", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.4, {ENTER} }}, {f3(END_AT)});',
     f'gtl.fromTo("#end-claim", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.36, {ENTER} }}, {f3(END_AT + 0.15)});',
     f'gtl.fromTo("#end-web", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.34, {ENTER} }}, {f3(END_AT + 0.25)});'])

graphics = f"""<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /></head>
  <body>
    <template>
      <style>{FONTS}
        #gfx-root {{ position: absolute; inset: 0; font-family: "Figtree", sans-serif; }}
        #gfx-root .card {{ position: absolute; left: 80px; right: 150px; padding: 36px 40px; border-radius: 28px; background: rgba(18,19,17,.88); border: 2px solid {BORDER}; color: {PAPER}; }}
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
        #hook {{ position: absolute; left: 40px; right: 40px; top: 330px; display: flex; flex-direction: column; align-items: center; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em;
              text-shadow: 0 0 46px rgba(18,19,17,.7), 0 6px 22px rgba(18,19,17,.65), 0 2px 4px rgba(18,19,17,.55); }}
        #hook-a {{ font-size: 220px; line-height: .9; color: {LIME}; white-space: nowrap; }}
        #hook-b {{ font-size: 112px; line-height: .95; color: {PAPER}; white-space: nowrap; }}
        #ring {{ position: absolute; left: 250px; top: 540px; width: 340px; height: 340px; border-radius: 999px; border: 10px solid {LIME}; box-shadow: 0 0 0 4px rgba(18,19,17,.35); }}
        #six {{ position: absolute; left: 70px; top: 560px; width: 300px; display: flex; flex-direction: column; align-items: center; font-family: "Bebas Neue", sans-serif; text-transform: uppercase;
              text-shadow: 0 6px 22px rgba(18,19,17,.55); }}
        #six-n {{ font-size: 420px; line-height: .8; color: {LIME}; }}
        #six-t {{ font-size: 110px; line-height: .9; color: {PAPER}; }}
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
Z = [(0.00, 1.06, 1.00, 0.70, "power3.out"),      # gancho
     (7.47, 1.00, 1.04, 2.50, "sine.inOut"),      # qué es
     (9.97, 1.00, 1.00, 0.01, "none"),
     (28.27, 1.00, 1.04, 3.40, "sine.inOut"),     # activado
     (31.67, 1.00, 1.00, 0.01, "none"),
     (43.63, 1.00, 1.05, 4.10, "sine.inOut"),     # seis modos
     (47.80, 1.00, 1.00, 0.01, "none")]
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
