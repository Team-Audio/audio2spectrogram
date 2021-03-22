import os
import sys
from pathlib import Path

import numpy as np

import audio_converters
from verbose_print import vprint1, vprint2, vprint3


class Converter:
    """
    Converter Driver, runs the whole operation

    See convert.py for a description of the args param for __init__
    """

    def __init__(self, args):
        self.args = args
        self.use_stdout = args["-s"] or False
        self.use_glue = args["-g"] or False
        self.dir_mode = args["dir"] or False
        self.file_mode = args["file"] or False
        self.module_mode = args["--modules"] or False

        self.input = args["<input_directory>"] or args["<input_file>"]
        self.output = args["<output_directory>"] or args["<output_file>"]
        self.glued = []

    def run(self):
        vprint2(f"[startup] {self.input} -> {self.output}")

        if self.dir_mode is True:
            # converting a directory and copy it to a different dir

            vprint1("[startup] converting directory")
            self.cvt_tree(self.input, self.output)

        elif self.file_mode is True:
            # convert just a single file

            vprint1("[startup] converting file")
            self.cvt_file(self.input, self.output)

        if self.module_mode is True:
            # this prints the currently installed modules
            print("\n".join([f"{v.__name__} -> \"{k}\"" for k, v in audio_converters.available.items()]))

    def cvt_file(self, input_path: str, output_path: str) -> None:
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
                vprint2("[cvt_file] creating instance of " + converter_name)
                converter = value()

                # tell the converter to create a spectrogram from the audio file
                try:
                    vprint2("[cvt_file] converting with " + converter_name)
                    array = converter.convert(input_path)
                except FileNotFoundError as e:

                    # if the input file does not exist we error out
                    # and return early
                    print("Failed to convert file: File not found!")
                    return

                # check if we should glue all the individual files into one
                if self.use_glue:
                    self.glued += [array]
                    return

                # save numpy array to disk in binary format
                if not self.use_stdout:
                    np.save(output_path, array)
                else:
                    # write header
                    sys.stdout.write(f"============== BEGIN SHAPE ==============\n# shape={array.shape}\n")
                    # iterate 3rd dim
                    for data_slice in array:
                        # write slice
                        np.savetxt(sys.stdout.buffer, data_slice, fmt='%-7.4f')
                        # write slice footer
                        sys.stdout.write("# slice\n")

                    # write footer
                    sys.stdout.write("=============== END SHAPE ===============")

                # stop looking for other converters
                return

    def cvt_tree(self, input_dir: str, output_dir: str) -> None:
        """Convert an entire folder from audio to numpy arrays.
           Uses all available converters.

        :param input_dir: the input directory containing the audio files
        :param output_dir: the directory to put the numpy arrays into,
                           this folder will be created if it does not exist.
        """

        # create output_dir and all parents if not exist
        vprint3(f"[cvt_tree] Ensuring that {output_dir} exists")
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # make sure we have a fresh array to glue together if required
        self.glued = []

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
            self.cvt_file(input_file, output_file)

        # check if there is something over to save to disk
        if len(self.glued) > 0:
            # save the glued together arrays to disk
            out = os.path.join(output_dir, "glued.npy")
            np.save(out, np.array(self.glued))

            # clear array
            self.glued = []
