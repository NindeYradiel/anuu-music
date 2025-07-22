import sys
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

UPLOAD_DIR = "uploads"
PROCESSED_DIR = "processed"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def process_audio(file_path: str, output_path: str) -> bool:
    # Aquí debería ir la integración con ddsp/magenta (simplificado)
    # Por ahora simula copia para prueba
    try:
        with open(file_path, "rb") as fsrc:
            with open(output_path, "wb") as fdst:
                fdst.write(fsrc.read())
        return True
    except Exception as e:
        print(f"Error procesando audio: {e}")
        return False

@app.post("/process/")
async def upload_audio(file: UploadFile = File(...), output_format: str = "wav"):
    if file.content_type not in ["audio/wav", "audio/mpeg"]:
        raise HTTPException(status_code=400, detail="Solo se permiten archivos .wav o .mp3")

    filename = file.filename
    upload_path = os.path.join(UPLOAD_DIR, filename)
    output_file = os.path.splitext(filename)[0] + f"_processed.{output_format}"
    output_path = os.path.join(PROCESSED_DIR, output_file)

    with open(upload_path, "wb") as f:
        f.write(await file.read())

    success = process_audio(upload_path, output_path)

    if not success:
        raise HTTPException(status_code=500, detail="Error en procesamiento")

    return FileResponse(path=output_path, filename=output_file, media_type=f"audio/{output_format}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
