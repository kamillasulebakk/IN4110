"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from . import io
from typing import Callable
import numpy as np

from .python_filters import python_color2gray, python_color2sepia
from .numpy_filters import numpy_color2gray, numpy_color2sepia
from .numba_filters import numba_color2gray, numba_color2sepia
from .cython_filters import cython_color2gray


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """

    # Call and compile numba's filter function in order to avoid timing compilation costs
    if filter_function == numba_color2gray or filter_function == numba_color2sepia:
        numba_color2gray(arguments[0])

    mean_time = 0
    for i in range(calls):
        start = time.perf_counter()
        filter_function(arguments[0])
        stop = time.perf_counter()
        elapsed_time = stop - start
        mean_time += elapsed_time

    mean_time /= calls

    return mean_time


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = io.read_image(filename)
    height, width, num_color_channels = np.shape(image)

    f = open('timing-report.txt', 'w')
    f.write(f'Timing performed using {filename}: {height}x{width}\n')

    filter_names = ['color2gray', 'color2sepia']

    functions = [[python_color2gray, numpy_color2gray, numba_color2gray, cython_color2gray],
                 [python_color2sepia, numpy_color2sepia, numba_color2sepia, cython_color2gray]]


    for i, filter_name in enumerate(filter_names):
        reference_filter = functions[i][0]

        reference_time = time_one(reference_filter, image)

        f.write('\n')
        f.write(f'Reference (pure Python) filter time {filter_name}: {reference_time:2.03f}s ({calls=})\n')

        implementations = ['numpy', 'numba', 'cython']


        for j in range(1, len(functions[i])):
            filter = functions[i][j]

            filter_time = time_one(filter, image)

            speedup = reference_time/filter_time

            f.write(f'Timing: {implementations[j-1]} {filter_name}: {filter_time:.3}s ({speedup:.2f}x)\n')

    f.close()

    with open('timing-report.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
