"""
Tests for our array class
"""

import pytest

from array_class import Array

# 1D and 2D tests

@pytest.mark.parametrize('shape', [3, [1, 2], '1'])
def test_shape_not_tuple_raises_TypeError(shape):
    with pytest.raises(TypeError):
        Array(shape, 2)

@pytest.mark.parametrize('shape', [(3.0,), (1, 2.0), (1.0, 2.0, 3.0)])
def test_shape_tuple_not_ints_raises_TypeError(shape):
    with pytest.raises(TypeError):
        Array(shape, 2)

def test_values_wrong_type_raises_ValueError():
    with pytest.raises(ValueError):
        Array((3,), '1', '2', '3')
    with pytest.raises(ValueError):
        Array((3,), [1, 2], [3, 4], [5, 6])

def test_different_types_values_raises_ValueError():
    with pytest.raises(ValueError):
        Array((4,), [1, 2], 3, 4, [5, 6])
    with pytest.raises(ValueError):
        Array((4,), '1', 2, 3, 4)
    with pytest.raises(ValueError):
        Array((4,), 1.0, 2, 3, 4)


@pytest.mark.parametrize(
    's, v',
    [((3,), (1, 2)),
        ((1, 2), (1, 2, 3)),
        ((1, 2), 1),
        ((1, 2, 3), (1, 2, 3, 4, 5)),
])
def test_shape_and_number_of_values_mismatch_raises_ValueError(s, v):
    with pytest.raises(ValueError):
        Array(s, v)

def test_get_item_1d():
    a = Array((5,), 0, 1, 2, 3, 4)
    for i in range(5):
        assert a[i] == i

def test_get_item_2d():
    a = Array((2, 3), 0, 1, 2, 3, 4, 5)
    for i in range(2):
        for j in range(3):
            assert a[i][j] == i*3 + j


def test_str_1d_and_2d():
    a = Array((4,), 1, 2, 3, 4)
    assert str(a) == '[ 1 2 3 4 ] '

    b = Array((3,2), 1, 2, 3, 4, 5, 6)
    assert str(b) == '[ [ 1 2 ] [ 3 4 ] [ 5 6 ] ] '


@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,), 1, 2, 3), 10, Array((3,), 11, 12, 13)),
        (Array((3,), 1, 2, 3), Array((3,), 1, 2, 3), Array((3,), 2, 4, 6)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), 10, Array((2, 3), 10, 11, 12, 13, 14, 15)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), Array((2, 3), 0, 1, 2, 3, 4, 5), Array((2, 3), 0, 2, 4, 6, 8, 10))]
)
def test_add_and_radd_1d_and_2d(a, b, c):
    assert a + b == c
    assert b + a == c


@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,), 1, 2, 3), 10, Array((3,), -9, -8, -7)),
        (Array((3,), 1, 2, 3), Array((3,), 1, 2, 1), Array((3,), 0, 0, 2)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), 10, Array((2, 3), -10, -9, -8, -7, -6, -5)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), Array((2, 3), 0, 1, 2, 3, 4, 2), Array((2, 3), 0, 0, 0, 0, 0, 3))]
)
def test_sub_and_rsub_1d_and_2d(a, b, c):
    assert a - b == c
    assert b - a == -c

@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,), 1, 2, 3), 10, Array((3,), 10, 20, 30)),
        (Array((3,), 1, 2, 3), Array((3,), 1, 2, 1), Array((3,), 1, 4, 3)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), 10, Array((2, 3), 0, 10, 20, 30, 40, 50)),
        (Array((2, 3), 0, 1, 2, 3, 4, 5), Array((2, 3), 0, 1, 2, 3, 4, 2), Array((2, 3), 0, 1, 4, 9, 16, 10))]
)
def test_mul_and_rmul_1d_and_2d(a, b, c):
    assert a*b == c
    assert b*a == c

