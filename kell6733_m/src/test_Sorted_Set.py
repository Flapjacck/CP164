"""
-------------------------------------------------------
Simple Set testing
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-23"
-------------------------------------------------------
"""
# Imports
from Sorted_Set_array import Sorted_Set

# Constants
SEP = "-" * 60


def print_set(source):
    """
    Prints contents of source in readable format.
    """
    print("{", end="")

    for value in source:
        print(f"{value}, ", end="")
    print("}")


def test_Sorted_Set():
    """
    Partial Sorted_Set testing.
    """
    # Testing
    source = Sorted_Set()
    print("Empty Set:")
    print(f"length: {len(source)}")
    print(f"is_empty: {source.is_empty()}")
    print_set(source)

    print(SEP)
    print("After adding:")

    for i in range(6):
        source.add(i)
    print(f"length: {len(source)}")
    print(f"is_empty: {source.is_empty()}")
    print_set(source)

    print(SEP)
    print(f"source.add(2): {source.add(2)}")

    print(SEP)
    key = 3
    print(f"discard {key}")
    discarded = source.discard(key)
    print(f"discarded: {discarded}")
    print("After discarding:")
    print(f"length: {len(source)}")
    print_set(source)

    print(SEP)
    key = 99
    print(f"discard {key}")
    discarded = source.discard(key)
    print(f"discarded: {discarded}")
    print("After discarding:")
    print(f"length: {len(source)}")
    print_set(source)

    print(SEP)
    key = 4
    print(f"{key} in source: {key in source}")

    print(SEP)
    key = 99
    print(f"{key} in source: {key in source}")

    print(SEP)
    target = Sorted_Set()

    for i in range(4, 8):
        target.add(i)
    print("target - ", end="")
    print_set(target)

    print(SEP)
    print(f"source == source: {source == source}")
    print(f"source == target: {source == target}")

    print(SEP)
    new_set = source.intersection(target)
    print("source.intersection(target): ", end="")
    print_set(new_set)

    print(SEP)
    new_set = source.union(target)
    print("source.union(target): ", end="")
    print_set(new_set)

    print(SEP)
    new_set = source.difference(target)
    print("source.difference(target): ", end="")
    print_set(new_set)

    print(SEP)
    new_set = source.symmetric_difference(target)
    print("source.symmetric_difference(target): ", end="")
    print_set(new_set)

    print(SEP)
    print(f"source.isdisjoint(target): {source.isdisjoint(target)}")

    print(SEP)
    print(f"source.issubset(source): {source.issubset(source)}")
    print(f"source.issubset(target): {source.issubset(target)}")

    print(SEP)
    print(f"source.issuperset(source): {source.issuperset(source)}")
    print(f"source.issuperset(target): {source.issuperset(target)}")


test_Sorted_Set()
