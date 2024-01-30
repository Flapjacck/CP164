"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
# Imports
from functions import gcd

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))
ans = gcd(m, n)

print("The greatest common denominator of", m, "and", n, "is", ans)
