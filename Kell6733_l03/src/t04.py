"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test

fh = open('foods.txt', 'r')

print(priority_queue_test(fh))

fh.close()
