# clip.py — 1-second clip extractor with filtering
import os
import sys
import glob
import librosa
import soundfile as sf
import numpy as np

SR         = 22000
DUR        = 1.0
HOP        = 0.5      # 50% overlap
MIN_RMS    = 0.01     # skip silent windows
MIN_PEAK   = 0.05     # skip flat windows
MAX_CLIP   = 0.99     # skip saturated windows

def clip_folder(in_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(in_dir, '*')))
    total = 0
    skipped_silent = 0
    skipped_clipped = 0

    for f in files:
        try:
            y, _ = librosa.load(f, sr=SR, mono=True)
        except Exception as e:
            print(f'  [skip] {f}: {e}')
            continue

        win = int(DUR * SR)
        hop = int(HOP * SR)
        for i in range(0, len(y) - win + 1, hop):
            seg = y[i:i+win]

            rms = np.sqrt(np.mean(seg ** 2))
            if rms < MIN_RMS:
                skipped_silent += 1
                continue

            peak = np.max(np.abs(seg))
            if peak < MIN_PEAK:
                skipped_silent += 1
                continue

            if peak > MAX_CLIP:
                skipped_clipped += 1
                continue

            base = os.path.splitext(os.path.basename(f))[0]
            out = os.path.join(out_dir, f'{base}_{i:08d}.wav')
            sf.write(out, seg.astype('float32'), SR)
            total += 1

    print(f'{in_dir} -> {total} clips, {skipped_silent} silent, {skipped_clipped} clipped')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python clip.py <input_dir> <output_dir>')
        sys.exit(1)
    clip_folder(sys.argv[1], sys.argv[2])
