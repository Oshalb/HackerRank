# Insert a node at a specific position in a linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def insert_node(self, pos, data):
        n = self.head
        node = Node(data)
        if pos == 0:
            self.head = node
            self.head.next = n
        else:
            t = n
            i = 0
            while i != pos:
                t = n
                n = n.next
                i += 1
            t.next = node
            node.next = n
            """
            Method without temporary node to save the previous node
            count = 1
            while count < position and node:
                count += 1
                node = node.next
            newNode = SinglyLinkedListNode(data)
            newNode.next = node.next
            node.next = newNode
            """

    def print_linked_list(self):
        if self.head:
            n = self.head
            while n:
                print(n.data, end=' ')
                n = n.next


if __name__ == "__main__":
    llist = LinkedList()
    number_of_elements = int(input())
    for _ in range(number_of_elements):
        llist.add_node(int(input()))
    value_to_be_inserted = int(input())
    position_to_insert = int(input())
    llist.insert_node(position_to_insert, value_to_be_inserted)
    llist.print_linked_list()
