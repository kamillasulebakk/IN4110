"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    weights = np.array([0.21, 0.72, 0.07])

    height, width, num_color_channels = image.shape
    gray_image = np.zeros((height, width))

    for H in range(height):
        for C, weight in enumerate(weights):
            gray_image[H] += image[H, :, C]*weight

    return gray_image.astype("uint8")

    # return image.dot(weights).astype('uint8')


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    # if not 0 <= k <= 1:
    #     # validate k (optional)
    #     raise ValueError(f"k must be between [0-1], got {k}")
    #
    # sepia_image = ...
    #
    # # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    # sepia_matrix = ..............................................................


    weights = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]

    height, width, num_color_channels = np.shape(image)

    sepia_image = np.zeros((height, width, num_color_channels))

    for H in range(height):
            RGB = np.transpose(image[H])
            new_RGB = weights@RGB
            np.clip(new_RGB, None, 255, out=new_RGB)
            sepia_image[H] = np.transpose(new_RGB)

    return sepia_image.astype('uint8')

