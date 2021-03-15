<h1 align="center">Convert Audio to Spectrograms</h1> 
<p align="center">
    <a href="https://lgtm.com/projects/g/Team-Audio/audio2spectrogram/alerts/"><img alt="Total alerts" src="https://img.shields.io/lgtm/alerts/g/Team-Audio/audio2spectrogram.svg?logo=lgtm&logoWidth=18"/></a>
<a href="https://lgtm.com/projects/g/Team-Audio/audio2spectrogram/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/Team-Audio/audio2spectrogram.svg?logo=lgtm&logoWidth=18"/></a>
</p>

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