"""Pasada 1 · montaje de las 5 tomas habladas: tramos, voz igualada y A-roll 1080x1920."""
import json, os, re, subprocess, sys
TOMAS = "/home/user/editor-videos/Reels con Claude/Tomas"
W = "/home/user/editor-videos/Reels con Claude/Reels/2026-11-23 · Pedir cita para probar/trabajo"
FPS = 30
snap = lambda t: round(t * FPS) / FPS
# (archivo, entrada, salida) en segundos del original; pausas >0,4 s cortadas
SEG = [("Untitled.mov", 1.04, 7.98), ("IMG_9641.MOV", 2.13, 7.88),
       ("IMG_9643.MOV", 1.53, 4.94), ("IMG_9643.MOV", 5.24, 6.32),
       ("IMG_9644.MOV", 1.44, 2.44), ("IMG_9644.MOV", 2.68, 6.58),
       ("IMG_9646.MOV", 2.17, 8.12), ("IMG_9646.MOV", 8.80, 10.45)]
SEG = [(f, snap(a), snap(b)) for f, a, b in SEG]
run = lambda c: subprocess.run(c, check=True, capture_output=True, text=True)

def lufs(path, a, b):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(a), "-to", str(b), "-i", path, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1])

gain = {}
for f in dict.fromkeys(s[0] for s in SEG):
    rs = [(a, b) for g, a, b in SEG if g == f]
    gain[f] = -20 - lufs(os.path.join(TOMAS, f), rs[0][0], rs[-1][1])
parts, vparts, t, tl = [], [], 0.0, []
inputs = []
for i, (f, a, b) in enumerate(SEG):
    inputs += ["-i", os.path.join(TOMAS, f)]
    d = b - a
    parts.append(f"[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,volume={gain[f]:.2f}dB,afade=t=in:d=0.015,afade=t=out:st={d-0.015:.3f}:d=0.015,aresample=48000,aformat=channel_layouts=mono[a{i}]")
    vparts.append(f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS,fps={FPS},scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p[v{i}]")
    tl.append({"file": f, "src_in": a, "src_out": b, "start": round(t, 3), "end": round(t + d, 3)}); t += d
n = len(SEG)
fc = ";".join(parts + vparts) + ";" + "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[a];" + "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v]"
os.makedirs(W, exist_ok=True)
run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[a]", "-c:a", "pcm_s24le", "-ar", "48000", f"{W}/audio48k.wav",
     "-map", "[v]", "-c:v", "libx264", "-preset", "fast", "-crf", "16", f"{W}/aroll.mp4"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/audio48k.wav", "-ac", "1", "-ar", "16000", f"{W}/audio16k.wav"])
json.dump({"duration": round(t, 3), "fps": FPS, "gain_db": gain, "segments": tl}, open(f"{W}/montaje.json", "w"), ensure_ascii=False, indent=1)
print(f"duración voz {t:.2f} s"); print({k: round(v, 1) for k, v in gain.items()})
