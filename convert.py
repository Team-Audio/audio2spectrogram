""" Audio To Spectrogram Convert.
Usage:
    convert.py dir <input_directory> ( <output_directory> | -s )  [ -v | -vv | -vvv ] [-g [-l]] [-f=RGX]
    convert.py file <input_file> ( <output_file> | -s ) [ -v | -vv | -vvv ]
    convert.py ( -h | --help)
    convert.py --version
    convert.py ( -m | --modules)

Options:
    -h --help     Show this screen.
    --version     Show version.
    -m --modules  Show installed modules.
    -v            Increase output verbosity
    -s            Use stdout and stdin
    -g            glue the output together and create one glued.npy
    -f RGX        regex filter that the file needs to match against
    -l            when gluing together files also glue the labels
"""

from docopt import docopt

import audio_converters
import verbose_print
from driver import Converter


# TODO (algorythmix):
# [X] reshape the output format to rgb instead of rgba (4->3)
# [X] implement tree conversion
# [ ] (optional:?) allow data-feeding via stdin and output via stdout [-s] and [-] switch


def main():
    # parse args, adjust verbosity level and output method
    arguments = docopt(__doc__,
                       version="converter v0.0.1-" + "-".join(audio_converters.available.keys()).replace('.', ''))
    verbose_print.verbosity_level = arguments["-v"]
    cvt = Converter(args=arguments)
    cvt.run()


if __name__ == "__main__":
    main()
