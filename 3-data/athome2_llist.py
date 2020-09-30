"""
Linked Lists Handout  
Due: Tuesday, Sept 29th

NOTES: 

- Reference class notes here: https://docs.google.com/document/d/1AWM3nnLc-d-4nYobBRuBTMuCjYWhJMAUx2ipdQ5E77g/edit?usp=sharing
- For the python exercises, please do NOT use online resources. They are common algorithm questions so
	they have answers online but it won't help your understanding. 
- If you are stuck or want help on any of them, come to office hours! 

Completed by Lucien Gaitskell (LUC) - September 29, 2020
"""


"""
LUC: Util 
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def new(self, next_data) -> 'Node':
        self.next = self.__class__(next_data)
        return self.next

    def resolve(self, start=None):
        if start is None:
            start = []
        start.append(self.data)
        if self.next is not None:
            return self.next.resolve(start)
        return start

    def traverse(self, head=True):
        print(self.data, end='')
        if self.next is not None:
            self.next.traverse(head=False)
        if head:
            print()

    def __repr__(self):
        return str(self.resolve())


## Exercises

# 1. How would you remove duplicates from an unsorted linked list?

def remove_duplicate(node):
    """ LUC """
    prev_node = node  # Set node to start comparison of next node from

    while prev_node is not None and prev_node.next is not None:
        # (1) Have to check that previous node is not none (to catch `prev_node = prev_node.next` if next is None)
        # (2) Make sure a next node exists

        if prev_node.next.data == node.data:  # Check if subsequent node has same data
            prev_node.next = prev_node.next.next  # If so, eliminate from linked list

        prev_node = prev_node.next  # Move previous node on

    # If node has next, then run again on next sub-list (n-1 length)
    if node.next is not None:
        remove_duplicate(node.next)

    # Return final list
    return node


dup_node = Node(0)
dup_node.new(1).new(2).new(3).new(2).new(8).new(2)
assert remove_duplicate(dup_node).resolve() == [0,1,2,3,8]


# 2. How would you find the kth to last element of an singly linked list?

def subset(node, k):
    """ LUC: Sub-list of linked-list, from kth idx to end beginning at root node """
    root = node
    for i in range(k):
        root = root.next
    return root

k_subset_node = Node(0)
k_subset_node.new(1).new(2).new(3).new(4).new(5).new(6)

assert subset(k_subset_node, 3).resolve() == [3, 4, 5, 6]


# 3. How would you delete a node in the middle of a singly linked list?

def remove_node(node, idx):
    if idx == 0:
        return node.next
    else:
        prev = node
        for i in range(idx-1):
            prev = prev.next

        prev.next = prev.next.next
        return node


element_remove_node = Node(0)
element_remove_node.new(5).new(2).new(1)

assert remove_node(element_remove_node, 0).resolve() == [5, 2, 1]
assert remove_node(element_remove_node, 1).resolve() == [0, 2, 1]  # NOTE: This edits existing list object...
# this could create errors when repeating function. To enable reuse, it is necessary to copy list before operation


# For ex, remove "H" from this linked list - don't need to return anything (just change the linked list)

this_node = Node("T")
this_node.new("H").new("I").new("S")

assert remove_node(this_node, 1).resolve() == ["T", "I", "S"]

#4. How would you check if a linked list is a palindrome?


def palindrome(node):
    """ LUC """

    # Create reverse linked list
    c_node = node
    reverse_node = None
    while c_node is not None:
        new_r_node = Node(c_node.data)
        new_r_node.next = reverse_node
        reverse_node = new_r_node
        c_node = c_node.next

    orig_i_node = node
    rvrs_i_node = reverse_node
    while orig_i_node is not None:
        if orig_i_node.data != rvrs_i_node.data:
            return False

        orig_i_node = orig_i_node.next
        rvrs_i_node = rvrs_i_node.next

    return True
    # NEED TO ADD COMPARISON


palindrome_node = Node(0)
palindrome_node.new(5).new(2).new(5).new(0)
assert palindrome(palindrome_node)
not_palindrome_node = Node(0)
not_palindrome_node.new(5).new(2).new(5)
assert not palindrome(not_palindrome_node)



#5. Recursion Detour

"""
    In class we discussed how a linked list is a recursive data structure. Recursion is very important to understand 
    because 1) it can simplify code 2) can speed up programs by requiring less information to be stored. One famous ex
    of recursion is the Fibonacci sequence. 

    TODO: The Fibonacci sequence is dened as follows: the rst number of the sequence is 0, the second number is 1, and the nth
            number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth 
            Fibonacci number. 
"""


# Can you come up with another solution to the problem? Hint: one should use recursion and the other should not (iterative solution)

def fibonacci(n, history=None):
    """ LUC: Recursive fibonacci """
    if n < 1:
        return []

    if history is None:  # First call
        history = [1]
    else:
        s = sum(history[-min(2, len(history)):])  # Sum up last two (or less if not long enough) elements
        history.append(s)  # Add to history

    fibonacci(n-1, history=history)  # execute subsequent step with reduced n
    return history


assert fibonacci(5) == [1, 1, 2, 3, 5]


def fibonacci_iterative(n):
    """ LUC: Iterative fibonacci """
    if n < 1:  # Prevent out of range structures
        return []
    history = [1]  # Beginning

    for i in range(1,n):
        s = sum(history[-min(2, len(history)):])  # Sum up last two (or less if not long enough) elements
        history.append(s)

    return history

assert fibonacci(6) == [1, 1, 2, 3, 5, 8]

# Question - In the recursive approach, how many calls to fibonacci(n) function do we make when we call fibonacci(4)?

# LUC: The recursive approach will take 5 calls to for n=4.


"""

    A frog wants to cross an 11-foot river. There are 10 stones that he can use. The rocks are seperated by 1 foot.
    He can only ever jump one foot forward to the next stone OR two feed forward to the stone after the next. 

    In how many different ways can he jump 11 feet to the other side of the river?

    How would you come up with recursive program to calculate this value for a distance of n?

"""


def frog(dist):
    """ LUC """
    total = 0  # Total ways underneath this level

    if dist == 0:  # Count as path if on the mark
        return 1
    elif dist < 0:  # Do not count as path if overshoot
        return 0

    total += frog(dist - 2)  # Add total ways of path with double jump after this step
    total += frog(dist - 1)  # Add total ways of path with single jump after this step
    return total


assert frog(2) == 2
assert frog(3) == 3
assert frog(4) == 5
print("The frog can jump 11 feet {} different ways".format(frog(11)))


"""
    A more natural application of recursion is the binary search algorithm which is used to find a value in a 
    SORTED list. 

    Implement the binary search algorithm via recursion. 

"""


def binary_search(values, target):
    """ LUC """

    p_idx = int(len(values)/2)  # Choose pivot position
    pivot = values[p_idx]  # Get pivot value

    if target < pivot:  # If pivot is greater than center
        pos = binary_search(values[:p_idx], target)  # Binary search first half
    elif target > pivot:  # If pivot is less than center
        pos = p_idx+1 + binary_search(values[p_idx+1:], target)  # Binary search second half (need to add initial index)
    else:  # If pivot is answer
        pos = p_idx

    return pos


assert binary_search([0,1,2,3,4,5,6], 3) == 3
assert binary_search(list(range(0, 10, 2)), 2) == 1
