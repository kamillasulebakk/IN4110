"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    a = Array((4,), 1, 2, 3, 4)
    elem = a[2]
    assert elem == 3
    assert str(a) == '(1 2 3 4 )'
    # få med feilmelding her

def test_add_1d():
    a = Array((4,), 1, 2, 3, 4)
    assert (a + 10) == [11, 12, 13, 14]

    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 4, 6, 8)
    sum1 = a + b
    assert sum1 == [3, 6, 9, 12]

    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 4, 6, 8)
    sum2 = b + a

    assert sum1 == sum2


def test_sub_1d():
    a = Array((4,), 1, 2, 3, 4)
    assert (a - 10) == [-9, -8, -7, -6]

    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 4, 6, 8)
    sum1 = a - b
    assert sum1 == [-1, -2, -3, -4]

    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 4, 6, 8)
    sum2 = b - a
    assert sum2 == [1, 2, 3, 4]


def test_mul_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 1, 2, 3, 4)
    product1 = a*b
    assert product1 == [1, 4, 9, 16]

    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 1, 2, 3, 4)
    product2 = b*a

    assert product1 == product2

def test_eq_1d():
    pass


def test_same_1d():
    pass


def test_smallest_1d():
    a = Array((10,), 6, 3, 5, 2, 1, 5, 4, 7, 8, 10)
    min = a.min_element()
    assert min == 1


def test_mean_1d():
    a = Array((10,), 6, 3, 5, 2, 1, 5, 4, 7, 8, 10)
    mean  = a.mean_element()
    assert mean == 5.1


# 2D tests (Task 6)


def test_add_2d():
    a = Array((3, 2), 8, 3, 4, 1, 6, 1)
    b = Array((3, 2), 8, 3, 4, 1, 6, 1)


    a = Array((3, 1), 8, 3, 4)
    b = Array((1, 3), 8, 3, 4)


    print(a+b)



def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()


    # Task 6: 2d tests
    # test_add_2d()
    # test_mult_2d()
    # test_same_2d()
    # test_mean_2d()
