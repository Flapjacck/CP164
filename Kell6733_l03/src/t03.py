"""
-------------------------------------------------------
[Lab 3, Task 3]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
#from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array

source = [1, 2, 5, 4, 8, 6, 7, 3, 9]
target = []
q = Priority_Queue()
array_to_pq(q, source)
#pq_to_array(q, target)
# print(target)
print(q._values)
