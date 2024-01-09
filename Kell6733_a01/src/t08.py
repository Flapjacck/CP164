"""
-------------------------------------------------------
[assignment 1, task 8]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-09"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
small, large, total, average = matrix_stats(a)

print(small, large, total, average)
