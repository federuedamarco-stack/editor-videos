"""Reel IFEMA v2 · constructor de versiones (A, B, D). Uso:  python ifema_build.py <A|B|D> <media|gfx|audio>
media: base.mp4 + pista de voz + subtítulos · gfx: proyecto HyperFrames · audio: música, efectos y mezcla.
Cambios v2: el actor termina en el plano en que cierra el maletero y sigue en off sobre el maletero cerrado; los cuatro primeros planos
van a la vez en pantalla dividida; cortes más lentos; el vídeo acaba con las dos personas de ExoMov; la A lleva un cuadro de «Reacciones»."""
import json, os, re, subprocess, sys
import numpy as np

ROOT = "/home/user/editor-videos/Reels con Claude"
TOMAS = ROOT + "/Tomas/2026-11-27 · IFEMA Ortopedia"
PROY = ROOT + "/Reels/2026-11-27 · IFEMA Ortopedia"
VIGX = ROOT + "/Reels/2026-11-24 · VIGX H1 PRO en 60 segundos"
SKILL = "/home/user/editor-videos/.claude/skills/editar-reels-claude/scripts"
BUILD = os.path.dirname(os.path.abspath(__file__))
F = 30
CLIPS = {"9703": "IMG_9703.MOV", "9709": "IMG_9709.mov", "9713": "IMG_9713.MOV", "9714": "IMG_9714.MOV", "9715": "IMG_9715.mov",
         "9716": "IMG_9716.mov", "9719": "IMG_9719.mov", "9734": "IMG_9734.MOV", "9735": "IMG_9735.MOV", "9737": "IMG_9737.MOV",
         "9743": "IMG_9743.mov", "9744": "IMG_9744.MOV", "9757": "IMG_9757.MOV", "9758": "IMG_9758.MOV", "9759": "IMG_9759.MOV",
         "9762": "IMG_9762.MOV", "9766": "IMG_9766.MOV", "9767": "IMG_9767.MOV"}
INK, LIME, PAPER, BORDER, S2 = "#121311", "#BEBD39", "#F6F6F1", "#3A3B35", "#262723"
CUT = 7.5            # segundo de 9762 en que se corta, con la tapa del maletero a mitad de caída
IN703 = 1.35         # segundo de 9703 en que entra la tapa (continúa el movimiento)
SLAM703 = 1.84       # el golpe de la tapa en el audio de 9703
TRI = [("9757", 0.8, 1.0, 700), ("9758", 0.3, 1.0, None), ("9759", 2.8, 1.0, None)]    # (clip, entrada, velocidad, recorte y de la franja superior)
QLAB = ["1 CINTURA", "2 PIERNA", "3 PIERNA"]


def cut(c, i, b, v=False, vd=None, fx="", lr=None, q=None, badge=False, sp=1.0, ov=None, thud=None):
    return dict(c=c, i=i, b=b, v=v, vd=vd, fx=fx, lr=lr, q=q, badge=badge, sp=sp, ov=ov, thud=thud)


def vo(c, i, d, at, lr=None):
    return dict(c=c, i=i, d=d, at=at, lr=lr)


def opening(beat, beats_actor, extra_closed):
    """Plano del actor hasta que cierra el maletero + plano del maletero ya cerrado."""
    return [cut("9762", round(CUT - beats_actor * beat, 2), beats_actor), cut("9703", IN703, extra_closed, fx="T", thud=SLAM703)]


def tricut(n): return cut("TRI", 0, n, q=TRI, fx="P")


def vo_at(beat, beats_actor, src_in): return round((src_in - round(CUT - beats_actor * beat, 2)) / beat, 3)


