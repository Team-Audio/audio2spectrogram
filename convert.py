""" Audio To Spectrogram Convert.

Usage:
    convert.py dir <input_directory> <output_directory>
    convert.py file <input_file> <output_file>
    convert.py ( -h | --help)
    convert.py --version
    convert.py ( -m | --modules)

Options:
    -h --help     Show this screen.
    --version     Show version.
    -m --modules  Show installed modules.

"""
import sys

import numpy as np
from docopt import docopt
import audio_converters

# TODO (algorythmix):
# [ ] make sure that the plot is 512x512
# [ ] reshape the output format to rgb instead of rgba (4->3)
# [ ] implement tree conversion
# [ ] (optional:Ilyas?) split samples that are longer than 512s into multiple spectrograms
# [ ] (optional:?) allow data-feeding via stdin and output via stdout



def main():
    arguments = docopt(__doc__,
                       version="converter v0.0.1-" + "-".join(audio_converters.available.keys()).replace('.', ''))

    if arguments["dir"] is True:
        cvt_tree(arguments["<input_directory>"], arguments["<output_directory>"])

    elif arguments["file"] is True:
        cvt_file(arguments["<input_file>"], arguments["<output_file>"])

    if arguments["--modules"] is True:
        print("\n".join([f"{v.__name__} -> \"{k}\"" for k, v in audio_converters.available.items()]))


def cvt_file(input_path: str, output_path: str):
    for key, value in audio_converters.available.items():
        if input_path.endswith(key):
            converter = value()
            array = converter.convert(input_path)
            np.save(output_path, array)


def cvt_tree(input_dir: str, output_dir: str):
    print("Not implemented yet, sorry!")
    sys.exit(1)


if __name__ == "__main__":
    main()
