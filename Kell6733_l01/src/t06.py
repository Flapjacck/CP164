"""
-------------------------------------------------------
[Lab 1, Task 6]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods, read_foods


fh = open("new_foods.txt", "w")

write_foods(fh, foods)

fh.close()
