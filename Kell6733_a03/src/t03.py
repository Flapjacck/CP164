"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from utilities import array_to_stack
from Stack_array import Stack
from idlelib.idle_test.test_colorizer import source


source1 = Stack()
array_to_stack(source1, [3, 6, 1, 7, 9, 14])
print(source1._values)
stack_reverse(source1)

print(source1._values)
