"""
-------------------------------------------------------
Stores a single word and counts occurrences and
comparisons when the word is used.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-03-24"
-------------------------------------------------------
"""


class Word:

    def __init__(self, word):
        """
        -------------------------------------------------------
        Initialize a Word object.
        Use: target = Word(string)
        -------------------------------------------------------
        Parameters:
            word - an single lowercase word (str)
        Returns:
            A new Word object.
        -------------------------------------------------------
        """
        assert word.isalpha() and word.islower(), "Invalid word"

        self.word = word
        self.comparisons = 0

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Word data.
        Use: print(m)
        Use: s = str(m)
        -------------------------------------------------------
        Returns:
            the value of self.word (str)
        -------------------------------------------------------
        """
        return f"{self.word}: {self.comparisons:,d}"

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this Word against another Word for equality.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Word to compare to (Word)
        Returns:
            result - True if text portions match, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        target.comparisons += 1
        result = self.word == target.word
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Word comes before another.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - Word to compare to (Word)
        Returns:
            result - True if source precedes target, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        target.comparisons += 1
        result = self.word < target.word
        return result

    def __gt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Word is greater than another.
        Use: source > target
        -------------------------------------------------------
        Parameters:
            target - Word to compare to (Word)
        Returns:
            result - True if source follows target, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        target.comparisons += 1
        result = self.word > target.word
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if this Word is less than or equal to another.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - Word to compare to (Word)
        Returns:
            result - True if source precedes or is equal to target,
                False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        target.comparisons += 1
        result = self.word <= target.word
        return result

    def __ge__(self, target):
        """
        -------------------------------------------------------
        Determines if this Word is greater than or equal to another.
        Use: source >= target
        -------------------------------------------------------
        Parameters:
            target - Word to compare to (Word)
        Returns:
            result - True if source follows or is equal to target,
                False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        target.comparisons += 1
        result = self.word >= target.word
        return result

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a word.
        Use: h = hash(word)
        -------------------------------------------------------
        Returns:
            value - the total of the characters in the word string (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.word:
            value += ord(c)
        return value
