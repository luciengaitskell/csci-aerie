"""
Arrays Handout  
Due: Tuesday, Sept 33nd 

NOTES: 

- Changed the format of the homework this time so the content review (summarization of our class today) 
    now includes knowledge check exercises. Hope this helps review some of the trickier content!
- For the python exercises, please do NOT use online resources. They are common algorithm questions so
    they have answers online but it won't help your understanding.
- If you are stuck or want help on any of them, come to office hours! 

"""


"""
A. Multidimensional arrays (2d or 3d) are highly relevant topic in computer vision (ex: images)


TODO Question 1 - for images, what do the values of the 3D array refer to?

    # LUC: 3D array dimensions correspond with x, y, and color/pixel data for the image. 


B. Search Algorithms - 
    A. Linear (move through a list sequentially) - worst run: O(n), best run: O(1), on average: (n+1)/2
    
    
    For unsorted lists, you can NOT do better than linear search but for sorted you can use BINARY SEARCH.
    
    B. Binary Search: repeatedly chooses a number in the middle of the remaining possible numbers, and then 
                      determines if the desired number would lie to the left or right of this chosen number 
       - Good because the number of elements keeps getting halved -
       Worst run: O(log n), best run: O(1), average: O(log n)

TODO Question 2 - Why is the average run time for linear different than the worst?

    # LUC: Linear search will check the elements sequentially, and therefore run a loop as many times as the value
        of the true index of the target value. Therefore, the search is highly dependent on the position of the
        target value. The worst case is that all data values (n) have to be searched, and the best is that only 1 does.
        Due to the probability and linear distribution of target position, the average runtime would be the average of
        both 1 and n.

TODO Question 3 - For binary, why is the average time the SAME as the worst? 

    # LUC: Binary search, by nature, will continue to half the size of the array being searched, until the target value
        is located. As a result, the worst time is log(n). Therefore  

========NEED HELP

C. Insertion sort is how we sort through a list. 

Brief overview of the algorithm:  

    1. We start from the left. At first there is one element (which is, trivially, already sorted).
    2. Colloquially speaking, for each subsequent element, we compare it to each of the elements to the left of it, moving right to left, 
    until we find where it “fits” in the sorted portion of the array.
    3. Since we are inserting the new element into the side of the array that is already sorted, the result will still be sorted.
    4. After we’ve inserted every element, we have a sorted array!

To visualize this algorithm, go to https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/

For insertion sort, the worst case is n^2 for large n and best case is n. 

In insertion sort, the worst case is unforunately far more likely. 

But don't worry, there are more efficent sorting algorithms and we'll be exploring them soon! 

TODO Question 4 - What is the correct big O classification for insertion sort? Remember big O is WORST CASE.
    # LUC: Insertion sort is O(N^2), as worst case each element has to be inserted at the end of the list. Therefore 
        the full list of elements has to be traversed for inserting a value, which then has to operate N times. 

TODO Question 5 - What is the best case? 
    # LUC: Insertion sort is Ω(N) if the values are inserted at the beginning of the list each loop. Therefore the
        insertion process is O(1) and has to be executed N times.

TODO Question 6 - In the worst case for a list with 10 distinct elements, how many comparisons between list elements are made in insert sort?
    # LUC: The insertion loop run for every original element, however the number of elements to compare to grows as
        insertion continues. Therefore each element requires 1 operation to add to the list, along with m comparisons,
        for m=(number of elements in sorted array)=(element number=1):
            (1) + (1 + 1) + (1 + 2) + (1 + 3) + ... + (1 + 9) 
            = 1 + 2 + 3 + ... + 10 = 55 operations

TODO Question 7 - What about in the best case?
    # LUC: In the best case, only one comparison has to be executed for each subsequent element added. Therefore,
        the first element requires 1 operation and all subsequent require 2 operations:
            (1) + (2) + ... + (2) = (1) + 9*(2) = 19 operations

D. Dynamic array (also known as a resizable array)

Dynamic arrays store a pointer to a dynamically allocated array and replace that pointer with a newly 
allocated array as needed. Or in other words, a dyanmic array generates a new array and copies items from an old array when an 
item fills up an old array.

SO if we start adding more and more items, when we add too many, we can just allocate a new array, copy over the old elements,
get rid of old old array, and update pointer. 

TODO Question 8 - what are the 5 basic operations of any data structure?
    # LUC: The basic operations are:
        1. Add/Insert
        2. Get
        3. Remove
        4. Search/Find
        5. Sort
===== CHECK


TODO Question 9 - in python, a list is a dynamic array, what are the functions that correlate to that 5 basic operations?
    # LUC:
        1. `.insert()` / `.append()`
        2. `[i]`
        3. `del`
        4. `.index()`
        5. `.sort()`

TODO Question 10 - do this hacker rank challenge on dynamic arrays: https://www.hackerrank.com/challenges/dynamic-array/problem. """

