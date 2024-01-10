"""
-------------------------------------------------------
[Lab 1, Task 5]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

fh = open('foods.txt', 'r')
foods = read_foods(fh)
print(foods)
fh.close()
