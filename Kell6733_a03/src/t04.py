"""
-------------------------------------------------------
[assignment 3, Task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-13"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack

source1 = Stack()
array_to_stack(source1, [3, 6, 1, 7, 9, 14])
print(source1._values)
source1.reverse()

print(source1._values)
