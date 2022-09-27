"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io
from . import python_filters
from . import numpy_filters
from . import numba_filters


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = ...
    if scale != 1:
        # Resize image, if needed
        ...

    # Apply the filter
    ...
    filtered = ...
    if out_file:
        # save the file
        ...
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    ...

    # parse arguments and call run_filter
    ...

    filename = "instapy/images/rain.jpg"
    pixels = io.read_image(filename)

    # pure python
    sepia_image = python_filters.python_color2sepia(pixels)
    sepia_image = Image.fromarray(sepia_image)
    sepia_image.save("instapy/images/rain_sepia_python.jpg")

    # numpy
    sepia_image = numpy_filters.numpy_color2sepia(pixels)
    sepia_image = Image.fromarray(sepia_image)
    sepia_image.save("instapy/images/rain_sepia_numpy.jpg")

    # numba
    sepia_image = numba_filters.numba_color2sepia(pixels)
    sepia_image = Image.fromarray(sepia_image)
    sepia_image.save("instapy/images/rain_sepia_numba.jpg")