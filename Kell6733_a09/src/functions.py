"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Spencer Kelly
ID:         169066733
Email:   Kell6733@mylaurier.ca
__updated__ = "2024-03-18"
-------------------------------------------------------
"""
# Imports
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = fv.readlines()

    for line in lines:

        line.strip()
        words = line.split()

        for word in words:

            if word.isalpha():
                word = word.lower()
                word_class = Word(word)
                hash_set.insert(word_class)

    fv.close()
    return


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = Word("a")
    for slot in hash_set._table:
        for item in slot:
            total += item.comparisons
            if item.comparisons > max_word.comparisons:
                max_word = item

    return total, max_word
