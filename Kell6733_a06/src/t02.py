"""
-------------------------------------------------------
[assignment 6, task 2]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

pq = Priority_Queue()

pq.insert('a')
pq.insert('b')
pq.insert('c')

print(pq._front._value, pq._count)
