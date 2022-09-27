"""Cython implementation of filter functions"""

import numpy as np
cimport numpy as np

def cython_color2gray(image):
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

def cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    ...
