## Convert Audio to Spectrograms

### TODO-List:
- [ ] make sure that the plot is 512x512
- [ ] reshape the output format to rgb instead of rgba (4->3)
- [X] implement tree conversion
- [ ] (optional:Ilyas?) split samples that are longer than 512s into multiple spectrograms
- [ ] (optional:?) allow data-feeding via stdin and output via stdout

### Usage
```
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
```