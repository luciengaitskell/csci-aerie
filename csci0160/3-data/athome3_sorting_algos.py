"""
Sorting Algos Handout  
Due: October 7th, 2020 

NOTES: 

- Reference class notes here: https://docs.google.com/document/d/1AWM3nnLc-d-4nYobBRuBTMuCjYWhJMAUx2ipdQ5E77g/edit?usp=sharing
- Do NOT use online resources. 
- If you are stuck or want help on any of them, come to office hours!  

Completed by Lucien Gaitskell (LUC)


EXERCISES 

1. Suppose we have 243 identical-looking boxes each containing a drone ready to ship, but we remember that one box is
missing instructions! This box will weigh a little less than the rest and there is a scale that can compare weights of
any two sets of boxes. Assuming the worst case scenario, what is the minimum number of weighings needed to determine
which box has the missing instructions?

Hint: review the Tower of Hanoi stuff from class

2. Implement the following sorting algos (Insertion Sort, Merge Sort, and Quick Sort) in Python. Use comments to
denotate which pieces of code refer to the recursive process of divide, conquer, and combine.
Include 3-5 test cases for each algo.

Hint: review the pseudocode from the lecture notes

3. In terms of time complexity, which one is more efficient - Merge Sort or Quick Sort? What about space memory efficiency?


"""


# LUC: Exercise 1
"""

As this is the worst case scenario, all the boxes have to be weighed in some form. As only two boxes can be weighed at
once, one option is to compare pairs of boxes. Two boxes will be paired and only compared against each other. 

If the weighing scale could compare more than two boxes, than I would use a binary search approach.

"""


# LUC: Exercise 2

def insertion_sort(l):
    """ LUC """
    # Validate input
    if len(l) < 1 or not isinstance(l, list):
        return l

    current = 1  # Set element to compare

    while current < len(l):  # Run until selected element is beyond range
        val = l[current]  # Get value of selected value to insert

        swap_idx = current  # Set initial index to compare for swap
        while val < l[swap_idx-1] and swap_idx>0:
            # If selected value is less than next swap element
            swap_idx -= 1  # Decrement swap position

        for i in reversed(range(swap_idx, current)):
            # Shift up each element after swap position
            l[i+1] = l[i]

        l[swap_idx] = val  # Swap selected element to swap position
        current += 1  # Increment comparison index (could increment a second time if swap occurred)
    return l


assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([2,1,5]) == [1, 2, 5]
assert insertion_sort([2,1,5,3,4]) == [1, 2, 3, 4, 5]
assert insertion_sort([5,4,3,2,1]) == [1, 2, 3, 4, 5]
assert insertion_sort([9,2,56,2,1]) == [1, 2, 2, 9, 56]


def merge_sort(l):
    """ LUC """

    if len(l) <= 1:  # Single or empty array -> already sorted
        return l

    pivot = int(len(l) / 2)  # DIVIDE

    sublist1 = merge_sort(l[:pivot])  # CONQUER
    s1idx = 0
    sublist2 = merge_sort(l[pivot:])  # CONQUER
    s2idx = 0

    for i in range(len(l)):  # COMBINE

        if (
                (not s2idx < len(sublist2))  # If at end of sublist 2
                or (s1idx < len(sublist1) and sublist1[s1idx] < sublist2[s2idx])
                # or if sublist 1 has remaining elements and selected element is smaller than in list two
        ):
            l[i] = sublist1[s1idx]
            s1idx += 1
        else:
            l[i] = sublist2[s2idx]
            s2idx += 1

    return l


assert merge_sort([2,1,4,6]) == [1, 2, 4, 6]
assert merge_sort([7,3,10,4]) == [3, 4, 7, 10]
assert merge_sort([7]) == [7]
assert merge_sort([]) == []


import math

DEBUG = False

def quick_sort(l, start=0, end=None):
    """ LUC
    :param l: Input list, to sort
    :param start: First index of range to operate on
    :param end: Last index of range to operate on (last element is end-1)
    :return: Sorted list
    """
    if DEBUG: print("\n\nStarting {}".format(l))
    if end is None:
        end = len(l)
    if DEBUG: print("Operating idx {}->{}-1".format(start, end))

    if end - start <= 1:  # Empty or single lists are sorted
        if DEBUG: print("Ended")
        return l

    # Select pivot
    pidx = math.ceil((end-start)/2) + start - 1
    pval = l[pidx]
    if DEBUG: print("Pivot: {} (idx {})".format(pval, pidx))

    # Move pivot to end
    l[pidx] = l[end-1]
    l[end-1] = pval
    pidx = end-1

    while True:
        if DEBUG: print("Loop {}".format(l))
        #if DEBUG: print(l[start:end])

        left = start  # Move left selector from start until reaching a value greater than or equal to pivot
        while l[left] < pval and left <= end-2:
            left += 1
        if DEBUG: print("Left:", left)

        right = end - 2  # Move right selector from second to last until reaching a value less than or equal to pivot
        while l[right] > pval and right >= start:
            right -= 1
        if DEBUG: print("Right:", right)

        #if DEBUG: input()

        if left >= right:  # selectors have crossed
            l[pidx] = l[right+1]
            l[right+1] = pval
            if DEBUG: print("Crossed swap {}".format(l))

            if DEBUG: print("Recurse...")
            quick_sort(l, start, left)  # Operate on left sublist
            quick_sort(l, left+1, end)  # Operate on right sublist
            return l
        else:  # intermediate swap
            # swap values at left and right selectors
            tmp = l[left]
            l[left] = l[right]
            l[right] = tmp
            if DEBUG: print("Intermediate swap {}".format(l))


assert quick_sort([10,3,6,4,11]) == [3,4,6,10,11]
assert quick_sort([10,8,3,6,20,4]) == [3, 4, 6, 8, 10, 20]
assert quick_sort([10,5,3,2,8,3,6,20,4]) == [2, 3, 3, 4, 5, 6, 8, 10, 20]
assert quick_sort([10,8,3,6,20,4,18]) == [3,4,6,8,10,18,20]
assert quick_sort([]) == []
assert quick_sort([1]) == [1]
assert quick_sort([2,1]) == [1,2]


# LUC: Question 3
"""
Quick Sort can be the most efficient, with a potential for O(n). On average, the time complexity is O(nlogn), which is
the same as the consistent values of Merge Sort. However, the inefficient quadratic cases for Quick Sort are very
unlikely and therefore lead it to be more efficient the majority of the time.

Merge Sort also requires O(n) memory, due to the nature of copying elements into new arrays and merging them afterwards.
On the other hand, Quick Sort operates on a single list, in place. Therefore the algorithm only requires O(logn) memory
complexity as the recursive operation will have a call stack of size ~logn.

"""