A_b, B_b, D_b = 60 / 152, 60 / 168, 60 / 140
SPECS = {
 "A": dict(dir="v-A-cronica", nombre="IFEMA A · Crónica al ritmo", bpm=152, bars=28, tail=0.8, seed=11, end_b=7, boost=11,
   keys={"ifema", "equipos", "títere", "ritmo", "cadencia", "sana"},
   title=dict(a=("NOS VAMOS A", PAPER, 112), b=("IFEMA", LIME, 260), beats=(0.5, 9)),
   vo=[vo("9762", 6.37, 6.25, vo_at(A_b, 3, 6.37), lr=(8.6, 12.3))],
   cuts=opening(A_b, 3, 7) + [tricut(10),
         cut("9709", 0.0, 5, fx="W", sp=0.5, ov=dict(a=("ORTO MEDICAL CARE", PAPER, 104), b=("2026", LIME, 230))),
         cut("9713", 2.4, 5, fx="W"), cut("9714", 0.3, 5, fx="W"), cut("9715", 1.75, 6, fx="W"),
         cut("9716", 0.2, 5, fx="W", badge=True),
         cut("9743", 0.0, 10, v=True, vd=3.85, badge=True), cut("9734", 5.52, 9, v=True, vd=3.5), cut("9735", 4.98, 9, v=True, vd=3.57), cut("9744", 0.65, 10, v=True, vd=3.5),
         cut("9719", 0.2, 4, fx="P"), cut("9767", 4.5, 7, fx="P"), cut("9766", 0.5, 10, fx="P")]),
 "B": dict(dir="v-B-relampago", nombre="IFEMA B · Relámpago", bpm=168, bars=20, tail=1.0, seed=23, end_b=5, boost=11,
   keys={"ifema", "equipos", "títere", "sana"},
   title=dict(a=("EXOESQUELETOS", LIME, 150), b=("EN IFEMA", PAPER, 150), beats=(0.5, 8.5)),
   vo=[vo("9762", 6.34, 1.43, vo_at(B_b, 4, 6.34), lr=(8.6, 12.3)), vo("9762", 8.55, 1.38, round(2.0 / B_b, 3), lr=(8.6, 12.3))],
   cuts=opening(B_b, 4, 5) + [tricut(11),
         cut("9766", 8.85, 4, fx="W"), cut("9709", 0.0, 2, fx="W"), cut("9715", 1.7, 4, fx="W"), cut("9713", 2.7, 4, fx="W"), cut("9714", 0.4, 4, fx="W"),
         cut("9743", 0.0, 11, v=True, vd=3.85), cut("9734", 9.0, 4, fx="P"), cut("9744", 0.65, 10, v=True, vd=3.5), cut("9735", 9.0, 4, fx="P"),
         cut("9767", 2.4, 8, fx="P")]),
 "D": dict(dir="v-D-un-dia", nombre="IFEMA D · Un día en IFEMA", bpm=140, bars=33, tail=0.8, seed=37, end_b=4, boost=11,
   keys={"ifema", "equipos", "tecnología", "profesionales", "potencia", "estándar", "ritmo", "cadencia", "títere", "sana"},
   title=dict(a=("UN DÍA EN", PAPER, 130), b=("IFEMA", LIME, 260), beats=(0.5, 12)),
   vo=[vo("9762", 6.34, 6.3, vo_at(D_b, 4, 6.34), lr=(8.6, 12.3))],
   cuts=opening(D_b, 4, 6) + [tricut(9),
         cut("9766", 3.0, 6), cut("9766", 8.75, 6, fx="W"),
         cut("9709", 0.0, 2, fx="W"), cut("9713", 2.4, 7, fx="W"), cut("9715", 1.5, 6, fx="W"), cut("9714", 0.2, 6, fx="W"),
         cut("9716", 0.2, 6, fx="W"), cut("9719", 0.0, 6, fx="P"),
         cut("9734", 1.65, 18, v=True, vd=7.65), cut("9735", 4.98, 9, v=True, vd=3.57), cut("9743", 0.0, 10, v=True, vd=3.85), cut("9744", 0.65, 10, v=True, vd=3.5),
         cut("9735", 9.5, 5, fx="P"), cut("9767", 2.4, 12, fx="P")]),
}


