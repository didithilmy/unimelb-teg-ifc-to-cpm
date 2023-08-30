import argparse

parser = argparse.ArgumentParser(
    prog="IfcToCpmConverter",
    description="This script converts IFC4 BIM file to Smart Crowd Model's CPM XML file.",
)

parser.add_argument("input_filename")
parser.add_argument("output_filename")
parser.add_argument("-W", "--width")
parser.add_argument("-H", "--height")
parser.add_argument("-x", "--offsetx")
parser.add_argument("-y", "--offsety")

args = parser.parse_args()

input_filename = args.input_filename
output_filename = args.output_filename

width, height = args.width, args.height
offsetx, offsety = args.offsetx, args.offsety


def validate_input():
    if width is not None or height is not None:
        if width is None or height is None:
            print("Error: Both width and height must be specified.")
            return False

    if offsetx is not None or offsety is not None:
        if offsetx is None or offsety is None:
            print("Error: Both offsetx and offsety must be specified.")
            return False

    return True


if validate_input():
    print(input_filename, output_filename, width, height)
    origin = None
    if offsetx is not None and offsety is not None:
        origin = (int(offsetx), int(offsety))

    dimension = None
    if width is not None and height is not None:
        dimension = (int(width), int(height))

    print("Converting IFC4 to CPM...")

    from ifc_to_cpm.IfcToCpmConverter import IfcToCpmConverter

    IfcToCpmConverter(input_filename, origin=origin, dimension=dimension).write(
        output_filename
    )
    print("Conversion complete!")
