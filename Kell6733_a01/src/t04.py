"""
-------------------------------------------------------
[assignment 1, Task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

fv = open('testing.txt', 'r')
upp, low, dig, whi, rem = file_analyze(fv)
print(upp, low, dig, whi, rem)
