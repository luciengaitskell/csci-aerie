""" In class examples 20200922 """


""" Linked list example """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def new(self, next_data):
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


if __name__ == "__main__":
    list = Node(1)
    list.new(2).new(3).new(4)
    print(list)


""" Recursion """

list = Node("T")
list.new("H").new("I").new("S")
list.traverse()

list.next = list.next.next
list.traverse()
