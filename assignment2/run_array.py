from array_class import Array
import numpy as np

a = Array((4,), 1, 2, 3, 4)
print(a.__str__())

elem = a[2]
print(elem.__str__())

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 2, 4, 6, 8)
print(a + b)
print(" ")

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 2, 4, 6, 8)
print(b + a)
print(" ")

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 2, 4, 6, 8)
print(a - b)
print(" ")

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 2, 4, 6, 8)
print(b - a)
print(" ")

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 1, 2, 3, 4)
print(a*b)
print(" ")

a = Array((4,), 1, 2, 3, 4)
b = Array((4,), 1, 2, 3, 4)
print(b*a)
print(" ")

a = Array((10,), 6, 3, 5, 2, 1, 5, 4, 7, 8, 10)
print(a.min_element())
print(a.mean_element())
print(" ")

a = Array((10,), 'a', 3, 5, 2, 1, 5, 4, 7, 8, 10)
print(a.min_element())
print(a.mean_element())
print(" ")
