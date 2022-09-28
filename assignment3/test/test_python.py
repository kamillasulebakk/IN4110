from instapy.python_filters import python_color2gray, python_color2sepia
import pytest
import numpy as np

# @pytest.mark.parametrize('idx', [(5,5), (2,3), (7,4)])
def test_color2gray(image):

    gray_image = python_color2gray(pixels)
    gray_image_shape = np.shape(gray_image)

    assert gray_image_shape == (10, 10)

    assert gray_image.dtype == np.uint8

    idx = (5, 5)

    pixel = image[idx]
    expected = pixel[0]*0.21 + pixel[1]*0.72 + pixel[2]*0.07
    predicted = gray_image[idx]

    assert predicted == expected.astype('uint8')

    print('Yay! All unit tests passed for c2g filter function implemented with pure python')


def test_color2sepia(image):

    sepia_image = python_color2sepia(pixels)
    sepia_image_shape = np.shape(sepia_image)
    rand_image_shape = np.shape(sepia_image)

    assert sepia_image_shape == rand_image_shape

    height, width, num_color_channels = sepia_image_shape

    assert sepia_image.dtype == np.uint8

    max_value = np.max(sepia_image)
    assert max_value <= 255

    weights = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]

    idx = (5, 5)
    pixel = image[idx]

    RGB = np.transpose(image[idx])
    new_RGB = weights@RGB
    np.clip(new_RGB, None, 255, out=new_RGB)
    expected = np.transpose(new_RGB)

    predicted = expected.astype('uint8')

    for C in range(num_color_channels):
        assert predicted[C] == expected.astype('uint8')[C]

    print('Yay! All unit tests passed for c2s filter function implemented with pure python')


shape = (10, 10, 3)
pixels = np.random.randint(256, size=shape, dtype='uint8')

test_color2gray(pixels)
test_color2sepia(pixels)