# Bird Song Classification — KNN

Team project for an AI course. Classify two bird species from ~1-second
audio clips using MFCC features and a K-Nearest-Neighbors classifier.

## Goal
Given a short audio clip, predict which of two bird species it belongs to.
Pipeline: audio → 1 s clips → MFCC features → KNN → predicted species.
Final deployment target is a microcontroller (ESP32 / Arduino / Raspberry Pico, TBD).

## Repository contents
- `clip.py` — extracts 1-second WAV clips from longer Xeno-Canto recordings **(planned)**
- `train_knn.m` — MATLAB pipeline: MFCC extraction, KNN training, confusion matrix **(planned)**
- `convert.py` — CSV → WAV converter for the Birdsong dataset (exploration only)
- `convert2.py` — same as above, with command-line arguments
- `Convert_Wavs_to_Data_Array.ipynb` — reference notebook from the Birdsong repo (not part of our pipeline)
- `data/` — recordings folder you create locally (not committed)
- `clips/` — extracted 1-second clips folder you create locally (not committed)

## Getting the data
We do **not** commit audio to this repository. To reproduce the pipeline:

1. Download labeled recordings from [Xeno-Canto](https://xeno-canto.org/) for the
   two target species.
2. Place them in `data/<species>/`.
3. Run the clip extractor:
   ```
   python clip.py data/<species> clips/<species>
   ```
4. Run `train_knn.m` in MATLAB.

## Data source note
We initially explored [SingingData/Birdsong](https://github.com/SingingData/Birdsong)
but found it has no per-file species labels (self-supervised dataset).
We pivoted to Xeno-Canto for labeled data.

## License
See `LICENSE`.

---

# Clasificación de cantos de aves — KNN

Proyecto en equipo para un curso de IA. Clasificar dos especies de aves a partir
de clips de audio de ~1 segundo usando características MFCC y un clasificador
K-Nearest-Neighbors.

## Objetivo
Dado un clip corto de audio, predecir a cuál de las dos especies pertenece.
Pipeline: audio → clips de 1 s → características MFCC → KNN → especie predicha.
El objetivo final de despliegue es un microcontrolador (ESP32 / Arduino / Raspberry Pico, por definir).

## Contenido del repositorio
- `clip.py` — extrae clips WAV de 1 segundo desde grabaciones largas de Xeno-Canto **(planeado)**
- `train_knn.m` — pipeline en MATLAB: extracción de MFCC, entrenamiento KNN, matriz de confusión **(planeado)**
- `convert.py` — convertidor CSV → WAV para el dataset Birdsong (solo exploración)
- `convert2.py` — igual que el anterior, con argumentos de línea de comandos
- `Convert_Wavs_to_Data_Array.ipynb` — cuaderno de referencia del repo Birdsong (no es parte de nuestro pipeline)
- `data/` — carpeta de grabaciones que se crea localmente (no se sube)
- `clips/` — carpeta de clips de 1 segundo que se crea localmente (no se sube)

## Cómo obtener los datos
**No** subimos audio a este repositorio. Para reproducir el pipeline:

1. Descargar grabaciones etiquetadas desde [Xeno-Canto](https://xeno-canto.org/)
   para las dos especies objetivo.
2. Colocarlas en `data/<especie>/`.
3. Ejecutar el extractor de clips:
   ```
   python clip.py data/<especie> clips/<especie>
   ```
4. Ejecutar `train_knn.m` en MATLAB.

## Nota sobre la fuente de datos
Inicialmente exploramos [SingingData/Birdsong](https://github.com/SingingData/Birdsong)
pero descubrimos que no tiene etiquetas de especie por archivo (dataset auto-supervisado).
Cambiamos a Xeno-Canto para datos etiquetados.

## Licencia
Ver `LICENSE`.
