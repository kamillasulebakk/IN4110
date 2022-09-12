"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    a = Array((4,), 1, 2, 3, 4)
    # print(a.__str__())

    elem = a[2]
    # print(elem.__str__())

    # a = Array((4,), 1, 2.4, 3.3, 4)
    # print(a)
    # assert

def test_add_1d():
    a = Array((4,), 1, 2, 3, 4)
    # term = 10
    term = [10, 20, 30, 40]
    # term = ['a', 10, 'b', 20]
    # term = [10, 20, 30, 40, 50]

    print(a.__add__(term))
    # print(a.__radd__(term))

    # print(term.__add__(a))


def test_sub_1d():
    pass


def test_mul_1d():
    pass


def test_eq_1d():
    pass


def test_same_1d():
    pass


def test_smallest_1d():
    pass


def test_mean_1d():
    pass


# 2D tests (Task 6)


def test_add_2d():
    pass


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
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
