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

    def combine(self, other):
        if self.head is None:
            self.head = other.head
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


lst1 = LinkedList()
lst2 = LinkedList()

n1 = 3
for i in range(n1):
    lst1.add_end(int(input("Enter number list1: ")))

n2 = 4
for i in range(n2):
    lst2.add_end(int(input("Enter number list2: ")))

print("First list:")
lst1.print_list()

print("Second list:")
lst2.print_list()

lst1.combine(lst2)

print("Combined list:")
lst1.print_list()