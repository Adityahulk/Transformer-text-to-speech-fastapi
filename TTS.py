# Set up the paths
from pathlib import Path
import numpy as np
import wave
from pydub import AudioSegment

MelGAN_path = "melgan/"
TTS_path = "TransformerTTS/"

import sys

sys.path.append(TTS_path)

from model.factory import tts_ljspeech
from data.audio import Audio

model, config = tts_ljspeech()
audio = Audio(config)

# 10% slower
# import IPython.display as ipd
from scipy.io.wavfile import write


def audio_gen(sentence, freq):
    p = np.arange(0, len(sentence), 1500)
    sen = []
    for i in range(len(p) - 1):
        sen.append(sentence[p[i] : p[i + 1]])
    k = 0
    sen.append(sentence[p[-1] : len(sentence)])
    in_files = []
    for text in sen:
        out = model.predict(sentence, speed_regulator=0.95)
        wav = audio.reconstruct_waveform(out["mel"].numpy().T)
        # ipd.Audio(wav, rate=config["sampling_rate"])
        write("test" + str(k) + ".wav", freq, wav)
        in_files.append("test" + str(k) + ".wav")
        k = k + 1

    return in_files


def output_file(sentence, freq):

    infiles = audio_gen(sentence, freq)
    combined_sound = 0
    for infile in infiles:
        sound = AudioSegment.from_wav(infile)
        combined_sound = combined_sound + sound

    combined_sound.export("output.wav", format="wav")
