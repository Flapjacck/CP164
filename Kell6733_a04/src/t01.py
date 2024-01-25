"""
-------------------------------------------------------
[assignment 4, task 1]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.insert(6)
q.insert(7)
q.insert(8)
q.insert(9)
q.insert(10)
print(q._values, q._front, q._rear)
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()
q.remove()

# q.insert(11)

# q.remove()

full = q.is_full()
n = len(q)
empty = q.is_empty()
print(q._values, q._front, q._rear)
print(empty, full, n)
s1 = Queue()
s2 = Queue()
s2.insert(1)
s1.insert(3)

equals = s1 == s2

print(equals)
