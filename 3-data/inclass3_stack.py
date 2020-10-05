""" In Class 201005 """

## STACK
stack = []
# push -> the same as append
stack.append('a')
stack.append('b')

# pop -> the same as pop
print(stack.pop())
print(stack)


# Stack class instead:
class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return "no element"

        return self.stack.pop()


## QUEUE

queue = ['a', 'b']

queue.append('c')

print(queue)

print(queue.pop(0))

print(queue)


class Queue:
    def __init__(self):
        self.stack = []

    def add(self, val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return "no element"

        return self.stack.pop(0)


""" Using Python lists internally is inefficient, especially with appends

Python has its own Queue objects
"""

import queue
newQueue = queue.Queue(maxsize=10)
newQueue.put('a')
newQueue.put('b')
print("Queue size: ", newQueue.qsize())
print(newQueue.get())
print("Queue size: ", newQueue.qsize())

newStack = queue.LifoQueue(maxsize=10)

newStack.put(1)
newStack.put(2)
newStack.put(3)

print("Stack size: ", newStack.qsize())
print(newStack.get())
print(newStack.get())
print("Stack size: ", newStack.qsize())

print("Stack full: ", newStack.full())
