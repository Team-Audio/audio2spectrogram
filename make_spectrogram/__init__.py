import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy import signal
from verbose_print import *


def create(rate, samples) -> np.array:
    """Takes a sample rate and a set of samples and creates a spectrogram from it
       It then renders that to a canvas and packs it into a numpy buffer containing
       rgb values (slightly silly maybe)

    :param rate: the sample rate
    :param samples: the samples to use for the spectrogram
    :return: a numpy array containing rgb values for each point in the spectrogram
    """

    vprint2("[make_spectrogram.create] Creating spectrogram")
    vprint3(f"[make_spectrogram.create]  With samples = {samples} and rate = {rate}")

    # calculate spectrogram
    frequencies, times, spectrogram = signal.spectrogram(samples, rate, nperseg=512, nfft=512)

    vprint2("[make_spectrogram.create] Creating matplotlib drawing-canvas and figure")

    # create Figure, Canvas and Axes
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.gca()

    # disable axis labeling and get rid of white border
    ax.axis('off')
    fig.subplots_adjust(0, 0, 1, 1)

    vprint3("[make_spectrogram.create] Drawing spectrogram to canvas")

    # draw the spectrogram to the canvas, it is put on a dB scale
    ax.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), shading='auto')

    # refresh the canvas
    canvas.draw()

    # get the rgba buffer and convert it to numpy
    image = np.asarray(canvas.buffer_rgba())

    # remove alpha channel
    image = np.delete(image, 3, 2)

    vprint3("[make_spectrogram.create] image:", image)

    return image
