"""
Array class for assignment 2
"""

from collections.abc import Sequence

class Array:

    def __init__(self, shape, *values):
        """
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        self.array = list()
        self.size = shape[0]

        if not isinstance(shape, tuple):
            raise TypeError('Shape of Array must be a tuple')

        if not isinstance(self.size, int):
            raise TypeError('Size of Array must be an integer')

        if not isinstance(values, tuple):
            raise TypeError('Values in Array must be given as a tuple')

        if all(isinstance(elem, int) for elem in values) or \
           all(isinstance(elem, float) for elem in values) or \
           all(isinstance(elem, bool) for elem in values):
           pass
        else:
            raise ValueError('All elements in Array must be of the same type')

        if len(values) == self.size:
            for i in range(len(values)):
                self.array.append(values[i])
        else:
            raise ValueError('The number of values in Array does not fit with the shape')


    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.
        """

        str_array = '('
        for i in range(self.size):
            str_array += str(self.array[i])
            str_array += ' '
        str_array += ')'

        return str_array

    def __getitem__(self, idx):
        array_elem = self.array[idx]
        return array_elem

    def __add__(self, term):
        """Element-wise adds Array with another Array or number.

        Returns:
            Array: the sum as a new array.
        """
        term = self.check_type_and_values(term)

        if type(term) != Array:
            for i in range(self.size):
                self.array[i] += term[0]
        else:
            for i in range(self.size):
                self.array[i] += term[i]

        return self.array


    def __radd__(self, term):
        """Element-wise adds Array with another Array or number.

        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(term)


    def __sub__(self, term):
        """Element-wise subtracts an Array or number from this Array.

        Returns:
            Array: the difference as a new array.
        """
        term = self.check_type_and_values(term)

        if type(term) != Array:
            for i in range(self.size):
                self.array[i] -= term[0]
        else:
            for i in range(self.size):
                self.array[i] -= term[i]

        return self.array

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        Returns:
            Array: the difference as a new array.
        """
        term = -term
        self.array = -self.array
        return self.__add__(term)

    def __mul__(self, term):
        """Element-wise multiplies this Array with a number or array.

        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        self.check_type_and_values(term)

        if term.size == 1:
            for i in range(self.size):
                self.array[i] *= term[0]
        else:
            for i in range(self.size):
                self.array[i] *= term[i]

        return self.array


    def __rmul__(self, term):
        """Element-wise multiplies this Array with a number or array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(term)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """


    def is_equal(self, term):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if term.size != self.size:
            raise ValueError('Array shapes do not match')

    def min_element(self):
        """Returns the smallest value of the array.

        Returns:
            float: The value of the smallest element in the array.
        """
        object = self.array
        self.check_if_bool(object)

        temp = self.array[0]
        for i in range(1, self.size):
            if self.array[i] < temp:
                temp = self.array[i]
        min = temp

        return min


    def mean_element(self):
        """Returns the mean value of an array

        Returns:
            float: the mean value
        """
        object = self.array
        self.check_if_bool(object)

        sum = 0
        for i in range(self.size):
            sum += self.array[i]

        mean = sum/self.size

        return mean


    def check_type_and_values(self, term):
        if type(term) == Array and term.size != self.size:
            raise TypeError('NotImplemented for this type. Term must be a scalar or an Array with the same shape')
        elif type(term) != Array:
            term = [term]

        self.check_if_bool(term)

        return term


    def check_if_bool(self, object):
        if all (isinstance(elem, int) for elem in object) or \
           all (isinstance(elem, float) for elem in object):
           pass
        else:
            raise ValueError('NotImplemented for booleans')