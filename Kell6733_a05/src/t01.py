"""
-------------------------------------------------------
[Assignment 5, Task 1]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-29"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list
from List_array import List

lst = List()
source = [1, 2, 3, 8, 4, 5, 6, 7, 7, 7, 8, 9]
array_to_list(lst, source)

lst.clean()
print(lst._values)
print('------------------------------------------------')

target = List()
source1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
source2 = List()
array_to_list(source2, source1)


target.combine(lst, source2)
# target.remove_front()
print(target._values)
print('------------------------------------------------')

target1, target2 = target.split()

print(target1._values, target2._values)
print('------------------------------------------------')

union = List()
l1 = List()
array_to_list(l1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

union.union(l1, target1)

print(l1._values, target1._values, union._values)
