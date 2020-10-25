"""
Trees and Heaps Handout 
Due: Friday, October 23rd

NOTES: 

- For the exercises, please do NOT use online resources. They are common algorithm questions so
    they have answers online but it won't help your understanding.
- If you are stuck or want help on any of them, come to office hours! 

Completed by Lucien Gaitskell (LUC)

"""


# Utils
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Exercises
"""
    1. Using the node class we created in class, implement functions to represent the 
        3 different orders  you can use to recursively conduct DFS 
        (each order should have a function).
"""

# Create test node structure
test_node = Node(1)
test_node.left = Node(2)
test_node.left.left = Node(3)
test_node.left.right = Node(4)
test_node.right = Node(5)
test_node.right.left = Node(6)
test_node.right.right = Node(7)


def dfs_post(n: Node):
    """ LUC

    :param n: node to search from
    """
    for next_n in [n.left, n.right]:  # Search left and right nodes first
        if next_n is not None:
            dfs_post(next_n)

    print(n.data)  # Display this node

# dfs_post(test_node)


def dfs_pre(n: Node):
    """ LUC

    :param n: node to search from
    """
    print(n.data)  # Display this node

    for next_n in [n.left, n.right]:  # Search left and right nodes after
        if next_n is not None:
            dfs_pre(next_n)

# dfs_pre(test_node)


def dfs_inplace(n: Node):
    """ LUC

    :param n: node to search from
    :return:
    """
    if n.left is not None:      # Search left node first
        dfs_inplace(n.left)

    print(n.data)               # Search this node

    if n.right is not None:     # Search right node after
        dfs_inplace(n.right)

# dfs_inplace(test_node)


"""
    2. Implement a priority queue simply using list. PQ class should include functions 
        that check if the PQ is empty, adds an element to the PQ, and finally removes 
        an element. 

        Reminder: Most of the logic in terms of how a PQ works is in how it REMOVES 
        an element (highest priority element is dequeued).
"""


class PriorityQueue:
    """ LUC """
    def __init__(self):
        self.q = []

    def empty(self):
        """ Determine if queue is empty

        :return: empty state
        """

        return len(self.q) < 1

    def add(self, v):
        """ Add value to priority queue, using value as priority

        :param v: value to add
        :return: index
        """

        idx = 0
        for q_v in self.q:  # Get all values in queue
            if v < q_v:     # Stop where target value is less than selected element
                break
            idx += 1

        self.q.insert(idx, v)   # Insert value

    def rem(self):
        """ Remove and get the highest priority value

        :return: highest priority value
        """

        return self.q.pop(-1)  # Remove from end


pq = PriorityQueue()
assert pq.empty()
pq.add(3)
pq.add(5)
pq.add(2)
pq.add(7)
assert not pq.empty()

assert pq.q == [2, 3, 5, 7]
assert pq.rem() == 7
assert pq.rem() == 5


"""
    3. Now implement a PQ using a linked list. 
"""


class LLNode:
    """ LUC

    Linked list node UTILITY
    From `athome3....py`
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def new(self, next_data) -> 'LLNode':
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


class PriorityQueueLinked:
    """ LUC """
    def __init__(self):
        self.q = LLNode(None)

    def empty(self):
        """ Determine if queue is empty

        :return: empty state
        """

        return self.q.data is None

    def add(self, v):
        """ Add value to priority queue, using value as priority

        :param v: value to add
        :return: index
        """

        new_node = LLNode(v)  # New node to add

        prev_n = self.q

        if prev_n.data is None:     # Edge case, no data yet
            prev_n.data = v
        elif v > prev_n.data:       # Edge case, greater than first value
            new_node.next = prev_n  # Swap nodes
            self.q = new_node
        else:                       # Standard case
            next_n = prev_n.next    # Set up next node to check

            while next_n is not None:   # Iterate until target value is greater than subsequent
                if v > next_n.data:
                    break

                prev_n = next_n             # Otherwise move on selected nodes
                next_n = next_n.next

            new_node.next = prev_n.next     # Insert new node after previous,
            prev_n.next = new_node          # and before next

    def rem(self):
        """ Remove and get the highest priority value

        :return: highest priority value
        """
        top = self.q    # Save top level node

        if self.q.next is not None:     # Check there is another node
            self.q = self.q.next            # Replace top node with next
        else:                           # Else, create empty node
            self.q = LLNode(None)

        return top.data     # Return removed node data


pq = PriorityQueueLinked()
assert pq.empty()
pq.add(3)
pq.add(5)
pq.add(2)
pq.add(7)
assert not pq.empty()

# print(pq.q.resolve())
assert pq.rem() == 7
assert pq.rem() == 5
assert pq.rem() == 3
assert pq.rem() == 2
assert pq.rem() is None


"""
    4. Write 4 examples of using each heap function:
        - calling heapify on a list
        - pushing an element onto a heap
        - popping the smallest element of a heap

        Hint: Utilize built-in functions (heappush, heappop, heapify) from module heapq.  
"""

import heapq
import random

# LUC
heap1 = list(range(10))
random.shuffle(heap1)
print("Original:", heap1)

#   heapify:
heapq.heapify(heap1)
print("Heap:", heap1)

#   push:
heapq.heappush(heap1, 5)
heapq.heappush(heap1, 10)
heapq.heappush(heap1, 5)
print("Push:", heap1)

#   pop:
for i in range(5):
    print("Pop #{}:".format(i), heapq.heappop(heap1))


"""
    5. Time complexity - what is the time complexity of a PQ implemented as a linked list vs a binary heap? 

LUC:

Linked list:
- push: O(n) - Have to search whole list for proper insertion point
- pop: O(1)  - Remove first element, no reshuffling
- peek: O(1) - Get first value

Binary heap:
- push: O(logn) - Only half of the nodes at each level have to be searched for point, through bubbling up   
- pop: O(logn)  - Remove first node; subsequently, half the nodes at each level have to be swapped to maintain heap 
- peek: O(1)    - Get first node, which is top-most

"""

