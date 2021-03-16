"""Glues numpy arrays together
Usage:
    glue.py <out> dir <dir>
    glue.py <out> files <file>...
"""
import os

import numpy as np
from docopt import docopt


def glue(result, inputs):
    arrays = [np.load(x) for x in inputs]
    np.save(result, np.array(arrays))


if __name__ == '__main__':
    arguments = docopt(__doc__)

    if arguments['dir'] is True:
        files = os.listdir(arguments['<dir>'])
        glue(result=arguments['<out>'], inputs=files)

    else:
        glue(result=arguments['<out>'], inputs=arguments['<file>'])
