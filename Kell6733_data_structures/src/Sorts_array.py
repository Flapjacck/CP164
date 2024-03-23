"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
# Imports
from math import log10, floor

from BST_linked import BST


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    Uses class attribute 'swaps' to determine how many times
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Insertion Sort algorithm.
        Use: Sorts.insertion_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)

        for i in range(1, n):
            # Move backwards through sorted sequence a[0...j-1]
            # Shift values to the right until proper place found
            key = a[i]
            j = i - 1

            while j >= 0 and a[j] > key:
                Sorts._shift(a, j + 1, j)
                j = j - 1
            a[j + 1] = key
        return

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Selection Sort algorithm.
        Use: Sorts.selection_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)

        for i in range(n):
            # Traverse entire array
            m = i

            for j in range(i + 1, n):
                # Find index of minimum value in unsorted part of array

                if a[m] > a[j]:
                    # Track smallest value so far
                    m = j

            if m != i:
                # swap elements only if necessary
                Sorts._swap(a, m, i)
        return

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Bubble Sort algorithm.
        Use: Sorts.bubble_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False
        last = len(a) - 1

        while not done:
            # assume done is true
            done = True
            last_swapped = 0
            i = 0

            while i < last:
                if a[i] > a[i + 1]:
                    # Save the list index swapped.
                    last_swapped = i
                    # The pair (a[i], a[i+1]) is out of order.
                    # Exchange a[i] and a[i + 1] to put them in sorted order.
                    Sorts._swap(a, i, i + 1)
                    # If you swapped you need another pass.
                    done = False
                i += 1
            last = last_swapped
            # Decreases 'last' because everything after last_swapped is already
            # in order. done == False iff no pair of keys swapped on last pass.
        return

    @staticmethod
    def bst_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Tree Sort algorithm.
        Use: Sorts.bst_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        bst = BST()

        for v in a:
            bst.insert(v)

        a[:] = bst.inorder()
        return

    @staticmethod
    def shell_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Shell Sort algorithm.
        Use: Sorts.shell_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)
        gap = int(n / 1.3)

        while gap > 0:
            i = gap

            for i in range(gap, n):
                key = a[i]
                j = i

                while j >= gap and a[j - gap] > key:
                    # insert a[i] in the the subarray containing
                    # values that are gap apart and before
                    # index i. The subarray is sorted.
                    a[j] = a[j - gap]
                    j = j - gap

                # put key (a[i]) in its correct place
                a[j] = key
            gap = int(gap // 1.3)
        return

    @staticmethod
    def merge_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Merge Sort algorithm.
        Use: Sorts.merge_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        Sorts._merge_sort_aux(a, 0, len(a) - 1)
        return

    @staticmethod
    def _merge_sort_aux(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into halves, sorts each half, then
        merges the halves back together. Contents of a from first
        to last are sorted.
        Use: Sorts._merge_sort_aux(a, first, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - end of subarray of a (int)
        Returns:
            None
        -------------------------------------------------------
        """

        if first < last:
            middle = (last - first) // 2 + first
            Sorts._merge_sort_aux(a, first, middle)
            Sorts._merge_sort_aux(a, middle + 1, last)
            Sorts._merge(a, first, middle, last)
        return

    @staticmethod
    def _merge(a, first, middle, last):
        """
        -------------------------------------------------------
        Merges two parts of an array together.
        Use: Sorts._merge(a, first, middle, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            middle - middle of subarray of a (int)
            last - end of subarray of a (int)
        Returns:
            None
        -------------------------------------------------------
        """
        temp = []
        i = first
        j = middle + 1

        while i <= middle and j <= last:

            if a[i] <= a[j]:
                # put leftmost element of left array into temp array
                temp.append(a[i])
                i += 1
            else:
                # put leftmost element of right array into temp array
                temp.append(a[j])
                j += 1

        # copy any remaining elements from the left half
        while i <= middle:
            temp.append(a[i])
            i += 1

        # copy any remaining elements from the right half
        while j <= last:
            temp.append(a[j])
            j += 1

        # copy the temporary array back to the passed array
        for i in range(len(temp)):
            a[first + i] = temp[i]
        return

    @staticmethod
    def quick_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Quick Sort algorithm.
        Use: Sorts.quick_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        Sorts._quick_sort_old_aux(a, 0, len(a) - 1)
        return

    @staticmethod
    def _quick_sort_old_aux(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into halves, sorts each half, then
        concatenates the halves back together. Contents of a
        from first to last are sorted.
        Use: Sorts._quick_sort_old_aux(a, first, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - end of subarray of a (int)
        Returns:
            None
        -------------------------------------------------------
        """
        # Sort the subarray a[first:last] of array a into ascending order.
        if first < last:
            p = Sorts._partition(a, first, last)
            Sorts._quick_sort_old_aux(a, first, p - 1)
            Sorts._quick_sort_old_aux(a, p + 1, last)
        return

    @staticmethod
    def _partition(a, first, last):
        """
        -------------------------------------------------------
        Divides an array into two parts. Contents of a from
        first to last are sorted.
        Use: Sorts._partition(a, first, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            first - beginning of subarray of a (int)
            last - last of subarray of a (int)
        Returns:
            None
        -------------------------------------------------------
        """
        # Partitions a[first:last] into a[first:pivot] and a[pivot+1:last].
        pivot = (first + last) // 2
        low = first
        high = last - 1  # After we remove pivot it will be one smaller
        # print("{} - {} - {}".format(a[first:pivot_index], a[pivot_index],
        #                        a[pivot_index + 1:last]))
        pivot_value = a[pivot]
        a[pivot] = a[last]

        while low <= high:
            # print("{} - {} - {}".format(a[first:pivot_index],
            #        a[pivot_index], a[pivot_index + 1:last]))
            while low <= high and a[low] < pivot_value:
                low = low + 1
            while low <= high and a[high] >= pivot_value:
                high = high - 1
            if low <= high:
                # Sorts._swap(a, low, high)
                a[low] = a[high]
        # Sorts._shift(a, last, low)
        a[last] = a[low]
        a[low] = pivot_value
        # print("{} - {} - {}".format(a[first:pivot_index], a[pivot_index],
        #                   a[pivot_index + 1:last]))
        # Return the new pivot position.
        return low

    @staticmethod
    def quick2_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Quick Sort algorithm.
        Use: Sorts.quick_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        Sorts._quick2_sort_aux(a, 0, len(a) - 1)
        return

    @staticmethod
    def _quick2_sort_aux(a, first, last):
        if first < last:
            pivot = (first + last) // 2
            Sorts._swap(a, pivot, last)

            i = first
            j = last - 1

            while True:
                while i <= j and a[i] < a[pivot]:
                    i += 1
                while i <= j and a[j] > a[pivot]:
                    j -= 1

                if i < j:
                    Sorts._swap(a, i, j)
                else:
                    break

            Sorts._swap(a, i, last)  # restore pivot
            Sorts._quick2_sort_aux(a, first, i - 1)
            Sorts._quick2_sort_aux(a, i + 1, last)
            return

    @staticmethod
    def heap_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Heap Sort algorithm.
        Use: Sorts.heap_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        first = 0
        last = len(a) - 1
        Sorts._build_heap(a, first, last)
        i = last

        while i > first:
            Sorts._swap(a, i, first)
            Sorts._reheap(a, first, i - 1)
            i -= 1
        return

    @staticmethod
    def _build_heap(a, first, last):
        """
        -------------------------------------------------------
        Creates a heap. Contents of a from first to last are sorted.
        Use: Sorts._build_heap(a, first, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (list)
            first - first element in array to process (int)
            last - last element in array to process (int)
        Returns:
            None
        -------------------------------------------------------
        """
        i = last // 2

        while i >= first:
            Sorts._reheap(a, i, last)
            i -= 1
        return

    @staticmethod
    def _reheap(a, first, last):
        """
        -------------------------------------------------------
        Establishes heap property in a. Contents of a from
        first to last are heaped.
        Use: Sorts._reheap(a, first, last)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            first - first element in array to process (int)
            last - last element in array to process (int)
        Returns:
            None
        -------------------------------------------------------
        """
        done = False

        while 2 * first + 1 <= last and not done:
            k = 2 * first + 1

            if k < last and a[k] < a[k + 1]:
                k += 1

            if a[first] >= a[k]:
                done = True
            else:
                Sorts._swap(a, first, k)
                first = k
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Comb Sort algorithm.
        Use: Sorts.comb_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)
        gap = n
        done = False

        while gap > 1 or not done:
            done = True
            gap = int(gap / 1.3)

            if gap < 1:
                gap = 1

            i = 0
            j = gap

            while j < n:
                if a[i] > a[j]:
                    Sorts._swap(a, i, j)
                    done = False
                i += 1
                j += 1
        return

    @staticmethod
    def cocktail_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Cocktail Sort algorithm.
        Use: Sorts.cocktail_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)
        first = 0
        last = n - 1

        while first < last:
            # Initialize last_swapped to the beginning of the array.
            # Stops bottom loop from executing if no swaps done by top loop.
            last_swapped = 0
            i = first

            while i < last:
                if a[i] > a[i + 1]:
                    # test whether the two elements are in the correct order
                    Sorts._swap(a, i, i + 1)
                    last_swapped = i
                i += 1
            last = last_swapped

            # Initialize first_swapped to the end of the array.
            # Stops top loop from executing if no swaps done by bottom loop.
            first_swapped = n - 1
            i = last

            while i > first:
                if a[i] < a[i - 1]:
                    # test whether the two elements are in the correct order
                    Sorts._swap(a, i, i - 1)
                    first_swapped = i
                i -= 1
            first = first_swapped
        return

    @staticmethod
    def binary_insert_sort(a):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts.binary_insert_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (list)
        Returns:
            None
        -------------------------------------------------------
        """
        n = len(a)
        i = 1

        while i < n:
            ins = Sorts._bin_srch_i(a, 0, i, a[i])
            # Move key bigger than save in a[1:n-1] one space to the right.
            if ins < i:
                save = a[i]
                j = i - 1

                while j > ins - 1:
                    Sorts._shift(a, j + 1, j)
                    # a[j + 1] = a[j]
                    j -= 1
                a[ins] = save
            i += 1
        return

    @staticmethod
    def _bin_srch_r(a, low, high, value):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts._bin_srch_r(a)
        Recursive algorithm.
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (list)
            low - starting point of a to search for value (int)
            high - end point of a to search for value (int)
            value - value to search for position in a (?)
        Returns:
            mid - the insert point for value in a between low and high
        -------------------------------------------------------
        """
        if low == high:
            mid = low
        else:
            mid = low + ((high - low) // 2)

            if value > a[mid]:
                mid = Sorts._bin_srch_r(a, mid + 1, high, value)
            elif value < a[mid]:
                mid = Sorts._bin_srch_r(a, low, mid, value)
        return mid

    @staticmethod
    def _bin_srch_i(a, low, high, value):
        """
        -------------------------------------------------------
        Sorts an array using the Binary Insertion Sort algorithm.
        Use: Sorts._bin_srch_r(a)
        Iterative algorithm.
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (list)
            low - starting point of a to search for value (int)
            high - end point of a to search for value (int)
            value - value to search for position in a (?)
        Returns:
            mid - the insert point for value in a between low and high
        -------------------------------------------------------
        """
        found = False
        mid = (low + high) // 2

        while low < high and not found:
            # Find the middle of the current subarray.
            if value > a[mid]:
                # Search the right subarray.
                low = mid + 1
                mid = (low + high) // 2
            elif value < a[mid]:
                # Search the left subarray.
                high = mid
                mid = (low + high) // 2
            else:
                found = True
        return mid

    # Sort Utilities

    @staticmethod
    def is_sorted(a):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            srtd - True if contents of a are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(a)
        i = 0

        while srtd and i < n - 1:

            if a[i] <= a[i + 1]:
                i += 1
            else:
                srtd = False
        return srtd

    @staticmethod
    def _swap(a, i, j):
        """
        -------------------------------------------------------
        Swaps the data contents of two array elements.
        Updates 'swaps'. Values in a[i] and a[j] are swapped.
        Use: Sorts._swap(a, i, j)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            i - index of one value (int 0 <= i < len(a))
            j - index of another value (int 0 <= j < len(a))
        Returns:
            None
        -------------------------------------------------------
        """
        Sorts.swaps += 1

        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        return

    @staticmethod
    def _shift(a, i, j):
        """
        -------------------------------------------------------
        Shifts the contents of a[j] to a[i]. Value in a[j] is copied to a[i].
        Updates 'swaps' - worth 1/3 of _swap
        Use: Sorts._shift(a, i, j)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
            i - index of one value (int 0 <= i < len(a))
            j - index of another value (int 0 <= j < len(a))
        Returns:
            None
        -------------------------------------------------------
        """
        Sorts.swaps += 0.34

        a[i] = a[j]
        return
