# IFC4 BIM to CPM file converter

This script is used to convert IFC4 Building Information Modeling file into The University of Melbourne Transport Engineering Group's Smart Crowd Model XML file.

### Usage

First, install the dependencies:
```sh
pip install -r requirements.txt
```

Then, run the script:
```sh
python convert.py input.ifc output.cpm
```

### Help

```
usage: IfcToCpmConverter [-h] [-W WIDTH] [-H HEIGHT] [-x OFFSETX] [-y OFFSETY]
                         input_filename output_filename

This script converts IFC4 BIM file to Smart Crowd Model's CPM XML file.

positional arguments:
  input_filename
  output_filename

optional arguments:
  -h, --help            show this help message and exit
  -W WIDTH, --width WIDTH
  -H HEIGHT, --height HEIGHT
  -x OFFSETX, --offsetx OFFSETX
  -y OFFSETY, --offsety OFFSETY
```
