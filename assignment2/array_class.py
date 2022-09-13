"""
Array class for assignment 2
"""
from itertools import chain

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
        self.shape_size = len(shape)
        self.shape = shape

        if self.shape_size > 1:
            for i in range(1, self.shape_size):
                self.size *= shape[i]

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

        if len(values) == self.size and self.shape_size == 1:
            for i in range(len(values)):
                self.array.append(values[i])
        elif len(values) == self.size and self.shape_size > 1:
            elem = 0
            for i in range(shape[1]):
                row_array = list()
                for j in range(shape[0]):
                    row_array.append(values[j+elem])
                elem += shape[0]
                self.array.append(row_array)
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

        # 1d array + scalar
        if type(term) != Array and self.shape_size == 1:
            for i in range(self.size):
                self.array[i] += term[0]
        # 2d array + scalar
        elif type(term) != Array and self.shape_size != 1:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.array[i][j] += term[0]
        # 1d array + 1d array
        elif term.shape_size == 1 and self.shape_size == 1:
            for i in range(self.size):
                self.array[i] += term[i]
        # 2d array + 2d array
        elif term.shape_size != 1 and self.shape_size != 1:
            for i in range(term.shape[0]):
                for j in range(term.shape[1]):
                    self.array[i][j] += term[i][j]
        else:
            raise ValueError('Could not perform the subraction')

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

        # legge inn true/false statements?
        # 1d array - scalar
        if type(term) != Array and self.shape_size == 1:
            for i in range(self.size):
                self.array[i] -= term[0]
        # 2d array - scalar
        elif type(term) != Array and self.shape_size != 1:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.array[i][j] -= term[0]
        # 1d array - 1d array
        elif term.shape_size == 1 and self.shape_size == 1:
            for i in range(self.size):
                self.array[i] -= term[i]
        # 2d array - 2d array
        elif term.shape_size != 1 and self.shape_size != 1:
            for i in range(term.shape[0]):
                for j in range(term.shape[1]):
                    self.array[i][j] -= term[i][j]
        else:
            raise ValueError('Could not perform the addition')

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

        # # 1d array * scalar
        # if type(term) != Array and self.shape_size == 1:
        #     for i in range(self.size):
        #         self.array[i] *= term[0]
        # # 2d array * scalar
        # elif type(term) != Array and self.shape_size != 1:
        #     for i in range(self.shape[0]):
        #         for j in range(self.shape[1]):
        #             self.array[i][j] *= term[0]
        # # 1d array * 1d array
        # elif term.shape_size == 1 and self.shape_size == 1:
        #     for i in range(self.size):
        #         self.array[i] *= term[i]
        # # 2d array - 2d array
        # elif term.shape_size != 1 and self.shape_size != 1:
        #     for i in range(term.shape[0]):
        #         for j in range(term.shape[1]):
        #             self.array[i][j] -= term[i][j]
        # else:
        #     raise ValueError('Could not perform the addition')



        self.check_type_and_values(term)

        if term.size == 1:
            for i in range(self.size):
                self.array[i] *= term[0]
        else:
            for i in range(self.size):
                self.array[i] *= term[i]

        return self.array

        # term = self.check_type_and_values(term)
        #
        # # 1d array * scalar
        # if type(term) != Array and self.array :
        #     for i in range(self.size):
        #         self.array[i] *= term[0]
        #
        # elif term.shape_size == 1:
        #     for i in range(self.size):
        #         self.array[i] *= term[i]
        # elif term.shape_size/self.shape[0] == 1:
        #     for i in range(self.shape[1]):
        #         for j in range(self.shape[0]):
        #             self.array[i][j] *= term[i][j]
        #
        # return self.array


    def __rmul__(self, term):
        """Element-wise multiplies this Array with a number or array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(term)

    def __eq__(self, term):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if type(term) != Array:
            return False
        elif term.size != self.size:
            return False

        pass



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

        self.check_if_bool(term)

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

        if type(object) == Array:
            if object.size >= 1:
                object = object.flat_array()

        if all (isinstance(elem, int) for elem in object) or \
           all (isinstance(elem, float) for elem in object):
           pass
        else:
            raise TypeError('NotImplemented for booleans. Term must be an int or an Array')


    def flat_array(self):
       """Flattens the N-dimensional array of values into a 1-dimensional array.
       Returns:
           list: flat list of array values.
       """
       flat_array = self.array
       for _ in range(len(self.shape[1:])):
           flat_array = list(chain(*flat_array))

       return flat_array