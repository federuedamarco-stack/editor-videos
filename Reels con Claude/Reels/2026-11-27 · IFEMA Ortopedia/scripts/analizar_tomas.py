"""Transcribe (palabra a palabra) y saca una tira de fotogramas de cada toma de una carpeta que aún no tenga análisis."""
import sys, os, json, glob, subprocess, whisper
D = sys.argv[1]; A = os.path.join(D, "_analisis"); os.makedirs(A, exist_ok=True)
m = None
for f in sorted(glob.glob(os.path.join(D, "*.MOV")) + glob.glob(os.path.join(D, "*.mov")) + glob.glob(os.path.join(D, "*.mp4"))):
    n = os.path.splitext(os.path.basename(f))[0]; out = os.path.join(A, n + ".json")
    if os.path.exists(out): continue
    wav = os.path.join(A, n + ".wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
    k = max(4, min(8, int(d // 2)))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", f"fps={k}/{d:.3f},scale=-2:400,tile={k}x1", "-frames:v", "1", os.path.join(A, n + "-frames.jpg")], check=True)
    if m is None: m = whisper.load_model("turbo", device="cpu")
    r = m.transcribe(wav, language="es", word_timestamps=True, condition_on_previous_text=False, fp16=False)
    words = [{"w": x["word"].strip(), "s": round(x["start"], 2), "e": round(x["end"], 2)} for s in r["segments"] for x in s.get("words", [])]
    json.dump({"file": os.path.basename(f), "duration": d, "text": r["text"].strip(), "words": words}, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"{n} ({d:.1f}s): {r['text'].strip()}", flush=True)
