"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-03-11"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from Food_utilities import read_foods
from functions import hash_table
fv = "foods.txt"
f = open(fv, "r", encoding="utf-8")
foods = read_foods(f)
hash_table(7, foods)
f.close()

h = Hash_Set(5)
l = [99, 11, 22, 33]
for f in l:
    h.insert(f)
h.debug()
