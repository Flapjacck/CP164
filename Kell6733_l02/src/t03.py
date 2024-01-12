"""
-------------------------------------------------------
[Lab 2, Task 3]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_foods

s = Stack()

fh = open('foods.txt', 'r')
foods = read_foods(fh)
st = stack_test(foods)

fh.close()
