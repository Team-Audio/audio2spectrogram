import audio_converters.base

from pydub import AudioSegment
import numpy as np

import make_spectrogram


class Mp3Converter(audio_converters.base.Converter):

    def __init__(self):
        super().__init__()
        self.responsibility = ".mp3"

    def convert(self, path: str) -> np.array:
        a = AudioSegment.from_mp3(path)
        raw = np.array(a.get_array_of_samples())

        print(a)
        print(raw)
        if a.channels == 2:
            raw = raw.reshape((-1, 2))
            return make_spectrogram.create(rate=a.frame_rate, samples=raw[0])
        else:
            return make_spectrogram.create(rate=a.frame_rate, samples=raw)

