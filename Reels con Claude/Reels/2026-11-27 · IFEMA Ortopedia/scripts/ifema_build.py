"""Reel IFEMA · constructor de versiones (A, B, D). Uso:  python ifema_build.py <A|B|D> <media|gfx|audio>
media: base.mp4 + pista de voz + subtítulos · gfx: proyecto HyperFrames · audio: música, efectos y mezcla."""
import json, os, re, subprocess, sys
import numpy as np

ROOT = "/home/user/editor-videos/Reels con Claude"
TOMAS = ROOT + "/Tomas/2026-11-27 · IFEMA Ortopedia"
PROY = ROOT + "/Reels/2026-11-27 · IFEMA Ortopedia"
SKILL = "/home/user/editor-videos/.claude/skills/editar-reels-claude/scripts"
BUILD = os.path.dirname(os.path.abspath(__file__))
F = 30
CLIPS = {"9703": "IMG_9703.MOV", "9709": "IMG_9709.mov", "9713": "IMG_9713.MOV", "9714": "IMG_9714.MOV", "9715": "IMG_9715.mov",
         "9716": "IMG_9716.mov", "9719": "IMG_9719.mov", "9734": "IMG_9734.MOV", "9735": "IMG_9735.MOV", "9737": "IMG_9737.MOV",
         "9743": "IMG_9743.mov", "9744": "IMG_9744.MOV", "9757": "IMG_9757.MOV", "9758": "IMG_9758.MOV", "9759": "IMG_9759.MOV",
         "9762": "IMG_9762.MOV", "9766": "IMG_9766.MOV", "9767": "IMG_9767.MOV"}
INK, LIME, PAPER, BORDER, S2 = "#121311", "#BEBD39", "#F6F6F1", "#3A3B35", "#262723"


def cut(c, i, b, v=False, vd=None, L=None, fx="", thud=None, lr=None):
    return dict(c=c, i=i, b=b, v=v, vd=vd, L=L, fx=fx, thud=thud, lr=lr)


