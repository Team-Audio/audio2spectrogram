import numpy as np
import make_spectrogram
from scipy.io.wavfile import read

import audio_converters.base
from verbose_print import vprint1


class WavConverter(audio_converters.base.Converter):

    def __init__(self):
        super().__init__()
        self.responsibility = ".wav"

    def convert(self, path: str) -> np.array:
        vprint1("[WavConverter.convert] Hello!")
        rate, samples = read(path)

        try:
            if samples.shape[1] == 2:
                samples = np.delete(samples, 1, 1).flatten()

        # ignore invalid access here, that just
        # means the data was already good
        except IndexError:
            pass

        return make_spectrogram.create(rate=rate, samples=samples)
