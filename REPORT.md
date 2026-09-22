# Bird Song Classification — Report

## 1. Species selected
- **Gorrión común** (House Sparrow, *Passer domesticus*)
- **Cuervo picogordo** (Thick-billed Raven, *Corvus crassirostris*)
- Rationale: Acoustically very distinct (high-frequency chirps vs. low-frequency
  croaks), both well-represented on Xeno-Canto, and easy to source from the
  same archive for a balanced comparison.

## 2. Dataset
- **Source:** Xeno-Canto (https://xeno-canto.org/), Quality A recordings only
- **Recordings downloaded:** 30 sparrow + 6 raven (via Xeno-Canto API v3)
- **Original dataset explored:** SingingData/Birdsong — abandoned because it
  has no per-file species labels (self-supervised dataset, multi-species
  recordings from a single camera)
- **Clip length:** 1 second, 22 kHz, mono WAV
- **Clips generated (after filtering):** 3,474 sparrow + 196 raven
- **Clips used (balanced):** 300 sparrow + 196 raven = 496 total

## 3. Preprocessing
- Downloaded raw recordings with `download_xc.py` (Xeno-Canto API v3)
- Sliced into 1-second windows with 50% overlap using `clip.py`
- Discarded silent windows (RMS < 0.01) and saturated windows (peak > 0.99)
- Resampled all audio to 22 kHz, mono, stored as WAV
- Trimmed the sparrow class down to 300 clips to correct the 17:1 class imbalance

## 4. Feature extraction (MATLAB)
- 13 MFCCs + deltas + delta-deltas (39 coefficients per frame)
- Aggregated per clip: mean and standard deviation → **78 features per clip**
- Feature matrix: 496 clips × 78 features

## 5. Classifier
- **k-Nearest Neighbors, k = 5**
- Uniform class prior (`'Prior', 'uniform'`) to compensate for residual imbalance
- Stratified 80/20 train/test split → 397 train, 99 test

## 6. Results
- **Accuracy: 97.98%** (97 of 99 test clips correct)
- **Confusion matrix:**

  |  | Predicted Sparrow | Predicted Raven |
  |---|---|---|
  | **True Sparrow** | 58 | 2 |
  | **True Raven** | 0 | 39 |

- **Interpretation:** The classifier correctly identified all 39 raven clips
  and 58 of 60 sparrow clips. The 2 errors are sparrow clips misclassified
  as raven.
- **Limitation:** The raven dataset comes from only 6 source recordings, so
  the high accuracy may partially reflect the model memorizing those specific
  recordings rather than generalizing across the species. More raven
  recordings would strengthen the result.

## 7. Deployment plan (future work)
- See DEPLOY.md
- Target board: ESP32 with I2S microphone (INMP441)
- Output: LED indicator (green = sparrow, red = raven)
- Approach options: Edge Impulse (cloud training → ESP32 library) or a
  hand-ported KNN with hardcoded feature vectors
