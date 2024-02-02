"""
-------------------------------------------------------
[assignment 5, Task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List


sl = Sorted_List()
sl.insert(1)
sl.insert(6)
sl.insert(3)
sl.insert(4)
sl.insert(5)
sl.insert(2)
print(sl._values, sl.find(6), sl.index(6))
print("------------------------")
sl2 = Sorted_List()
target = Sorted_List()
sl2.insert(1)
sl2.insert(6)
sl2.insert(3)
sl2.insert(4)
sl2.insert(5)
sl2.insert(2)
sl2.insert(1)
sl2.insert(7)
sl2.clean()
target.intersection(sl, sl2)
print(sl2._values, target._values)
print("------------------------")


target1, target2 = target.split_key(3)
print(target1._values, target2._values)
