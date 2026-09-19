import os
import glob
import pandas as pd
from scipy.io import wavfile
import numpy as np

# --- SETTINGS ---
input_dir  = 'raw-test-arrays'            # folder with CSVs
output_dir = 'converted-raw-test-arrays'  # folder for WAVs
sample_rate = 22000

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Find all CSV files in the input directory
csv_files = sorted(glob.glob(os.path.join(input_dir, '*.csv')))

if not csv_files:
    print(f"No CSV files found in {input_dir}")
    raise SystemExit

print(f"Found {len(csv_files)} CSV files.")

for csv_path in csv_files:
    try:
        # Read the CSV (no header, single column expected)
        data = pd.read_csv(csv_path, header=None).values.flatten()

        # Skip empty or malformed files
        if data.size == 0:
            print(f"  [skip] {csv_path} is empty")
            continue

        # Normalize to [-1.0, 1.0] for audiowrite/wavfile
        peak = np.max(np.abs(data))
        if peak > 1.0:
            data = data / peak

        # Build output filename (same base name, .wav extension)
        base = os.path.splitext(os.path.basename(csv_path))[0]
        wav_path = os.path.join(output_dir, base + '.wav')

        # Write WAV (needs float32 for [-1,1] range)
        wavfile.write(wav_path, sample_rate, data.astype(np.float32))

        print(f"  [ok] {csv_path} -> {wav_path}")

    except Exception as e:
        print(f"  [error] {csv_path}: {e}")

print("Done.")