def sh(cmd, **kw): return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def timeline(S):
    beat = 60 / S["bpm"]; out, b = [], 0
    for cu in S["cuts"]:
        sf, ef = round(b * beat * F), round((b + cu["b"]) * beat * F)
        out.append(dict(cu, ts=sf / F, te=ef / F, n=ef - sf, b0=b)); b += cu["b"]
    assert b + S["end_b"] == S["bars"] * 4, (b, S["end_b"], S["bars"] * 4)
    vs = [dict(c=cu["c"], i=cu["i"], d=cu["vd"], ts=cu["ts"], lr=cu["lr"]) for cu in out if cu["v"]]
    vs += [dict(c=x["c"], i=x["i"], d=x["d"], ts=round(x["at"] * beat, 3), lr=x["lr"]) for x in S.get("vo", [])]
    vs.sort(key=lambda v: v["ts"])
    return out, beat, b * beat, round((S["bars"] * 4 * beat + S["tail"]) * F) / F, vs


def paths(k):
    S = SPECS[k]; P = f"{PROY}/{S['dir']}"
    return S, P, f"{P}/trabajo", f"{P}/graficos"


def lufs(path, a, b):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(a), "-to", str(b), "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r); return float(m[-1]) if m else -30.0


# ------------------------------------------------------------------ MEDIA
def clean_word(w): return re.sub(r"[¿?¡!,.;:]", "", w).strip()


def captions_for(S, VS):
    caps = []
    for vc in VS:
        A = json.load(open(f"{TOMAS}/_analisis/IMG_{vc['c']}.json"))["words"]
        ws = [(clean_word(w["w"]), vc["ts"] + (w["s"] - vc["i"]), vc["ts"] + (min(w["e"], w["s"] + 0.7) - vc["i"]), w["w"]) for w in A if vc["i"] - 0.02 <= w["s"] < vc["i"] + vc["d"] - 0.05]
        chunk = []
        def flush():
            nonlocal chunk
            if chunk: caps.append(dict(text=" ".join(x[0] for x in chunk), key=False, start=chunk[0][1], end=chunk[-1][2], words=[dict(w=x[0], t=x[1]) for x in chunk]))
            chunk = []
        for t, s, e, raw in ws:
            if not t: continue
            if t.lower() in S["keys"]:
                flush(); caps.append(dict(text=t, key=True, start=s, end=e, words=[dict(w=t, t=s)])); continue
            if chunk and (s - chunk[-1][2] > 0.4 or len(chunk) >= 3): flush()
            chunk.append((t, s, e))
            if raw.endswith((".", "?", "!")): flush()
        flush()
    caps.sort(key=lambda c: c["start"])
    for x, y in zip(caps, caps[1:]):
        x["end"] = min(y["start"], x["end"] + 0.3)
        if x["end"] - x["start"] < 0.3 and y["start"] - x["start"] >= 0.3: x["end"] = x["start"] + 0.3
    for c in caps: c["start"], c["end"] = round(max(0.0, c["start"]), 3), round(c["end"] + (0.25 if c is caps[-1] else 0), 3)
    return caps


VF1 = f"tpad=stop_mode=clone:stop_duration=3,fps={F},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"


