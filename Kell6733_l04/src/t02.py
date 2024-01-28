"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array

llist = List()
source = [1, 2, 3, 4, 5, 6, 7]
array_to_list(llist, source)
print(llist._values, source)

target = []
list_to_array(llist, target)
print(llist._values, target)
