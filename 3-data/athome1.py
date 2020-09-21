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



B. Search Algorithms - 
    A. Linear (move through a list sequentially) - worst run: O(n), best run: O(1), on average: (n+1)/2
    
    
    For unsorted lists, you can NOT do better than linear search but for sorted you can use BINARY SEARCH.
    
    B. Binary Search: repeatedly chooses a number in the middle of the remaining possible numbers, and then 
                      determines if the desired number would lie to the left or right of this chosen number 
       - Good because the number of elements keeps getting halved -
       Worst run: O(log n), best run: O(1), average: O(log n)

TODO Question 2 - Why is the average run time for linear different than the worst? 

TODO Question 3 - For binary, why is the average time the SAME as the worst? 


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

TODO Question 5 - What is the best case? 

TODO Question 6 - In the worst case for a list with 10 distinct elements, how many comparisons between list elements are made in insert sort?

TODO Question 7 - What about in the best case?

D. Dynamic array (also known as a resizable array)

Dynamic arrays store a pointer to a dynamically allocated array and replace that pointer with a newly 
allocated array as needed. Or in other words, a dyanmic array generates a new array and copies items from an old array when an 
item fills up an old array.

SO if we start adding more and more items, when we add too many, we can just allocate a new array, copy over the old elements,
get rid of old old array, and update pointer. 

TODO Question 8 - what are the 5 basic operations of any data structure?

TODO Question 9 - in python, a list is a dynamic array, what are the functions that correlate to that 5 basic operations?

TODO Question 10 - do this hacker rank challenge on dynamic arrays: https://www.hackerrank.com/challenges/dynamic-array/problem. 

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

    # 2. Given two strings, write a method to decide if one is a permutation of the other.

    # 3. Given a string, write a function to check if it is a permutation of a palindrome.

    # 4. Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.

    # 5. Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.


## FUN-er Exercises 

    # 1. Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

    # 2. Do this hackerrank challenge: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