SPECS = {
 "A": dict(dir="v-A-cronica", bpm=152, bars=29, tail=0.8, seed=11, end_b=7, cta_cut=22, boost=11,
   keys={"ifema", "equipos", "títere", "ritmo", "cadencia", "sana"},
   title=dict(a=("NOS VAMOS A", PAPER, 112), b=("IFEMA", LIME, 260), beats=(2, 10)),
   cuts=[cut("9703", 0.91, 6, fx="T", thud=1.70),
         cut("9762", 6.34, 16, v=True, vd=6.25, lr=(8.6, 12.3)),
         cut("9757", 0.9, 4, L=("1", "CINTURA"), fx="PK"), cut("9758", 1.6, 4, L=("2", "MUSLO"), fx="PK"),
         cut("9759", 4.2, 4, L=("3", "CORREA"), fx="PK"), cut("9737", 0.0, 4, L=("4", "RODILLA"), fx="PK"),
         cut("9766", 8.75, 4, fx="W"), cut("9709", 0.0, 2, fx="W"), cut("9713", 2.5, 4, fx="W"), cut("9715", 1.7, 4, fx="W"), cut("9714", 0.4, 4, fx="W"),
         cut("9716", 0.2, 5, fx="W"),
         cut("9743", 0.0, 10, v=True, vd=3.85), cut("9734", 5.52, 9, v=True, vd=3.5), cut("9735", 4.98, 9, v=True, vd=3.57), cut("9744", 0.65, 10, v=True, vd=3.5),
         cut("9719", 0.2, 3, fx="P"), cut("9743", 0.4, 2, fx="P"), cut("9744", 2.4, 2, fx="P"), cut("9714", 1.0, 3, fx="P")]),
 "B": dict(dir="v-B-relampago", bpm=168, bars=21, tail=1.0, seed=23, end_b=5, cta_cut=26, boost=11,
   keys={"ifema", "equipos", "títere", "sana"},
   title=dict(a=("EXOESQUELETOS", LIME, 150), b=("EN IFEMA", PAPER, 150), beats=(2, 9.5)),
   cuts=[cut("9703", 0.99, 6, fx="T", thud=1.70),
         cut("9762", 6.34, 4, v=True, vd=1.43, lr=(8.6, 12.3)), cut("9762", 8.55, 4, v=True, vd=1.38, fx="I", lr=(8.6, 12.3)),
         cut("9757", 1.0, 2, L=("", "CINTURA"), fx="PK"), cut("9758", 1.6, 2, L=("", "MUSLO"), fx="PK"), cut("9759", 4.2, 2, fx="PK"),
         cut("9737", 0.0, 2, L=("", "RODILLA"), fx="PK"), cut("9757", 2.0, 2, fx="PK"), cut("9758", 2.8, 2, fx="PK"), cut("9759", 5.0, 2, fx="PK"),
         cut("9719", 0.0, 3, L=("", "APP"), fx="PK"),
         cut("9766", 8.85, 3, fx="W"), cut("9715", 1.8, 3, fx="W"), cut("9713", 2.9, 3, fx="W"), cut("9714", 0.5, 3, fx="W"),
         cut("9743", 0.0, 11, v=True, vd=3.85), cut("9734", 9.0, 4, fx="P"), cut("9744", 0.65, 10, v=True, vd=3.5), cut("9735", 9.0, 4, fx="P"),
         cut("9716", 0.2, 4, fx="P"), cut("9735", 3.0, 3, fx="P")]),
 "D": dict(dir="v-D-un-dia", bpm=140, bars=35, tail=0.8, seed=37, end_b=4, cta_cut=22, boost=11,
   keys={"ifema", "equipos", "tecnología", "profesionales", "potencia", "estándar", "ritmo", "cadencia", "títere", "sana"},
   title=dict(a=("UN DÍA EN", PAPER, 130), b=("IFEMA", LIME, 260), beats=(2, 12)),
   cuts=[cut("9703", 0.41, 10, fx="T", thud=1.70),
         cut("9762", 6.34, 15, v=True, vd=6.3, lr=(8.6, 12.3)),
         cut("9757", 0.5, 6, L=("1", "CINTURA"), fx="PK"), cut("9758", 1.2, 5, L=("2", "MUSLO"), fx="PK"),
         cut("9759", 4.2, 5, L=("3", "CORREA"), fx="PK"), cut("9737", 0.0, 4, L=("4", "RODILLA"), fx="PK"),
         cut("9766", 3.0, 5), cut("9767", 2.4, 5, fx="P"), cut("9766", 8.75, 6, fx="W"),
         cut("9709", 0.0, 2, fx="W"), cut("9713", 2.5, 4, fx="W"), cut("9715", 1.6, 4, fx="W"), cut("9714", 0.3, 4, fx="W"),
         cut("9716", 0.2, 5, fx="W"), cut("9719", 0.0, 5, fx="P"),
         cut("9734", 1.65, 18, v=True, vd=7.65), cut("9735", 4.98, 9, v=True, vd=3.57), cut("9743", 0.0, 10, v=True, vd=3.85), cut("9744", 0.65, 9, v=True, vd=3.5),
         cut("9735", 9.5, 5, fx="P")]),
}


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def timeline(S):
    beat = 60 / S["bpm"]; out, b = [], 0
    for cu in S["cuts"]:
        sf, ef = round(b * beat * F), round((b + cu["b"]) * beat * F)
        out.append(dict(cu, ts=sf / F, te=ef / F, n=ef - sf, b0=b)); b += cu["b"]
    assert b + S["end_b"] == S["bars"] * 4, (b, S["end_b"], S["bars"] * 4)
    return out, beat, b * beat, round((S["bars"] * 4 * beat + S["tail"]) * F) / F


def paths(k):
    S = SPECS[k]; P = f"{PROY}/{S['dir']}"
    return S, P, f"{P}/trabajo", f"{P}/graficos"


def lufs(path, a, b):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(a), "-to", str(b), "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r); return float(m[-1]) if m else -30.0


# ------------------------------------------------------------------ MEDIA
KEEPSTR = "ABCD"
def clean_word(w): return re.sub(r"[¿?¡!,.;:]", "", w).strip()


