"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Deques.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2024-03-25"
-------------------------------------------------------
"""
# pylint: disable=W0212

# Imports
from math import log
from Deque_linked import Deque


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked Deque using the Selection Sort algorithm.
        Finds maximum value each pass.
        Use: selection_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked Deque of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        # Split the Deque into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None
        # Go through each node in the unsorted Deque and find the max value
        # to insert at the front of the sorted Deque.
        while unsorted is not None:
            max_node = unsorted
            current = max_node._next

            while current is not None:

                if current._value > max_node._value:
                    max_node = current
                current = current._next

            # Remove the max node from the deque.
            if max_node._prev is None and max_node._next is None:
                # Remove the last remaining node
                unsorted = None
            elif max_node is unsorted:
                # Remove the first node
                unsorted = max_node._next
                unsorted._prev = None
            elif max_node._next is None:
                # Remove the rear node
                max_node._prev._next = None
            else:
                # Remove any other node
                max_node._prev._next = max_node._next
                max_node._next._prev = max_node._prev

            # Move the max node to the front of the sorted deque.
            if a._front is not None:
                a._front._prev = max_node
            max_node._prev = None
            max_node._next = a._front
            a._front = max_node
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked Deque using the Bubble Sort algorithm.
        Use: bubble_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked Deque of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False
        last = a._rear

        while not done:
            # if no elements have been swapped, then the deque is sorted
            done = True
            # Get the front of the Deque.
            swapped = a._front
            current = a._front

            while current is not last and current is not a._rear:

                if current._value > current._next._value:
                    # If you swapped you need another pass.
                    done = False
                    # The pair current, current._next is out of order.
                    Sorts.swaps += 1
                    a._swap(current, current._next)
                    # Keep track of the next node to process
                    swapped = current
                else:
                    # Move to next node.
                    current = current._next
            last = swapped
        # done == True iff no pair of keys was swapped on the last pass.
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an Deque using the Comb Sort algorithm.
        Use: comb_sort(a)
        -------------------------------------------------------
        Parameters:
          a - a linked Deque of comparable elements (?)
        Returns:
          None
        -------------------------------------------------------
        """
        n = len(a)
        gap = n
        done = False

        while gap > 1 or not done:
            done = True
            current = a._front
            gap = int(gap / 1.3)

            if gap < 1:
                gap = 1

            i = 0
            far = current
            # Move to the far node for comparison.
            while i < gap and far is not None:
                far = far._next
                i += 1

            while current is not None and far is not None:
                if current._value > far._value:
                    a._swap(current, far)
                    done = False
                # Increment both nodes.
                far = far._next
                current = current._next
        return

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked Deque using the Insertion Sort algorithm.
        Use: insertion_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked Deque of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Split the Deque into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None

        # Go through each node in the unsorted Deque and insert it into the
        # proper position in the sorted Deque.
        while unsorted is not None:
            # Isolate the first node of the unsorted Deque.
            node = unsorted
            unsorted = unsorted._next
            # Find the proper place for the new node in the sorted so far Deque.
            # (Very similar to priorityQueue insertion.)
            previous = None
            current = a._front

            while current is not None and current._value < node._value:
                previous = current
                current = current._next

            # Insert node into the proper place in the sorted deque.
            node._next = current
            node._prev = previous

            if a._front is None:
                # Add first node into deque
                a._front = node
                a._rear = node
            elif previous is None:
                # Add node to beginning of deque
                a._front._prev = node
                a._front = node
            elif current is None:
                # Add node to end of deque
                a._rear._next = node
                a._rear = node
            else:
                # Add node elsewhere in deque
                previous._next = node
                current._prev = node
        return

    @staticmethod
    def merge_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked Deque using the Merge Sort algorithm.
        Use: merge_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked Deque of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        a._front = Sorts._merge_sort_aux(a._front)
        return

    @staticmethod
    def _merge_sort_aux(current):
        """
        -------------------------------------------------------
        Divides a linked Deque into halves, sorts each half, then
        merges the halves back together.
        Use: current = _merge_sort_aux(current)
        -------------------------------------------------------
        Parameters:
          current - pointer to a Deque node (_DequeNode)
        Returns:
          returns:
          current - pointer to sorted Deque segment (_DequeNode)
        -------------------------------------------------------
        """
        # Split the Deque only if there are at least two elements.
        if current is not None and current._next is not None:
            # Generate the left and right Deques.
            left, right = Sorts._merge_split(current)
            # Put the left Deque in order.
            left = Sorts._merge_sort_aux(left)
            # Put the right Deque in order.
            right = Sorts._merge_sort_aux(right)
            # Merge the left and right Deques.
            current = Sorts._merge(left, right)
        return current

    @staticmethod
    def _merge_split(current):
        """
        -------------------------------------------------------
        Split the Deque by putting alternating nodes into left and right Deques.
        Use: left, right = _merge_split(current)
        -------------------------------------------------------
        Parameters:
          current - pointer to a Deque node (_DequeNode)
        Returns:
          returns:
          left - pointer to left Deque segment (_DequeNode)
          right - pointer to right Deque segment (_DequeNode)
        -------------------------------------------------------
        """
        #
        left = None
        right = None
        toggle = 'lst'

        while current is not None:
            next_node = current._next

            if toggle == 'lst':
                current._next = left
                left = current
                toggle = 'r'
            else:
                current._next = right
                right = current
                toggle = 'lst'

            current = next_node
        return left, right

    @staticmethod
    def _merge(left, right):
        """
        -------------------------------------------------------
        Merges two parts of a linked Deque together.
        Use: new = _merge(left, right)
        -------------------------------------------------------
        Parameters:
          left - pointer to a Deque node (_DequeNode)
          right - pointer to a Deque node (_DequeNode)
        Returns:
          returns:
          new - pointer to sorted merge of left and right (_DequeNode)
        -------------------------------------------------------
        """
        # Initialize the new Deque.
        if left._value <= right._value:
            new = left
            left = left._next
        else:
            new = right
            right = right._next

        # Create a pointer to traverse the new Deque.
        current = new

        # Traverse both Deques appending larger value to the end of the Deque.
        while left is not None and right is not None:

            if left._value <= right._value:
                current._next = left
                current = current._next
                left = left._next
            else:
                current._next = right
                current = current._next
                right = right._next

        # Append the remaining Deque.
        if left is not None:
            current._next = left
        elif right is not None:
            current._next = right
        return new

    @staticmethod
    def quick_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked Deque using the Quick Sort algorithm.
        Use: quick_sort(a)
        -------------------------------------------------------
        Parameters:
          a - a linked Deque of comparable elements (?)
        Returns:
          None
        -------------------------------------------------------
        """
        a._front = Sorts._quick_sort_old_aux(a._front)
        return

    @staticmethod
    def _quick_sort_old_aux(current):
        """
        -------------------------------------------------------
        Divides a linked Deque into halves, sorts each half, then
        concatenates the halves back together.
        Use: current = _quick_sort_old_aux(current)
        -------------------------------------------------------
        Parameters:
          current - pointer to a Deque node (_DequeNode)
        Returns:
          returns:
          current - pointer to a sorted Deque (_DequeNode)
        -------------------------------------------------------
        """
        # to sort the subDeque a[p:q] of linked Deque a into ascending order
        if current is not None:
            # partitions a[first:last] into a[first:pivot] and a[pivot+1:last]
            lesser, equals, greater = Sorts._partition(current)
            lesser = Sorts._quick_sort_old_aux(lesser)
            greater = Sorts._quick_sort_old_aux(greater)
            current = Sorts._append(lesser, equals)
            current = Sorts._append(current, greater)
        return current

    @staticmethod
    def _partition(current):
        """
        -------------------------------------------------------
        Divides a linked Deque into three parts.
        Use: lst, e, g = _partition(current)
        -------------------------------------------------------
        Parameters:
          current - pointer to a Deque node containing pivot value (_DequeNode)
        Returns:
          returns:
          lesser - a Deque of values less than the pivot value (_DequeNode)
          greater - a Deque of values greater than the pivot value (_DequeNode)
          equals - a Deque of values equal to the pivot value (_DequeNode)
        -------------------------------------------------------
        """
        pivotValue = current._value
        lesser = None
        greater = None
        equals = None

        while current is not None:
            next_node = current._next

            if pivotValue > current._value:
                current._next = lesser
                lesser = current
            elif pivotValue < current._value:
                current._next = greater
                greater = current
            else:
                current._next = equals
                equals = current

            current = next_node
        return lesser, equals, greater

    @staticmethod
    def _append(head, tail):
        """
        -------------------------------------------------------
        Combines two Deques together in order.
        Use: current = _append(head, tail)
        -------------------------------------------------------
        Parameters:
          head - pointer to a Deque node of the first Deque (_DequeNode)
          tail - pointer to a Deque node of the second Deque (_DequeNode)
        Returns:
          returns:
          head - pointer to the combined nodes in order (_DequeNode)
        -------------------------------------------------------
        """
        current = head
        previous = None

        while current is not None:
            previous = current
            current = current._next

        if previous is None:
            head = tail
        else:
            previous._next = tail
        return head

    @staticmethod
    def cocktail_sort(a):
        """
        -------------------------------------------------------
        Sorts a deque using the Cocktail Sort algorithm.
        Use: cocktail_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a deque of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False
        first = a._front
        last = a._rear

        while not done:
            # if no elements have been swapped, then the Deque is sorted
            done = True
            # Get the first node not yet swapped.
            current = first
            swapped = a._front

            while current is not last and current._next is not None:

                if current._value > current._next._value:
                    # If you swapped you need another pass.
                    done = False
                    # The pair current, current._next is out of order.
                    Sorts.swaps += 1
                    a._swap(current, current._next)
                    # Keep track of last node swapped
                    swapped = current
                    # Make sure first is not moved down the Deque
                    if first is current:
                        first = current._prev
                    # current = swapped
                else:
                    # Move to next node.
                    current = current._next
            last = swapped

            # Compare values starting at last node swapped. If previous loop
            # is done, then last is None, and the second loop does not execute.
            current = last
            swapped = a._rear

            while current is not first and current._prev is not None:

                if current._value < current._prev._value:
                    # If you swapped you need another pass.
                    done = False
                    # The pair current, current._prev is out of order.
                    Sorts.swaps += 1
                    a._swap(current, current._prev)
                    # Keep track of last node swapped
                    swapped = current
                    # Make sure last is not moved up the Deque
                    if last is current:
                        last = current._prev
                else:
                    # Move to previous node.
                    current = current._prev
            first = swapped
        return

    # Sort Utilities

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked deque is sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
            a - a linked deque of comparable elements (?)
        Returns:
            returns
            is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        # Test forward links
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._value <= current._next._value:
                current = current._next
            else:
                is_sorted = False
        # Test reverse links
        current = a._rear

        while is_sorted and current is not None and \
                current._prev is not None:

            if current._value >= current._prev._value:
                current = current._prev
            else:
                is_sorted = False

        return is_sorted

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked structure of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        if a._front is not None:
            gnome = a._front._next
        else:
            gnome = None

        while gnome is not None:

            if gnome._value >= gnome._prev._value:
                gnome = gnome._next

            else:

                a._swap(gnome, gnome._prev)

                if gnome == a._front:
                    gnome = gnome._next

        return
