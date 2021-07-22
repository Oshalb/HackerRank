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

    def reverse_list(self):
        t = self.head
        while t.next:
            t = t.next
        node = Node(t.data)
        self.head = node
        self.head.next = t.prev
        temp = self.head.next
        while temp:
            f = temp.next
            temp.next = temp.prev
            temp.prev = f
            temp = temp.next

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
        print("Enter Length of List")
        length_of_list = int(input())
        print("Enter values into list, seperate by enter")
        for i in range(length_of_list):
            dllist.add_node(int(input()))
        print("Select Options", "0. Exit", "1. Insert", "2. Reverse", "3. Print", sep="\n")
        s = int(input())
        while s != 0:
            if s == 1:
                value_to_be_inserted = int(input())
                dllist.insert_into_sorted_list(value_to_be_inserted)
            elif s == 2:
                dllist.reverse_list()
            elif s == 3:
                dllist.print_list()
            else:
                print("String does not match")
            print("Select Options", "0. Exit", "1. Insert", "2. Reverse", "3. Print", sep="\n")
            s = int(input())
