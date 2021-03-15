import numpy as np
from PIL import Image


array = np.load('out.npy')

im = Image.fromarray(array)

im.show()