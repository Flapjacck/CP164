"""
-------------------------------------------------------
[assignment 4, Task 4]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

target1, target2 = q.split_alt()

print("Target1: {}".format(target1._values))
print("Target2: {}".format(target2._values))