def test_eq_1d_and_2d():
    assert Array((1,), 5) == Array((1,), 5)
    assert Array((1,), 5) != Array((1,), 4)
    assert Array((2,), 5, 10) != Array((1,), 4)
    assert Array((2,), 5, -2) == Array((2,), 5, -2)
    assert Array((2,), 5, -2) != Array((2,), 5, -1)
    assert Array((2, 3), 0, 1, 2, 3, 4, 5) == Array((2, 3), 0, 1, 2, 3, 4, 5)
    assert Array((6,), 0, 1, 2, 3, 4, 5) != Array((2, 3), 0, 1, 2, 3, 4, 5)
    assert Array((3, 2), 0, 1, 2, 3, 4, 5) != Array((2, 3), 0, 1, 2, 3, 4, 5)
    assert Array((3, 2), 0, 1, 2, 3, 4, 5) != Array((2, 3), 0, 1, 2, 3, 4, 5)
    assert Array((2, 3), 0, 1, 2, 3, 4, 5) != Array((2, 3), 0.0, 1.0, 2.0, 3.0, 4.0, 5.0)

@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,), 1, 2, 3), Array((3,), 1, 2, 3), Array((3,), True, True, True)),
        (Array((3,), 1, 2, 3), Array((3,), 1, 1, 1), Array((3,), True, False, False)),
        (Array((3,), 1, 2, 3), 1, Array((3,), True, False, False)),
        (Array((3,), 1, 2, 3), 3, Array((3,), False, False, True))]
)
def test_is_eq_1d_and_2d(a, b, c):
    assert a.is_equal(b) == c

@pytest.mark.parametrize(
    'a, b',
    [(Array((3,), 1, 2, 3), Array((4,), 4, 5, 6, 7)),
        (Array((3,2), 1, 2, 3, 4, 5, 6), Array((2,3), 1, 2, 3, 4, 5, 6))]
)
def test_is_eq_1d_and_2d_raises_ValueError(a, b):
    with pytest.raises(ValueError):
        a.is_equal(b)

@pytest.mark.parametrize(
    'a, min',
    [(Array((3,), 1, 2, 3), 1),
        (Array((5,), 4, 2, -3, 7, 1), -3),
        (Array((2, 3), 2, 1, 0, 3, 4, 5), 0),
        (Array((2, 3), 1, 2, 2, 3, -4, 5), -4)]
)
def test_min_1d_and_2d(a, min):
    assert a.min_element() == min

@pytest.mark.parametrize(
    'a, mean',
    [(Array((3,), 1, 2, 3), 2),
        (Array((5,), 4, 2, -3, 7, 1), 2.2),
        (Array((2, 3), 2, 1, 0, 3, 4, 5), 2.5),
        (Array((2, 3), 1, 2, 2, 3, -4, 5), 1.5)]
)
def test_mean_1d_and_2d(a, mean):
    assert a.mean_element() == mean

# 3D tests
def test_str_3d():
    a = Array((2,2,2), 1, 2, 3, 4, 5, 6, 7, 8)
    assert str(a) == '[ [ [ 1 2 ] [ 3 4 ] [ 5 6 ] [ 7 8 ] ] ] '

@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,2,2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), 10,
      Array((3,2,2), 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)),
     (Array((3,2,2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
      Array((3,2,2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
      Array((3,2,2), 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24))]
)
def test_add_and_radd_3d(a, b, c):
    assert a + b == c
    assert b + a == c


@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,2,2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), 10,
      Array((3,2,2), -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2))]
)
def test_sub_and_rsub_1d_and_2d(a, b, c):
    assert a - b == c
    assert b - a == -c

@pytest.mark.parametrize(
    'a, b, c',
    [(Array((3,2,2), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), 10,
      Array((3,2,2), 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)),
     (Array((2,2,2), 1, 2, 3, 4, 5, 6, 7, 8), Array((2,2,2), 1, 2, 3, 4, 5, 6, 7, 8),
      Array((2,2,2), 1, 4, 9, 16, 25, 36, 49, 64))]
)

def test_mul_3d(a, b, c):
    assert a*b == c
    assert b*a == c

def test_min_3d():
    a = Array((2,2,2), 1, 2, 3, 4, 5, 6, 0, 8)
    assert a.min_element() == 0

def test_mean_3d():
    a = Array((2,2,2), 2, 2, 2, 2, 2, 2, 2, 2)
    assert a.mean_element() == 2


