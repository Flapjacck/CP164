"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
from copy import deepcopy


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        # your code here

        return

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        # your code here

        return value

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"

        # your code here

        return value

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
