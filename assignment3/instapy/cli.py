"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io
from instapy.python_filters import python_color2gray, python_color2sepia
from instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
from instapy.numba_filters import numba_color2gray, numba_color2sepia


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "gray",
    factor: int = 1,
    scale: str = "upscale"
) -> None:
    """Run the selected filter"""

    pixels = io.read_image(file)

    if scale == "upscale":
        pixels = pixels.repeat(factor, axis=0).repeat(factor, axis=1)
    else:
        pixels = pixels[::factor, ::factor]

    filter_function = {
        "gray": eval(f"{implementation}_color2gray"),
        "sepia": eval(f"{implementation}_color2sepia")
    }[filter]

    filtered_image = filter_function(pixels)

    if out_file:
        filtered_image = Image.fromarray(filtered_image)
        filtered_image.save(out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered_image)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")

    parser.add_argument("-o", "--out", help="The output filename", type=str, default = None)

    parser.add_argument("-i", "--implementation", help="The implementation",
                        choices = ["python", "numba" , "numpy", "cython"], default = "python")

    parser.add_argument("-fi", "--filter", help="Select filter",
                        choices = ["gray", "sepia"], default = "gray")

    parser.add_argument("-fa", "--factor", help="Scale factor to resize image", type=int, default=1)

    parser.add_argument("-sc", "--scale", help="Select upscaling or downscaling of image ",
                        choices = ["upscale", "downscale"], default = "upscale")

    # parser.add_argument("-t", "--time", help="Select upscaling or downscaling of image ",
    #                     choices = ["yes", "no"], default = "yes")
    #                     -r, --runtime
    args = parser.parse_args()

    run_filter(args.file, args.out, args.implementation, args.filter, args.factor, args.scale)

