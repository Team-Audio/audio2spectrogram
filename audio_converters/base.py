import abc

import numpy as np


# Abstract Base Class for audio to spectrogram conversion
class Converter(metaclass=abc.ABCMeta):

    def __init__(self):
        # initializes the "responsibility" which dictates the files this will be used on
        # should be the file ending of the files this converter can process
        # your class should overwrite this
        self.responsibility = ""

    @abc.abstractmethod
    def convert(self, path: str) -> np.array:
        """ converts a single audio file to a numpy.array containing an rgb
            representation of the spectrogram

        :param path: the input path of the file
        :return: an numpy array containing the spectrogram
        """
        pass
