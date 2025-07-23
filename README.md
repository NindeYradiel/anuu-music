# Anuu Music

Este repositorio contiene una aplicación sencilla basada en **FastAPI** para procesar audio empleando componentes de la librería **DDSP**.

## Requisitos
- Python 3.10 o superior
- `ffmpeg` y `libsndfile1` para la manipulación de audio (instalados automáticamente si se usa Docker)

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar el servidor de desarrollo ejecuta:

```bash
python app.py
```

El servicio quedará disponible en `http://localhost:8000`. Puedes enviar archivos de audio a la ruta `/process/` para recibir el archivo procesado.

## Docker

Opcionalmente puedes construir y ejecutar la imagen Docker:

```bash
docker build -t anuu-music .
docker run -p 8000:8000 anuu-music
```

Esto iniciará el servicio en el puerto 8000 dentro del contenedor.
