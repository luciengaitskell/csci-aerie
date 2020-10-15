"""
Stacks and Queues Handout 
Due: Tuesday, October 13th 

NOTES: 

- For the exercises, please do NOT use online resources. They are common algorithm questions so
    they have answers online but it won't help your understanding.
- If you are stuck or want help on any of them, come to office hours! 

Completed by Lucien Gaitskell (LUC)

"""


## Exercises

# 1.  Describe how you could use a single array to implement three stacks

""" LUC

Using the maximum size of the stacks (n), the size of the array would ultimately be 3x that. Therefore the starting
indices could be determined by the various multiples of `n`:
    Stack 1: 0  -> n-1 
    Stack 2: n  -> 2n-1
    Stack 3: 2n -> 3n-1

Another method could be to alternate using these rules, for x as the element index:
    Stack 1: x   % 3 == 0
    Stack 2: x+1 % 3 == 0
    Stack 3: x+2 % 3 == 0

"""

# 2. How would you design a stack which, in addition to push and pop,
#       has a function min which returns the minimum element?
""" LUC

(a)
A second data structure could be used to store the index locations of values in sorted order. However, this would
greatly increase the push and pop operation time. The `min` function would be constant time.

(b)
Another method, would be to simply search the entire stack for the minimum value for `min`. It is not possible to store
min/max ordering in the same data structure, as original order is necessary to maintain. 

"""

# 3. In reference to question 2, what is the run time of all of these three operations?
""" LUC

(a)
push: O(N)  - has to search through value ordered index reference array and insert index in proper location
pop: O(N)   - has to find index reference in value ordered index reference array and remove
min: O(1)   - grab from bottom/top of value ordered index reference array

(b)
push: O(1)  - add to end
pop: O(1)   - remove from end
min: O(N) - need to search to find smallest   

"""

# 4.  Implement a MyQueue class which implements a queue using two stacks
import queue


class MyQueue:
    """ LUC """
    def __init__(self, n):
        self.stack = queue.LifoQueue(maxsize=n)

    def put(self, val):
        self.stack.put(val)

    def get(self):
        save_s = queue.LifoQueue(maxsize=self.stack.qsize())

        if self.stack.empty():
            return None

        while not self.stack.empty():
            save_s.put(self.stack.get())

        val = save_s.get()
        while not save_s.empty():
            self.stack.put(save_s.get())
        return val


q = MyQueue(10)
q.put('a')
q.put('b')
q.put('c')
assert q.get() == 'a'
assert q.get() == 'b'
assert q.get() == 'c'
assert q.get() is None


# 5.  Write a program to sort a stack such that the smallest items are on the top. You can use
#       an additional temporary stack, but you may not copy the elements into any other data structure
#       (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
def sort_stack(s: queue.LifoQueue):
    """ LUC """
    rev = queue.LifoQueue(s.maxsize)  # Reversed, temporary storage queue

    for sort_level in range(0, s.qsize()):  # Current level on stack of current soring - sort until end
        max_val = None  # Max value of remaining values in stack

        while s.qsize() > sort_level:  # Operate over remaining values in stack up to and including sort level
            new_val = s.get()

            if max_val is None or new_val > max_val:  # Find and save maximum value
                max_val = new_val
            rev.put(new_val)  # Add data to temporary structure

        s.put(max_val)  # Add maximum value back stack

        while not rev.empty():  # Get all values from reversed temporary structure
            new_val = rev.get()

            if new_val != max_val:  # Add value to stack if not maximum value (which has already been added)
                s.put(new_val)
            else:
                max_val = None      # Prevent multiple occurrences of a max value from being reduced to one value

    return s


stack1 = queue.LifoQueue(10)
stack1.put(4)
stack1.put(6)
stack1.put(2)
stack1.put(9)

sort_stack(stack1)
assert stack1.get() == 2
assert stack1.get() == 4
assert stack1.get() == 6
assert stack1.get() == 9


# 6.  Remember this question from the arrays homework?
#       "Given an array of integers and an integer k, you need to find the total number of continuous
#       subarrays whose sum equals to k."
#
#       With you new understanding of how hashtables work, implement a solution to this problem using a dictionary.
import math


def subarrays(l, k):
    """
    LUC

    :param l: List to search through
    :param k: Subarray count target
    :return: Number of subarray combinations that add to k
    """

    # Sum count data
    sums = {}
    # structure: {sum: count}
    #   NOTE: count will mostly be duplicate by the end
    #       except for single element sub arrays
    #       THEREFORE: Have to divide by 2 and take ceil

    for val in l:   # Iterate through all values
        new_sums = {}   # New calculated sum counts from this value `val`
        for s, s_val in sums.items():   # Iterate through all previous sum/count pairs
            new_s = s+val   # Calculate new sum from existing sum plus this value
            new_sums[new_s] = sums.get(new_s, 0) + (sums[s] + 1)
            #   Increment new sum count (starting from 0 if not yet set)
            #       and add previous sum `s` counts plus 1

        sums.update(new_sums)  # Update sum structure with these changes / new values

        sums[val] = sums.get(val, 0) + 1  # Also include this value as single set in sum count

    return math.ceil(sums.get(k, 0)/2)  # Get sums for size k: reference note on `sums`


assert subarrays([1, 1, 2, 3, 4], 4) == 4
assert subarrays([1, 2, 3, 4], 4) == 2
assert subarrays([], 4) == 0
assert subarrays([2], 4) == 0
assert subarrays([4], 4) == 1
assert subarrays([1,4,5,10], 10) == 2
assert subarrays([1,4,5,5,10], 10) == 4
