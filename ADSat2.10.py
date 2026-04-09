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

    def sort(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next

                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


lst = LinkedList()

n = 5

for i in range(n):
    lst.add_end(int(input("Enter number: ")))

print("Before sort:")
lst.print_list()

lst.sort()

print("After sort:")
lst.print_list()