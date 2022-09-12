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
            raise TypeError('"shape" must be a tuple')

        if not isinstance(self.size, int):
            raise TypeError('size of array must be an integer')

        if not isinstance(values, tuple):
            raise TypeError('"values" must be a tuple')

        if all(isinstance(elem, int) for elem in values) or \
           all(isinstance(elem, float) for elem in values) or \
           all(isinstance(elem, bool) for elem in values):
           pass
        else:
            raise ValueError('all elements in "values" must be of the same type')

        if len(values) == self.size:
            for i in range(len(values)):
                self.array.append(values[i])
        else:
            raise ValueError('the number of values does not fit with the shape')


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
        if not isinstance(term, Sequence):
            term = [term]
        elif len(term) != self.size:
            return "NotImplemented"

        if all (isinstance(elem, int) for elem in term) or \
           all (isinstance(elem, float) for elem in term):
           pass
        else:
            return "NotImplemented"

        if len(term) == 1:
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
        print('hei')
        self.__add__(term)
        print('hadet')

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        pass

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        pass

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        pass

    def is_equal(self, other):
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

        pass

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        pass

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        pass


    # def check_datatype(self, term):
    #
    #     if not isinstance(self.term, Sequence):
    #         self.term = [self.term]
    #     elif len(self.term) != self.size:
    #         # return "NotImplemented"
    #         # sys.exit()
    #         raise ValueError
    #
    #     if all (isinstance(elem, int) for elem in self.term) or \
    #        all (isinstance(elem, float) for elem in self.term):
    #        pass
    #     else:
    #         # return "NotImplemented"
    #         # sys.exit()
    #         raise ValueError
