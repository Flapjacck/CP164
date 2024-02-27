"""
-------------------------------------------------------
[lab 7, Task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-02-27"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()
l2 = List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(5)

print(l.is_identical_r(l2))
