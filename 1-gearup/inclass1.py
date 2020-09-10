""" Python Gear Up: Part 1
Lucien Gaitskell 200910
"""


## LISTS
lunch_items = [
    "sandwich",
    "salad",
    "smoothie",
    "bagel",
    "pizza"
]

print(lunch_items[-1])

lunch_items[2] = "soup"
print(lunch_items[2])

for num in range(1000+1):
    print(num)

long_list = list(range(1, 10**3+1))
print(long_list)

num_list = [1, 2, 3, 4, 5]

print("Sum: ", sum(num_list))

num_short = num_list[:3]
print(num_short)

print(num_list[1:4])
print(num_list[-3:])

num_list.append(6)
print(num_list)

num_list.insert(3, 3.5)
print(num_list)

del num_list[-1]
print(num_list)

print("Len: ", len(num_list))

print(sorted(num_list, reverse=True))
num_list.sort(reverse=True)
print(num_list)

squares = []
for i in range(1, 10+1):
    squares.append(i**2)
print(squares)

# List comprehension
print([i**2 for i in range(1, 10+1)])

set_values = (48, 64)

try:
    set_values[0] = 20
except:
    print('ERROR')
print(set_values)
set_values = (86, 78)
print(set_values)


## DICTIONARIES
d = {
    'thursday': 6,
    'friday': 7,
    'sunday': None,
}

print(d['thursday'])
print(d.get('thursday'))
print(d.get('sunday', None))

d['thursday'] = 8
print(d)

del d['thursday']
print(d)

for k, v in d.items():
    print("{}: {}".format(k, v))

for k in d.keys():
    print(k)


# Nested data
students = [
    {'name': "Albert", 'age': 17},
    {'name': "Bob", 'age': 18},
    {'name': "Charles", 'age': 19},
]

students.append({'name': "Diane", 'age': 17})
print(students)

for s in students:
    print("{}: age {}".format(s['name'], s['age']))


favorite_languages = {
    'Albert': ["Spanish", "German"],
    'Bob': ["English", "Hebrew"],
    'Charles': ["Japanese", "Italian"],
    'Diane': ["Korean", "Swedish"]
}

for name, languages in favorite_languages.items():
    print("{}: {}".format(name, languages))

from collections import OrderedDict

ordered = OrderedDict()
ordered['first'] = 1
ordered['second'] = -100
ordered['third'] = 93
print(ordered)