def make_piece(cu, out):
    if cu["c"] != "TRI":
        sp = cu.get("sp", 1.0); vf = VF1 if sp == 1.0 else VF1.replace("fps=", f"setpts=PTS/{sp},fps=", 1)
        sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{cu['i']:.3f}", "-i", f"{TOMAS}/{CLIPS[cu['c']]}", "-an", "-vf", vf, "-frames:v", str(cu["n"]),
            "-c:v", "libx264", "-preset", "fast", "-crf", "15", out]); return
    inp, fc = [], []
    for k, (c, i, sp, cy) in enumerate(cu["q"]):
        inp += ["-ss", f"{i:.3f}", "-i", f"{TOMAS}/{CLIPS[c]}"]
        base = f"[{k}:v]tpad=stop_mode=clone:stop_duration=3,setpts=PTS/{sp},fps={F},"
        if k == 0: fc.append(base + f"scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:960:0:{cy},setsar=1,format=yuv420p[p0]")
        else: fc.append(base + f"scale=540:960:force_original_aspect_ratio=increase:flags=lanczos,crop=540:960,setsar=1,format=yuv420p[p{k}]")
    fc.append("[p1][p2]hstack=inputs=2[bot];[p0][bot]vstack=inputs=2[v]")
    sh(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", "[v]", "-an", "-frames:v", str(cu["n"]), "-c:v", "libx264", "-preset", "fast", "-crf", "15", out])


def media(k):
    S, P, W, G = paths(k); TL, beat, t_end, DUR, VS = timeline(S)
    os.makedirs(W + "/piezas", exist_ok=True)
    if os.environ.get("SKIP_BASE") != "1":
        lst = ""
        for i, cu in enumerate(TL):
            make_piece(cu, f"{W}/piezas/p{i:02d}.mp4"); lst += f"file 'p{i:02d}.mp4'\n"
        open(f"{W}/piezas/lista.txt", "w").write(lst)
        sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/piezas/lista.txt", "-vf", f"tpad=stop_mode=add:stop_duration={DUR - t_end + 0.5:.3f}:color=0x121311,trim=duration={DUR:.3f}",
            "-r", str(F), "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p", f"{W}/base.mp4"])
    from scipy.io import wavfile
    SR = 48000; track = np.zeros(int(round(DUR * SR)), np.float32)
    for vc in VS:
        src = f"{TOMAS}/{CLIPS[vc['c']]}"; a, d = vc["i"], vc["d"]
        g = -20 - lufs(src, *(vc["lr"] or (a, a + d)))
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        x = np.frombuffer(raw, np.float32).copy() * 10 ** (g / 20)
        fd = int(0.015 * SR); x[:fd] *= np.linspace(0, 1, fd); x[-fd:] *= np.linspace(1, 0, fd)
        i0 = int(round(vc["ts"] * SR)); track[i0:i0 + len(x)] += x[: len(track) - i0]
    wavfile.write(f"{W}/audio48k.wav", SR, track)
    sh(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/audio48k.wav", "-ac", "1", "-ar", "16000", f"{W}/audio16k.wav"])
    json.dump({"duration": DUR, "fps": F, "segments": [[0, DUR]], "words": []}, open(f"{W}/words.json", "w"))
    caps = captions_for(S, VS); json.dump(caps, open(f"{W}/captions.json", "w"), ensure_ascii=False, indent=1)
    json.dump({"DUR": DUR, "beat": beat, "cuts": TL, "voces": VS}, open(f"{W}/montaje.json", "w"), ensure_ascii=False, indent=1)
    print(k, f"base {DUR:.2f} s · {len(TL)} cortes · {len(VS)} frases de voz · {len(caps)} subtítulos")
    print(" | ".join(f"{c['start']:.1f} " + (c["text"].upper() if c["key"] else c["text"]) for c in caps if c["start"] < 9))


# ------------------------------------------------------------------ GRÁFICOS
FONTS = '''@font-face { font-family: "Bebas Neue"; src: url("assets/fonts/bebas-neue-400.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-700.woff2") format("woff2"); font-weight: 700; }
@font-face { font-family: "Figtree"; src: url("assets/fonts/figtree-800.woff2") format("woff2"); font-weight: 800; }'''
f3 = lambda x: f"{x:.3f}"


def gfx(k):
    S, P, W, G = paths(k); TL, beat, t_end, DUR, VS = timeline(S)
    caps = json.load(open(f"{W}/captions.json")); END = t_end
    os.makedirs(G + "/compositions", exist_ok=True); os.makedirs(G + "/assets", exist_ok=True)
    for sub in ("fonts", "logos"):
        if not os.path.exists(f"{G}/assets/{sub}"): sh(["cp", "-r", f"{VIGX}/graficos/assets/{sub}", f"{G}/assets/{sub}"])
    if not os.path.exists(f"{G}/assets/gsap.min.js"): sh(["cp", f"{VIGX}/graficos/assets/gsap.min.js", f"{G}/assets/gsap.min.js"])
    if os.path.lexists(f"{G}/assets/base.mp4"): os.remove(f"{G}/assets/base.mp4")
    os.symlink("../../trabajo/base.mp4", f"{G}/assets/base.mp4")
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
    gh, gj = [], []
    T = S["title"]; t0, t1 = T["beats"][0] * beat, T["beats"][1] * beat
    gh.append(f'<div id="hook" class="clip" data-start="{f3(t0)}" data-duration="{f3(t1 - t0)}" data-track-index="1"><div id="hook-a" style="color:{T["a"][1]};font-size:{T["a"][2]}px">{T["a"][0]}</div><div id="hook-b" style="color:{T["b"][1]};font-size:{T["b"][2]}px">{T["b"][0]}</div></div>')
    gj += [f'gtl.fromTo("#hook-a", {{ opacity: 0, y: 40, scale: .92 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(t0)});',
           f'gtl.fromTo("#hook-b", {{ opacity: 0, y: 30, scale: .92 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(t0 + beat * .5)});',
           f'gtl.to("#hook", {{ opacity: 0, duration: 0.12, ease: "power2.in" }}, {f3(t1 - 0.12)});']
    for qi, cu in enumerate(TL):
        if cu["c"] != "TRI": continue
        a, b = cu["ts"], cu["te"]
        gh.append(f'<div id="qv{qi}" class="qline clip" data-start="{f3(a)}" data-duration="{f3(b - a)}" data-track-index="1" style="left:537px;top:960px;width:6px;height:960px"></div>'
                  f'<div id="qh{qi}" class="qline clip" data-start="{f3(a)}" data-duration="{f3(b - a)}" data-track-index="1" style="left:0;top:957px;width:1080px;height:6px"></div>')
        pos = [(24, 872), (24, 984), (564, 984)]
        for p, (x, y) in enumerate(pos):
            num, word = QLAB[p].split(" ", 1)
            gh.append(f'<div id="ql{qi}-{p}" class="plab clip" data-start="{f3(a)}" data-duration="{f3(b - a)}" data-track-index="1" style="left:{x}px;top:{y}px"><span class="n">{num}</span><span class="wd">{word}</span></div>')
            gj.append(f'gtl.fromTo("#ql{qi}-{p}", {{ opacity: 0, scale: 1.25 }}, {{ opacity: 1, scale: 1, duration: 0.14, ease: "power4.out" }}, {f3(a + 0.12 * (p + 1))});')
    for oi, cu in enumerate(TL):                      # texto sobre un plano (p. ej. el cartel de la feria)
        if not cu["ov"]: continue
        a, b = cu["ts"] + 0.05, cu["te"] + 0.3 * beat
        o = cu["ov"]
        gh.append(f'<div id="ov{oi}" class="ovt clip" data-start="{f3(a)}" data-duration="{f3(b - a)}" data-track-index="1"><div id="ov{oi}a" style="color:{o["a"][1]};font-size:{o["a"][2]}px">{o["a"][0]}</div><div id="ov{oi}b" style="color:{o["b"][1]};font-size:{o["b"][2]}px">{o["b"][0]}</div></div>')
        gj += [f'gtl.fromTo("#ov{oi}a", {{ opacity: 0, y: 30, scale: .94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(a)});',
               f'gtl.fromTo("#ov{oi}b", {{ opacity: 0, y: 30, scale: .94 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.2, ease: "power4.out" }}, {f3(a + 0.15)});',
               f'gtl.to("#ov{oi}", {{ opacity: 0, duration: 0.12, ease: "power2.in" }}, {f3(b - 0.12)});']
    bi = [i for i, c in enumerate(TL) if c["badge"]]
    if bi:
        a, b = TL[bi[0]]["ts"] + 0.1, TL[bi[-1]]["te"]
        gh.append(f'<div id="badge" class="card clip" data-start="{f3(a)}" data-duration="{f3(b - a)}" data-track-index="1" style="top:270px"><div class="step" style="color:{LIME}">En IFEMA</div><div class="btitle">Reacciones de<br>los profesionales</div></div>')
        gj.append(f'gtl.fromTo("#badge", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {f3(a)});')
        gj.append(f'gtl.to("#badge", {{ opacity: 0, y: -24, duration: 0.2, ease: "power2.in" }}, {f3(b - 0.2)});')
    cta_t0 = TL[-1]["ts"] + 0.3 * beat
    gh.append(f'<div id="cta" class="card lime clip" data-start="{f3(cta_t0)}" data-duration="{f3(END - cta_t0 - 0.05)}" data-track-index="1" style="top:300px"><div class="step">ExoMov</div><div class="ctat">Descubre<br>cómo probarlo</div>'
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
#gfx-root .card {{ position: absolute; left: 80px; right: 150px; top: 300px; padding: 36px 40px; border-radius: 28px; background: rgba(18,19,17,.9); border: 2px solid {BORDER}; color: {PAPER}; }}
#gfx-root .card.lime {{ background: {LIME}; border-color: #828120; color: {INK}; }}
#gfx-root .step {{ font-weight: 700; font-size: 28px; line-height: 1; letter-spacing: .06em; text-transform: uppercase; color: #2C2B0E; }}
#gfx-root .btitle {{ font-family: "Bebas Neue", sans-serif; font-size: 104px; line-height: .92; letter-spacing: .01em; text-transform: uppercase; margin-top: 12px; color: {PAPER}; }}
#gfx-root .ctat {{ font-family: "Figtree", sans-serif; font-weight: 800; font-size: 76px; line-height: 1.04; text-transform: uppercase; letter-spacing: .005em; margin-top: 14px; color: {INK}; }}
#gfx-root .ctas {{ display: flex; align-items: center; gap: 14px; margin-top: 18px; font-weight: 700; font-size: 40px; color: {INK}; }}
#gfx-root .qline {{ position: absolute; background: {INK}; }}
#gfx-root .plab {{ position: absolute; display: flex; align-items: baseline; gap: 14px; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em; text-shadow: 0 4px 16px rgba(18,19,17,.85), 0 1px 3px rgba(18,19,17,.8); white-space: nowrap; }}
#gfx-root .plab .n {{ font-size: 96px; line-height: .8; color: {LIME}; }}
#gfx-root .plab .wd {{ font-size: 70px; line-height: .9; color: {PAPER}; }}
#hook {{ position: absolute; left: 40px; right: 40px; top: 290px; display: flex; flex-direction: column; align-items: center; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em; text-shadow: 0 0 46px rgba(18,19,17,.7), 0 6px 22px rgba(18,19,17,.65), 0 2px 4px rgba(18,19,17,.55); }}
#hook-a, #hook-b {{ line-height: .92; white-space: nowrap; }}
#gfx-root .ovt {{ position: absolute; left: 30px; right: 30px; top: 1090px; display: flex; flex-direction: column; align-items: center; font-family: "Bebas Neue", sans-serif; text-transform: uppercase; letter-spacing: .01em; text-shadow: 0 0 46px rgba(18,19,17,.75), 0 6px 22px rgba(18,19,17,.7), 0 2px 4px rgba(18,19,17,.6); }}
#gfx-root .ovt div {{ line-height: .92; white-space: nowrap; }}
#endcard {{ position: absolute; inset: 0; background: {INK}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; padding-bottom: 120px; }}
#end-logo {{ width: 640px; height: auto; }}
#end-claim {{ max-width: 700px; font-family: "Bebas Neue", sans-serif; font-size: 112px; line-height: .95; letter-spacing: .01em; text-transform: uppercase; color: {PAPER}; text-align: center; }}
#end-web {{ font-weight: 700; font-size: 44px; color: {LIME}; letter-spacing: .01em; }}
</style>
<div id="gfx-root" data-composition-id="graphics" data-width="1080" data-height="1920" data-duration="{DUR}">{chr(10).join(gh)}</div>
<script>const gtl = gsap.timeline({{ paused: true }});
{chr(10).join(gj)}
window.__timelines["graphics"] = gtl;</script></template></body></html>'''
    zj = []
    for cu in TL:
        ts = cu["ts"]
        if "W" in cu["fx"] and ts > 0.2:
            zj.append(f'tl.fromTo("#zoom", {{ x: 0, scale: 1, filter: "blur(0px)" }}, {{ x: -150, scale: 1.14, filter: "blur(24px)", duration: 0.09, ease: "power2.in", immediateRender: false }}, {f3(ts - 0.09)});')
            zj.append(f'tl.fromTo("#zoom", {{ x: 150, scale: 1.14, filter: "blur(24px)" }}, {{ x: 0, scale: 1, filter: "blur(0px)", duration: 0.17, ease: "power3.out", immediateRender: false }}, {f3(ts)});')
        if "T" in cu["fx"]:
            zj.append(f'tl.fromTo("#zoom", {{ scale: 1.12 }}, {{ scale: 1, duration: 0.3, ease: "power3.out", immediateRender: false }}, {f3(ts + cu["thud"] - cu["i"])});')
        if "P" in cu["fx"]:
            zj.append(f'tl.fromTo("#zoom", {{ scale: 1.08 }}, {{ scale: 1, duration: 0.2, ease: "power3.out", immediateRender: false }}, {f3(ts)});')
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
    S, P, W, G = paths(k); TL, beat, t_end, DUR, VS = timeline(S)
    sh(["python3", f"{BUILD}/rock_track.py", "--bpm", str(S["bpm"]), "--bars", str(S["bars"]), "--tail", str(S["tail"] + 0.4), "--seed", str(S["seed"]), "--style", "garage", "--out", f"{W}/musica.wav"])
    if not os.path.exists(W + "/sfx"): sh(["cp", "-r", f"{VIGX}/trabajo/sfx", W + "/sfx"])
    slam = f"{W}/sfx/slam.wav"
    if not os.path.exists(slam): sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{SLAM703 - 0.06:.2f}", "-t", "0.7", "-i", f"{TOMAS}/IMG_9703.MOV", "-vn", "-af", "highpass=f=40,afade=t=out:st=0.4:d=0.3,loudnorm=I=-18:TP=-2:LRA=7", "-ar", "48000", "-ac", "2", slam])
    E, R, f = "1", 0.25, 10 ** (S["boost"] / 20) - 1
    voice = sorted((v["ts"], v["ts"] + v["d"] + 0.15) for v in VS)
    edges, prev = [], 0.0
    for a, b in voice:
        if a - prev > 0.3: edges.append((prev, a))
        prev = max(prev, b)
    edges.append((prev, DUR + 1))
    for a, b in edges:
        E += (f"+{f:.3f}*max(0,min(1,min((t-{a:.3f})/{R},({b:.3f}-t)/{R})))" if a > 0 else f"+{f:.3f}*max(0,min(1,({b:.3f}-t)/{R}))")
    sh(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/musica.wav", "-af", f"volume='{E}':eval=frame", "-c:a", "pcm_s24le", f"{W}/musica_env.wav"])
    ev = []
    def add(name, t, db, mx=None):
        if 0 <= t < DUR: ev.append({"file": f"sfx/{name}.wav", "t": round(t, 3), "db": db, **({"max": mx} if mx else {})})
    for cu in TL:
        if "W" in cu["fx"] and cu["ts"] > 0.2: add("whoosh", cu["ts"] - 0.07, -22)
        if cu["c"] == "TRI":
            add("whoosh", cu["ts"] - 0.05, -21)
            for p in range(3): add("uiclick", cu["ts"] + 0.12 * (p + 1), -23, 0.3)
        if "T" in cu["fx"]: add("slam", cu["ts"] + cu["thud"] - cu["i"] - 0.06, -9)     # golpe real de la tapa (audio de 9703)
    add("riser", t_end - 2.6, -27); add("uiclick", t_end, -23, 0.3); add("impact", S["bars"] * 4 * beat, -18)
    json.dump(sorted(ev, key=lambda e: e["t"]), open(f"{W}/sfx.json", "w"), indent=1)
    r = subprocess.run(["python3", f"{SKILL}/mix.py", "--work", W, "--sfx", f"{W}/sfx.json", "--music", f"{W}/musica_env.wav", "--music-under", "-1", "--duck", "9", "--tp", "-5"], capture_output=True, text=True)
    print(k, r.stdout.strip().splitlines()[-1][:70], r.stderr[-300:] if r.returncode else "")


if __name__ == "__main__":
    k, step = sys.argv[1], sys.argv[2]
    {"media": media, "gfx": gfx, "audio": audio}[step](k)