def dynamicArray(n, queries):
    """ LUC """
    seqList = []
    for i in range(n):  # Can't use list comprehension :/
        seqList.append([])
    lastAnswer = 0

    ret_values = []

    for q, x, y in queries:
        seq = seqList[(x ^ lastAnswer) % n]
        if q == 1:
            seq.append(y)
        if q == 2:
            lastAnswer = seq[y % len(seq)]
            ret_values.append(lastAnswer)

    return ret_values


def q10():
    """ LUC """
    select = input()
    num_seq, num_query = map(int, select.split(" "))

    query_lines = []
    for q_id in range(num_query):
        query_lines.append(map(int, input().split(" ")))

    for v in dynamicArray(num_seq, query_lines):
        print(v)

# LUC
#q10()


""""  

E. Amortized run time is a tricky concept to explain but essentially it comes doewn to the fundamental idea that 
looking at the individual worst case may be too severe - what if we just wanted to look at the total worst cost for a 
SEQUENCE of operations?

For ex, for dynamic arrays, the worst case of runtime for insertion is O(n), and this happens in the array is full
and you have to copy every single element over to the new array. 

However, this does NOT happen very often. Most of the times, insertion of a single element is in O(1) time.

This is what amortized time allows us to explain - yes, the worst case will happen once every while
but once it happens it won't happen for a long time (once again its the mindset of viewing things as a SEQUENCE). 

During class, you asked a question about how to compute amortized run time. I don't think I answered it well because its
not relevant to our course but this idea of how you compute amortized run time does exist - and its called amortized analysis. 

There are a handful of methods that compute this time mathematically (aggregate, bankers, etc). You can learn about them
here: https://cs.brown.edu/courses/csci0180//content/lectures/15dynArrayAnalysis-java.pdf. 

If you want to explore this topic, let me know so I can review it and come up with content on it! 

"""

## Exercises


# 1. Implement an algorithm to determine if a string has all unique characters.

def unique(s):
    """ LUC """
    for i1, c1 in enumerate(s):  # Iterate through whole string
        for i2 in range(i1+1, len(s)):  # Iterate from next character to end
            if c1 == s[i2]:  # Compare characters to check for similarity
                return False
    return True


assert unique("")
assert unique("abcd")
assert not unique("abcdd")
assert not unique("abcda")


# 2. Given two strings, write a method to decide if one is a permutation of the other.
def perm(s1, s2):
    """ LUC """
    if len(s1) != len(s2):  # Can't be a permutation if they're different lengths - Also necessary for algo
        return False

    for c in s1:  # Get each character in first string
        if s1.count(c) != s2.count(c):  # compare number of occurrences of character between strings
            return False
    return True


assert perm("", "")
assert perm("abc", "cba")
assert not perm("a", "cba")
assert not perm("abc", "cbb")
assert not perm("abc", "cbbc")


# 3. Given a string, write a function to check if it is a permutation of a palindrome.
def palinperm(s1):
    """ LUC """
    max_odds = len(s1) % 2  # If length is even, no odd counts allowed. If odd, one odd is allowed

    # TODO: need to prevent already counted character from
    odds = []  # Number of past odd character counts
    for c in s1:  # Log counts of each
        if s1.count(c) % 2 == 1 and c not in odds:  # If odd count
            odds.append(c)
        if len(odds) > max_odds:  # If exceeded max odds, then can't be a palindrome
            return False
    return True

