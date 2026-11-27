#!/bin/bash
# uso: finish.sh <carpeta de la versión> <nombre del archivo>
D="$1"; N="$2"
cd "$D/graficos" && npx hyperframes render . -o ../trabajo/reel-video.mp4 --fps 30 --quality looks >/dev/null 2>&1 || { echo "RENDER FALLÓ"; exit 1; }
ffmpeg -v error -y -i "$D/trabajo/reel-video.mp4" -i "$D/trabajo/master.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -shortest -movflags +faststart "$D/$N.mp4" || exit 1
ffmpeg -v error -y -i "$D/$N.mp4" -c:v libx264 -preset slow -crf 23 -maxrate 6M -bufsize 12M -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$D/$N (ligero).mp4" || exit 1
echo "LISTO $N $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$D/$N.mp4") s"
