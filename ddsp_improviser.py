import ddsp
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 16000
print("Cargando DDSP modelo...")
model = ddsp.training.models.Autoencoder()
model.restore('https://storage.googleapis.com/ddsp/models/ae_violin/model.ckpt-100000')

def callback(indata, outdata, frames, _, status):
    audio_in = indata[:, 0]
    outdata[:] = np.expand_dims(audio_in, axis=1)

def main():
    print("Iniciando improvisación DDSP...")
    with sd.Stream(channels=1, samplerate=SAMPLE_RATE, callback=callback):
        sd.sleep(1000000)

if __name__ == "__main__":
    main()