def captions_for(S, TL):
    caps = []
    for cu in TL:
        if not cu["v"]: continue
        A = json.load(open(f"{TOMAS}/_analisis/IMG_{cu['c']}.json"))["words"]
        ws = [(clean_word(w["w"]), cu["ts"] + (w["s"] - cu["i"]), cu["ts"] + (min(w["e"], w["s"] + 0.7) - cu["i"]), w["w"]) for w in A if cu["i"] - 0.02 <= w["s"] < cu["i"] + cu["vd"] - 0.05]
        chunk = []
        def flush():
            nonlocal chunk
            if chunk: caps.append(dict(text=" ".join(x[0] for x in chunk), key=False, start=chunk[0][1], end=chunk[-1][2], words=[dict(w=x[0], t=x[1]) for x in chunk]))
            chunk = []
        for j, (t, s, e, raw) in enumerate(ws):
            if not t: continue
            if t.lower() in S["keys"]:
                flush(); caps.append(dict(text=t, key=True, start=s, end=e, words=[dict(w=t, t=s)])); continue
            if chunk and (s - chunk[-1][2] > 0.4 or len(chunk) >= 3): flush()
            chunk.append((t, s, e));
            if raw.endswith((".", "?", "!")): flush()
        flush()
    caps.sort(key=lambda c: c["start"])
    for x, y in zip(caps, caps[1:]):
        x["end"] = min(y["start"], x["end"] + 0.3)
        if x["end"] - x["start"] < 0.3 and y["start"] - x["start"] >= 0.3: x["end"] = x["start"] + 0.3
    for c in caps: c["start"], c["end"] = round(c["start"], 3), round(c["end"] + (0.25 if c is caps[-1] else 0), 3)
    return caps


