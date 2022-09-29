"""numba-optimized filters"""
from numba import jit
import numpy as np
from .python_filters import python_color2gray


@jit(nopython=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    weights = np.array([0.21, 0.72, 0.07])

    height, width, num_color_channels = np.shape(image)

    gray_image = np.zeros((height, width))

    for H in range(height):
        for W in range(width):
            gray_single_channel = 0
            for C, weight in enumerate(weights):
                gray_single_channel += image[H][W][C]*weight
            gray_image[H][W] = gray_single_channel

    return gray_image.astype("uint8")

@jit(nopython=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    weights = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]

    height, width, num_color_channels = np.shape(image)

    sepia_image = np.zeros((height, width, num_color_channels))

    for H in range(height):
        for W in range(width):
            R, G, B = image[H,W]

            new_R = 0.393*R + 0.769*G + 0.189*B
            new_G = 0.349*R + 0.686*G + 0.168*B
            new_B = 0.272*R + 0.534*G + 0.131*B

            if new_R > 255:
                new_R = 255

            if new_G > 255:
                new_G = 255

            if new_B > 255:
                new_B = 255

            sepia_image[H, W] = (new_R, new_G, new_B)


    return sepia_image.astype('uint8')

