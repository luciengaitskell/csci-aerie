"""
Big O Notation Handout 
Due: Thursday, Sept 17th 

NOTES: 

- If there are no specific instructions for the problems,you need to find 
	Big O time for each of the following exercises. But don't just provide the
	final answer - explain your reasoning to how you got there. Partly because
	this is good practice but also you can get to the right answer the wrong way
	and I want to make sure you really understand big O notation before we move on. 
- Do NOT use online resources to solve the problems.
- Make sure to explain how you got to your answer as well as providing it.
	For ex, don't just say O(n) if originally the exercise had O(5) + O(n).  
- If you are stuck or want help on any of them, come to office hours! 

"""

"""
Quick review - big O is about measuring time comlexity of algorithms. Refers to 
the asymptotic WORST-CASE running time which is computed by the number of operations
on worst-case input as a function of n as n goes to INFINITY. 

Review cs16 slides here if you want to refresh: http://cs.brown.edu/courses/cs016/static/files/lectures/slides/02_analysisOfAlgos.pdf

Some of the most common runtimes are O(1), O(log N), O(N log N), O(N), O(N²), and O(2ⁿ).

Quick reminders: 
	1. Drop the constants - Big O notation doesn't care about constants because Big O 
	    notation only describes the long-term growth rate of functions. So drop the constants, 
	    no matter how large they are.
	2. Drop the non-dominant terms - Using Big O notation, we're interested in the upper 
		bound.Therefore non-dominant terms are non-important.
	3. Add vs. multiply - We add when there is a separate chunk of work(separate for-loops)
		in a function, and we multiply when we combine chunks of work(nested for-loops).
	4. Log N runtimes - We use Log N if the array range gets divided into half of the current
		range in a for-loop.Constant time algorithms are the quickest. Logarithmic time(log N) is 
		the second quickest.Mostly used in binary search.
	5. Recursive runtimes - Runtimes of a recursive function with multiple branches is 
		typically O( branchesᵈᵉᵖᵗʰ ).
	6. Derive by counting iteration - Do not memorize common patterns; rather, deeply 
		comprehend the algorithms and monitor the iterations, for they will give you a hint 
		in deriving the time complexity.

"""

## Exercise 1

def ex1(lis): 
	sm = 0
	product = 0 
	for x in range(len(lis)):
		sm += lis(x)
	for x in range(len(lis)):
		product *= lis(x)
	print("Sum = {}, Product = {}".format(sm,product))

#ex1([0,1,2])

## Exercise 2 

def ex2(lis): 
	for x in range(len(lis)): 
		for y in range(len(lis)):
			print("Pair = ({},{})".format(lis(x),lis(y)))

#ex2([0,1,2])

## Exercise 3

def ex3(lis): 
	for x in range(len(lis)): 
		for y in range(1,len(lis)):
			print("Pair = ({},{})".format(lis(x),lis(y)))

#ex3([0,1,2])


## Exercise 4 
def ex4(lis1,lis2): 
	for x in range(len(lis1)): 
		for y in range(len(lis2)):
			if lis1[x] > lis2[y]: 
				print("Pair = ({},{})".format(lis1[x],lis2[y]))


#ex4([0,1,2], [1,2,3])

## Exercise 5 
def ex5(lis1,lis2): 
	for x in range(len(lis1)): 
		for y in range(len(lis2)):
			for z in range(10000):
				print("Pair = ({},{})".format(lis1[x],lis2[y]))


#ex5([0,1,2], [1,2,3])


## Exercise 6 

def ex6(lis): 
	for i in reversed(lis):
		print(i)

# ex6([0,1,2])

## Exercise 7 

	# Which of the following are equivalent to O(N)? Why? 
	# 1. 0(N+P),where P < n/2
	# 2. O(2N)
	# 3. O(N + log N)
	# 4. O(N + M)

## Exercise 8 

	# Suppose we had an algorithm that took in list of strings, 
	# sorted each string, and then sorted the full list. What would the runtime be?

	# Hint: runtime of sorting a string (worst case) is log linear 


## Exercise 9 


def ex9(items):

    for i in range(5):
        print ("Python is awesome")

    for item in items:
        print(item)

    for item in items:
        print(item)

    print("HEY")
    print("LUC")

#ex9([1, 2, 3, 4])

## Exercise 10 

def ex10(num, items):
    for item in items:
        if item == num:
            return "num is in list items"
        else:
            return "num is NOT in list items"

# nums = [2, 4, 6, 8, 10]
# print(ex10(12, nums))

# TODO: In addition to answering what is worst case complexity (Big O), what do you think is best case? Explain.

## Exercise 11 

def ex11(n):
    square_list = []
    for num in n:
        square_list.append(num * num)

    return square_list

# nums = [2, 4, 6, 8, 10]
# print(ex11(nums))

# TODO: In addition to answering what is worst case complexity (Big O), what is space complexity? Explain. 

