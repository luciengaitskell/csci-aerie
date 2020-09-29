"""
Linked Lists Handout  
Due: Tuesday, Sept 29th

NOTES: 

- Reference class notes here: https://docs.google.com/document/d/1AWM3nnLc-d-4nYobBRuBTMuCjYWhJMAUx2ipdQ5E77g/edit?usp=sharing
- For the python exercises, please do NOT use online resources. They are common algorithm questions so
	they have answers online but it won't help your understanding. 
- If you are stuck or want help on any of them, come to office hours! 

Completed by Lucien Gaitskell (LUC)
"""

## Exercises

	# 1. How would you remove duplicates from an unsorted linked list?

	# 2. How would you find the kth to last element of an singly linked list?

	# 3. How would you delete a node in the middle of a singly linked list? 

		# For ex, remove "H" from this linked list - don't need to return anything (just change the linked list)

		Node1.data = "T"
		Node1.next = Node2
		Node2.data = "H"
		Node2.next = Node3
		Node3.data = "I"
		Node3.next = Node4
		Node4.data = "S"
		Node4.next = null

	#4. How would you check if a linked list is a palindrome? 


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

				# Question - In the recusirve approach, how many calls to fibonacci(n) function do we make when we call fibonacci(4)? 

			"""
			
				A frog wants to cross an 11-foot river. There are 10 stones that he can use. The rocks are seperated by 1 foot.
				He can only ever jump one foot forward to the next stone OR two feed forward to the stone after the next. 

				In how many different ways can he jump 11 feet to the other side of the river?

				How would you come up with recursive program to calculate this value for a distance of n?

			"""


			"""
				A more natural application of recursion is the binary search algorithm which is used to find a value in a 
				SORTED list. 

				Implement the binary search algorithm via recursion. 
	
			"""



