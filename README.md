# Bird Song Classification — KNN

Team project for ProbStats / AI course.

## Goal
Classify two bird species from ~1-second audio clips using MFCC features
and a K-Nearest-Neighbors classifier.

## Pipeline
1. Download labeled recordings from Xeno-Canto → `data/<species>/`
2. `python clip.py data/<species> clips/<species>` → 1 s WAV clips
3. `train_knn.m` in MATLAB → MFCC extraction, KNN, confusion matrix
4. Deploy to ESP32 / Arduino / Raspberry Pico (TBD)

## Data source note
We initially explored [SingingData/Birdsong](https://github.com/SingingData/Birdsong)
but found it has no per-file species labels (self-supervised dataset).
Pivoted to Xeno-Canto for labeled data.

## Files
- `convert.py` — CSV → WAV converter for the Birdsong dataset (exploration)
- `clip.py` — 1-second clip extractor for Xeno-Canto recordings
- `train_knn.m` — MATLAB MFCC + KNN pipeline
- `notebooks/` — original notebook from Birdsong repo (reference)
