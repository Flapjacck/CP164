"""
-------------------------------------------------------
[assignment 3, Task 7]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
from Stack_array import Stack


maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
path = stack_maze(maze)
print("Path found:", path)
