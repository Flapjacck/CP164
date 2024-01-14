"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from utilities import array_to_stack
from Stack_array import Stack

source1 = Stack()
source2 = Stack()
array_to_stack(source1, [5, 8, 12, 8])
array_to_stack(source2, [3, 6, 1, 7, 9, 14])
target = stack_combine(source1, source2)

print(target._values)
