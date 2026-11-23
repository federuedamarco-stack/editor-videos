"""Base del reel: A-roll + planos de la prueba encima (sin sonido) + 2,5 s de cola para el cierre."""
import json, os, subprocess
TOMAS = "/home/user/editor-videos/Reels con Claude/Tomas"
W = "/home/user/editor-videos/Reels con Claude/Reels/2026-11-23 · Pedir cita para probar/trabajo"
FPS = 30; END = 2.5
snap = lambda t: round(t * FPS) / FPS
# (archivo, entrada en el original, inicio en el reel, fin en el reel, recorte)
B = [("IMG_9628.MOV", 6.00, 1.20, 2.50, None),          # 0 · «exoesqueleto»: aparato en la cadera
     ("IMG_9628.MOV", 2.60, 13.66, 15.95, None),        # A · ajuste de las cinchas
     ("IMG_9629.MOV", 1.80, 15.95, 17.18, None),        # A · primeros pasos
     ("IMG_9635.MOV", 0.00, 18.18, 19.88, None),        # B · app en el móvil
     ("IMG_9631.MOV", 0.20, 19.88, 21.28, 380),         # B · camina (horizontal recortado)
     ("IMG_9632.MOV", 4.00, 23.00, 25.62, None)]        # C · escaleras
B = [(f, s, snap(a), snap(b), c) for f, s, a, b, c in B]
os.makedirs(f"{W}/broll", exist_ok=True)
for i, (f, s, a, b, crop) in enumerate(B):
    vf = (f"crop=607:1080:{crop}:0," if crop is not None else "") + f"fps={FPS},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1,format=yuv420p"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-i", os.path.join(TOMAS, f), "-t", f"{b - a:.3f}", "-an", "-vf", vf,
                    "-c:v", "libx264", "-preset", "fast", "-crf", "15", f"{W}/broll/b{i}.mp4"], check=True)
inp = ["-i", f"{W}/aroll.mp4"] + sum([["-i", f"{W}/broll/b{i}.mp4"] for i in range(len(B))], [])
fc = [f"[0:v]tpad=stop_mode=add:stop_duration={END}:color=0x121311[v0]"]
for i, (f, s, a, b, c) in enumerate(B):
    fc.append(f"[{i+1}:v]setpts=PTS-STARTPTS+{a}/TB[b{i}]")
    fc.append(f"[v{i}][b{i}]overlay=eof_action=pass:enable='between(t,{a},{b - 0.001})'[v{i+1}]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", f"[v{len(B)}]", "-r", str(FPS),
                "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p", f"{W}/base.mp4"], check=True)
d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{W}/base.mp4"], capture_output=True, text=True).stdout)
json.dump([{"file": f, "src": s, "start": a, "end": b} for f, s, a, b, c in B], open(f"{W}/broll.json", "w"), indent=1)
print(f"base.mp4 · {d:.2f} s")
