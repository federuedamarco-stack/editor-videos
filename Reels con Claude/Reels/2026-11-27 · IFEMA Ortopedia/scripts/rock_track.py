"""Pista de rock/indie original generada en código (batería, bajo, guitarras con distorsión y melodía).
  python rock_track.py --bpm 152 --bars 8 --out pista.wav [--style garage|indie] [--seed 1]
Escribe también pista.beats.json con el compás para sincronizar los cortes."""
import argparse, json, wave
import numpy as np
from scipy import signal

SR = 44100
ap = argparse.ArgumentParser()
ap.add_argument("--bpm", type=float, default=152)
ap.add_argument("--bars", type=int, default=8)
ap.add_argument("--out", required=True)
ap.add_argument("--style", default="garage")        # garage: más sucio y rápido · indie: más limpio y abierto
ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--key", type=int, default=-5)      # semitonos respecto a La (-5 = Mi)
ap.add_argument("--tail", type=float, default=1.2)
a = ap.parse_args()
rng = np.random.default_rng(a.seed)
beat = 60 / a.bpm; bar = 4 * beat
N = int((a.bars * bar + a.tail) * SR)
out = np.zeros((N, 2), np.float32)
t_ = lambda n: np.arange(n) / SR
hz = lambda semis: 440 * 2 ** ((semis + a.key + 5) / 12 - 1 + 0)   # semis desde la tónica (E) en la octava 2


def put(x, t0, pan=0.0, gain=1.0):
    i = int(t0 * SR)
    if i >= N: return
    x = x[: N - i] * gain
    out[i:i + len(x), 0] += x * (1 - max(0, pan)); out[i:i + len(x), 1] += x * (1 + min(0, pan))


def lp(x, f, order=2): return signal.sosfilt(signal.butter(order, f, "low", fs=SR, output="sos"), x)
def hp(x, f, order=2): return signal.sosfilt(signal.butter(order, f, "high", fs=SR, output="sos"), x)


def kick():
    n = int(0.22 * SR); t = t_(n); f = 48 + 110 * np.exp(-t * 38)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14) * 1.0 + hp(rng.normal(0, 1, n), 2500) * np.exp(-t * 90) * 0.15


def snare():
    n = int(0.22 * SR); t = t_(n)
    return (hp(rng.normal(0, 1, n), 1500) * np.exp(-t * 20) * 0.8 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 28) * 0.55)


def hat(open_=False):
    n = int((0.16 if open_ else 0.045) * SR); t = t_(n)
    return hp(rng.normal(0, 1, n), 7000) * np.exp(-t * (22 if open_ else 95)) * 0.32


def saw(f, n, detune=0.0):
    t = t_(n); return 2 * ((t * f * (1 + detune)) % 1) - 1


def guitar(root_semis, dur, mute=False, gain=1.0):
    n = int(dur * SR); x = np.zeros(n)
    notes = [root_semis, root_semis + 7, root_semis + 12]       # quinta: root + 5ª + octava
    for s in notes:
        f = 82.41 * 2 ** (s / 12)
        for d in (-0.004, 0.0, 0.004):
            x += saw(f, n, d)
    x = np.tanh(x * (2.4 if a.style == "garage" else 1.5)) * 0.5
    x = hp(lp(x, 4200), 110)
    env = np.exp(-t_(n) * (22 if mute else 3.2)); env[: int(0.004 * SR)] *= np.linspace(0, 1, int(0.004 * SR))
    return x * env * gain


def bass(root_semis, dur):
    n = int(dur * SR); f = 41.2 * 2 ** (root_semis / 12)
    x = np.tanh(lp(saw(f, n), 600) * 2.0) * 0.8 + np.sin(2 * np.pi * f * t_(n)) * 0.5
    return x * np.exp(-t_(n) * 4.0) * np.minimum(1, t_(n) * 400)


