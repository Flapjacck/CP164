"""
-------------------------------------------------------
[Assignment 3, Task 6]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import postfix

string = "5 1 2 + 4 * + 3 -"
answer = postfix(string)

print(answer)