import random
def _str_shuffle(s):
    shuf = list(s)
    random.shuffle(shuf)
    return ''.join(shuf)

PALIN = "abcba"
palin_shuffle = _str_shuffle(PALIN)

NOT_PALIN = "abecjba"
not_palin_shuffle = _str_shuffle(NOT_PALIN)

assert palinperm(palin_shuffle)
assert not palinperm(not_palin_shuffle)


# 4. Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
#       the image by 90 degrees.
def rotate(mat):
    # Create final empty array:
    mat_final = []
    for i in range(len(mat)):
        mat_final.append([None for i in range(len(mat[i]))])

    for r_idx, row in enumerate(mat):
        for c_idx, val in enumerate(row):
            mat_final[c_idx][r_idx] = val
    return mat_final


MAT = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def ex4():
    print('[')
    for row in rotate(MAT):
        print(" ", row)
    print(']')

# ex4()


# 5. Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.
def rowzero(mat):
    for row_idx, row in enumerate(mat):
        for col_idx, val in enumerate(row):  # Iterate through all values
            if val == 0:  # Operate if value is zero
                for rep_row_idx, rep_val in enumerate(mat):  # Operate along row of the zero value
                    if rep_val != 0:  # Skip if value is also zero, to allow later operation at that position
                        mat[rep_row_idx][col_idx] = None  # Flag for deletion
                for rep_col_idx, rep_val in enumerate(mat[row_idx]):  # Operate along column of the zero value
                    if rep_val != 0:  # Skip if value is also zero, to allow later operation at that position
                        mat[row_idx][rep_col_idx] = None  # Flag for deletion

    # Set flagged items to zero
    for row_idx, row in enumerate(mat):
        for col_idx, val in enumerate(row):
            if val is None:
                mat[row_idx][col_idx] = 0
    return mat


MAT = [
    [1, 2, 3],
    [0, 5, 0],
    [7, 8, 9]
]

#print(rowzero(MAT))


## FUN-er Exercises 

# 1. Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# TODO: Could swap k,counter_sum to just k
def sumk(arr, k, counter_sum=0):
    """ LUC

    :param arr: array to search through
    :param k: target sum
    :param counter_sum: exisitng count
    :return: array of arrays of valid sum sets
    """
    valid_sets = []  # list of valid sets

    arr_copy = arr[:]  # Array copy of this tree to allow element removal without conflicts

    for i in reversed(range(len(arr_copy))):
        e = arr[i]  # Save current value
        del arr_copy[i]  # Remove current element to prevent double counting and permutations on this recursive level

        curr_sum = counter_sum + e  # Evaluate current sum
        if curr_sum == k:  # If current sum is target
            valid_sets.append([e])  # Add final ending value to valid sets sets list
        elif curr_sum < k:  # If below target
            for l in sumk(arr_copy, k, curr_sum):  # Get each solution set that worked on subset
                valid_sets.append([e]+l)  # add current value on to each solution from subset

    return valid_sets


# print(sumk([1,2,3,4,5,6], 10))

# 2. Do this hackerrank challenge: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def rotLeft(a, d):
    """ LUC
    :param a:
    :param d:
    :return:
    """

    a_final = [None for v in a]  # Create empty array of same size

    for i, v in enumerate(a):  # Iterate through all array values
        a_final[(i-d) % len(a)] = v  # Assign same values at shifted index
    return a_final


def funq2():
    """ LUC """
    a_len, d = map(int, input().split(" "))  # Get config input

    a = list(map(int, input().split(" ")))  # Get array input
    if len(a) != a_len:
        raise ValueError("Incorrect array length")

    for v in rotLeft(a, d):  # Execute algo and print data
        print(v, end=" ")
    print()


#print(rotLeft([1,2,3,4,5], 4))
# funq2()
