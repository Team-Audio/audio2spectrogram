import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy import signal


def create(rate, samples) -> np.array:
    frequencies, times, spectrogram = signal.spectrogram(samples, rate)

    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.gca()
    ax.axis('off')
    fig.subplots_adjust(0, 0, 1, 1)

    ax.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), shading='auto')

    canvas.draw()
    image = np.asarray(canvas.buffer_rgba())
    return image
