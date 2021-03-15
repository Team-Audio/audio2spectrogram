import abc

import numpy as np


class Converter(metaclass=abc.ABCMeta):

    def __init__(self):
        self.responsibility = ""

    @abc.abstractmethod
    def convert(self, path: str) -> np.array:
        pass