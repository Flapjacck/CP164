"""
-------------------------------------------------------
[Lab 2, Task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
from utilities import stack_to_array
from utilities import stack_test


stack = Stack()
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array_to_stack(stack, source)

target = source

stack_to_array(stack, target)

print(target, source)

print(stack._values)


print(stack_test(source))
