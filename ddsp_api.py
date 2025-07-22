from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import librosa
import ddsp.training.preprocessing
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process_ddsp")
async def process_ddsp(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        audio, sr = librosa.load(io.BytesIO(contents), sr=16000, mono=True)
    except Exception as e:
        return {"error": f"Error al cargar audio: {e}"}

    audio = audio / np.abs(audio).max()

    try:
        features = ddsp.training.preprocessing.compute_features(audio, sample_rate=sr)
    except Exception as e:
        return {"error": f"Error al extraer características DDSP: {e}"}

    features_json = {}
    for k, v in features.items():
        if isinstance(v, np.ndarray):
            features_json[k] = v.tolist()
        else:
            features_json[k] = v

    return {"features": features_json}
