# Queues: A Tale of Two Stacks

class Queue(object):
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if len(self.q) != 0:
            self.q.pop(0)
        else:
            print("Queue is empty; Cannot remove")

    def peek(self):
        if len(self.q) != 0:
            return self.q[0]
        else:
            return "Queue is Empty; Cannot Print"


if __name__ == "__main__":
    queue = Queue()
    number_of_testcases = int(input())
    for _ in range(number_of_testcases):
        command_to_check = list(map(int, input().rstrip().split()))
        if command_to_check[0] == 1:
            queue.enqueue(command_to_check[1])
        elif command_to_check[0] == 2:
            queue.dequeue()
        elif command_to_check[0] == 3:
            print(queue.peek())