def lead(semis, dur):
    n = int(dur * SR); f = 82.41 * 2 ** ((semis + 24) / 12); t = t_(n)
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t) * np.minimum(1, t * 6)
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f * vib) / SR)) * 0.5 + np.sin(2 * np.pi * np.cumsum(f * vib) / SR) * 0.5
    return lp(x, 3800) * np.exp(-t * 2.2) * np.minimum(1, t * 300)


# progresión en La menor-ish (aquí tónica = Mi): i - VI - III - VII  → Em C G D
PROG = [0, -4, 3, -2]
HOOK = [12, 15, 14, 12, 10, 12, 7, 10]              # pentatónica menor, 2 compases a corcheas
for b in range(a.bars):
    t0 = b * bar; root = PROG[(b // 1) % 4]
    full = b >= 2
    fill = (b == a.bars - 1) or (b % 4 == 3)
    # batería
    for k in range(4):
        tk = t0 + k * beat
        if full or b == 1:
            if k in (0, 2) or (k == 3 and b % 2 == 1): put(kick(), tk, 0, 1.0)
            if k in (1, 3): put(snare(), tk, 0, 0.9)
            else: put(kick(), tk + beat / 2, 0, 0.55) if (b % 2 == 0 and k == 2) else None
        for h in range(2):
            put(hat(open_=(h == 1 and k == 3 and full)), tk + h * beat / 2, 0.25, 1.6 if full or b == 1 else 1.3)
    if fill:                                         # redoble de caja en el último compás
        for k in range(8): put(snare(), t0 + 2 * beat + k * beat / 4, 0, 0.45 + 0.06 * k)
    if b == 0:
        put(kick(), t0, 0, 1.0); put(kick(), t0 + 2 * beat, 0, 0.9)
        put(snare(), t0 + 3 * beat, 0, 0.8); put(snare(), t0 + 3.5 * beat, 0, 0.9)
    # bajo
    if b >= 1:
        for h in range(8): put(bass(root, beat / 2 * 0.95), t0 + h * beat / 2, 0, 0.8)
    # guitarras: golpe abierto en 1 y en el "y" del 2, el resto palm-mute a corcheas
    if b >= 2 or a.style == "indie" and b >= 1:
        for h in range(8):
            open_ = h in (0, 3)
            put(guitar(root, beat * (1.4 if open_ else 0.4), mute=not open_, gain=0.55), t0 + h * beat / 2, -0.55)
            put(guitar(root, beat * (1.4 if open_ else 0.4), mute=not open_, gain=0.55), t0 + h * beat / 2 + 0.006, 0.55)
    # melodía en la segunda mitad
    if b >= a.bars // 2 and b % 2 == 0:
        for k, s in enumerate(HOOK): put(lead(s + root, beat * 0.5), t0 + k * beat / 2, 0.1, 0.28)
if a.bars >= 1:                                      # remate final: acorde abierto + platillo
    put(guitar(PROG[(a.bars) % 4], a.tail, gain=0.7), a.bars * bar, -0.5)
    put(guitar(PROG[(a.bars) % 4], a.tail, gain=0.7), a.bars * bar + 0.006, 0.5)
    put(kick(), a.bars * bar, 0, 1.0); put(hat(True), a.bars * bar, 0.2, 1.4)

out = out / (np.max(np.abs(out)) + 1e-9) * 0.8
out = np.tanh(out * 1.25) / np.tanh(1.25) * 0.8      # pegamento suave
with wave.open(a.out, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype("<i2").tobytes())
json.dump({"bpm": a.bpm, "beat": beat, "bar": bar, "bars": a.bars, "duration": a.bars * bar + a.tail,
           "beats": [round(i * beat, 4) for i in range(a.bars * 4 + 1)]}, open(a.out.replace(".wav", ".beats.json"), "w"))
print(f"ok · {a.bpm} bpm · {a.bars} compases · {a.bars * bar + a.tail:.1f} s")
