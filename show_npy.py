import numpy as np
from PIL import Image
import sys

array = np.load(sys.argv[1])

im = Image.fromarray(array)

im.show()