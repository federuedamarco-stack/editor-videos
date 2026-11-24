"""Reel «VIGX H1 PRO en 60 segundos» (versión retención) · montaje de voz y vídeo base (1080x1920, 30 fps, 60 s)."""
import json, os, subprocess
T1 = "/home/user/editor-videos/Reels con Claude/Tomas"
T2 = T1 + "/2026-11-24 · reel publicado"
P = "/home/user/editor-videos/Reels con Claude/Reels/2026-11-24 · VIGX H1 PRO en 60 segundos"
W = P + "/trabajo"; os.makedirs(W + "/piezas", exist_ok=True)
FPS, DUR, END = 30, 60.0, 2.0
RAW = T2 + "/IMG_9611_pequeno.mp4"
src = {"9611": RAW, "9602": T2 + "/IMG_9602.MOV", "9605": T2 + "/IMG_9605.MOV", "9612": T2 + "/IMG_9612.MOV",
       "9613": T2 + "/IMG_9613.MOV", "9614": T2 + "/IMG_9614.MOV", "9615": T2 + "/IMG_9615.MOV", "9616": T2 + "/IMG_9616.MOV",
       "9617": T2 + "/IMG_9617.MOV", "9628": T1 + "/IMG_9628.MOV", "9629": T1 + "/IMG_9629.MOV", "9632": T1 + "/IMG_9632.MOV"}
snap = lambda t: round(t * FPS) / FPS

# ---- voz: (inicio en el reel, [(entrada, salida) en IMG_9611])
VOZ = [(0.35, [(0.78, 3.86)]),                                   # VIGX H1 Pro en 60 segundos
       (7.60, [(5.22, 7.44)]),                                   # Se trata de un exoesqueleto de cadera
       (10.05, [(8.01, 8.88), (9.18, 10.54)]),                   # Esta parte se pone | aquí en la cintura
       (13.55, [(14.52, 14.98), (15.57, 17.25)]),                # Y | esto se pone en las rodillas
       (15.95, [(17.76, 18.56), (18.86, 23.29)]),                # Tiene que quedar… | como tres o cuatro dedos…
       (21.55, [(54.33, 57.43)]),                                # Se enciende con un interruptor…
       (24.80, [(60.82, 61.02), (61.42, 64.56)]),                # y | luego se le da a play…
       (28.35, [(65.02, 65.47), (65.98, 67.13), (68.02, 69.48)]),# ahí | ya estaría activado | entonces ya empieza a actuar
       (35.80, [(69.95, 72.15), (72.70, 74.54), (74.92, 78.43)]),# Aquí podemos regular la | potencia… | y luego… modos de uso
       (43.75, [(88.42, 92.38)])]                                # Tiene seis modos de uso…
GAP = 0.08
voz_clips, t_check = [], []
for t0, rs in VOZ:
    t = t0
    for a, b in rs:
        voz_clips.append((t, a, b)); t += (b - a) + GAP
    t_check.append((t0, round(t - GAP, 2)))
print("voz:", t_check)

# ---- vídeo: (fuente, entrada, duración, velocidad, inicio esperado)
V = [("9629", 2.00, 1.35), ("9632", 4.50, 1.30), ("9628", 5.00, 1.35),                       # 0 gancho
     ("9602", 0.00, 0.5), ("9602", 1.60, 0.5), ("9602", 3.20, 0.5), ("9602", 5.00, 0.5), ("9602", 7.00, 0.5),
     ("9605", 0.30, 0.5), ("9605", 2.00, 0.5),                                                  # 1 caja
     ("9611", 5.12, 2.50),                                                                      # 2 qué es
     ("9612", 3.50, 2.40), ("9612", 6.00, 1.10, 2.0),                                           # 3 cintura (+ acelerado)
     ("9613", 0.50, 4.00), ("9614", 1.50, 4.00),                                                # 4 rodillas
     ("9615", 0.30, 3.20),                                                                      # 5 interruptor
     ("9616", 6.50, 3.60),                                                                      # 6 play
     ("9611", 64.97, 0.53), ("9611", 65.93, 1.23), ("9611", 67.97, 1.64),                       # 7 activado (mismos cortes que la voz)
     ("9611", 107.00, 2.00), ("9629", 4.00, 2.00),                                              # 8 en acción
     ("9616", 9.00, 4.30), ("9617", 2.00, 3.65),                                                # 9 potencia y modos
     ("9611", 88.32, 4.15),                                                                     # 10 seis modos
     ("9632", 2.50, 2.00), ("9628", 2.60, 1.50), ("9629", 0.80, 1.20), ("9632", 8.00, 2.00),
     ("9628", 6.40, 1.10), ("9611", 108.20, 2.00), ("9629", 5.20, 0.40)]                        # 11 montaje
V = [(s, a, d, (x[0] if x else 1.0)) for s, a, d, *x in V]
pieces, t = [], 0.0
for i, (s, a, d, sp) in enumerate(V):
    n = round(d * FPS)
    vf = (f"setpts=PTS/{sp}," if sp != 1 else "") + f"fps={FPS},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"
    out = f"{W}/piezas/p{i:02d}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", src[s], "-an", "-vf", vf, "-frames:v", str(n),
                    "-c:v", "libx264", "-preset", "fast", "-crf", "15", out], check=True)
    pieces.append({"i": i, "src": s, "in": a, "dur": n / FPS, "speed": sp, "start": round(t, 3)}); t += n / FPS
print(f"vídeo: {t:.2f} s de planos + {END} s de cierre")
lst = f"{W}/piezas/lista.txt"
open(lst, "w").write("".join(f"file 'p{p['i']:02d}.mp4'\n" for p in pieces))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-vf", f"tpad=stop_mode=add:stop_duration={DUR - t:.3f}:color=0x121311",
                "-r", str(FPS), "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p", f"{W}/base.mp4"], check=True)

# ---- pista de voz de 60 s (los huecos en silencio)
inp, fc = ["-i", RAW], []
for k, (t0, a, b) in enumerate(voz_clips):
    d = b - a
    fc.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={d - 0.015:.3f}:d=0.015,adelay={int(t0 * 1000)}|{int(t0 * 1000)}[a{k}]")
fc.append("".join(f"[a{k}]" for k in range(len(voz_clips))) + f"amix=inputs={len(voz_clips)}:normalize=0,apad=whole_dur={DUR},atrim=0:{DUR},aformat=channel_layouts=mono[v]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", "[v]", "-ar", "48000", "-c:a", "pcm_s24le", f"{W}/audio48k.wav"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/audio48k.wav", "-ac", "1", "-ar", "16000", f"{W}/audio16k.wav"], check=True)
json.dump({"duration": DUR, "voz": [{"start": round(t0, 3), "in": a, "out": b} for t0, a, b in voz_clips], "piezas": pieces},
          open(f"{W}/montaje.json", "w"), ensure_ascii=False, indent=1)
print("ok")
