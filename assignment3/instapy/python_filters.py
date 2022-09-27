"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
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

    return gray_image.astype('uint8')


def python_color2sepia(image: np.array) -> np.array:
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

            new_R = weights[0][0]*R + weights[0][1]*G + weights[0][2]*B
            new_G = weights[1][0]*R + weights[1][1]*G + weights[1][2]*B
            new_B = weights[2][0]*R + weights[2][1]*G + weights[2][2]*B

            if new_R > 255:
                new_R = 255

            if new_G > 255:
                new_G = 255

            if new_B > 255:
                new_B = 255

            sepia_image[H, W] = (new_R, new_G, new_B)


    return sepia_image.astype('uint8')
