"""
-------------------------------------------------------
[Lab 7, task 1]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-02-26"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()

l.append(1)
l.append(2)
l.append(2)
l.append(4)
l.append(5)
l.append(2)
key = 2
p, c, i = l._linear_search_r(key)
print(p._value, c._value, i)
