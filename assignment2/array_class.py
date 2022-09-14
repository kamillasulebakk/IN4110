"""
Array class for assignment 2
"""
from itertools import chain

class Array:
    def __init__(self, shape, *values):
        """
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n
                elements will have shape = (n,).
            *values: The values in the array. These should all be the same data
                type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        if not isinstance(shape, tuple):
            raise TypeError('Shape of Array must be a tuple')
        if not all(isinstance(d, int) for d in shape):
            raise TypeError('Values in shape must be int')

        if not isinstance(values, tuple):
            raise TypeError('Values in Array must be given as a tuple')

        if not isinstance(values[0], (int, float, bool)):
            raise ValueError(f'Elements in array must be (int, float, bool), not {type(values[0])}')

        self.type = type(values[0])

        if not all(isinstance(d, self.type) for d in values):
            raise ValueError('All elements in Array must be of the same type')

        self.array = list()
        self.shape = shape
        self.len = self.len_from_shape(shape)

        if not len(values) == self.len:
            raise ValueError('The number of values in Array does not fit with the shape')

        for e in values:
            self.array.append(e)

    def len_from_shape(self, shape):
        length = shape[0]
        for d in shape[1:]:
            length *= d
        return length

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        if len(self.shape) == 1:
            str_array = '[ '
            for i in range(self.len):
                str_array += str(self.array[i])
                str_array += ' '
            str_array += ']'
        else:
            str_array = (len(self.shape)-1)*'[ '
            idx = 0
            while idx < self.len:
                str_array += '[ '
                for _ in range(self.shape[-1]):
                    str_array += str(self.array[idx])
                    str_array += ' '
                    idx += 1
                str_array += '] '
            str_array += ']'

        return str_array

    def __getitem__(self, idx):
        if not isinstance(idx, int):
            raise TypeError(f'Array index must be int, not {type(idx)}')
        if idx >= self.shape[0]:
            raise IndexError(f'Index {idx} out of range for dim with size {self.shape[0]}')

        if len(self.shape) == 1:
            return self.array[idx]
        else:
            sub_arr_shape = self.shape[1:]
            sub_arr_len = self.len_from_shape(sub_arr_shape)
            sub_arr_values = self.array[idx*sub_arr_len:(idx + 1)*sub_arr_len]
            return Array(sub_arr_shape, *sub_arr_values)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        Returns:
            Array: the sum as a new array.
        """
        if not isinstance(other, (type(self), int, float)):
            raise TypeError(f'Add not implemented for type {type(other)}')
        if isinstance(other, type(self)):
            if self.shape != other.shape:
                raise IndexError(f'Shape mismatch in add: {self.shape} and {other.shape}')
            if self.type == bool or other.type == bool:
                raise TypeError('Add not implemented for arrays of type bool')

        if isinstance(other, type(self)):
            new_values = [a + b for a, b in zip(self.array, other.array)]
        else:
            new_values = [a + other for a in self.array]
        return Array(self.shape, *new_values)


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        Returns:
            Array: the sum as a new array.
        """
        return self + other


    def __neg__(self):
        if self.type == bool:
            raise TypeError(f'Add/sub/neg not implemented for type bool Arrays')
        new_values = [-a for a in self.array]
        return Array(self.shape, *new_values)


    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        Returns:
            Array: the difference as a new array.
        """
        if not isinstance(other, (type(self), int, float)):
            raise TypeError(f'Sub not implemented for type {type(other)}')
        return self + (-other)


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        Returns:
            Array: the difference as a new array.
        """
        return -(self - other)


    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        if not isinstance(other, (type(self), int, float)):
            raise TypeError(f'Mul not implemented for type {type(other)}')
        if isinstance(other, type(self)):
            if self.shape != other.shape:
                raise IndexError(f'Shape mismatch in mul: {self.shape} and {other.shape}')
            if self.type == bool or other.type == bool:
                raise TypeError('Multiplication not implemented for arrays of type bool')

        if isinstance(other, type(self)):
            new_values = [a * b for a, b in zip(self.array, other.array)]
        else:
            new_values = [a * other for a in self.array]

        return Array(self.shape, *new_values)



    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if type(self) != type(other):
            return False
        if other.shape != self.shape:
            return False
        if self.type != other.type:
            return False
        are_equal = (self.array == other.array)
        return are_equal

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        """
        if type(other) == type(self) and other.shape != self.shape:
            raise ValueError(f'Shape mismatch: {self.shape} and {other.shape}')
        if not isinstance(other, (type(self), int, float)):
            raise TypeError(f'Add not implemented for type {type(other)}')

        if isinstance(other, type(self)):
            new_values = [a == b for a, b in zip(self.array, other.array)]
        else:
            new_values = [a == other for a in self.array]

        return Array(self.shape, *new_values)


    def min_element(self):
        """Returns the smallest value of the array.

        Returns:
            float: The value of the smallest element in the array.
        """
        if self.type == bool:
            raise TypeError('Min not possible for arrays of type bool')

        temp = self.array[0]
        for i in range(1, self.len):
            if self.array[i] < temp:
                temp = self.array[i]
        min = temp

        return min


    def mean_element(self):
        """Returns the mean value of an array

        Returns:
            float: the mean value
        """
        if self.type == bool:
            raise TypeError('Min not possible for arrays of type bool')

        sum = 0
        for i in range(self.len):
            sum += self.array[i]

        mean = sum/self.len

        return mean





