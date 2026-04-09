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

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Wrong position")
            return

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


lst = LinkedList()

n = 3

for i in range(n):
    x = int(input("Enter number: "))
    lst.add_end(x)

print("Before insert:")
lst.print_list()

value = int(input("Enter number to insert: "))
pos = int(input("Enter position: "))

lst.insert_at_position(value, pos)

print("After insert:")
lst.print_list()