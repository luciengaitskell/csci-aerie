"""
Python Gear Up Handout 
Due: Thursday, Sept 14th 

Completed by Lucien Gaitskell

NOTE: this is just handout to work through - answer the questions to the best 
      of your ability, and include test cases (1-2 is fine) just like we were
      doing in class, don't worry about answering in a specific format - this
      is just a review for your benefit!

"""

### TOPIC - IF and WHILE Functions ###

## Conditional test is something that returns true or false
sport_A = "basketball"
sport_B = "rowing"
sport_C = "Basketball"

# How would you check if the values of sport_A and sport_B are equal?
print(sport_A == sport_B)
# Does case (upper or lower case) matter when checking for equality?
print(sport_A.lower() == sport_B.lower())
# How you check if they are inequal?
print(sport_A.lower() != sport_B.lower())


## Checking multiple conditions - use and/or

age_1 = 18
age_2 = 22

# Check if age_1 AND age_2 are both over 18.
print(age_1 > 18 and age_2 > 2)
# Check if either age_1 OR age_2 are over 21.
print(age_1 > 21 or age_2 > 21)


## Boolean Values - True or False

the_year_is_2020 = True
covid_is_fake = False

if the_year_is_2020:
    print("There's an election!")

if not covid_is_fake:
    print("Social distance!")


## If statements

persona1 = {'Name': 'Sam', 'Age' : 18}

# Define a simple IF statement to check if Sam's old enough to vote, and if so return a "GO VOTE." statement
if persona1['Age'] >= 18:
    print("GO VOTE.")
# Now add an elif statement if she's not old enough to vote, and returns a statement that says "You're not old enough to vote."
elif persona1['Age'] >= 0:
    print("You're not old enough to vote")
else:
    print("Really?")


##- Input Statement - allows users to enter input

# Using the input() function, ask the users their age
age = input("What is your age? ")

# Now return their age back to them - "You are [AGE] years old!"
if age.isnumeric():
    print("You are {} years old".format(age))
else:
    print("Age is not a number")


## While loop - repeats block of code as long as condition is True

starting_number = 1

# Define a while loop that prints out the value of starting_number until the starting_number is greater than 5
while starting_number <= 5:
    print(starting_number)
    starting_number += 1
    # Make sure to increment the number as well in each loop)


fruit = ["Apple", "Orange", "Grape", "Apple"]

# How would you remove "Apple" from the list?
fruit.remove("Apple")

# Does it remove only one instance of "Apple" or all instances?
assert fruit[-1] == "Apple"

# Use a while loop to remove all instances of "Apple"
value = "Apple"
while value in fruit:
    fruit.remove(value)

## Last note about while loops - you can use BREAK to quit a loop and CONTINUE to skip over certain items in a loop.


### TOPIC - Functions

# Define a function called 'welcome' that prints out a greeting (desired output: “Welcome to the Wheeler School!”)
def welcome():
    print("Welcome to the Wheeler School!")
welcome()


# Add a parameter to the function so you can take in an argument for a person’s name (desired output: “Welcome to the Wheeler School, Luc!”)
def welcome(name):
    print("Welcome to the Wheeler School, {}!".format(name))
welcome("Luc")


## Positional vs Keyword Arguments

# Define a function called student that takes in two positional arguments (name and age) and prints them
def student(name, age):
    print("{}: {} years old".format(name, age))
student("Luc", 17)

# Do users have to specific order?
## LUC: Do you mean arguments? If so, arguments have a specific order, in this case `student(name, age)`


# Now change the function so that its a keyword argument
def student(*, name, age):
    print("{}: {} years old".format(name, age))
student(name="Luc", age=17)

# Does order matter now?
## LUC: No, order does not matter for keyword arguments


## Default Values

# Add a default value to the age parameter
# Now change the age parameter to make that argument optional
def student(name, *, age=17):
    print("{}: {} years old".format(name, age))
student("Luc")


## Return Values

# Modify the same 'welcome' function to return a student information in the form of a dictionary
def student(name, *, age=17):
    return {
        'name': name,
        'age': age
    }
print(student("Luc"))


## Arbitrary Number of Arguments

# Add a parameter to the function called classes that allows an arbitrary number of arguments
def student(name, *classes, age=17):
    return {
        'name': name,
        'age': age
    }


# Return the students information (including name, age, and classes) as a dictionary
def student(name, *classes, age=17):
    return {
        'name': name,
        'age': age,
        'classes': classes
    }
print(student("Luc", "CS", "Linear Algebra", "Molecular Biology", "English", "Spanish", "Economics"))


### FUN Exercises 

# 1. Given a string, write a python function to check if it is palindrome or not.
def pal(phrase: str):
    phrase = phrase.replace(' ', '')
    l = len(phrase)

    for i in range(0, int(l/2)):
        if phrase[i].lower() != phrase[l-1-i].lower():
            return False
    return True


assert pal("abcccba")
assert pal("")
assert not pal("ab")
assert not pal("abc")
assert pal("aba")
assert pal("hghgh")
assert pal("Do geese see God")
assert pal("Was it a car or a cat I saw")


# Great! Now for extra credit, can you think of another approach? 
def pal(phrase: str):
    phrase = phrase.replace(' ', '').lower()
    l = len(phrase)
    pivot = int(l / 2)

    p1 = phrase[:pivot]

    p2 = phrase[:pivot-1+(l % 2):-1]
    '''
    # Should be faster than:
    p2 = phrase[-pivot:]
    p2 = p2[::-1]
    '''
    return p1 == p2


assert pal("abcccba")
assert pal("")
assert not pal("ab")
assert not pal("abc")
assert pal("aba")
assert pal("hghgh")
assert pal("Do geese see God")
assert pal("Was it a car or a cat I saw")


# 2. Write a function that prints each number from 1 to 100 on a new line.
# 	 For each multiple of 3, print "Covid" instead of the number. 
# 	 For each multiple of 5, print "Pandemic" instead of the number. 
# 	 For numbers which are multiples of both 3 and 5, print "CovidPandemic" instead of the number. 

for num in range(1,100+1):
    p = False
    if num % 3 == 0:
        print("Covid", end="")
        p = True
    if num % 5 == 0:
        print("Pandemic", end="")
        p = True

    if p:
        print()
    else:
        print(num)
