import audio_converters.base

from pydub import AudioSegment
import numpy as np

import make_spectrogram
from verbose_print import vprint1,vprint2


class Mp3Converter(audio_converters.base.Converter):

    def __init__(self):
        super().__init__()

        # set personal responsibility to be mp3 files
        self.responsibility = ".mp3"

    def convert(self, path: str) -> np.array:
        vprint1("[Mp3Converter.convert] Hello!")

        # create numpy data from AudioSegment
        a = AudioSegment.from_mp3(path)
        raw = np.array(a.get_array_of_samples())

        if a.channels == 2:
            vprint2("[Mp3Converter.convert] Audio was stereo I am extracting a single channel!")
            raw = raw.reshape((-1, 2))
            return make_spectrogram.create(rate=a.frame_rate, samples=raw[0])
        else:
            return make_spectrogram.create(rate=a.frame_rate, samples=raw)

