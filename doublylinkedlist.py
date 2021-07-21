# Inserting a Node Into a Sorted Doubly Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def insert_into_sorted_list(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        elif self.head.data > data:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            t = self.head
            while t.data < data and t.next is not None:
                t = t.next
            if t.next is not None:
                t.prev.next = node
                node.prev = t.prev
                t.prev = node
                node.next = t
            else:
                if data < t.data:
                    t.prev.next = node
                    node.prev = t.prev
                    node.next = t
                    t.prev = node
                else:
                    t.next = node

    def print_list(self):
        if self.head:
            n = self.head
            while n:
                print(n.data, end=' ')
                n = n.next
        else:
            print("Linked list is Empty")


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        length_of_list = int(input())
        for i in range(length_of_list):
            dllist.add_node(int(input()))
        value_to_be_inserted = int(input())
        dllist.insert_into_sorted_list(value_to_be_inserted)
        dllist.print_list()
