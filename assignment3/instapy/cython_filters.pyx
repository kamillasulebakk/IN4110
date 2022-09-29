"""Cython implementation of filter functions"""

import numpy as np
cimport numpy as np

def cython_color2gray(np.ndarray[np.uint8_t, ndim=3] image):
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]

    cdef np.ndarray[np.float64_t, ndim=2] gray_image = np.zeros((height, width))

    cdef int H, C
    for H in range(height):
        for W in range(width):
            gray_image[H,W] = 0.21*image[H,W,0] + 0.72*image[H,W,1] + 0.07*image[H,W,2]

    print(np.shape(gray_image))
    return gray_image.astype('uint8')

def cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef int height = image.shape[0]
    cdef int width = image.shape[1]
    cdef int num_color_channels = image.shape[2]

    cdef np.ndarray[np.float64_t, ndim=3] sepia_image = np.zeros((height, width, num_color_channels))

    cdef int H, C
    cdef double R, G, B
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