def media(k):
    S, P, W, G = paths(k); TL, beat, t_end_cuts, DUR = timeline(S)
    os.makedirs(W + "/piezas", exist_ok=True)
    lst = ""
    for i, cu in (enumerate(TL) if os.environ.get("SKIP_BASE") != "1" else []):
        out = f"{W}/piezas/p{i:02d}.mp4"
        vf = f"tpad=stop_mode=clone:stop_duration=3,fps={F},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"
        sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{cu['i']:.3f}", "-i", f"{TOMAS}/{CLIPS[cu['c']]}", "-an", "-vf", vf, "-frames:v", str(cu["n"]),
            "-c:v", "libx264", "-preset", "fast", "-crf", "15", out])
        lst += f"file 'p{i:02d}.mp4'\n"
    pad = DUR - t_end_cuts
    if os.environ.get("SKIP_BASE") != "1":
        open(f"{W}/piezas/lista.txt", "w").write(lst)
        sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/piezas/lista.txt", "-vf", f"tpad=stop_mode=add:stop_duration={pad + 0.5:.3f}:color=0x121311,trim=duration={DUR:.3f}",
            "-r", str(F), "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p", f"{W}/base.mp4"])
    # voz: cada frase se coloca en su muestra exacta (sin filtros de retraso)
    from scipy.io import wavfile
    SR = 48000; track = np.zeros(int(round(DUR * SR)), np.float32)
    for cu in [c for c in TL if c["v"]]:
        src = f"{TOMAS}/{CLIPS[cu['c']]}"; a, d = cu["i"], cu["vd"]
        g = -20 - lufs(src, *(cu["lr"] or (a, a + d)))
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        x = np.frombuffer(raw, np.float32).copy() * 10 ** (g / 20)
        fd = int(0.015 * SR); x[:fd] *= np.linspace(0, 1, fd); x[-fd:] *= np.linspace(1, 0, fd)
        i0 = int(round(cu["ts"] * SR)); track[i0:i0 + len(x)] += x[: len(track) - i0]
    wavfile.write(f"{W}/audio48k.wav", SR, track)
    sh(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/audio48k.wav", "-ac", "1", "-ar", "16000", f"{W}/audio16k.wav"])
    json.dump({"duration": DUR, "fps": F, "segments": [[0, DUR]], "words": []}, open(f"{W}/words.json", "w"))
    vcuts = [c for c in TL if c["v"]]
    caps = captions_for(S, TL); json.dump(caps, open(f"{W}/captions.json", "w"), ensure_ascii=False, indent=1)
    json.dump({"DUR": DUR, "beat": beat, "cuts": TL}, open(f"{W}/montaje.json", "w"), ensure_ascii=False, indent=1)
    print(k, f"base {DUR:.2f} s · {len(TL)} cortes · {len(vcuts)} tomas de voz · {len(caps)} subtítulos")
    print(" | ".join(" ".join(x["text"].upper() if x["key"] else x["text"] for x in caps if abs(x["start"] - cu["ts"]) < cu["vd"] + 0.2 and x["start"] >= cu["ts"] - 0.1) for cu in vcuts))


# ------------------------------------------------------------------ GRÁFICOS
FONTS = '''@font-face { font-family: "Bebas Neue"; src: url("assets/fonts/bebas-neue-400.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-700.woff2") format("woff2"); font-weight: 700; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-800.woff2") format("woff2"); font-weight: 800; }'''
f3 = lambda x: f"{x:.3f}"


def gfx(k):
    S, P, W, G = paths(k); TL, beat, t_end, DUR = timeline(S)
    caps = json.load(open(f"{W}/captions.json")); END = t_end
    os.makedirs(G + "/compositions", exist_ok=True); os.makedirs(G + "/assets", exist_ok=True)
    for sub in ("fonts", "logos"):
        if not os.path.exists(f"{G}/assets/{sub}"): sh(["cp", "-r", f"{PROY}/../2026-11-24 · VIGX H1 PRO en 60 segundos/graficos/assets/{sub}", f"{G}/assets/{sub}"])
    if not os.path.exists(f"{G}/assets/gsap.min.js"): sh(["cp", f"{PROY}/../2026-11-24 · VIGX H1 PRO en 60 segundos/graficos/assets/gsap.min.js", f"{G}/assets/gsap.min.js"])
    if os.path.lexists(f"{G}/assets/base.mp4"): os.remove(f"{G}/assets/base.mp4")
    os.symlink("../../trabajo/base.mp4", f"{G}/assets/base.mp4")
    # --- subtítulos
    ch, cj = [], []
    for i, c in enumerate(caps):
        st, en = c["start"], min(c["end"], DUR)
        ch.append(f'<div id="cap-{i}" class="cap clip{" key" if c["key"] else ""}" data-start="{f3(st)}" data-duration="{f3(en - st)}" data-track-index="1"><div class="line">' +
                  "".join(f'<span id="w{i}-{j}" class="w">{w["w"]}</span>' for j, w in enumerate(c["words"])) + "</div></div>")
        if c["key"]: cj.append(f'ctl.fromTo("#cap-{i} .line", {{ opacity: 0, y: 26, scale: .94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.3, ease: "power3.out" }}, {f3(st)});')
        else:
            for j, w in enumerate(c["words"]): cj.append(f'ctl.fromTo("#w{i}-{j}", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.26, ease: "power3.out" }}, {f3(max(st, w["t"]))});')
    cap_html = f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /></head><body><template>
<style>{FONTS}
#captions-root {{ position: absolute; inset: 0; }}
#captions-root .cap {{ position: absolute; left: 80px; right: 150px; top: 1260px; height: 260px; display: flex; align-items: center; justify-content: center; text-align: center; }}
#captions-root .line {{ display: flex; flex-wrap: wrap; justify-content: center; align-items: baseline; gap: 0 16px; max-width: 100%; }}
#captions-root .w {{ display: inline-block; font-family: "Figtree", sans-serif; font-weight: 700; font-size: 62px; line-height: 1.1; color: {PAPER}; text-shadow: 0 4px 18px rgba(18,19,17,.65), 0 1px 3px rgba(18,19,17,.75); }}
#captions-root .key .w {{ font-family: "Bebas Neue", sans-serif; font-weight: 400; font-size: 168px; line-height: .92; letter-spacing: .01em; text-transform: uppercase; color: {LIME}; text-shadow: 0 6px 24px rgba(18,19,17,.7), 0 2px 4px rgba(18,19,17,.6); }}
</style>
<div id="captions-root" data-composition-id="captions" data-width="1080" data-height="1920" data-duration="{DUR}">{chr(10).join(ch)}</div>
<script>const ctl = gsap.timeline({{ paused: true }});
{chr(10).join(cj)}
window.__timelines["captions"] = ctl;</script></template></body></html>'''
    # --- gráficos
    gh, gj = [], []
    T = S["title"]; t0, t1 = T["beats"][0] * beat, T["beats"][1] * beat
    gh.append(f'<div id="hook" class="clip" data-start="{f3(t0)}" data-duration="{f3(t1 - t0)}" data-track-index="1"><div id="hook-a" style="color:{T["a"][1]};font-size:{T["a"][2]}px">{T["a"][0]}</div><div id="hook-b" style="color:{T["b"][1]};font-size:{T["b"][2]}px">{T["b"][0]}</div></div>')
    gj += [f'gtl.fromTo("#hook-a", {{ opacity: 0, y: 40, scale: .92 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(t0)});',
           f'gtl.fromTo("#hook-b", {{ opacity: 0, y: 30, scale: .92 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(t0 + beat * .5)});',
           f'gtl.to("#hook", {{ opacity: 0, duration: 0.12, ease: "power2.in" }}, {f3(t1 - 0.12)});']
    for i, cu in enumerate(TL):
        if cu["L"]:
            num, word = cu["L"]
            gh.append(f'<div id="lb{i}" class="lab clip" data-start="{f3(cu["ts"])}" data-duration="{f3(cu["te"] - cu["ts"])}" data-track-index="1">' + (f'<span class="n">{num}</span>' if num else "") + f'<span class="wd">{word}</span></div>')
            gj.append(f'gtl.fromTo("#lb{i}", {{ opacity: 0, scale: 1.22 }}, {{ opacity: 1, scale: 1, duration: 0.14, ease: "power4.out" }}, {f3(cu["ts"])});')
    first_m = len(TL)
    while first_m > 0 and not TL[first_m - 1]["v"]: first_m -= 1
    cta_t0 = TL[first_m]["ts"] + 0.4 * beat
    gh.append(f'<div id="cta" class="card lime clip" data-start="{f3(cta_t0)}" data-duration="{f3(END - cta_t0 - 0.05)}" data-track-index="1"><div class="step">ExoMov</div><div class="ctat">Descubre<br>cómo probarlo</div>'
              '<div class="ctas"><svg viewBox="0 0 24 24" width="44" height="44" aria-hidden="true"><path d="M12 3.5c-4.97 0-9 3.47-9 7.75 0 2.08.95 3.97 2.5 5.36L4.8 20.5l4.2-1.86c.94.24 1.95.36 3 .36 4.97 0 9-3.47 9-7.75S16.97 3.5 12 3.5z" fill="none" stroke="#121311" stroke-width="2" stroke-linejoin="round"/></svg>Consúltanos por WhatsApp</div></div>')
    gj += [f'gtl.fromTo("#cta", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {f3(cta_t0)});']
    gh.append(f'<div id="endcard" class="clip" data-start="{f3(END - 0.05)}" data-duration="{f3(DUR - END + 0.05)}" data-track-index="2"><img id="end-logo" src="assets/logos/exomov-logo-blanco.png" alt="ExoMov" /><div id="end-claim">Libertad de movimiento</div><div id="end-web">exomov.com</div></div>')
    gj += [f'gtl.fromTo("#endcard", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.12, ease: "power2.out" }}, {f3(END - 0.05)});',
           f'gtl.fromTo("#end-logo", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.34, ease: "power3.out" }}, {f3(END)});',
           f'gtl.fromTo("#end-claim", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {f3(END + 0.15)});',
           f'gtl.fromTo("#end-web", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {f3(END + 0.3)});']
    gfx_html = f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8" /></head><body><template>
<style>{FONTS}
#gfx-root {{ position: absolute; inset: 0; font-family: "Figtree", sans-serif; }}
#gfx-root .card {{ position: absolute; left: 80px; right: 150px; top: 300px; padding: 36px 40px; border-radius: 28px; background: rgba(18,19,17,.88); border: 2px solid {BORDER}; color: {PAPER}; }}
#gfx-root .card.lime {{ background: {LIME}; border-color: #828120; color: {INK}; }}
#gfx-root .step {{ font-weight: 700; font-size: 28px; line-height: 1; letter-spacing: .06em; text-transform: uppercase; color: #2C2B0E; }}
#gfx-root .ctat {{ font-family: "Figtree", sans-serif; font-weight: 800; font-size: 76px; line-height: 1.04; text-transform: uppercase; letter-spacing: .005em; margin-top: 14px; color: {INK}; }}
#gfx-root .ctas {{ display: flex; align-items: center; gap: 14px; margin-top: 18px; font-weight: 700; font-size: 40px; color: {INK}; }}
#gfx-root .lab {{ position: absolute; left: 60px; right: 150px; top: 300px; display: flex; align-items: baseline; justify-content: center; gap: 28px; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em; text-shadow: 0 6px 22px rgba(18,19,17,.7), 0 2px 4px rgba(18,19,17,.6); white-space: nowrap; }}
#gfx-root .lab .n {{ font-size: 260px; line-height: .8; color: {LIME}; }}
#gfx-root .lab .wd {{ font-size: 170px; line-height: .9; color: {PAPER}; }}
#hook {{ position: absolute; left: 40px; right: 40px; top: 290px; display: flex; flex-direction: column; align-items: center; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em; text-shadow: 0 0 46px rgba(18,19,17,.7), 0 6px 22px rgba(18,19,17,.65), 0 2px 4px rgba(18,19,17,.55); }}
#hook-a, #hook-b {{ line-height: .92; white-space: nowrap; }}
#endcard {{ position: absolute; inset: 0; background: {INK}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; padding-bottom: 120px; }}
#end-logo {{ width: 640px; height: auto; }}
#end-claim {{ max-width: 700px; font-family: "Bebas Neue", sans-serif; font-size: 112px; line-height: .95; letter-spacing: .01em; text-transform: uppercase; color: {PAPER}; text-align: center; }}
#end-web {{ font-weight: 700; font-size: 44px; color: {LIME}; letter-spacing: .01em; }}
</style>
<div id="gfx-root" data-composition-id="graphics" data-width="1080" data-height="1920" data-duration="{DUR}">{chr(10).join(gh)}</div>
<script>const gtl = gsap.timeline({{ paused: true }});
{chr(10).join(gj)}
window.__timelines["graphics"] = gtl;</script></template></body></html>'''
    # --- zoom, barridos y golpes de zoom sobre la base
    zj = []
    for cu in TL:
        ts = cu["ts"]
        if "W" in cu["fx"] and ts > 0.2:
            zj.append(f'tl.fromTo("#zoom", {{ x: 0, scale: 1, filter: "blur(0px)" }}, {{ x: -150, scale: 1.14, filter: "blur(24px)", duration: 0.09, ease: "power2.in", immediateRender: false }}, {f3(ts - 0.09)});')
            zj.append(f'tl.fromTo("#zoom", {{ x: 150, scale: 1.14, filter: "blur(24px)" }}, {{ x: 0, scale: 1, filter: "blur(0px)", duration: 0.17, ease: "power3.out", immediateRender: false }}, {f3(ts)});')
        if "P" in cu["fx"]:
            zj.append(f'tl.fromTo("#zoom", {{ scale: 1.08 }}, {{ scale: 1, duration: 0.2, ease: "power3.out", immediateRender: false }}, {f3(ts)});')
        if "T" in cu["fx"]:
            tt = ts + (cu["thud"] - cu["i"])
            zj.append(f'tl.fromTo("#zoom", {{ scale: 1.14 }}, {{ scale: 1, duration: 0.32, ease: "power3.out", immediateRender: false }}, {f3(tt)});')
    index = f'''<!doctype html>
<html lang="es" data-resolution="portrait"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="assets/gsap.min.js"></script>
<style>* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {INK}; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; }}
#zoom {{ position: absolute; inset: 0; transform-origin: 50% 45%; }}
#base {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
.layer {{ position: absolute; inset: 0; }}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
<div id="zoom"><video id="base" class="clip" src="assets/base.mp4" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="0"></video></div>
<div id="captions-host" class="layer" data-composition-id="captions" data-composition-src="compositions/captions.html" data-track-kind="captions" data-start="0" data-duration="{DUR}" data-track-index="2" data-width="1080" data-height="1920"></div>
<div id="graphics-host" class="layer" data-composition-id="graphics" data-composition-src="compositions/graphics.html" data-start="0" data-duration="{DUR}" data-track-index="3" data-width="1080" data-height="1920"></div>
</div>
<script>const tl = gsap.timeline({{ paused: true }});
{chr(10).join(zj)}
window.__timelines["main"] = tl;</script></body></html>'''
    open(f"{G}/index.html", "w", encoding="utf-8").write(index)
    open(f"{G}/compositions/captions.html", "w", encoding="utf-8").write(cap_html)
    open(f"{G}/compositions/graphics.html", "w", encoding="utf-8").write(gfx_html)
    print(k, "gráficos ok · CTA desde", round(cta_t0, 2), "s · cierre desde", round(END, 2), "s")


# ------------------------------------------------------------------ AUDIO
def audio(k):
    S, P, W, G = paths(k); TL, beat, t_end, DUR = timeline(S)
    sh(["python3", f"{BUILD}/rock_track.py", "--bpm", str(S["bpm"]), "--bars", str(S["bars"]), "--tail", str(S["tail"] + 0.4), "--seed", str(S["seed"]), "--style", "garage", "--out", f"{W}/musica.wav"])
    if not os.path.exists(W + "/sfx"): sh(["cp", "-r", f"{PROY}/../2026-11-24 · VIGX H1 PRO en 60 segundos/trabajo/sfx", W + "/sfx"])
    # música: más fuerte en los tramos sin voz, rampa de 0,25 s
    E, R, f = "1", 0.25, 10 ** (S["boost"] / 20) - 1
    voice = [(cu["ts"], cu["ts"] + cu["vd"] + 0.15) for cu in TL if cu["v"]]
    edges, prev = [], 0.0
    for a, b in voice: edges.append((prev, a)); prev = b
    edges.append((prev, DUR + 1))
    for a, b in edges:
        if b - a > 0.3: E += f"+{f:.3f}*max(0,min(1,min((t-{a:.3f})/{R},({b:.3f}-t)/{R})))" if a > 0 else f"+{f:.3f}*max(0,min(1,({b:.3f}-t)/{R}))"
    sh(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/musica.wav", "-af", f"volume='{E}':eval=frame", "-c:a", "pcm_s24le", f"{W}/musica_env.wav"])
    ev = []
    def add(name, t, db, mx=None):
        if 0 <= t < DUR: ev.append({"file": f"sfx/{name}.wav", "t": round(t, 3), "db": db, **({"max": mx} if mx else {})})
    for cu in TL:
        if "W" in cu["fx"] and cu["ts"] > 0.2: add("whoosh", cu["ts"] - 0.07, -22)
        if "K" in cu["fx"]: add("uiclick", cu["ts"], -21, 0.3)
        if "T" in cu["fx"]: add("impact", cu["ts"] + cu["thud"] - cu["i"], -16)
        if "I" in cu["fx"]: add("impact", cu["ts"], -24)
    add("riser", t_end - 2.6, -27); add("uiclick", t_end, -23, 0.3)
    add("impact", S["bars"] * 4 * beat, -18)
    json.dump(sorted(ev, key=lambda e: e["t"]), open(f"{W}/sfx.json", "w"), indent=1)
    r = subprocess.run(["python3", f"{SKILL}/mix.py", "--work", W, "--sfx", f"{W}/sfx.json", "--music", f"{W}/musica_env.wav", "--music-under", "-1", "--duck", "9"], capture_output=True, text=True)
    print(k, r.stdout.strip().splitlines()[-1], r.stderr[-300:] if r.returncode else "")


if __name__ == "__main__":
    k, step = sys.argv[1], sys.argv[2]
    {"media": media, "gfx": gfx, "audio": audio}[step](k)
