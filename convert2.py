import os
import sys
import glob
import pandas as pd
from scipy.io import wavfile
import numpy as np

# --- SETTINGS ---
# Use command-line args if provided, otherwise fall back to defaults
input_dir  = sys.argv[1] if len(sys.argv) > 1 else 'raw-test-arrays'
output_dir = sys.argv[2] if len(sys.argv) > 2 else 'converted-raw-test-arrays'
sample_rate = 22000

os.makedirs(output_dir, exist_ok=True)
csv_files = sorted(glob.glob(os.path.join(input_dir, '*.csv')))

if not csv_files:
    print(f"No CSV files found in {input_dir}")
    raise SystemExit

print(f"Found {len(csv_files)} CSV files in {input_dir}")

for csv_path in csv_files:
    try:
        data = pd.read_csv(csv_path, header=None).values.flatten()
        if data.size == 0:
            print(f"  [skip] {csv_path} is empty")
            continue

        peak = np.max(np.abs(data))
        if peak > 1.0:
            data = data / peak

        base = os.path.splitext(os.path.basename(csv_path))[0]
        wav_path = os.path.join(output_dir, base + '.wav')
        wavfile.write(wav_path, sample_rate, data.astype(np.float32))

    except Exception as e:
        print(f"  [error] {csv_path}: {e}")

print("Done.")
