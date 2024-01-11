"""
-------------------------------------------------------
[assignment 2, Task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
from Food_utilities import average_calories
from Food import Food

f = Food("grape", 3, True, 1)
f2 = Food("apple", 3, True, 7)
f3 = Food("banana", 1, True, 6)

foods = [f, f2, f3]

print(average_calories(foods))
