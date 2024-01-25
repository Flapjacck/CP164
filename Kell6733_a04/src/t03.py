"""
-------------------------------------------------------
[Assingment 4, Task 3]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt

source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
print(source._values)
target1, target2 = queue_split_alt(source)

print(target1._values, target2._values)
