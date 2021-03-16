""" Audio To Spectrogram Convert.

Usage:
    convert.py dir <input_directory> <output_directory> [ -v | -vv | -vvv ]
    convert.py file <input_file> <output_file> [ -v | -vv | -vvv ]
    convert.py ( -h | --help)
    convert.py --version
    convert.py ( -m | --modules)

Options:
    -h --help     Show this screen.
    --version     Show version.
    -m --modules  Show installed modules.
    -v            Increase output verbosity

"""

import numpy as np
from docopt import docopt
import audio_converters
from pathlib import Path
import os
import verbose_print
from verbose_print import *

# TODO (algorythmix):
# [X] reshape the output format to rgb instead of rgba (4->3)
# [X] implement tree conversion
# [ ] (optional:?) allow data-feeding via stdin and output via stdout


def main():

    # parse args and adjust verbosity level
    arguments = docopt(__doc__,
                       version="converter v0.0.1-" + "-".join(audio_converters.available.keys()).replace('.', ''))
    verbose_print.verbosity_level = arguments["-v"]

    if arguments["dir"] is True:
        # converting a directory and copy it to a different dir

        vprint1("[startup] converting directory")
        vprint2(f"[startup] {arguments['<input_directory>']} -> {arguments['<output_directory>']}")

        cvt_tree(arguments["<input_directory>"], arguments["<output_directory>"])

    elif arguments["file"] is True:
        # convert just a single file

        vprint1("[startup] converting file")
        vprint2(f"[startup] {arguments['<input_file>']} -> {arguments['<output_file>']}")

        cvt_file(arguments["<input_file>"], arguments["<output_file>"])

    if arguments["--modules"] is True:
        print("\n".join([f"{v.__name__} -> \"{k}\"" for k, v in audio_converters.available.items()]))


def cvt_file(input_path: str, output_path: str) -> None:
    """Convert a single audio file to a numpy array, uses available converters.

    :param input_path: the path to the input file
    :param output_path: the path to the output file
    """

    # check all available converters
    for key, value in audio_converters.available.items():

        # prepare some reusable debug info
        converter_name = value.__name__
        check_string = f"\"{input_path}\".endswith(\"{key}\")"

        vprint2(f"[cvt_file] checking converter {converter_name} with type \"{key}\"")

        # check if the converter matches the file ending of the input file
        vprint3("[cvt_file] checking if " + check_string)
        if input_path.endswith(key):
            vprint3(f"[cvt_file] {check_string} = True")

            # instantiate converter
            vprint2("[cvt_file] creating instance of "+converter_name)
            converter = value()

            # tell the converter to create a spectrogram from the audio file
            try:
                vprint2("[cvt_file] converting with "+converter_name)
                array = converter.convert(input_path)
            except FileNotFoundError as e:

                # if the input file does not exist we error out
                # and return early
                print("Failed to convert file: File not found!")
                return

            # save numpy array to disk in binary format
            np.save(output_path, array)

            # stop looking for other converters
            return


def cvt_tree(input_dir: str, output_dir: str) -> None:
    """Convert an entire folder from audio to numpy arrays.
       Uses all available converters.

    :param input_dir: the input directory containing the audio files
    :param output_dir: the directory to put the numpy arrays into,
                       this folder will be created if it does not exist.
    """

    # create output_dir and all parents if not exist
    vprint3(f"[cvt_tree] Ensuring that {output_dir} exists")
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        vprint3(f"[cvt_tree] processing {filename} in {input_dir}")

        # get the "filename without extension" from filename
        pre, _ = os.path.splitext(filename)

        # put input_dir and filename together
        input_file = os.path.join(input_dir, filename)

        # put output_dir and "filename with new extension together"
        output_file = os.path.join(output_dir, pre + ".npy")

        vprint3(f"[cvt_tree] converting {input_file} to {output_file}")
        cvt_file(input_file, output_file)


if __name__ == "__main__":
    main()
