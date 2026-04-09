class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


lst = LinkedList()

n = 3

for i in range(n):
    x = int(input("Input numbers: "))
    lst.add_end(x)

print("Before deletion:")
lst.print_list()

lst.remove_last()

print("After deletion:")
lst.print_list()